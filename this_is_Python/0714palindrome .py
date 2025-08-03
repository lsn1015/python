def is_palindrome(phrase):
    cleaned = [i for i in phrase.lower() if phrase.isalnum()]
    return cleaned == cleaned[::-1]

print(is_palindrome('abba'))

