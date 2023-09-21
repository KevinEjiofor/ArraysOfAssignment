def reverse (word):
    return  word[:: -1]

if __name__ == "__main__":
    m = "Hello"
    result = reverse(m.casefold())

print(result)
