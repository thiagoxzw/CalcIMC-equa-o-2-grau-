peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    categoria = "Abaixo do peso"
    a = -1
    b = 10
elif imc < 25:
    categoria = "Normal"
    a = -1
    b = 12
else:
    categoria = "Sobrepeso"
    a = -1
    b = 14

x = -b / (2 * a)  # treino ideal
desempenho = a * (x ** 2) + b * x

print("Resultado do treino:" )
print(f"IMC: {imc:.2f} kg")
print(f"Classificação: {categoria}")
print(f"Treino ideal: {x:.1f} horas/semana")
print(f"Tempo de treino na semana (em horas): {desempenho:.2f}")