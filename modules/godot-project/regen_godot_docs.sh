#!/usr/bin/env bash
# Regenerate docs/godot-api/ from the installed Godot binary.
#
# Pipeline:
#   1. `godot --doctool` exports XML class references into a tempdir.
#      The output is split across doc/classes/, modules/<m>/doc_classes/,
#      and platform/<p>/doc_classes/.
#   2. Flatten every XML file into one tempdir (no name collisions exist).
#   3. `uv run c3-godot-docs-gen --index` renders per-class Markdown
#      plus index.md into docs/godot-api/. The tool lives in this
#      repo's pyproject.toml; `uv run` resolves it from the venv.
#
# Run from the repo root. Exits non-zero on the first failure.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_ROOT"

XML_ROOT="$(mktemp -d)"
FLAT_DIR="$(mktemp -d)"
cleanup() { rm -rf "$XML_ROOT" "$FLAT_DIR"; }
trap cleanup EXIT

# Step 1: export XML from the installed Godot.
godot --doctool "$XML_ROOT"

# Step 2: flatten. doc/classes/ holds the core classes; modules and
# platform subdirs hold the rest. Confirmed: no XML filename collisions
# between these trees.
cp "$XML_ROOT"/doc/classes/*.xml "$FLAT_DIR/"
find "$XML_ROOT"/modules "$XML_ROOT"/platform -name '*.xml' -exec cp {} "$FLAT_DIR/" \;

# Step 3: render Markdown into the canonical (gitignored) output dir.
# `uv run` resolves c3-godot-docs-gen from this repo's pyproject.toml.
rm -rf docs/godot-api
uv run c3-godot-docs-gen --index "$FLAT_DIR" docs/godot-api
