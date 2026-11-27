# importando bibliotecas

import random # numeros aleatorios
import subprocess # processos

def soma(a, b):
    r = a + b

    return r

def sub(a, b):
    r = a - b

    return r

def mult(a, b):
    r = a * b

    return r

def div(a, b):
    r = a / b

    return r


# num1 = float(input('Digite um numero: '))
# num2 = float(input('Digite um numero: '))

subprocess.run('cls' , shell=True)

num1 = random.randint(10,100)
num2 = random.randint(1, 10)

print(f'numero {num1} e numero {num2}')

print("""
[1] - soma
[2]- subtracao 
[3] - multiplicação
[4] - divisão
""")

operacao = int(input('deseja fazer qual operação?'))

match operacao:
    case 1:
        resultado = soma(num1, num2)

    case 2:
        resultado = sub(num1, num2)

    case 3:
        resultado = mult(num1, num2)

    case 4:
        resultado = div(num1, num2)

    case _:
        resultado = 'invalido!!!!'

print(f'resultado: {resultado}')