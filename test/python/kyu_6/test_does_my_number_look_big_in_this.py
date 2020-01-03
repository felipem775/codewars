import pytest

from python.kyu_6.does_my_number_look_big_in_this import narcissistic

EXAMPLES = (
    ("input", "output", "comment"),
    [
        (7, True, "7 is narcissistic"),
        (371, True, "371 is narcissistic"),
        (122, False, "122 is not narcissistic"),
        (4887, False, "4887 is not narcissistic"),
    ],
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(input, output, comment):
    assert narcissistic(input) == output
