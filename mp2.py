import re

cases = int(input())

for i in range(cases):
    regEx = input().strip().replace(' ', '').replace('e', '')
    regEx = regEx.replace('+','|')
    stringSize = int(input())
    strings = [input().strip().replace('e', '') for i in range(stringSize)]

    for string in strings:
        if re.fullmatch(regEx, string):
            print("yes")
        else:
            print("no")