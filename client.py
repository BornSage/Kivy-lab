import socket
from threading import Thread

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 8888))


class BoxLayoutLab(BoxLayout):
    data = ""
    label_data = ""
    def listening_to_server(self):
        self.data = client.recv(2048).decode("utf-8")
        self.label_data = client.recv(2048).decode("utf-8")

    def dodo(self, key, Input, output, toggle,table_switch, label):

        what_to_do = key.text.upper()+" "+Input.text.upper()+" "+toggle.text+" "+table_switch.text
        client.send(what_to_do.encode("utf-8"))

        data = client.recv(2048).decode("utf-8")
        output.text = data
        label_data = client.recv(2048).decode("utf-8")
        label.text = label_data



class CRApp(App):
    pass


CRApp().run()

