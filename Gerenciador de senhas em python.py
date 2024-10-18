#calculadora de imc em python#


#pedindo irformacões ao úsuario#
peso = int(input("Digite seu peso em KG: "))
alt = float(input("Digite sua altura em metros:  "))

#calculando dados obtidos#
quadrado = alt * alt
imc = peso / quadrado

#razão matemática, dados retidos de https://www.tuasaude.com/calculadora/imc/#
if imc <= 18.5:
    print(f"IMC: {imc:.2f}, Magreza")
elif imc <= 24.9:
    print(f"IMC: {imc:.2f}, Normal")
elif imc <= 29.9:
    print(f"IMC: {imc:.2f}, Sobrepeso")
elif imc <= 34.9:
    print(f"IMC: {imc:.2f}, Obesidade de grau 1")
elif imc <= 40:
    print(f"IMC: {imc:.2f}, Obsidade de grau 2(Severa)")
else:
    print(f"IMC: {imc:.2f}, Obesidade de grau 3(Mórbida)")
exit()