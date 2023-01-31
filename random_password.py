import random

loop = True
while loop:
    try:
        pass_length = int(input("Masukkan panjang password: "))
        char = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$&*?~"
        password = "".join(random.sample(char, pass_length))
        print(password)
        loop = False
    except:
        print("Masukkan angka saja!")
