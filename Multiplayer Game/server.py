import socket
from _thread import *
import sys

server = "192.168.86.65"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

def read_tank(str):
    str = str.split(",")
    return float(str[0]), float(str[1]), float(str[2])

def make_tank(tup):
    return str(tup[0])+","+str(tup[1])+","+str(tup[2])

def make_bullet(tup):
    return "bullet:"+str(tup[0])+","+str(tup[1])+","+str(tup[2])+","+tup[3]

def read_bullet(str):
    str = str.split(":")[1]
    str = str.split(",")
    return float(str[0]), float(str[1]), float(str[2]), str[3]

tank_data = [(100,235, 0),(300,235, 180)]
bullet_toAdd_to0 = []
bullet_toAdd_to1 = []

def threaded_client(conn, player):
    conn.send(str.encode(make_tank(tank_data[player])))
    reply = ""
    while True:
        try:
            #This is a string that was sent by the client
            data= conn.recv(2048).decode()

            #The String that is going to be sent to the client
            reply = ""

            if not data:
                print("Disconnected")
                break
            elif data[0:7]=="bullet:":
                new_bullet = read_bullet(data)
                reply = "Successfully recorded bullet"
                if player==0:
                    bullet_toAdd_to1.append(new_bullet)
                else:
                    bullet_toAdd_to0.append(new_bullet)
            else:
                tank_data[player] = read_tank(data)
                if player==1:
                    reply = make_tank(tank_data[0])
                    if len(bullet_toAdd_to1)==1:
                        reply+=make_bullet(bullet_toAdd_to1[0])
                        del bullet_toAdd_to1[0]
                else:
                    reply =make_tank(tank_data[1])
                    if len(bullet_toAdd_to0)==1:
                        reply+=make_bullet(bullet_toAdd_to0[0])
                        del bullet_toAdd_to0[0]
            print("Received: ", data)
            print("Sending: ", reply)

            conn.sendall(str.encode(reply))

        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,currentPlayer))
    currentPlayer+=1