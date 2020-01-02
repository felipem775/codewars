import pytest

from python.kyu_6.is_integer_array import is_int_array

EXAMPLES = (
    ("input", "output", "values"),
    [
        ([], True, "Input: []"),
        ([1, 2, 3, 4], True, "Input: [1, 2, 3, 4]"),
        ([-11, -12, -13, -14], True, "Input: [-11, -12, -13, -14]"),
        ([1.0, 2.0, 3.0], True, "Input: [1.0, 2.0, 3.0]"),
        ([1, 2, None], False, "Input: [1,2, None]"),
        (None, False, "Input: None"),
        ("", False, "Input: ''"),
        ([None], False, "Input: [None]"),
        ([1.0, 2.0, 3.0001], False, "Input: [1.0, 2.0, 3.0001]"),
        (["-1"], False, "Input: ['-1']"),
    ],
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(input, output, values):
    assert is_int_array(input) == output
