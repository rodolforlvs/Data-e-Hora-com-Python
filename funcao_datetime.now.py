from datetime import datetime

data = datetime.now()
atual = data.strftime("%d/%m/%Y, %H:%M:%S")
print(f'A data e hora atual de hoje é: \n{atual}')
