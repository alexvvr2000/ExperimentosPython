def mcm(num1: float, num2: float) -> float:
    # Primera iteracion para ver si el num1 es el mcm
    residuo: float = num1 % num2
    divisor_actual = num1

    # Almacena el residuo actual y le saca el siguiente con el almacenado
    while residuo != 0:
        divisor_actual = residuo
        residuo: float = divisor_actual % residuo

    return divisor_actual


if __name__ == "__main__":
    print(mcm(1, 2))
