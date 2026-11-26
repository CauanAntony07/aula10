def pesca(p):
    e = p - 100
    m = e * 4 
    return e, m


# e = excedende
# m = multa
# def alguma coisa(letra q vem dps do =)
# usamos apenas uma letra para fazer esse calculo dentro do "def"
# dps return as letrinhas 


peso_maximo = 100
# cria a variavel do peso maximo
peso = float(input('Informe  o peso dos peixes: '))
# pergunta o peso

if peso > peso_maximo:
    pes_exc, multa = pesca(peso)
    # coloca variaveis novas aqui dentro com , e espaço, dps coloca = (oq vc colocou no dps de def)
    print(f'\nVoce pescou demais, sua multa e de: {pes_exc}')
    print(f'sua multa e de: {multa}')

else:
    print('Pescou no limite, sem multa.')