import csv
from datetime import datetime
import operator
from socket import *
import pandas as pd

serverPort = 9000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("the server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    print(addr)
    print(sentence)
    ip = addr[0]
    port = addr[1]
    headers = sentence.split('\n')
    print(headers)
    file = headers[0].split()[1]
    # to know the request
    if file == '/' or file == '/index.html':
        file = 'Main.html'
        # trying to open the index file and send it to client
        try:
            fin = open(file)
            content = fin.read()
            fin.close()
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            connectionSocket.send(bytes("Content-Type: text/html\r\n", "UTF-8"))
            print("Content-Type: text/html\r\n")
            connectionSocket.send(bytes("\r\n", "UTF-8"))
            print("\r\n")
            connectionSocket.sendall(bytes(content, "UTF-8"))
        except FileNotFoundError:  # in case i didn't find the file -> not found -> 404
            connectionSocket.send(bytes("HTTP/1.1 404 Not Found \r\n", "UTF-8"))
            print("HTTP/1.1 404 Not Found \r\n")
    elif file == '/Network1.jpg':

        # open the picture and mode: read & binary
        try:
            fin = open("counter.jpg", "rb")
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            now = datetime.now()
            connectionSocket.send(bytes("Date and Time: " + now.strftime("%d/%m/%Y, %H:%M:%S") + "\r\n", "UTF-8"))
            print("Date and Time: " + now.strftime("%d/%m/%Y, %H:%M:%S") + "\r\n")
            connectionSocket.send(bytes("Content-Type: image/jpeg\r\n\r\n", "UTF-8"))
            print("Content-Type: image/jpeg\r\n\r\n")
            connectionSocket.send(fin.read())  # send the contents of the picture
            print(str(fin.read()))
        except FileNotFoundError:
            connectionSocket.send(bytes("HTTP/1.1 404 Not Found \r\n", "UTF-8"))
            print("HTTP/1.1 404 Not Found \r\n")
    elif file == '/file.html':

        file = 'file.html'
        # trying to open the index file and send it to client
        try:
            fin = open(file)
            content = fin.read()
            fin.close()
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            connectionSocket.send(bytes("Content-Type: text/html\r\n", "UTF-8"))
            print("Content-Type: text/html\r\n")
            connectionSocket.send(bytes("\r\n", "UTF-8"))
            print("\r\n")
            connectionSocket.sendall(bytes(content, "UTF-8"))
        except FileNotFoundError:  # in case i didn't find the file -> not found -> 404
            connectionSocket.send(bytes("HTTP/1.1 404 Not Found \r\n", "UTF-8"))
            print("HTTP/1.1 404 Not Found \r\n")
    elif file == '/file.css':

        file = 'file.css'
        # trying to open the index file and send it to client
        try:
            fin = open(file)
            content = fin.read()
            fin.close()
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            connectionSocket.send(bytes("Content-Type: text/html\r\n", "UTF-8"))
            print("Content-Type: text/html\r\n")
            connectionSocket.send(bytes("\r\n", "UTF-8"))
            print("\r\n")
            connectionSocket.sendall(bytes(content, "UTF-8"))
        except FileNotFoundError:  # in case i didn't find the file -> not found -> 404
            connectionSocket.send(bytes("HTTP/1.1 404 Not Found \r\n", "UTF-8"))
            print("HTTP/1.1 404 Not Found \r\n")
    elif file == '/Network1.png':
        fin = open("decoder.png", "rb")
        # open the picture and mode: read & binary
        try:
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            now = datetime.now()
            connectionSocket.send(bytes("Date and Time: " +
                                        now.strftime("%d/%m/%Y, %H:%M:%S") + "\r\n", "UTF-8"))
            print("Date and Time: " + now.strftime("%d/%m/%Y, %H:%M:%S") + "\r\n")
            connectionSocket.send(bytes("Content-Type: image/jpeg\r\n\r\n", "UTF-8"))
            print("Content-Type: image/jpeg\r\n\r\n")
            connectionSocket.send(fin.read())  # send the contents of the picture
            print(str(fin.read()))
        except FileNotFoundError:
            connectionSocket.send(bytes("HTTP/1.1 404 Not Found \r\n", "UTF-8"))
            print("HTTP/1.1 404 Not Found \r\n")

    elif file == '/SortName':

        try:
            df = pd.read_csv("smartphones.csv")
            sorted_names = df.sort_values(by=["Name"], ascending=True)
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            now = datetime.now()  # to send date & time with the response
            connectionSocket.send(bytes("Date and Time: " + now.strftime("%d/%m/%Y, %H:%M:%S") + "\r\n", "UTF-8"))
            print("Date and Time: " + now.strftime("%d/%m/%Y, %H:%M:%S") + "\r\n")
            connectionSocket.send(bytes("Content-Type: text/plain\r\n", "UTF-8"))
            print("Content-Type: text/plain\r\n")
            connectionSocket.send(bytes("\r\n", "UTF-8"))
            print("\r\n")
            content = sorted_names
            content = bytes(content.to_string(), "UTF-8")
            connectionSocket.send(content)
        except FileNotFoundError:
            connectionSocket.send(bytes("HTTP/1.1 404 Not Found \r\n", "UTF-8"))
            print("HTTP/1.1 404 Not Found \r\n")
    elif file == '/SortPrice':

        try:
            df = pd.read_csv("smartphones.csv")
            sorted_prices = df.sort_values(by=["Price"], ascending=True)
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            now = datetime.now()  # to send date & time with the response
            connectionSocket.send(bytes("Date and Time: " + now.strftime("%d/%m/%Y, %H:%M:%S") + "\r\n", "UTF-8"))
            print("Date and Time: " + now.strftime("%d/%m/%Y, %H:%M:%S") + "\r\n")
            connectionSocket.send(bytes("Content-Type: text/plain\r\n", "UTF-8"))
            print("Content-Type: text/plain\r\n")
            connectionSocket.send(bytes("\r\n", "UTF-8"))
            print("\r\n")
            content = sorted_prices
            content = bytes(content.to_string(), "UTF-8")
            connectionSocket.send(content)
        except FileNotFoundError:
            connectionSocket.send(bytes("HTTP/1.1 404 Not Found \r\n", "UTF-8"))
            print("HTTP/1.1 404 Not Found \r\n")