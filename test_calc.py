# test_calc.py
# Create a file called test_calc.py
with open("test_calc.py", "w") as f:
    f.write("""
from calc import add, subtract

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2
""")
