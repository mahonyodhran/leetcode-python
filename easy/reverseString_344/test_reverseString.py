from reverseString344 import reverseString

def test_reverse_string_one():
    input = ["h","e","l","l","o"]
    reversed = reverseString(input)
    assert reversed == ["o","l","l","e","h"]
    
def test_reverse_string_two():
    input = ["H","a","n","n","a","h"]
    reversed = reverseString(input)
    assert reversed == ['h', 'a', 'n', 'n', 'a', 'H']
