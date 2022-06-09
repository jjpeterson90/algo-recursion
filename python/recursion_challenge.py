def factorial(x):
    if x < 2:
        return 1
    return x * factorial(x-1)


def palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    return False


def bottles(num, original=None):
    if original == None:
        original = num
    if num == 0:
        print('No more bottles of beer on the wall, no more bottles of beer.')
        if original != 1:
            print(f'Go to the store and buy some more, {original} bottles of beer on the wall.')
        else:
            print(f'Go to the store and buy some more, {original} bottle of beer on the wall.')
    else:
        if num == 1:
            bottle = 'bottle'
            reduced_num = 'no more'
            new_bottle = 'bottles'
        if num >= 2:
            bottle = 'bottles'
            reduced_num = num-1
            if reduced_num == 1:
                new_bottle = 'bottles'
            else:
                new_bottle = 'bottle'
        print(f'{num} {bottle} of beer on the wall, {num} {bottle} of beer.')
        print(f'Take one down and pass it around, {reduced_num} {new_bottle} of beer on the wall.')
        return bottles(num-1, original)



ROMAN_TO_ARABIC = {'M': 1000,'CM': 900,'D': 500,'CD': 400,'C': 100,'XC': 90,'L': 50,'XL': 40,'X': 10,'IX': 9,'V': 5,'IV': 4,'I': 1,}
def to_roman_recursive(num, roman_result = '', roman_to_arabic = ROMAN_TO_ARABIC):
    if num == 0:
        return roman_result
    for key in roman_to_arabic:
        if num / roman_to_arabic[key] >= 1:
            return to_roman_recursive(num - roman_to_arabic[key], roman_result + key, roman_to_arabic)