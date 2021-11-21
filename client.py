import socket

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 8888))


class BoxLayoutLab(BoxLayout):
    def dodo(self, key, Input, output, toggle):
        what_to_do = key.text.upper()+" "+Input.text.upper()+" "+toggle.text
        client.send(what_to_do.encode("utf-8"))
        data = client.recv(2048)
        output.text = data


class CRApp(App):
    pass


CRApp().run()

