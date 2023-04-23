import socket
import threading
import customtkinter as ct
class client:
    
    def start(self):
        self.inchat = False
        ct.set_appearance_mode("dark")
        ct.set_default_color_theme("dark-blue")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.read_config()
        
        self.connect()
        self.gui_thread = threading.Thread(target=self.gui_loop)
        self.gui_thread.start()
    def send_data(self, data=str):
        self.socket.send(f"{self.con}\n{str(data)}".encode())
    def receive_data(self):
        #self.identif = self.socket.recv(2048).decode()
        while True:
            self.data = self.socket.recv(2048).decode()
            
            if not self.data:
                self.socket.close()
                break
            
            print(self.data)
            if "Added" in self.data and self.inchat == False:
                try:
                    self.disconnect.destroy()
                except:
                    pass
                try:
                    self.label.destroy()
                except:
                    pass
                try:
                    self.confirm_b.destroy()
                except:
                    pass
                try:
                    self.search_bar.destroy()
                except:
                    pass
                
                self.add(method="found", contact=str(self.data.split("$")[1]))
            try:
                self.messages.insert("0.0", f"[{self.con}]: "+self.data+"\n")
            except Exception as e:
                print(e)
    def getcon(self):
        return self.search_bar.get()
    def clean(self):
        try:
            
            self.disconnect.destroy()
        except:
            pass
        try:
            self.label.destroy()
        except:
            pass
        try:
            self.confirm_b.destroy()
        except:
            pass
        try:
            self.search_bar.destroy()
        except:
            pass
    def read_config(self):
        
        with open("server.cfg", "r") as config:
            lines = config.read().split("\n")
            self.ip = lines[0].split("=")[1]
            self.port = lines[1].split("=")[1]
            self.max_c = lines[2].split("=")[1]
            self.max_data = lines[3].split("=")[1]
            config.close()
        
    def connect(self):
        self.socket.connect((self.ip, int(self.port)))
        self.recv_thread = threading.Thread(target=self.receive_data)
        self.recv_thread.start()
        #self.send_data("0\nhi")
    def lol(self):
        self.socket.send(f"{self.con}\n{self.message.get()}".encode())
        self.messages.insert("0.0", "[You]: "+self.message.get()+"\n")
    def add(self, method, contact=None):
        self.inchat = True
        if method == "normal":
            
        
            #self.msg = input("")
            self.socket.send(f"{self.search_bar.get()}\nAdded${self.data}".encode())
            
            self.label.destroy()
            self.disconnect.destroy()
            
            self.confirm_b.destroy()
            self.con = self.search_bar.get()
            self.contact_name = ct.CTkLabel(master=self.frame, text=f"CONTACT {self.search_bar.get()}", font=("Roboto", 16))
            self.search_bar.destroy()
            self.contact_name.pack(pady=12, padx=10, side=ct.TOP)
            
            self.messages = ct.CTkTextbox(master=self.frame, width=250)
            self.messages.pack(pady=15, padx=10)
            self.messages.insert("0.0", "The beggining of your glorious conversation")
            self.message = ct.CTkEntry(master=self.frame, placeholder_text="message")
          #  self.message.pack(pady=12, padx=10, side=ct.BOTTOM)#, anchor=ct.NW)
            
            self.send_b = ct.CTkButton(master = self.frame, text="Send", command=self.lol)
            self.send_b.pack(pady=0, padx=10, side=ct.BOTTOM)#, anchor=ct.NE)
            self.message.pack(pady=12, padx=10, side=ct.BOTTOM)
        else:
            self.con = contact
           # self.socket.send(f"{self.search_bar.get()}\nAdded".encode())
            try:
                self.label.destroy()
                self.disconnect.destroy()
            
                self.confirm_b.destroy()
            except:
                pass
           # self.con = self.search_bar.get()
            self.contact_name = ct.CTkLabel(master=self.frame, text=f"CONTACT {contact}", font=("Roboto", 16))
            try:
                self.search_bar.destroy()
            except:
                pass
            try:
                self.continue_b.destroy()
            except:
                pass
            self.contact_name.pack(pady=12, padx=10, side=ct.TOP)
            
            self.messages = ct.CTkTextbox(master=self.frame, width=250)
            self.messages.pack(pady=15, padx=10)
            self.messages.insert("0.0", "The beggining of your glorious conversation")
            self.message = ct.CTkEntry(master=self.frame, placeholder_text="message")
          #  self.message.pack(pady=12, padx=10, side=ct.BOTTOM)#, anchor=ct.NW)
            
            self.send_b = ct.CTkButton(master = self.frame, text="Send", command=self.lol)
            self.send_b.pack(pady=0, padx=10, side=ct.BOTTOM)#, anchor=ct.NE)
            self.message.pack(pady=12, padx=10, side=ct.BOTTOM)
    def msg(self):
        try:
            self.disconnect.destroy()
            self.continue_b.destroy()
            self.label.destroy()
        except:
            pass
        self.label = ct.CTkLabel(master=self.frame, text=f"Your ID {self.data}", font=("Roboto", 14))
        self.label.pack(pady=12, padx=10)
        
        self.search_bar = ct.CTkEntry(master=self.frame, placeholder_text="Contact's id")
        self.search_bar.pack(pady=12, padx=10)
        
        self.confirm_b = ct.CTkButton(master = self.frame, text="Search", command=lambda : self.add("normal"))
        self.confirm_b.pack(pady=12, padx=10)
        self.disconnect = ct.CTkButton(master=self.frame, text="Disconnect", command=self.close)
        self.disconnect.pack(pady=12, padx=10)
    def close(self):
        self.socket.close()
        self.label.configure(text="Disconnected,\nit's safe to exit the app")
        self.disconnect.destroy()
    def gui_loop(self):
        self.win = ct.CTk()
        self.win.geometry("700x500")
        self.frame = ct.CTkFrame(master=self.win)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)
        
        self.label = ct.CTkLabel(master=self.frame, text=f"Welcome {self.data}", font=("Roboto", 24))
        self.label.pack(pady=12, padx=10)
        self.continue_b = ct.CTkButton(master=self.frame, text="Open messages", command=self.msg)
        self.continue_b.pack()
        self.disconnect = ct.CTkButton(master=self.frame, text="Disconnect", command=self.close)
        self.disconnect.pack(pady=12, padx=10)
        self.win.mainloop()
client().start()