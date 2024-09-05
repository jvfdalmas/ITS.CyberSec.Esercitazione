def decimal_to_binary(decimal):
    return bin(decimal).replace("0b", "")

def hex_to_binary(hex_num):
    return bin(int(hex_num, 16)).replace("0b", "")

def binary_to_decimal(binary):
    return int(binary, 2)

def binary_to_hex(binary):
    return hex(int(binary, 2)).replace("0x", "").upper()

def add_binary(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2)).replace("0b", "")

def subtract_binary(bin1, bin2):
    return bin(int(bin1, 2) - int(bin2, 2)).replace("0b", "")

def multiply_binary(bin1, bin2):
    return bin(int(bin1, 2) * int(bin2, 2)).replace("0b", "")

def divide_binary(bin1, bin2):
    return bin(int(bin1, 2) // int(bin2, 2)).replace("0b", "")

def main():
    while True:
        print("\nMenu:")
        print("1. Convert Decimal to Binary")
        print("2. Convert Hexadecimal to Binary")
        print("3. Convert Binary to Decimal")
        print("4. Convert Binary to Hexadecimal")
        print("5. Add two Binary Numbers")
        print("6. Subtract two Binary Numbers")
        print("7. Multiply two Binary Numbers")
        print("8. Divide two Binary Numbers")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            decimal = int(input("Enter a decimal number: "))
            print(f"Binary: {decimal_to_binary(decimal)}")
        
        if choice == '2':
            hex_num = input("Enter a hexadecimal number: ")
            print(f"Binary: {hex_to_binary(hex_num)}")
        
        if choice == '3':
            binary = input("Enter a binary number: ")
            print(f"Decimal: {binary_to_decimal(binary)}")
        
        if choice == '4':
            binary = input("Enter a binary number: ")
            print(f"Hexadecimal: {binary_to_hex(binary)}")
        
        if choice == '5':
            bin1 = input("Enter the first binary number: ")
            bin2 = input("Enter the second binary number: ")
            print(f"Result: {add_binary(bin1, bin2)}")
        
        if choice == '6':
            bin1 = input("Enter the first binary number: ")
            bin2 = input("Enter the second binary number: ")
            print(f"Result: {subtract_binary(bin1, bin2)}")
        
        if choice == '7':
            bin1 = input("Enter the first binary number: ")
            bin2 = input("Enter the second binary number: ")
            print(f"Result: {multiply_binary(bin1, bin2)}")
        
        if choice == '8':
            bin1 = input("Enter the first binary number: ")
            bin2 = input("Enter the second binary number: ")
            print(f"Result: {divide_binary(bin1, bin2)}")
        
        if choice == '9':
            break

if __name__ == "__main__":
    main()
