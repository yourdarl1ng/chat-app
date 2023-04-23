# chat-app
simple chat app written in python
Server uses threading and has a client handle for each client.
It is ready to run right away if you have all the libs.


# Libraries and installation
required libs-> `customtkinter`
if you can't run the client or still get a module not found error execute this command `pip3 install <missingpackage>` replace `<missingpackage>` with the missing package

# Running it
### Server
First run the server with `python server.py` or `python3 server.py` and server.cfg should be created in the directory. You can tweak the server's configuration there.
### Client
To run the client you need to install the library mentioned above. You can run the client by simply opening it as any other app or with a command `python client.py` or `python3 client.py`. Client requires the server.cfg file in the same directory so it knows what server it should connect to.
Every client has a unique number assigned to them as their identifier, you enter this number to add someone in the chat(you can also add your own if you want to test it). 
