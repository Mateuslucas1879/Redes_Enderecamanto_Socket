import socket
import threading
import sys
from os import remove

HOST = sys.argv[1] if len(sys.argv) >= 2 else '0.0.0.0'
PORT = int(sys.argv[2]) if len(sys.argv) >= 3 else 25000

clients = {}
clients_lock = threading.Lock()

def broadcast(message, except_sock=None):
    if except_sock is None:
        except_list = []
    elif isinstance(except_sock, socket.socket):
        except_list = [except_sock]
    else:
        except_list = list(except_sock)

    with clients_lock:
        for sock in list(clients.keys()):
            if sock in except_list:
                continue
            try:
                sock.sendall(message)
            except Exception:
                remove_client(sock)


def remove_client(sock):
    with clients_lock:
        info = clients.pop(sock, None)
    try:
        sock.close()
    except Exception:
        pass
    if info:
        nick, addr = info
        print(f"[DESCONEXÃO] {nick} {addr}")
        broadcast(f"*** {nick} deixou o chat.\n".encode('utf-8'))


def handle_client(sock, addr):
    try:
        def send(sock, msg):
            sock.sendall((msg + "\n").encode("utf-8"))
        send(sock, "Bem-vindo ao chat! Use /nick seu_nome para escolher um nickname.")

        nick = None
        while True:
            data = sock.recv(4096)
            if not data:
                break

            lines = data.decode("utf-8").strip()
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if line.startswith('/nick'):
                    newnick = line[6:].strip()
                    if not newnick:
                        sock.sendall(f"Nickname inválido.\n")
                        continue
                    with clients_lock:
                        existing = {v[0] for v in clients.values()}
                        if newnick in existing:
                            sock.sendall(f"Nickname já em uso.\n")
                        else:
                            old = clients[sock][0]
                            clients[sock] = (newnick, addr)
                            nick = newnick
                            if old == '':  # primeira atribuição
                                broadcast(f"*** {nick} entrou no chat.\n".encode('utf-8'), except_sock=sock)
                                sock.sendall(b"Nickname registrado.\n")
                            else:
                                broadcast(f"*** {old} mudou nickname para {nick}.\n".encode('utf-8'))
                elif line == '/list':
                    with clients_lock:
                        names = [v[0] for v in clients.values() if v[0]]
                    sock.sendall(("Usuarios: " + ", ".join(names) + "\n").encode('utf-8'))

                elif line == '/quit':
                    sock.sendall(b"Adeus!\n")
                    remove_client(sock)
                    return
                else:
                    with clients_lock:
                        sender = clients.get(sock, ('', addr))[0] or str(addr)
                    message = f"[{sender}] {line}\n"
                    broadcast(message.encode('utf-8'), except_sock=None)
    except ConnectionResetError:
        pass
    finally:
        remove_client(sock)

def accept_loop(server_sock):
    print(f"Servidor rodando em {HOST}:{PORT}. Aguardando conexões...")
    while True:
        try:
            client_sock, addr = server_sock.accept()
        except KeyboardInterrupt:
            break
        client_sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY,1)
        with clients_lock:
            clients[client_sock] = ('', addr)
        print(f"[CONEXÃO] {addr}")
        temp = threading.Thread(target=handle_client, args=(client_sock, addr), daemon=True)
        temp.start()


def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((HOST, PORT))
    server_sock.listen(100)
    try:
        accept_loop(server_sock)
    except KeyboardInterrupt:
        print("Encerrando servidor...")
    finally:
        server_sock.close()
        with clients_lock:
            for serv in list(clients.keys()):
                try:
                    serv.close()
                except Exception:
                    pass

if __name__ == '__main__':
    main()