# Module: godot-gdunit4

Opt-in module that adds gdUnit4 as the unit-test framework to a Godot 4
project. It vendors the addon, enables the plugin, ships a sample suite, and
keeps the test artifacts out of git.

## What it is

gdUnit4 is an embedded unit-test framework for GDScript and C#. The plugin
lives under `addons/gdUnit4/`. This module installs the latest release and
wires it into the target project.

## Depends on

The `godot-project` module. This module appends a bullet to the target's
`## Project context` section, which `godot-project` writes. Apply
`godot-project` first.

## External dependencies

The installer probes, the user does not vendor.

- `godot` on `PATH` — imports the addon, refreshes the class registry, and
  runs the suite.
- Network access to `github.com` — resolves the latest release and downloads
  its source archive.
- `gh` on `PATH`, optional — resolves the latest release tag. The installer
  falls back to the releases API without it.

## What it installs in the target repo

1. Vendors `addons/gdUnit4/` from the latest gdUnit4 release.
2. Enables `res://addons/gdUnit4/plugin.cfg` in `project.godot`.
3. Copies `templates/ExampleTest.gd` to `test/ExampleTest.gd`.
4. Appends the lines in `gitignore` to the target `.gitignore`.
5. Appends `fragments/project-context-row.md` to the target's
   `## Project context` section.
6. Refreshes the class registry with a headless editor pass, then runs the
   sample suite.

## Version

The installer resolves the latest release at install time and records the
resolved tag in the install entry. The latest release carries no binary asset as
of v6.2.2 (verified 2026-10-14). The source archive at
`archive/refs/tags/<tag>.zip` exists for every tag, so the installer uses it
unconditionally.

The upstream repository is `godot-gdunit-labs/gdUnit4`. It was formerly
`MikeSchulze/gdUnit4`. The old slug redirects, but the installer uses the
canonical slug.

## Compatibility

gdUnit4 tracks Godot releases. The latest release requires the newest Godot
line. When the target declares an older Godot, pin the matching gdUnit4 line:

| gdUnit4 | Godot |
| --- | --- |
| v6.x | 4.5 or newer |
| v5.x | 4.3 – 4.4.1 |
| v4.x | 4.2 – 4.4.dev2 |

## Opt-in gate

The module applies only when:

1. The `godot-project` module applies — `project.godot` exists at the root.
2. The project declares a Godot version the chosen release supports — 4.5 or
   newer for the latest line.
3. The user opts in at the Phase 2 confirm point.

Default: no.
