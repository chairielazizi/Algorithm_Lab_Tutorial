def isPalindrome(word):
    for i in range(0,len(word),1):
        if word[i]!=(word[len(word)-1-i]):
            return False
    return True

str=raw_input("Enter a string:")

if isPalindrome(str):
    print("%s is a palindrome"%str)
else:
    print("%s is not a palindrome"%str)