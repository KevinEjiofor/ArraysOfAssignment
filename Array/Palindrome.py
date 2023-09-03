def is_palindrome(word):
    words = word[::1] == word[:: -1]

    return words


letter  = ["a", "d", "e"]
call = is_palindrome(letter)
print(call)
