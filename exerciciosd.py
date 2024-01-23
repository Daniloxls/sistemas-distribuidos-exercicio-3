from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import datetime
# Registrar caminho para o servidor
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('10.0.84.194', 21212),requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    #Definição de funções
    def reverse_word(s):
        return s[::-1]
    

    mensagens = []
    
    def armazenar(mensagem):
        mensagens.append(mensagem)
        return (True)
    
    def getMensagens():
        return(mensagens)
    
    acum = 0
    
    def add_acum(num):
        acum += num
        return (True)
    
    def getAcumulado():
        return(acum)
    
    def date_time():
        return datetime.datetime.now()
    
    def get_ip():
        return('200.129.47.239')

    #Registrar funções
    server.register_function(reverse_word, 'reverse')
    server.register_function(get_ip, 'ip')
    server.register_function(add_acum, 'acumular')
    server.register_function(getAcumulado, 'acumulado')
    server.register_function(armazenar, 'armazenar')
    server.register_function(getMensagens, 'getMensagens')
    server.register_function(date_time, 'datahora')

    # Iniciar servidor
    server.serve_forever()