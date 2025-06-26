lista_produtos = []
lista_codigo = []

with open("arquivos_csv/arquivo.csv", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        partes = linha.strip().split(',')
    
        tupla = (
            str(partes[0]),
            str(partes[1]),
            float(partes[2]),
            int(partes[3]),
            int(partes[4])
        )

        lista_produtos.append(tupla)

print(lista_produtos)
