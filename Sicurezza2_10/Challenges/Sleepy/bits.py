FLAG = 'zZZzzZZz zZZzZZzz zZZzzzzZ zZZzzZZZ zZZZZzZZ zZzzZzzZ zzZzzzzz zZzzZZzz zZZzZZZZ zZZZzZZz zZZzzZzZ zzZzzzzz zZzzzzzZ zZzZzzZZ zZzzzzZZ zZzzZzzZ zZzzZzzZ zZZZZZzZ'

def sleepy(s):
    # Convert string to binary with zero-fill to 8 bits
    binary = ''.join(format(ord(i), '08b').zfill(8) for i in s)

    # Replace 0 with lowercase letter and 1 with uppercase letter
    encoded = binary.replace('0', 'z').replace('1', 'Z')

    # Add a space after every 8 characters
    readable_encoded = ' '.join(encoded[i:i+8] for i in range(0, len(encoded), 8))

    return readable_encoded

def awake(s):
    # Rimuovere gli spazi e sostituire le lettere con bit
    binary_str = s.replace('z', '0').replace('Z', '1').replace(' ', '')
    
    # Convertire ogni 8 bit in un carattere ASCII
    decoded_chars = [chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8)]
    
    # Ricostruire la stringa originale
    return ''.join(decoded_chars)

# output
print(awake(FLAG))

