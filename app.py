# Projeto impar ou par
# 0 2 4 6 8 10...(pares)
# 1 3 5 7 9 11...(ímpares)
# operador Mod() = % = módulos
# o que determina se o valor é par ou ímpar é o 'resto' que sobrar de X % 2
# resto = 0 (par) | resto = 1 (ímpar)
while True:
    try:
        valor = int(input('Digite um valor:'))
        if valor % 2 == 0:
            print('Número par')
        else:
            print('Número ímpar')
    except:
        print('Digite apenas números')
