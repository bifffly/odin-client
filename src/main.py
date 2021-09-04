import socket

class TCPClient:
    host = "127.0.0.1"
    port = 1866

    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        print("Connected to", s.getsockname())

        req = input("Enter req: ")
        s.sendall(str.encode(req))
        res = s.recv(4096)
        print(res.decode())
        s.close()

if __name__ == '__main__':
    client = TCPClient()
    client.start()
