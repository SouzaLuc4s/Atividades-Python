frase = 'o rato roeu a roupa do rei de roma'.strip()
tamanho_frase = len(frase)
contador = 0
nova = ''
letras = input('Qual letra você quer maiúscula? ')
# Isso se chama iteração (Ato de percorrer todos os elementos iteravies!)
while contador < tamanho_frase:
    letra = frase [contador]
    if letra == letras :
        nova+= letras.upper()
    else:
        nova += letra
    contador +=1
print(nova)