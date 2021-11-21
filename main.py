from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class BoxLayoutLab(BoxLayout):
    '''
    def on_toggle_button_state(self, toggle):
        if toggle.state == "down":
            toggle.text = "Decipher"
        else:
            toggle.text = "Encrypt"
    '''
    def dodo(self, key, input, output, toggle):
        if toggle.text == "Encrypt":
            self.encrypt(key.text.upper(), input.text.upper(), output)

        else:
            self.decipher(key.text.upper(), input.text.upper(), output)


    def decipher(self, enc_key, enc_input, enc_output):
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
        enc_output.text = deciphered
        print(word, "+", key, "=", deciphered)

    def encrypt(self, enc_key, enc_input, enc_output):
        encrypted = ""
        word = enc_input#enc_input.text.upper()
        key = enc_key#enc_key.text.upper()

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
        enc_output.text = encrypted
        print(word, "+", key, "=", encrypted)


class CRApp(App):
    pass



CRApp().run()


