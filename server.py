import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM == TCPiP

server.bind(("127.0.0.1", 8888))

server.listen(5)



arr = [0]*26
for i in range(26):
    arr[i] = [0]*26
n=0
for i in range(26):
    for j in range(26):

        arr[i][j] = chr(n+65)
        n+=1
        if n+65>90:
            n = 0
    n+=1

def encrypt_with_table(enc_key, enc_input):
    global arr
    encrypted = ""
    word = enc_input
    key = enc_key

    temporal_key = ""
    for i in range(len(key)):
        if 65 <= ord(key[i]) <= 90:
            temporal_key += key[i]
    key = temporal_key

    j = 0
    for i in range(len(word)):
        if 65 <= ord(word[i]) <= 90:
            encrypted += arr[ord(key[j]) - 65][ord(word[i]) - 65]
        else:
            encrypted += word[i]
        j += 1
        if j >= len(key):
            j = 0
    print("encrypted with table", word, "+", key, "=", encrypted)
    return encrypted


def decipher_with_table(enc_key, enc_input):
    global arr
    deciphered = ""
    word = enc_input
    key = enc_key

    temporal_key = ""
    for i in range(len(key)):
        if 65 <= ord(key[i]) <= 90:
            temporal_key += key[i]
    key = temporal_key

    j = 0
    check = 0
    for i in range(len(word)):
        if 65 <= ord(word[i]) <= 90:
            for n in range(26):
                if arr[ord(key[j]) - 65][n] == word[i]:
                    check = n
                    break

            deciphered += arr[0][n]
        else:
            deciphered += word[i]
        j += 1
        if j >= len(key):
            j = 0
    print("deciphered with table- ",word, "+", key, "=", deciphered)
    return deciphered

def encrypt(enc_key, enc_input):
    encrypted = ""
    word = enc_input
    key = enc_key

    word = word.replace(" ", "")

    temporal_key = ""
    for i in range(len(key)):
        if 65 <= ord(key[i]) <= 90:
            temporal_key += key[i]
    key = temporal_key

    j = 0
    for i in range(len(word)):
        if 65 <= ord(word[i]) <= 90 and (ord(key[j]) - 65) + (ord(word[i]) - 65) <= 25:  # 65 - ROT0 ("a" преобразуется в "а"); 64 - ROT1 ("а" преобразуется в "б")
            encrypted += chr(((ord(key[j]) - 65) + (ord(word[i]) - 65)) + 65)
        elif 65 <= ord(word[i]) <= 90 and (ord(key[j]) - 65) + (ord(word[i]) - 65) > 25:
            encrypted += chr(((ord(key[j]) - 65) + (ord(word[i]) - 65)) - 26 + 65)
        else:
            encrypted += word[i]
        j += 1
        if j >= len(key):
            j = 0
    print("encrypted with formula- ",word, "+", key, "=", encrypted)
    return encrypted


def decipher(enc_key, enc_input):
    deciphered = ""
    word = enc_input
    key = enc_key

    word = word.replace(" ", "")

    temporal_key = ""
    for i in range(len(key)):
        if 65 <= ord(key[i]) <= 90:
            temporal_key += key[i]
    key = temporal_key

    j = 0
    for i in range(len(word)):
        if 65 <= ord(word[i]) <= 90 and (ord(word[i]) - 65) - (ord(key[j]) - 65) >= 0:  # 65 - ROT0 ("a" преобразуется в "а") 25; 64 - ROT1 ("а" преобразуется в "б") 26!!!
            deciphered += chr(((ord(word[i]) - 65) - (ord(key[j]) - 65)) + 65)
        elif 65 <= ord(word[i]) <= 90 and ord(word[i]) - 65 - ord(key[j]) - 65 < 0:
            deciphered += chr(((ord(word[i]) - 65) - (ord(key[j]) - 65)) + 26 + 65)
        else:
            deciphered += word[i]
        j += 1
        if j >= len(key):
            j = 0
    print("deciphered with formula- ",word, "+", key, "=", deciphered)
    return deciphered
'''
users = []
def listen_and_send(user_socket):
    while True:
        data = user_socket.recv(2048).decode("utf-8")
        data = data.split()
        if data[2] == "Encrypt":
            if data[3] == "Formula":
                new_data = encrypt(data[0], data[1])
                label_data = "encrypted with formula= " + new_data
            else:
                new_data = encrypt_with_table(data[0], data[1])
                label_data = "encrypted with table= " + new_data
        else:
            if data[3] == "Formula":
                new_data = decipher(data[0], data[1])
                label_data = "deciphered with formula= " + new_data
            else:
                new_data = decipher_with_table(data[0], data[1])
                label_data = "deciphered with table= " + new_data
        user_socket.send(new_data.encode("utf-8"))
        user_socket.send(label_data.encode("utf-8"))
'''
user_socket, address = server.accept()
while True:

    print("Listening...")
    #users.append(user_socket)
    #user = Thread(target=listen_and_send, args=(user_socket,))
    #user.start()

    data = user_socket.recv(2048).decode("utf-8")
    data = data.split()
    if data[2] == "Encrypt":
        if data[3] == "Formula":
            new_data = encrypt(data[0], data[1])
            label_data = "encrypted with formula= "+new_data
        else:
            new_data = encrypt_with_table(data[0],data[1])
            label_data = "encrypted with table= " + new_data
    else:
        if data[3] == "Formula":
            new_data = decipher(data[0], data[1])
            label_data = "deciphered with formula= " + new_data
        else:
            new_data = decipher_with_table(data[0],data[1])
            label_data = "deciphered with table= " + new_data
    user_socket.send(new_data.encode("utf-8"))
    user_socket.send(label_data.encode("utf-8"))

