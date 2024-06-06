nome_aluno = input("Digite o nome do aluno: ")
nome_disciplina = input("Digite o nome da disciplina: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2)/2
if media >=6:
    situacao = "Aprovado(a)"
else:
    situacao = "Reprovado(a)"
print(f'{nome_aluno} está {situacao} na disciplina {nome_disciplina}')