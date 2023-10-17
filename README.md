# Gerenciador de Senhas

Este é um simples gerenciador de senhas em Python que eu desenvolvi com base em um vídeo do DevWithMe (link abaixo). Ele permite que você armazene senhas de forma segura e também as recupere quando necessário.

https://www.youtube.com/@DevWithMe

## Funcionalidades

- **Armazenamento Seguro:** As senhas são armazenadas em um formato criptografado usando o método de criptografia SHA-256. A senha original não é armazenada, apenas a versão criptografada.
- **Geração de Senha Aleatória:** O programa pode gerar senhas aleatórias para você com o número desejado de caracteres.
- **Recuperação de Senha:** Você pode procurar senhas armazenadas por usuário ou website e recuperá-las.

## Requisitos

Para executar este programa, você precisará de Python instalado em seu computador. Além disso, é necessário ter as bibliotecas `hashlib` e `binascii`, que são comuns em instalações padrão do Python.

## Como Usar

1. Clone este repositório em sua máquina local.
2. Execute o arquivo `main.py` em seu terminal ou IDE Python.
3. Siga as instruções na tela para adicionar ou procurar senhas.

## Exemplo de Uso

```python
Para criar uma nova senha: 
# Você deseja incluir um [R]egistro ou [P]rocurar por sua senha?: R
# (Siga as instruções para inserir informações de usuário e senha)

Para procurar uma senha:
# Você deseja incluir um [R]egistro ou [P]rocurar por sua senha?: P
# (Siga as instruções para procurar senhas)
