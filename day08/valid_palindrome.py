def isPalindrome(s):
    new_s = ""

    for char in s:
        if char.isalnum():
            new_s += char.lower()

    return new_s == new_s[::-1]


s = "A man, a plan, a canal: Panama"

print(isPalindrome(s))