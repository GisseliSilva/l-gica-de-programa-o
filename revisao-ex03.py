while True:
    nome = input('Digite o seu nome: ')
    if len(nome) < 3:
        print('erro: nome tem que ter mais que 3 caractere.Tente novamente.\n')
    else:
        print('priximo \n')
        break

while True:
    idade = int(input('Digite sua idade: '))
    if idade<0 or idade>150:
        print('erro: numero maior que 0 e menor que 150.Tente novamente.\n')
    else:
        print('próximo \n')
        break

while True:
    salario = float(input('Digite o seu sálario: '))
    if salario < 0:
        print('erro: o valor tem que ser maior que 0.Tente novamente.\n')
    else:
        print('próximo \n')
        break

while True:
    genero = input('Digite seu gênero. \n F (feminino) ou M (masculino): ')
    if genero == f or m:
        print('próximo \n')
    else:
        print('erro: o valor tem que ser maior que 0.Tente novamente.\n')
        break
while True:
    estadocivil = input ('Digite seu estado civil; s para solteiro, c para casado, v para viúvo, D para divorciado: ')
    if estadocivil != ('s','c','v','d'):
        print('erro: o valor tem que ser maior que 0.Tente novamente.\n')
    else:
        print('próximo \n')
        break

print("informacões completa")
print(f'{nome}, {idade}, {salario}, {genero}, {estadocivil}')













    






    


        
