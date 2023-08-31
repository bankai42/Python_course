def getMaxLen(string_1, string_2):
    return max(len(string_1), len(string_2))

string_1 = input('Input first string: ')
string_2 = input('Input second string: ')
print('Max length is ' + str(getMaxLen(string_1, string_2)))