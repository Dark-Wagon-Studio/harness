extends GdUnitTestSuite


func test_addition_holds() -> void:
	assert_int(1 + 1).is_equal(2)
