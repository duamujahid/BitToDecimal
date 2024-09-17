def binary_to_decimal(binary):
    
    decimal = 0
    base = 1
    temp = int(binary)
    
    while temp > 0:
        last_digit = temp % 10
        decimal += last_digit * base
        base = base * 2
        temp = temp // 10
    
    return decimal

binary_input1 = "010"
binary_input2 = "1101"

print("Binary: {binary_input1} => Decimal: {binary_to_decimal(binary_input1)}")
print("Binary: {binary_input2} => Decimal: {binary_to_decimal(binary_input2)}")
