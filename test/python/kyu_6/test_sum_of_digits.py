import pytest

from python.kyu_6.sum_of_digits import digital_root

EXAMPLES = (
    ("input", "output"),
    [(16, 7), (456, 6,),],
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(input, output):
    assert digital_root(input) == output
