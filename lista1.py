import math

def ex1():
    n = int(input("Digite um numero: "))
    if n > 0:
        print("Positivo")
    elif n == 0:
        print("Zero")
    else:
        print("Negativo")

def ex2():
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite um número: "))
    if n1 > n2:
        print(f"{n1} é maior que {n2}")
    elif n1 < n2:
        print(f"{n1} é menor que {n2}")
    else:
        print("Os números são iguais")

def ex3():
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        print("Par")
    else:
        print("Impar")

def ex4():
    nota = int(input("Nota do aluno: "))
    if nota >= 6:
        print("Aprovado")
    else:
        print("Reprovado")

def ex5():
    idade = int(input("Qual sua idade?: "))
    if idade < 18:
        print("Você é menor de idade")
    else:
        print("Boa sorte, você é maior de idade")

def ex6():
    valor = int(input("Qual o valor da compra?: "))
    if valor > 100:
        desconto = valor * 0.10
        valornovo = valor - desconto
        print(valornovo)
    else:
        print("Valor cheio")

def ex7():
    n = int(input("Digite um número: "))
    if n > 10 and n < 50:
        print("O número está entre 10 e 50")
    else:
        print(f"O numero é {n} e ele não está entre 10 e 50")

def ex8():
    lado1 = int(input("Digite o primeiro lado: "))
    lado2 = int(input("Digite o segundo lado: "))
    lado3 = int(input("Digite o terceiro lado: "))
    if lado1 == lado2 == lado3:
        print("Equilatero")
    elif (lado1 == lado2 and lado1 != lado3) or (lado3 == lado1 and lado3 != lado2) or (lado2 == lado3 and lado2 != lado1):
        print("Isosceles")
    else:
        print("Escaleno")

def ex9():
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite um número: "))
    op = input("Digite a operação desejada: +, -, *, / -> ")
    if op == "+":
        print(n1 + n2)
    elif op == "-":
        print(n1 - n2)
    elif op == "*":
        print(n1 * n2)
    elif op == "/":
        print(n1 / n2)
    else:
        print("Não tem esse calculo")

def ex10():
    ano = int(input("Digite o ano desejado: "))
    conta = ano % 4
    if conta == 0:
        conta1 = ano % 100 
        if conta1 == 00:
            conta2 = ano % 400
            if conta2 == 0:
                print("Ano Bissexto")
            else:
                print("Ano normal")
        else:
            print("Ano Bissexto")
    else:
        print("Ano normal")

def ex11():
    user = "navi"
    passw = "n4vi"
    login = input("Digite seu Login: ")
    senha = input("Digite sua senha: ")
    if user == login and passw == senha:
        print("Login Bem-Sucedido")
    else:
        print("Acesso Negado")

def ex12():
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))
    calculo = altura * altura
    imc = peso / calculo
    print(imc)
    if imc < 18.5:
        print("Abaixo do peso.")
    elif imc >= 18.5 and imc <= 24.9:
        print("Peso Ideal")
    elif imc >= 25.0 and imc <= 29.9:
        print("Sobrepeso")
    elif imc >= 30.0 and imc <= 34.9:
        print("Obesidade Grau 1")
    elif imc >= 35.0 and imc <= 39.9:
        print("Obesidade Grau 2")
    else:
        print("Obesidade gordao XJ")

def ex13():
    temp = int(input("Digite a temperatura: "))
    if temp < 15:
        print("Frio")
    elif temp >= 15 and temp <= 25:
        print("Agradavel")
    else:
        print("Quente")

def ex14():
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    n3 = int(input("Digite o terceiro numero: "))
    if n1 > n2 and n1 > n3:
        print(f"O maior número é {n1}")
    elif n2 > n1 and n2 > n3:
        print(f"O maior número é {n2}")
    else:
        print(f"O maior número é {n3}")

def ex15():
    nota = int(input("Digite a nota: "))
    if nota >= 9:
        print("Excelente")
    elif nota >= 7 and nota <= 8:
        print("Bom")
    elif nota == 6:
        print("Regular")
    else:
        print("Reprovado")

def ex16():
    n = int(input("Verifique se o número é primo: "))
    i = 2
    while i < n:
        if n % i == 0:
            break
        else:
            i = i + 1
    if i == n:
        print("O número é primo.")
    else:
        print("Não é primo")

def ex17():
    valor = int(input("Valor do produto: "))
    if valor <= 2000:
        print("Isento")
    elif valor > 2000 and valor < 5000:
        imposto =  valor * 0.10
        print(f"Imposto de {imposto}")
    else:
        imposto1 = valor * 0.20
        print(f"Imposto de {imposto1}")


        
        

    

