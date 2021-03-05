select = input('Type denary for denary conversion or binary for binary conversion: ').lower()
# conversion of denary to binary
def choose(option):
    if option == 'binary':
        denary = int(input('Enter the number for binary conversion: '))
        binary = ''
        while denary != 0:
            mod_value = denary % 2
            binary += str(mod_value)
            denary = denary//2
        binary = binary[::-1]
        print(binary)
#conversion of binary to denary
    else:
        binary = input('Enter the number for denary conversion: ')
        denary = 0
        value = binary[::-1]
        mul = 1
        for numbers in value:
            denary += int(numbers) * mul
            mul = mul * 2
        print(denary)
choose(select)
