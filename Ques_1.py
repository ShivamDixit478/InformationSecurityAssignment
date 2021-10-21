# Write a program that can encrypt and decrypt using the Additive Cipher.

"""
Purpose :   This function encrypt the pain text using Additive chiper
Input   :   message -> plain text which we want to encrpty
            key -> integer, its key which tell how to charater shift
output  :   return the encrypted text
"""
def encrypt(message, key):
    encrypted_msg = ""
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # traverse text
    for character in message:        
        # Encrypt lowercase characters
        if character in lower_alphabet:
            shift = (lower_alphabet.index(character) + key) % len(lower_alphabet)
            encrypted_msg += lower_alphabet[shift]
        # Encrypt uppercase characters
        elif character in upper_alphabet:
            shift = (upper_alphabet.index(character) + key) % len(upper_alphabet)
            encrypted_msg += upper_alphabet[shift]
        # other than alphabet like digit , whitespace , symbol
        else:
            encrypted_msg += character

    return encrypted_msg


"""
Purpose :   This function decrpty the encrypted text using Additive chiper
Input   :   message -> encrypted text which we want to decrpty
            key -> integer, its key which tell how to charater shift
output  :   return the encrypted text
"""
def decrypt(message, key):
    key = key * -1
    # call the encrypted function with negative key to decrypted the message
    return encrypt(message, key)


# Driver code main
if __name__ == "__main__":
   
    key = int(input("ENTER THE KEY : "))
             
    while(True):
        print("\n1. ENCRYPTION \n2. DECRYPTION \n3. QUIT")
        choice = input("\nENTER YOUR CHOICE: ")

        if choice not in "123":
            print("INVALID KEY")
        elif choice == "1":
            message = input("\nENTER THE MESSAGE: ").lower()
            print("\nENCRYPTED MESSAGE : " + encrypt(message, key))
        elif choice == "2":
            message = input("Enter the encrypted message: ")
            print("\nDECRYPTED MESSAGE : " + decrypt(message, key))
        elif choice == "3":
            break
