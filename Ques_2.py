# Write a program that can encrypt and decrypt using the Affine Cipher.

lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# The gcd function is going to help co-prime function
def gcd(a, b):
    # Everything divides 0
    if (a == 0 or b == 0):
        return 0
    # base case
    if (a == b):
        return a
    # a is greater
    if (a > b):
        return gcd(a - b, b)
    return gcd(a, b - a)


# Function to check if two numbers are co-prime or not
def coprime(a, b):
    if (gcd(a, b) == 1):
        return True
    else:
        return False


"""
Purpose :   This function encrypt the pain text using Affine chiper
Input   :   message -> plain text which we want to encrpty
            key1 -> integer, must me co-prime of 26 and key to help encrypt plain text
            key2 -> integer , key to help encrypt plain text
output  :   return the encrypted text
"""
def encrypt(message, key1, key2):
    encrypted_msg = ""

    # traverse text
    # and  applying encryption formula ( a x + b ) mod m
    for character in message:
        # Encrypt uppercase characters
        if character in upper_alphabet:
            new_char = (key1 * upper_alphabet.index(character) + key2) % len(upper_alphabet)
            encrypted_msg += upper_alphabet[new_char]
        # Encrypt lowercase characters
        elif character in lower_alphabet:
            new_char = (key1 * lower_alphabet.index(character) + key2) % len(lower_alphabet)
            encrypted_msg += lower_alphabet[new_char]
        # other than alphabet like digit , whitespace , symbol
        else:
            encrypted_msg += character
    return encrypted_msg

# function to find out modular multiplicative inverse of a number
def mod_inverse(num, mod):
    for x in range(1, mod):
        flag = (num*x) % mod
        # Check if (num*x)%26 == 1 ,then x will be the multiplicative inverse of num
        if flag == 1:
            return x


"""
Purpose :   This function encrypt the pain text using Affine chiper
Input   :   message -> plain text which we want to encrpty
            key1 -> integer, must me co-prime of 26 and key to help encrypt plain text
            key2 -> integer , key to help encrypt plain text
output  :   return the encrypted text
"""
def decrypt(message, key1, key2):
    decrypted_msg = ""
    # Find key1^-1 (the multiplicative inverse of key1 in the group of integers modulo 26.)
    key_inverse = mod_inverse(key1, len(upper_alphabet))

    # traverse encrypted text
    # and Applying decryption formula a^-1 ( x - b ) mod m
    for character in message:
        # Encrypt uppercase characters
        if character in upper_alphabet:
            decrypt_char = ( key_inverse * (upper_alphabet.index(character) - key2)) % len(upper_alphabet)
            decrypted_msg += upper_alphabet[decrypt_char]
        # Encrypt lowercase characters
        elif character in lower_alphabet:
            decrypt_char = ( key_inverse * (lower_alphabet.index(character) - key2)) % len(lower_alphabet)
            decrypted_msg += lower_alphabet[decrypt_char]
        # other than alphabet like digit , whitespace , symbol
        else:
            decrypted_msg += character

    return decrypted_msg


# Driver code main
if __name__ == "__main__":
    while(True):
        key1 = int(input("ENTER THE FIRST KEY (MUST BE COPRIME OF 26)"))
        if not (coprime(key1, len(lower_alphabet))):
            print("FIRST KEY IS THE COPRIME OF 26")
            continue
        key2 = int(input("ENTER THE SECOND KEY : "))
        break
        
    while(True):
        print("\n1. ENCRYPTION \n2. DECRYPTION \n3. QUIT")
        choice = input("\nENTER YOUR CHOICE: ")

        if choice not in "123":
            print("INVALID OPTION")
        elif choice == "1":
            message = input("\nENTER THE MESSAGE: ")
            print("\nENCRYPTED MESSAGE : " +
                    encrypt(message, key1, key2))
        elif choice == "2":
            message = input("ENTER THE ENCRYPTED MESSAGE: ")
            print("\nDECRYPTED MESSAGE : " +
                    decrypt(message, key1, key2))
        elif choice == "3":
            break
        