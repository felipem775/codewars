import pytest

from python.kyu_6.your_order_please import order

EXAMPLES = (
    ("unordered", "ordered"),
    [
        ("is2 Thi1s T4est 3a", "Thi1s is2 3a T4est"),
        ("4of Fo1r pe6ople g3ood th5e the2", "Fo1r the2 g3ood 4of th5e pe6ople"),
        ("", ""),
    ],
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(unordered, ordered):
    assert order(unordered) == ordered
