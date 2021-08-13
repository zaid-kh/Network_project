from socket import *
import pandas as pd


# function to deal with wrong requests and
def not_found(file):
    print("this is the not_found function")
    file = 'NotFound.html'
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


serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("the server is ready to receive")
while True:
    connectionSocket, address = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    print(address)
    print(sentence)
    ip = address[0]
    port = address[1]
    headers = sentence.split('\n')
    print(headers)
    file = headers[0].split()[1]
    # request cases
    if file == '/' or file == '/index.html':
        file = 'Main.html'
        # requesting Main.html and sending it to client
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
        except FileNotFoundError:  # in case file not found => 404
            connectionSocket.send(bytes("HTTP/1.1 404 Not Found \r\n", "UTF-8"))
            print("HTTP/1.1 404 Not Found \r\n")
            not_found(file)
        # requesting a jpg image file
    elif file == '/Network1.jpg':
        try:
            fin = open("neapolitan.jpg", "rb")
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            connectionSocket.send(bytes("Content-Type: image/jpeg\r\n\r\n", "UTF-8"))
            print("Content-Type: image/jpeg\r\n\r\n")
            connectionSocket.send(fin.read())
            print(str(fin.read()))
        except FileNotFoundError:
            connectionSocket.send(bytes("HTTP/1.1 404 Not Found \r\n", "UTF-8"))
            print("HTTP/1.1 404 Not Found \r\n")
            not_found(file)
        # requesting an html file
    elif file == '/file.html':
        file = 'file.html'
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
        except FileNotFoundError:
            connectionSocket.send(bytes("HTTP/1.1 404 Not Found \r\n", "UTF-8"))
            print("HTTP/1.1 404 Not Found \r\n")
            not_found(file)
        # requesting a css file
    elif file == '/file.css':
        file = 'Network_styles.css'
        try:
            fin = open(file)
            content = fin.read()
            fin.close()
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            connectionSocket.send(bytes("Content-Type: text/plain\r\n", "UTF-8"))
            print("Content-Type: text/plain\r\n")
            connectionSocket.send(bytes("\r\n", "UTF-8"))
            print("\r\n")
            connectionSocket.sendall(bytes(content, "UTF-8"))
        except FileNotFoundError:
            connectionSocket.send(bytes("HTTP/1.1 404 Not Found \r\n", "UTF-8"))
            print("HTTP/1.1 404 Not Found \r\n")
            not_found(file)
        # requesting a png image file
    elif file == '/Network1.png':
        fin = open("decoder.png", "rb")
        try:
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            connectionSocket.send(bytes("Content-Type: image/png\r\n\r\n", "UTF-8"))
            print("Content-Type: image/png\r\n\r\n")
            connectionSocket.send(fin.read())  # send the contents of the picture
            print(str(fin.read()))
        except FileNotFoundError:
            connectionSocket.send(bytes("HTTP/1.1 404 Not Found \r\n", "UTF-8"))
            print("HTTP/1.1 404 Not Found \r\n")
            not_found(file)
            # requesting a sorted csv file by name
    elif file == '/SortName':
        try:
            df = pd.read_csv("smartphones.csv")
            sorted_names = df.sort_values(by=["Name"], ascending=True)
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
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
            not_found(file)
        # requesting a sorted csv file by price
    elif file == '/SortPrice':
        try:
            df = pd.read_csv("smartphones.csv")
            sorted_prices = df.sort_values(by=["Price"], ascending=True)
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
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
            not_found(file)
        # wrong request id
    else:
        not_found(file)
