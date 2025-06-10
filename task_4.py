def is_palindrome(object):
    return object == object[::-1]


object = "!2A"
print(is_palindrome(object) is False)
object = "Racecar"
print(is_palindrome(object) is False)
object = [1, 2, 3, 2, 1]
print(is_palindrome(object) is True)
