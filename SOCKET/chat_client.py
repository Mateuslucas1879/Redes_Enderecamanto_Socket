import socket
import sys
import threading


HOST = sys.argv[1] if len(sys.argv) >= 2 else '127.0.0.1'
PORT = int(sys.argv[2]) if len(sys.argv) >= 3 else 25000

def recv_loop(sock):
    try:
        while True:
            data = sock.recv(4096)
            if not data:
                print("Conexão fechada pelo servidor.")
                break
            print(data.decode('utf-8', errors='replace'), end='')
    except Exception:
        pass
    finally:
        try:
            sock.close()
        except:
            pass

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    t = threading.Thread(target=recv_loop, args=(sock,), daemon=True)
    t.start()
    try:
        while True:
            line = input()
            if not line:
                continue
            sock.sendall((line + '\n').encode('utf-8'))
            if line.strip() == '/quit':
                break
    except KeyboardInterrupt:
        pass
    finally:
        try:
            sock.close()
        except:
            pass

if __name__ == '__main__':
    main()