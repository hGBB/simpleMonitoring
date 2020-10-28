import pickle
from CheckServer import Server

servers = pickle.load(open("servers.pickle", "rb"))

print("Example to add server")

servername = input("enter server name")
port = int(input("enter a port number"))
connection = input("enter a type ping/plain/ssl")
priority = input("enter a priority high or low")

new_server = Server(servername, port, connection, priority)
servers.append(new_server)

pickle.dump(servers, open("servers.pickle", "wb"))