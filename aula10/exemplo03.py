


import random
import subprocess
from auxiliar import dobro, triplo , quadrado

# def dobro(a):
#     r = a * 2
    
#     return r 

# def triplo(a):
#     r = a * 3
    
#     return r 

# def quadrado(a):
#     r = a ** 2
    
#     return r 


  
# numero = float(input("Digite um número: "))

subprocess.run('cls' , shell=True)

numero = random.randint(10,100)

print("""
[2] - dobro
[3]- triplo 
[4] - Quadrado
""")

opcao = int(input('informe a opçao: '))

print(f'numero sorteado {numero}')

match opcao:
    case 2:
        resultado = dobro(numero)  
        # print(f"O dobro de  {numero} é {resultado1}")

    case 3:
        resultado = triplo(numero) 
        # print(f"O triplo de  {numero} é {resultado2}")

    case 4:
        resultado = quadrado(numero) 
        # print(f"O quadrado de  {numero} é {resultado3}")
    case _:
        resultado = 'opcao invalida'
        # print('opcao invalida')

print(f'resultado: {resultado}')
