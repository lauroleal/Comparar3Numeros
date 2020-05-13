
# ENTRADA DO PRIMEIRO NÚMERO

numero_Um = int(input("Digite o primeiro número: "))

# SUPONDO QUE O PRIMEIRO NÚMERO DIGITADO É O MAIOR

maior_Numero = numero_Um

# ENTRADA DO SEGUNDO NÚMERO

numero_Dois = int(input("Digite o segundo número: "))

# ENCONTANDO O #MAIOR E O #MENOR DOS DOIS PRIMEIROS NÚMEROS DIGITADOS

if  maior_Numero <= numero_Dois:
    maior_Numero = numero_Dois
    menor_Numero = numero_Um
else:
    menor_Numero = numero_Dois

# ENTRADA DO TERCEIRO NÚMERO

numero_Tres = int(input("Digite o terceiro número: "))

# COMPARANDO O TERCEIRO NÚMERO DIGITADO COM O #MAIOR E O #MENOR
# NÚMERO JÁ ENCONTRADOS

if maior_Numero <= numero_Tres:
    maior_Numero = numero_Tres
else:
    if menor_Numero >= numero_Tres:
        menor_Numero = numero_Tres

# ......................................................................
# NÚMEROS SÃO IGUAIS
# ......................................................................

if numero_Um == numero_Dois:
    if numero_Dois == numero_Tres:
        print("........................")
        print("Os 03 números são iguais")
        print("........................")
else:

    # ...................................................................
    # MOSTRANDO O MAIOR E O MENOR NÚMERO
    # ...................................................................

    print(".....................................")
    print("...... O maior número é:", maior_Numero)
    print("...... O menor número é:", menor_Numero)
    print(".....................................")

