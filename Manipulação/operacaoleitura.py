arquivo = open('Manipulação\lore.txt', 'r')
print(arquivo.read())
arquivo.close()

arquivo = open('C:/Users/Rosana/Documents/Git/DIO-POO/Manipulação/lore.txt', 'r')
print(arquivo.read())
arquivo.close()

arquivo = open(r'C:\Users\Rosana\Documents\Git\DIO-POO\Manipulação\lore.txt', 'r')
print(arquivo.read())
arquivo.close()

arquivo = open('C:\\Users\\Rosana\\Documents\\Git\DIO-POO\\Manipulação\\lore.txt', 'r')
print(arquivo.read())
arquivo.close()

lendolinha = open('C:\\Users\\Rosana\\Documents\\Git\DIO-POO\\Manipulação\\lore.txt', 'r')
print(lendolinha.readline())
print(lendolinha.readline())
print(lendolinha.readline())
print(lendolinha.readline())
arquivo.close()

loop_leitura_por_linha =  open('C:\\Users\\Rosana\\Documents\\Git\DIO-POO\\Manipulação\\lore.txt', 'r')
for linha in loop_leitura_por_linha.readline(): #lista de strings com todas as linhas do arquivo
    print(linha)
arquivo.close()

loop_leitura_por_linha =  open('C:\\Users\\Rosana\\Documents\\Git\DIO-POO\\Manipulação\\lore.txt', 'r')
for linha in loop_leitura_por_linha.readlines(): #separa em lista para fazer pre processamento
    print(linha)
arquivo.close()


manipula_por_linha =  open('C:\\Users\\Rosana\\Documents\\Git\DIO-POO\\Manipulação\\lore.txt', 'r')
#tip
while len(linha := manipula_por_linha.readlinhe()):
    print(linha)
arquivo.close()

