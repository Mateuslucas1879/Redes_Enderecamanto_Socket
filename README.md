# SOCKET 
### Como testar (threads)

  No terminal A: python3 chat_server_threaded.py 0.0.0.0 25000
  
  Em N terminais diferentes: python3 chat_client.py 127.0.0.1 25000
  
  No cliente, defina nickname: /nick Mateus
  
  Envie mensagens: Olá turma! — serão broadcastadas.
  
  Comandos: /list, /quit.
