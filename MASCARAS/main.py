from sys import prefix


def ip_to_int(ip):
    partes = list(map(int, ip.split(".")))
    valor = (partes[0] << 24) | (partes[1] << 16) | (partes[2] << 8) | (partes[3])
    return valor
def int_to_ip(num):
    return ".".join(str((num >> shift) & 255) for shift in (24,16,8,0))

def cidr_to_mask(prefixo):
    mascara_int = (2**32 - 1) ^ (2**(32 - prefixo) - 1)
    return int_to_ip(mascara_int)

def calcular_subrede(cidr):
    ip_str, prefixo_str = cidr.split("/")
    prefixo = int(prefixo_str)

    ip_int = ip_to_int(ip_str)

    mascara_int = (2**32 - 1) ^ (2**(32 - prefixo) - 1)
    mascara = int_to_ip(mascara_int)

    rede_int = ip_int & mascara_int
    rede = int_to_ip(rede_int)

    broadcast_int = rede_int | ((2**32 - 1) ^ mascara_int)
    broadcast = int_to_ip(broadcast_int)

    if prefixo <= 30:
        hosts = (2**(32 - prefixo)) - 2
    else:
        host = 0

    if hosts > 0:
        primeiro_host = int_to_ip(rede_int + 1)
        ultimo_host = int_to_ip(broadcast_int - 1)
    else:
        primeiro_host = "-"
        ultimo_host = "-"

    return {
        "IP": ip_str,
        "Prefixo": f"/{prefixo}",
        "Máscara": mascara,
        "Endereço de Rede": rede,
        "Broadcast": broadcast,
        "Primeiro Host": primeiro_host,
        "Último Host": ultimo_host,
        "Quantidade de Hosts": hosts
    }


ex1 = calcular_subrede("146.164.0.0/16")
ex2 = calcular_subrede("152.92.55.0/24")


print("EXEMPLO 01")
for nome, valor in ex1.items():
    print(f"{nome}: {valor}")

print("\n---\n")
print("EXEMPLO 02")
for nome, valor in ex2.items():
    print(f"{nome}: {valor}")