#Importar biblioteca
import xmlrpc.client
import socket
#Definir servidor
s = xmlrpc.client.ServerProxy('http://10.0.84.194:21212')
#Chamar funções disponíveis no servidor
s.armazenar(socket.gethostname())
s.armazenar("dannilo")
s.armazenar("ueba")
print(s.getMensagens())
print(s.datahora())
# Print list of available methods
print(s.system.listMethods())
