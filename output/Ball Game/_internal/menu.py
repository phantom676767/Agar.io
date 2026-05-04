from customtkinter import *


class Launcher(CTk):
    def __init__(self):
        super().__init__()

        self.name = ""
        self.ip = ""
        self.port = 0
        
        self.geometry("1000x700")
        self.title("AGARIO LAUNCHER")
        self.configure(fg_color = "black")

        self.heading = CTkLabel(self, text = "🐍 AGARIO BATTLE 🐍", text_color = "#D30000", font = (None, 68))
        self.heading.pack(pady = (75, 50))

        self.entry_name = CTkEntry(self, placeholder_text = "Your nickname", placeholder_text_color = "#ABABAB", text_color = "#FFFFFF", border_color = "#ABABAB", border_width = 2, corner_radius = 10, width = 500, height = 48, font = (None, 24), fg_color = "#4B4B4B")
        self.entry_name.pack(pady = 25)

        self.entry_ip = CTkEntry(self, placeholder_text = "Server IP", placeholder_text_color = "#ABABAB", text_color = "#FFFFFF", border_color = "#ABABAB", border_width = 2, corner_radius = 10, width = 500, height = 48, font = (None, 24), fg_color = "#4B4B4B")
        self.entry_ip.pack(pady = 25)

        self.entry_port = CTkEntry(self, placeholder_text = "Server PORT ", placeholder_text_color = "#ABABAB", text_color = "#FFFFFF", border_color = "#ABABAB", border_width = 2, corner_radius = 10, width = 500, height = 48, font = (None, 24), fg_color = "#4B4B4B")
        self.entry_port.pack(pady = 25)

        self.button = CTkButton(self, text = "🌌 PLAY 🌌", text_color = "#FFFFFF", fg_color = "#00FF04", width = 250, height = 100, corner_radius = 20, font = (None, 32), command = self.connect_game)
        self.button.pack(pady = (75, 0))
    
    def connect_game(self):
        self.name = self.entry_name.get()
        self.ip = self.entry_ip.get()
        self.port = int(self.entry_port.get())
        self.destroy()


