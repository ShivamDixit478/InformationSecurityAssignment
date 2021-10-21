# Write a program that can encrypt and Decrypt using a 2 X 2 Hill Cipher
# pip install numpy

import numpy as np


alphabet = "abcdefghijklmnopqrstuvwxyz"+" "

"""
Purpose :   Function used to generate key matrix which use for encrpty and decrypt text
Input   :   key -> string , used to generate key matrix
Output  :   return key matrix
"""
def generate_key_marix(key):
    key_matrix = [[0]*2 for _ in range(2)]
    k = 0
    for i in range(2):
        for j in range(2):
            key_matrix[i][j] = alphabet.index(key[k])
            k += 1
    return key_matrix


"""
Pupose  :   Function used to convert text into martix(that has been mapped to numbers) and split it in correct size
Input   :   message -> Text which hab been mapped to number then convert into martix and then split into matrix of 2 x 1
Ouput   :   return matrix which is mapped according to message
"""
def text_to_matrix(messaage):
    messaage_in_number = [alphabet.index(char) for char in messaage]
    messaage_matrix = [messaage_in_number[i:i + 2]
                       for i in range(0, len(messaage_in_number), 2)]
    return messaage_matrix


"""
Purpose :   Convert the matrix into text
Input   :   matrix  -> matrix which we want to convert
Output  :   return converted text
"""
def matrix_to_text(matrix):
    text = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            text += alphabet[matrix[i][j]]
    return text


"""
Purpose :   Function to encrypt plain text using Hill chiper
Input   :   meassge -> plain text matrix to encrypt
            key ->  key matrix which used to encrypt
Ouput   :   return encrypted text
"""
def encrypt(message, key):
    # convert text to matrix
    message = text_to_matrix(message)

    encrypted_message = list()

    # iterate through each partial message
    # encryt using (K*P)mod26
    for P in message:
        # P = Vector of plaintext (that has been mapped to numbers)
        while len(P) != len(key):
            P.append(alphabet.index(" "))
        P = np.transpose(np.asarray(P))

        encrypted_message.append(np.dot(key, P) % len(alphabet))

    # convert into text and return it
    return matrix_to_text(encrypted_message)


"""
Purpose :   Find the matrix modulus inverse by
            Step 1) Find determinant
            Step 2) Find determinant value in a specific modulus (usually length of alphabet)
            Step 3) Take that det_inv times the det*inverted matrix (this will then be the adjoint) in mod 26
Input   :   matrix  -> which whose matrix modulus inverse we want to find
            mod -> specific modulus (usually length of alphabet)
Output  :   return martix modulus inverse of given matrix
"""
def matrix_mod_inverse(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))  # step 1
    # step 2
    det_inv = mod-1
    for x in range(1, mod+1):
        flag = (det*x) % mod
        if flag == 1:
            det_inv = x
            break
    matrix_modulus_inverse = det_inv * \
        np.round(det*np.linalg.inv(matrix)).astype(int) % mod  # step 3
    return matrix_modulus_inverse


"""
Purpose :   Function to decrypt encrypted text using Hill chiper
Input   :   meassge -> plain text matrix to encrypt
            key ->  key matrix which used to encrypt
Ouput   :   return encrypted text
"""
def decrypt(message, key):
    # convert text to matrix
    message = text_to_matrix(message)

    decrypted_message = list()

    # Find K_inverse (the matrix modulus inverse of key with modulus 26)
    K_inv = matrix_mod_inverse(key, len(alphabet))

    # iterate through each partial chiper text
    # decrypt using inv(K)*C mod 26
    for C in message:
        # C = Vector of Ciphered text (in numbers)
        C = np.transpose(np.asarray(C))
        decrypted_message.append(np.dot(K_inv, C) % len(alphabet))

    # Convert dechipered matrix into text and return it
    return matrix_to_text(decrypted_message)


# Driver Code Main
if __name__ == "__main__":
    while(True):
        key = input("ENTER THE KEY(LENGTH MUST NOT GREATER THAN 4): ").lower()
        if len(key) == 4 :
            break
        else:
            print("ENTER CORRECT KEY")
    key = generate_key_marix(key)
    while(True):
        print("\n1. ENCRYPTION \n2. DECRYPTION \n3. QUIT")
        choice = input("\nENTER YOUR CHOICE: ")

        if choice not in "123":
            print("INVALID OPTION")
        elif choice == "1":
            message = input("\nENTER THE MESSAGE: ").lower()
            print("\nENCRYPTED MESSAGE : " + encrypt(message, key))
        elif choice == "2":
            message = input("ENTER THE ENCRYPTED MESSAGE: ").lower()
            print("\nDECRYPTED MESSAGE : " + decrypt(message, key))
        elif choice == "3":
            break
