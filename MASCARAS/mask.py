def cidr_para_mascara(cidr_notacao):
    ip, prefixo = cidr_notacao.split('/')
    prefixo = int(prefixo)

    # Criando a máscara em binário: prefixo bits 1, resto 0
    mascara_bin = ('1' * prefixo).ljust(32, '0')

    # Dividindo em grupos de 8 bits
    octetos = [mascara_bin[i:i+8] for i in range(0, 32, 8)]

    # Convertendo cada octeto binário para decimal
    mascara_decimal = '.'.join(str(int(o, 2)) for o in octetos)

    return mascara_decimal


# teste
print("146.164.0.0/16 →", cidr_para_mascara("146.164.0.0/16"))
print("152.92.55.0/24 →", cidr_para_mascara("152.92.55.0/24"))
