
import os,binascii

# L= input("Input a length L:\n")
# N = input("Input a number of messages N:\n")
# n = int(N)
# l = int(L)
n= 2
l = 60
plaintext_lst = ["5769736874686174496861646265656e626f726e6c6f6e676265666f7265","4d7962726f7468657273676f746d657570616761696e737474686577616c","4f6e656d6f7265646179616e644977696c6c62655468656b696e67466f72"]
ciphertext_lst = ["cdf1a3f9fc5f273f8be012e35a4277fae43d0a81cbec165ff1230478f8d7","d5f6b5fce745232fa3f112e95c6e65fdea3e1a8af3eb1d53fa280551e5c0","cdf1a3f9fc5f273f8be012e35a4277fae43d0a81cbec165ff1230478f8d7"]
# for i in range(n):
#     plaintext_lst.append((input("Plaintext "+str(i)+":\n")))
#
# for i in range(n):
#     ciphertext_lst.append((input("Ciphertext "+str(i)+":\n")))


# For every plaintext and cipher pairs, iterate all over, until two keys match.
# This should take O(N^2*L), N^2 for iterating all over the plaintext-cipher pairs,
# the L is for the length of each of them.
key_list = []
key_string = ""
for p in range(n):
    for a in range(l):
        plain_hex = int(plaintext_lst[p][a],16)
        cipher_hex = int(ciphertext_lst[p][a],16)
        var = (plain_hex ^ cipher_hex)
        # print(hex(var))
        var1 = str(hex(var))[2:]
        # print(var1)
        # key_list.append(var1)
        key_string += var1

    key_list.append(key_string)



# Plaintext 1: 5769736874686174496861646265656e626f726e6c6f6e676265666f7265
# Plaintext 2: 4d7962726f7468657273676f746d657570616761696e737474686577616c
# Plaintext 3: 4f6e656d6f7265646179616e644977696c6c62655468656b696e67466f72
# Ciphertext 1: d7e1b2e3e7432e2eb0fb14e84c4a77e1f6331f8eceed0b4ce72e0760ebde
# Ciphertext 2: d5f6b5fce745232fa3f112e95c6e65fdea3e1a8af3eb1d53fa280551e5c0
# Ciphertext 3: cdf1a3f9fc5f273f8be012e35a4277fae43d0a81cbec165ff1230478f8d7

# for p in range(n):
#     obj = bytes.fromhex(plaintext_lst[i])
#     ascii_string = obj.decode("ASCII")
#     print(ascii_string)

# key = binascii.b2a_hex(os.urandom(l))
key = ""
print("key:\n",key_string)
