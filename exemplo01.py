def calcula_bonus(v, s):
    b = v * 0.10
    s = s + b
    return b, s



# incio do codigo
META = 12000


venda = float(input('informe a venda do vendedor: '))
salario = float(input('informe o salario: '))


if venda >= META:
    # CHAMA A FUNÇAO P/ BONUS DE 10
    bonus, novo_salario = calcula_bonus(venda, salario)
    print(f'\nValor do bonus R$: {bonus:.2f}')
    print(f'salario com bonus R$: {novo_salario}')

else:
    print('sem bonus')
    print(f'Salario: R$: {salario}')