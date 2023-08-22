import socket
from _thread import *
import threading
global clients
import random

clients = {}

class client_handle:
    def accept(self, socketc):
       
        self.connection, self.address = socketc.accept()
        self.identificator = random.randint(1000000, 9999999)
        try:
            print(clients[self.identificator])
            self.identificator = random.randint(1000000, 9999999)
        except:
            clients[self.identificator]=self.connection
            
  
        print(f"[LOGS]: New connection {self.connection} {self.address}")
        self.rec = threading.Thread(target=self.receive_data)
        self.rec.start()
        self.send_data(self.connection, self.identificator)
    def send_data(self, connection, data):
        connection.send(str(data).encode())
        
    def disconnect(self):
        self.connection.close()
    def receive_data(self):
        while True:
            self.received = self.connection.recv(int(2048)).decode()
            if not self.received:
                clients.pop(self.identificator)
                
                self.connection.close()
                
                print("[LOGS]: Closed a connection")
                break
            try:
                self.primatel = self.received.split("\n")[0]
                self.sprava = self.received.split("\n")[1]
               # print(clients[int(self.primatel)])
                self.send_data(clients[int(self.primatel)], str(self.sprava))
            except Exception as e:
                print(e, "[ERROR]")
            print(self.received)
        
class server:
    def start(self):
        self.clients = []
        self.load_config()
        self.bind_server()
        
        self.client_handler = threading.Thread(target=self.handler)
        self.client_handler.start()
    def load_config(self):
        try:
            with open("server.cfg", "r") as config:
                lines = config.read().split("\n")
                self.ip = lines[0].split("=")[1]
                self.port = lines[1].split("=")[1]
                self.max_c = lines[2].split("=")[1]
                self.max_data = lines[3].split("=")[1]
                config.close()
        except Exception:
            print("[CFG]: Couldn't open configuration, restoring defaults")
            with open("server.cfg", "w+") as config:
                config.write(f"ip={socket.gethostbyname(socket.gethostname())}\nport=37653\nmax_clients=100\nmax_data=2048")
                self.ip=socket.gethostbyname(socket.gethostname())
                self.port=37653
                self.max_c=100
                self.max_data = 2048
                config.close()
    def bind_server(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.bind((self.ip, int(self.port)))
        except Exception as e:
            print(e)
            print("[ERROR]: Port is already in use! Change it in the config file")
            
            exit()
        self.socket.listen(int(self.max_c))
        print("[LOGS]: Listening started")
    def handler(self):
        while True:
            #self.ident = client_handle()
            client_handle().accept(self.socket)
            #print(clients)
          #  print(clients[0])
            #clients.append(self.ident)
           # for client in clients:
             #   print(client)
            #self.clients.append(self.ident)
            
server().start()
    
