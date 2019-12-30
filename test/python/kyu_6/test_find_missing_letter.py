import pytest

from python.kyu_6.find_the_missing_letter import find_missing_letter

EXAMPLES = (
    ("input", "output"),
    [(["a", "b", "c", "d", "f"], "e"), (["O", "Q", "R", "S"], "P")],
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(input, output):
    assert find_missing_letter(input) == output
