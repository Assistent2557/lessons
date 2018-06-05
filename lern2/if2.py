
str1 = input ('Введите первую строку\n')
str2 = input ('Введите вторую строку\n')
if str1 == str2:
    print('1')
elif len(str1) < len(str2) and str2 != 'learn':
    print('2')
elif len(str1) < len(str2):
    print('3')
