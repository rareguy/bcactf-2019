from socket import socket
from string import ascii_letters

#flag: thepassword = "bcactf{y0u_4r3_4_m4573rm1nD!_Ym9vbGlu}"
sock = socket()
sock.connect(('challenges.ctfd.io', 30133))
stringnow = "bcactf{\n"
print(ascii_letters)
sock.send(stringnow.encode())
data = sock.recv(1024)
print("> " + repr(data))
data = sock.recv(1024)
datanow = data.decode()
print("> " + datanow)
thepassword = "bcactf{"
iterasi = len(thepassword)
while True:
    for c in ascii_letters + '_' + '1234567890' + '!@#$%^&*()-=+{}':
        cur_pass = thepassword + c + '\n'
        print(cur_pass)
        sock.sendall(cur_pass.encode())
        print("sent.")
        data = sock.recv(1024)
        datanow = data.decode()
        datanow = datanow.split('\n')
        try:
            print("> " + datanow[0])
        except:
            pass
        try:
            if datanow[0][iterasi] == "1":
                thepassword = thepassword + c
                break
        except:
            data = sock.recv(1024)
            datanow = data.decode()
            datanow = datanow.split('\n')
            if datanow[0][iterasi] == "1":
                thepassword = thepassword + c
                break
    iterasi+= 1
sock.close()

# # def netcat(host, port):
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect((host, int(port)))
#     stringnow = "bcactf{"
#     s.send(stringnow.encode())
#     
#     while True:
#         data = s.recv(1024)
#         if not data:
#             break
#         print(repr(data))
#         s.send(stringnow.encode())
#     s.close()
#     s.shutdown(socket.SHUT_WR)
#     #s.shutdown(socket.SHUT_WR)

#nc challenges.ctfd.io 30133

# netcat("challenges.ctfd.io", 30133)
