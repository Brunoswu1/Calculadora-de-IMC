print("----------CALCULADORA DE IMC----------")
peso = int(input("Digite o seu Peso em KG:"))
altura = float(input("Digite a sua Altura em Metros:"))
imc = peso/altura**2
imc2 = round(imc,1)
print (f"o seu IMC é", (imc2))
if imc < 18.5:
    print("Você está abaixo do peso ideal.")
elif imc >= 18.5 and imc <=24.9:
    print("Você está no peso ideal.")
elif imc >= 25.0 and imc <=30:
    print("Você está acima do peso ideal.")
elif imc >= 30.1 and imc <=39.9:
    print("Você apresenta obesidade.")
else:
    print("Você apresenta obesidade mórbida")

