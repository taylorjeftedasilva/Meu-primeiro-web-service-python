import SOAPpy
server=SOAPpy.SOAPProxy("http://localhost:8011/")
print server.Train_Soap('nome do cliente')
