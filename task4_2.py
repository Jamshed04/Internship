
def palindrome(st):
    rev_st = st[::-1]
    return st == rev_st


s = str(input("Введите строку "))
for i in range(0, len(s)):
    for j in range(i + 1, len(s) + 1):
        if palindrome(s[i:j]) and len(s[i:j]) > 1:
            print(s[i:j])
