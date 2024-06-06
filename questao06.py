nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))
if idade >=16:
    print(f'{nome}, você está apto(a) a emitir seu título de eleitor.')
else:
    print(f'{nome}, vocÊ não está apto(a) a emitir seu título de eleitor')