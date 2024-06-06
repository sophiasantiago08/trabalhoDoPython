hora = int(input("Digite uma hora: "))
if 0<= hora <12:
        periodo = "Manhã"
elif 12<= hora <18:
    periodo = "Tarde"
else:
    periodo = "Noite"
print(f'O horário corresponde á {periodo}')