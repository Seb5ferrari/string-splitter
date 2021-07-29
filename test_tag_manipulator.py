from tag_manipulator import TagManipulator


def test_split_empty_string_result_empty_array():
    # arrange
    stringToSplit = ""
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult


def test_split_comma_empty_string_result_empty_array():
    # arrange
    stringToSplit = ","
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)
    print(result)

    # assert
    assert result == expResult


def test_split_one_string_result_array_of_one():
    # arrange
    stringToSplit = "java"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)
    print(result)

    # assert
    assert result == expResult


def test_split_one_comma_start():
    # arrange
    stringToSplit = ",java"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)
    print(result)

    # assert
    assert result == expResult


def test_split_one_comma_end():
    # arrange
    stringToSplit = "java,"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)
    print(result)

    # assert
    assert result == expResult


def test_split_one_comma_in_between_tokens():
    # arrange
    stringToSplit = "java, python"
    regex = ","
    expResult = ["java", "python"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)
    print(result)

    # assert
    assert result == expResult
