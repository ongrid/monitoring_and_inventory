import json
import socket

def test():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('192.168.201.106', 3333))
        s.sendall(b'{"id":0,"jsonrpc":"2.0","method":"miner_getstat1"}')
        data = s.recv(1024)
        # весь массив, возвращённый c клэймора
    returned = json.loads(data.decode("utf-8"))['result']
    print(returned)

test()