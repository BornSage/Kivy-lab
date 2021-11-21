import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM == TCPiP

server.bind(("127.0.0.1", 8888))

server.listen(5)


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
    print(word, "+", key, "=", encrypted)
    return encrypted


def decipher(enc_key, enc_input):
    deciphered = ""
    word = enc_input  # enc_input.text.upper()
    key = enc_key  # enc_key.text.upper()

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
    print(word, "+", key, "=", deciphered)
    return deciphered


user_socket, address = server.accept()

while True:
    print("Listening...")
    data = user_socket.recv(2048).decode("utf-8")
    data = data.split()
    if data[2] == "Encrypt":
        new_data = encrypt(data[0], data[1])
    else:
        new_data = decipher(data[0], data[1])
    user_socket.send(new_data.encode("utf-8"))
