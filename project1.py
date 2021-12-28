L= input("Input a length L:\n")
N = input("Input a number of messages N:\n")
n = int(N)
l = int(L)
# n= 2
# l = 60
plaintext_lst = []
ciphertext_lst = []
for i in range(n):
    plaintext_lst.append((input("Plaintext "+str(i+1)+":\n")))

for i in range(n):
    ciphertext_lst.append((input("Ciphertext "+str(i+1)+":\n")))


# For every plaintext and cipher pairs, iterate all over, until two keys match.
# This should take O(N^2*L), N^2 for iterating all over the plaintext-cipher pairs,
# the L is for the length of each of them.
previous_key = ""
key_string = ""
real_key = ""
key_list1 = []
key_list2 = []
key_list3 = []
# Observed from the loops, the complexity is indeed O(N^2*L)
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
# O(N^2) here for getting the identical keys.
for j in range(n):
    if n>1:
        for k in range(n):
            if key_list1[j] == key_list2[k]:
                identical_keys.append(key_list1[j])
                # real_key = key_list1[j]
                # print("k", k)
                # pair_list.append((j,k))

# print("identical_keys:\n", identical_keys)
# Getting the identical keys from n=2, and applying it to a next possible key,
# which will give the real key value.
for j in range(n):
    if n>2:
        for i in range(len(identical_keys)):
            if identical_keys[i] == key_list3[j]:
                real_key = identical_keys[i]

# Now, we know the key, it is time to reveal every pair.
# This is again O(N^2*L) which will yield a total of O(N^2*L) complexity.
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
list_of_pairs = []
for l,m in pair_list:
    list_of_pairs.append(("Plaintext"+str(l+1), "Ciphertext"+ str(m+1)))

print("Pairs:")
print(list_of_pairs)

# Given data for test.
# Plaintext 1: 5769736874686174496861646265656e626f726e6c6f6e676265666f7265
# Plaintext 2: 4d7962726f7468657273676f746d657570616761696e737474686577616c
# Plaintext 3: 4f6e656d6f7265646179616e644977696c6c62655468656b696e67466f72
# Ciphertext 1: d7e1b2e3e7432e2eb0fb14e84c4a77e1f6331f8eceed0b4ce72e0760ebde
# Ciphertext 2: d5f6b5fce745232fa3f112e95c6e65fdea3e1a8af3eb1d53fa280551e5c0
# Ciphertext 3: cdf1a3f9fc5f273f8be012e35a4277fae43d0a81cbec165ff1230478f8d7

if n>2:
    print("key:", key_string)
    print(real_key)
else:
    print("One of these keys are correct but cannot differentiate with n<3:\n", key_string)
    print(identical_keys)

# The output of the example in the assignment is as follows:
# Pairs:
# [('Plaintext1', 'Ciphertext3'), ('Plaintext2', 'Ciphertext1'), ('Plaintext3', 'Ciphertext2')]
# key:
# 9a98d0918837464bc288738738271294865278efa7837838934662178ab2

# Test
# Pt1:
# 30343334303039343034666a66723066346a766a32333972393332376b63736e656f39787a31302e
# Ct1:
# 9ff9cd60e3421dcf5a2786ed11dcfa0b9cb8d1b8dad8d4e20de3bd4398ded69161ec9b5242c50552
# Pt2:
# 33387265387575646864643965393433307039303463c4b176c4b166766a76666ac4b1333033396b
# Ct2:
# 9cf58c31eb07519f027784be1297fe5e98a29ee2dc88292142143e1285d7d3996e47131908c70c17
# Pt3:
# 78687565646d64387a326e6d6479393466383939663875383932336d79373837686a647a38307633
# Ct3:
# d7a58b31b71f40c310218eea13d7f359ceea9eeb8ed398a80de2bc198a8a9dc86ce9c65000c4434f
# Pt4:
# 687565c4b164c4b16575643833386475387563c3b639633375383364c4b139636cc3b67665303233
# Ct4:
# c7b89b906216e04a0f6684bf4496ae1890a7c4115ed28ea341e8bc10370c9c9c6840145c5dc4074f
# Pt5:
# 30723975386c6b7864396564396d6478653839307a656b6c306678396d657739666dc3b665666532
# Ct5:
# 9fbfc721eb1e4f830e2a85e34ec3ae15cdea9ee2928e86fc04b6f74d9ed8d2c662ee619c5d92504e
# Pt6:
# 38657a38656d337a39386d66386d3866386d3cc4b1706164786b7a30397ac3b6646b39646dc3b638
# Ct6:
# 97a8846cb61f1781532b8de14fc3f20b90bf9b16599b8cf44cbbf544cac7664960e89b4e55378344

# When this test runs, with the corresponding pairs (unshuffled) the result is:
# Pairs:
# [('Plaintext1', 'Ciphertext1'), ('Plaintext2', 'Ciphertext2'), ('Plaintext3', 'Ciphertext3'), ('Plaintext4', 'Ciphertext4'), ('Plaintext5', 'Ciphertext5'), ('Plaintext6', 'Ciphertext6')]
# key:
# afcdfe54d37224fb6a13e08777aeca6da8d2a7d2e8ebed9034d08f74f3bda5ff0483a22a38f4357c
# which yields the correct result.
# Moreover, the program yields the same key result for every iteration of plaintext - ciphertext pair.
