import openpyxl

# Cria uma nova planilha
wb = openpyxl.Workbook()

# Seleciona a planilha ativa
planilha = wb.active

# Define o valor da célula A1
planilha['A1'] = 'Olá, Excel com Python!'

# Salva a planilha com o nome "Exemplo.xlsx"
wb.save('Exemplo.xlsx')

print("Planilha criada com sucesso!")
