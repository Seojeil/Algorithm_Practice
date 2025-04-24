import sys

input = sys.stdin.readline

T = int(input())


def recursion(word, l, r, count):
    count += 1

    if l >= r:
        return 1, count
    elif word[l] != word[r]:
        return 0, count
    else:
        return recursion(word, l+1, r-1, count)


def isPalindrome(word):
    count = 0
    result, calls = recursion(word, 0, len(word)-1, count)
    return result, calls


for _ in range(T):

    word = input()[:-1]

    palindrome, count = isPalindrome(word)

    print(palindrome, count)
