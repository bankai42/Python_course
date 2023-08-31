def getAbbr(string):
    try:
        words = string.split()
        abbr = ''
        for word in words:
            abbr += word[0]

        return str(abbr)
    except Exception:
        print('Incorrect input data')

string_1 = 'This is String'
string_2 = 123
print(getAbbr(string_1))
