def tabla_amortizacion(dinero, plazo, interes):
    exp = pow(1 + interes, plazo)

    cuota = dinero * ((exp * interes) / (exp - 1))
    interes_actual = dinero * interes
    abono = cuota - interes_actual
    saldo = dinero - abono

    datos_periodo = {
        "periodo": 1,
        "cuota": cuota,
        "intereses": interes_actual,
        "abono_k": abono,
        "saldo": saldo,
    }

    periodo = 1
    while periodo <= plazo:
        yield datos_periodo

        datos_periodo["intereses"] = datos_periodo["saldo"] * interes
        datos_periodo["abono_k"] = cuota - datos_periodo["intereses"]
        datos_periodo["saldo"] -= datos_periodo["abono_k"]

        periodo += 1
        datos_periodo["periodo"] = periodo


if __name__ == "__main__":
    intereses = {6: 0.20, 12: 0.25, 24: 0.30, 36: 0.35, 0.48: 0.40, 72: 0.50}

    meses = 6
    cuota_t = 0
    interes_t = 0
    abono_t = 0
    for fila in tabla_amortizacion(10000, meses, intereses[meses]):
        string = (
            f"Periodo: {fila['periodo']} \n"
            f"Cuota: {fila['cuota']} \n"
            f"Intereses: {fila['intereses']} \n"
            f"Abono capital: {fila['abono_k']} \n"
            f"Saldo: {fila['saldo']} \n"
        )
        print(string)
        cuota_t += fila["cuota"]
        interes_t += fila["intereses"]
        abono_t += fila["abono_k"]

    resumen = (
        "TOTAL: \n"
        f"Total de cuota: {cuota_t} \n"
        f"Total de intereses: {interes_t} \n"
        f"Total de abono capital: {abono_t} \n"
    )
    print(resumen)
