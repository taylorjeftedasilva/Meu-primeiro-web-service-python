import SOAPpy
from cliente import cliente
def Train_Soap(n):
    client=cliente(n)
    return client.retorno
local=("localhost",8011)
server=SOAPpy.SOAPServer(local)
server.registerFunction(Train_Soap)
server.serve_forever()
