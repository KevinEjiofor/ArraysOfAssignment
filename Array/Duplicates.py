def check_duplicates(word):
    dup = [i for i in word if word.count(i) > 1]
    return dup[0]


print(check_duplicates(["james", "paul", "paul", "paul" ,"peter", "james"]))

# if len(word) != len(set(word)):
