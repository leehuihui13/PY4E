import socket

try:
    url = input('Enter URL: ')

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((url.split("/")[2], 80))
    cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)

    info=b""

    while True:
        data = mysock.recv(512)
        if len(data) < 1: break
        info = info + data

    info = info.decode()
    pos = info.find('\r\n\r\n')
    x = info[pos+4:]
    print(x)
    print(len(x))

    mysock.close()

except:
    print ('url is invalid')
