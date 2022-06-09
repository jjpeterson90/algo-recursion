from recursion_challenge import factorial, palindrome, bottles, to_roman_recursive

print("\n\n--== Factorial ==--")
print(factorial(5)) # 120
print(factorial(8)) # 40320

print("\n\n--== Palindrome ==--")
print(palindrome('racecar')) # True
print(palindrome('railcar')) # False

print("\n\n--== 99 Bottles Song ==--")
print(bottles(5))

print("\n\n--== Arabic to Roman ==--")
print(to_roman_recursive(27)) # XXVII
print("\n")