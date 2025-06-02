def is_palindrome(word):
    """
        Check if word is a palindrome
        Arguments:
        word - word to be check
    """
    if word.lower() == word.lower()[::-1]:
        return True
    else:
        return False

print(is_palindrome('Kajak'))