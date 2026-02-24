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

ex9()



