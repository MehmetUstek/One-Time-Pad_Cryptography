
import os,binascii

L= input("Input a length L:\n")
N = input("Input a number of messages N:\n")
n = int(N)
l = int(L)
plaintext_lst = []
for i in range(n):
    plaintext_lst.append((input("Plaintext "+str(i)+":\n")))

for p in range(n):
    pass

key = binascii.b2a_hex(os.urandom(l))
print("key:\n",key)
