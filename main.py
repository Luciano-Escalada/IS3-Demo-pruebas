from scripts.liquidacion import Liquidacion


def main():
    print("Liquidacion de sueldos de prueba")

    horas = int(input("Ingrese cantidad de horas trabajadas: "))
    antiguedad = int(input("Ingrese la antiguedad del empleado: "))

    liq = Liquidacion()

    print("Se procede con la liquidacion:")
    sueldo_basico = liq.calcular_sueldo_basico(horas)
    print(f"Sueldo basico: ${sueldo_basico}")

    sueldo_bruto = liq.calcular_sueldo_bruto(sueldo_basico, antiguedad)
    print(f"Sueldo bruto: ${sueldo_bruto}")

    sueldo_neto = liq.calcular_sueldo_neto(sueldo_bruto)
    print(f"Sueldo neto: ${sueldo_neto}")

    total = liq.calcular_sueldo_empleado(horas, antiguedad)
    print(f"Sueldo neto a pagar: ${total}")

if __name__ == "__main__":
    main()
