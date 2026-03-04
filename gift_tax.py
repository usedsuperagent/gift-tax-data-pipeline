# Gift Tax Calculator
# Calculates gift tax based on Finnish tax brackets
# Author: Ricky W.

value = int(input('Value of gift: '))
tax_1 = 100 + (value - 5000) * 0.08
tax_2 = 1700 + (value - 25000) * 0.10
tax_3 = 4700 + (value - 55000) * 0.12
tax_4 = 22100 + (value - 200000) * 0.15
tax_5 = 142100 + (value - 1000000) * 0.17

if value < 5000:
    print('No tax!')
elif 5000 <= value < 25000:
    print(f'Amount of tax: {tax_1}')
elif 25000 <= value < 55000:
    print(f'Amount of tax: {tax_2}')
elif 55000 <= value < 200000:
    print(f'Amount of tax: {tax_3}')
elif 200000 <= value < 1000000:
    print(f'Amount of tax: {tax_4}')
else:
    print(f'Amount of tax: {tax_5}')