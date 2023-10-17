# Gerenciador de Senhas
import random
import string
import hashlib
import binascii
import os

sistema_iniciar = input('Você deseja incluir um [R]egistro ou [P]rocurar por sua senha?: ')
sistema_iniciar.lower()

if sistema_iniciar == 'r':
    def armazenar_senha():
        # Usuario
        usuario = str(input('Seu usuario: '))
        # Website
        website = str(input("Website: "))
        # Gerar senhas randomicamente - random choice (string ascii)
        digito = int(input('Quantos digitos você quer em sua senha? (apenas números inteiros): '))

        senha = ''
        for i in range(digito):
            caractere = random.choice(string.ascii_letters)
            senha += caractere

        # Transformar a senha em hash usando hashlib (SHA-256 neste exemplo)
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', senha.encode('utf-8'), salt, 100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        pwdhash = (salt + pwdhash.encode('ascii')).decode('ascii')

        # Armazenar em arquivo
        f = open('Senha.txt', 'a')
        f.write(f'{usuario}-{website}-{str(senha)}-{str(pwdhash)}\n')
        f.close()

        print(f' Aqui está sua senha: {senha}')
    armazenar_senha()


##########

### LOCALIZADOR DE SENHAS ###

else:

    def procurar():    
        usuario_ou_website = str(input('Você quer procurar por usuário ou website?: '))
        valor = str(input('Qual valor?: '))
        f = open('Senha.txt', 'r')
        for linha in f:
            info = linha.split('-')
            if usuario_ou_website == 'usuario':
                if valor == info[0]:
                    return info[2] 
                # Procurar por usuário
            else:
                if valor == info[1]:
                    return info[2]
            #Procurar por Website
            

    resultado = procurar()

    if resultado == None: 
        print('Nenhum resultado encontrado')
    else:
        print(f'Aqui está sua senha: {resultado}')

##########
