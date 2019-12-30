import pytest

from python.kyu_6.duplicate_encoder import duplicate_encode

EXAMPLES = (
    ("input", "output"),
    [
        ("din","((("),
        ("recede","()()()"),
        ("Success",")())())"),
        ("(( @","))((")
    ],
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(input, output):
    assert duplicate_encode(input) == output
