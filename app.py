import hashlib


with open('document.txt', 'r') as file:
    content = file.read()

    teks_list = content.splitlines()
    pin = ''
    for teks in teks_list:
        hash_hex = hashlib.md5(teks.encode()).hexdigest()
        pin += str(int(hash_hex, 16))[:4]
print("PIN:", pin)
