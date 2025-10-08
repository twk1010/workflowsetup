# test_main.py

from main import add

def test_add_success():
    # ✅ Should pass
    assert add(2, 3) == 5
