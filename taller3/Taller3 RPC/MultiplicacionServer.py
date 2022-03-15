# server program
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

class Funciones:
    Cadena = ''
    def __init__(self):
        self.Cadena = 'Multiplicacion Server'
    def multiplicacion(self, x, y):
        return x * y

def main():
	server = SimpleJSONRPCServer(('localhost', 5003))
	server.register_instance(Funciones())
	print("Multiplicacion Server Corriendo")
	server.serve_forever()
if __name__ == '__main__':  
    main()
