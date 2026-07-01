from scripts.liquidacion import Liquidacion


def test_luciano_integracion_liquidacion_completa_45_horas_8_antiguedad():
    """
    Prueba de integración:
    valida el circuito completo de liquidación:
    sueldo básico -> sueldo bruto -> sueldo neto.
    """
    liquidacion = Liquidacion()

    basico = liquidacion.calcular_sueldo_basico(45)
    bruto = liquidacion.calcular_sueldo_bruto(basico, 8)
    neto = liquidacion.calcular_sueldo_neto(bruto)

    resultado_integrado = liquidacion.calcular_sueldo_empleado(45, 8)

    assert basico == 2475000.00
    assert bruto == 3168000.00
    assert neto == 2724480.00
    assert resultado_integrado == neto