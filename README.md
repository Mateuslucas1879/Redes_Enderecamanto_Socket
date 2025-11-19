# 📘 Fundamentos de Sistemas Distribuídos e Comunicação em Rede

Este repositório reúne uma explicação teórica completa sobre **Sistemas Distribuídos**, **Escalabilidade**, **Clusters**, **Threads** e **Comunicação entre Processos em Rede**.  
Todo o conteúdo foi preparado com rigor acadêmico, como seria apresentado em aulas de graduação e pós-graduação em Ciência da Computação.

---

# 📌 Sumário

1. [O que são Sistemas Distribuídos](#o-que-são-sistemas-distribuídos)  
2. [Escalabilidade](#escalabilidade)  
   - Escalabilidade Vertical  
   - Escalabilidade Horizontal  
3. [Clusters](#clusters)  
4. [Threads](#threads)  
5. [Princípios Básicos da Comunicação de Processos em Rede](#princípios-básicos-da-comunicação-de-processos-em-rede)  
6. [Arquitetura em Camadas e Sockets](#arquitetura-em-camadas-e-sockets)  
7. [Consistência, Tempo e Falhas](#consistência-tempo-e-falhas)  
8. [Conclusão](#conclusão)

---

# 🧩 O que são Sistemas Distribuídos

Um **Sistema Distribuído** é um conjunto de computadores independentes que, para o usuário final, se comportam como um único sistema coerente.

Em outras palavras, várias máquinas autônomas, conectadas por rede, cooperam para executar tarefas comuns e fornecer um serviço integrado.

### Características centrais:

- Não existe memória compartilhada entre máquinas.  
- A comunicação ocorre através de **troca de mensagens**.  
- Cada máquina possui seu próprio sistema operacional, relógio e estado.  
- Falhas são inevitáveis e devem ser tratadas como parte do modelo.  
- O sistema precisa fornecer transparência ao usuário (de falha, localização, concorrência etc.).

### Importância
Sistemas distribuídos são a base da Internet moderna, computação em nuvem, bancos de dados distribuídos, microserviços, jogos online e praticamente todos os serviços de larga escala.

---

# 🚀 Escalabilidade

Escalabilidade é a capacidade de um sistema **aumentar seu desempenho**, **suportar mais usuários** ou **processar maiores volumes de dados** sem degradação significativa.

Existem dois modelos principais:

---

## 🔼 Escalabilidade Vertical (Scale Up)

Consiste em **aumentar a capacidade de uma única máquina**.

Exemplos:
- mais CPU  
- mais RAM  
- SSD mais rápido  
- processadores com mais núcleos  

**Vantagem:** simples, não exige mudar o software.  
**Desvantagem:** existe um limite físico; se a máquina falha, o sistema cai.

---

## 🔁 Escalabilidade Horizontal (Scale Out)

Consiste em **adicionar mais máquinas** para compartilhar o trabalho.

É o modelo usado por Google, Amazon, Netflix e grandes sistemas distribuídos.

**Vantagens:**
- alta disponibilidade  
- escala praticamente ilimitada  
- redundância de dados  
- tolerância a falhas  

**Desafios teóricos:**
- coordenação distribuída  
- sincronização  
- consistência  
- comunicação por mensagens  

---

# 🖥️ Clusters

Um **cluster** é um conjunto de computadores independentes (nós) que trabalham juntos como se fossem um único sistema.

Cada nó possui:
- seu próprio sistema operacional  
- sua própria CPU  
- sua própria memória  
- sua própria comunicação  

### Tipos comuns de clusters:

#### 🔹 Cluster de Alto Desempenho (HPC)
Usados para cálculos científicos e simulações.

#### 🔹 Cluster de Alta Disponibilidade (HA)
Focados em nunca ficar offline; se um nó falha, outro assume.

#### 🔹 Cluster de Balanceamento de Carga
Vários servidores dividem as requisições de usuários.

#### 🔹 Cluster de Armazenamento Distribuído
Ex.: Hadoop HDFS, Google File System, Ceph.

Clusters são a base da computação moderna e tornam possível a escalabilidade horizontal.

---

# 🧵 Threads

Uma **thread** é uma linha de execução dentro de um processo.

Enquanto o cluster trabalha com múltiplas máquinas,
as threads trabalham com múltiplos fluxos dentro da mesma máquina.

### Características:
- compartilham memória  
- executam em paralelo se houver múltiplos núcleos  
- usadas para acelerar tarefas ou processar múltiplas operações simultâneas  

### Hierarquia completa:

### Como testar (threads)

  - No terminal A: python3 chat_server_threaded.py 0.0.0.0 25000
  -  Em N terminais diferentes: python3 chat_client.py 127.0.0.1 25000


---

# 🔗 Princípios Básicos da Comunicação de Processos em Rede

Processos em máquinas diferentes não compartilham:
- memória  
- relógio  
- sistema operacional  

Eles só conseguem cooperar através de **mensagens enviadas pela rede**.

### Propriedades fundamentais:

#### 📡 Comunicação por mensagens
A única forma de interação entre processos distribuídos.

Problemas naturais:
- atraso variável  
- perda de pacotes  
- duplicação  
- chegada fora de ordem  

#### 🧠 Estado isolado
Cada processo conhece apenas seu próprio estado e aquilo que recebe por mensagens.

#### ❗ Falhas são parte do modelo
Máquinas podem:
- desligar  
- travar  
- enviar mensagens incorretas  
- falhar de forma bizantina  

---

# 🏛️ Arquitetura em Camadas e Sockets

A comunicação ocorre através da **arquitetura TCP/IP**, composta por cinco camadas:

1. **Aplicação** — HTTP, FTP, DNS  
2. **Transporte** — TCP, UDP  
3. **Rede** — IP  
4. **Enlace** — Ethernet, Wi-Fi  
5. **Física** — transmissão dos bits

### 📨 Sockets
Um **socket** é a interface que conecta um processo à rede.

Um socket é identificado por:


É o mecanismo usado pelas aplicações para enviar e receber mensagens.

### 🔄 Encapsulamento
Cada camada adiciona seu próprio cabeçalho ao dado original.  
No destino, ocorre o **desencapsulamento**, camada por camada.

---

# ⏳ Consistência, Tempo e Falhas

Sistemas distribuídos precisam lidar com desafios teóricos profundos:

### 🕒 Tempo
Não existe relógio global perfeito.  
Surgem conceitos como:
- relógios lógicos (Lamport)  
- ordenação parcial  
- causalidade entre eventos  

### 🧩 Consistência
Garantir que todos os nós enxergam o mesmo estado é difícil.  
Teoremas fundamentais:
- **CAP** — Consistência, Disponibilidade, Tolerância a Particionamento  
- **FLP** — impossibilidade de consenso perfeito em sistemas assíncronos com falhas  

### ⚠️ Falhas
Falhas são inevitáveis:  
- falhas por parada  
- falhas de omissão  
- falhas temporárias  
- falhas bizantinas  

Sistemas distribuídos precisam ser robustos o suficiente para continuar funcionando apesar delas.

---

# 🧠 Conclusão

Sistemas distribuídos são o coração da computação moderna.  
Eles permitem conectar máquinas independentes para construir serviços globais, escaláveis e resilientes.

Para torná-los possíveis, precisamos dominar:
- comunicação por mensagens  
- escalabilidade horizontal  
- clusters  
- threads  
- protocolos e camadas  
- consistência e tolerância a falhas  

Este documento serve como base teórica completa para entendimento desses sistemas.

---

# 📚 Licença

Este repositório é de uso educacional e aberto para estudos, melhorias e compartilhamento.

  
