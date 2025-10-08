# test_main.py

from main import add

def test_add_success():
    # ✅ Should pass
    assert add(2, 3) == 5

def test_add_fail():
    # ❌ Intentionally fails
    assert add(3, 5) == 1
