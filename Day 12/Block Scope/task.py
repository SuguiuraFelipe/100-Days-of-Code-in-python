def is_prime(num):
    # 1 não é um número primo
    if num <= 1:
        return False
    # 2 e 3 são primos
    if num == 2 or num == 3:
        return True
    # Elimina números pares e divisíveis por 3
    if num % 2 == 0 or num % 3 == 0:
        return False
    # Verificar outros possíveis divisores até a raiz quadrada de num
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True