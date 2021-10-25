
L= input("Input a length L:\n")
N = input("Input a number of messages N:\n")
n = int(N)
l = int(L)
# n= 2
# l = 60
plaintext_lst = []
ciphertext_lst = []
for i in range(n):
    plaintext_lst.append((input("Plaintext "+str(i)+":\n")))

for i in range(n):
    ciphertext_lst.append((input("Ciphertext "+str(i)+":\n")))


# For every plaintext and cipher pairs, iterate all over, until two keys match.
# This should take O(N^2*L), N^2 for iterating all over the plaintext-cipher pairs,
# the L is for the length of each of them.
previous_key = ""
key_string = ""
real_key = ""
key_list1 = []
key_list2 = []
key_list3 = []
# Need to have a key matrix?
for p in range(n):
    for p1 in range(n):
        for a in range(l):
            plain_hex = int(plaintext_lst[p][a], 16)
            cipher_hex = int(ciphertext_lst[p1][a],16)
            var = (plain_hex ^ cipher_hex)
            # print(hex(var))
            var1 = str(hex(var))[2:]
            # print(var1)
            # key_list.append(var1)
            key_string += var1
        if n < 2:
            real_key = key_string
        if p == 0:
            key_list1.append(key_string)
            key_string = ""

        elif p == 1:
            key_list2.append(key_string)
            key_string = ""
        elif p == 2:
            key_list3.append(key_string)
            key_string = ""


    # print(key_list1)
    # print(key_list2)
pair_list = []
identical_keys = []
for j in range(n):
    if n>1:
        for k in range(n):
            if key_list1[j] == key_list2[k]:
                identical_keys.append(key_list1[j])
                # real_key = key_list1[j]
                # print("k", k)
                # pair_list.append((j,k))

# print("identical_keys:\n", identical_keys)
for j in range(n):
    if n>2:
        for i in range(len(identical_keys)):
            if identical_keys[i] == key_list3[j]:
                real_key = identical_keys[i]

key_string = ""
for p in range(n):
    for c in range(n):
        for a in range(l):
            plain_hex = int(plaintext_lst[p][a], 16)
            cipher_hex = int(ciphertext_lst[c][a],16)
            var = (plain_hex ^ cipher_hex)
            # print(hex(var))
            var1 = str(hex(var))[2:]
            # print(var1)
            # key_list.append(var1)
            key_string += var1
        # print(key_string)
        if key_string == real_key:
            pair_list.append((p,c))
            key_string = ""
        else:
            key_string = ""



# Outputting pairs
# print("pairsss", pair_list)
list_of_pairs = []
for l,m in pair_list:
    list_of_pairs.append(("Plaintext"+str(l+1), "Ciphertext"+ str(m+1)))

# list_of_pairs.append("Plaintext"+)
print("Pairs:")
print(list_of_pairs)




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


if n>2:
    print("key:\n", key_string)
    print(real_key)
else:
    print("One of these keys are correct but cannot differentiate with n<3:\n", key_string)
    print(identical_keys)