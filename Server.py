import socket
from _thread import *
def client_handler(c,add):
 while True:
  i = ArrPort.index(add[1])
  temp1=ArrName[i]
  word = c.recv(1024).decode()
  print("message from "+ str(temp1) + ' , PortNumber : ' + str(add[1])+" > " + word)
  if word != "close connection":
   res = word.upper()
   c.sendall(bytes('UPPER CASE : ' + res + '\n' + 'Enter the word needed to be capitalized or use "close connection" to terminate it','utf-8'))
  else:
   c.close()
   ArrName.pop(i)
   ArrPort.pop(i)
   print("connection terminated with " + str(temp1)+ ' , PortNumber : ' + str(add[1]))
   break
IP = "127.0.0.1"
port = 1234
ArrName=[]
ArrPort=[]
threadNum=0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")
try:
    s.bind((IP, port))
except socket.error as e:
    print(str(e))
print(f'Server is listing on the port {port}...')
s.listen(5)
print("Waiting for connections ")
while True :
 c , add = s.accept()
 threadNum+=1
 ArrPort.append(add[1])
 name = c.recv(1024).decode()
 ArrName.append(name)
 print ("thread "+str(threadNum))
 print("Connected to " + name,"-> IpAddress : "+ add[0] + ' , PortNumber :' + str(add[1]))
 c.send(bytes("Hi " + name, 'utf-8'))
 start_new_thread(client_handler, (c,add,))






