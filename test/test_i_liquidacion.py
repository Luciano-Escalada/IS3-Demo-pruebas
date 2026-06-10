###########################################################################################################
# Test de integración del caso de Liquidación de sueldos.
#
# Se valida el flujo completo de cálculo (básico -> bruto -> neto) comparando:
# 1) el resultado del método integral `calcular_sueldo_empleado`, y
# 2) el resultado obtenido al ejecutar paso a paso cada función.
#
# Además, se verifican valores esperados explícitos para distintos tramos de antigüedad.
##########################################################################################################

import pytest
import scripts.liquidacion as lq


@pytest.fixture
def setup():
    """Crea una instancia estándar de Liquidacion para reutilizar en pruebas."""
    instancia = lq.Liquidacion()
    return instancia


@pytest.mark.parametrize(
    "hs_trabajadas, antiguedad, total_esperado",
    [
        (40, 3, 2232560.00),
        (40, 6, 2421760.00),
        (40, 12, 2610960.00),
        (40, 25, 2800160.00),
    ],
)
def test_integrado(setup, hs_trabajadas, antiguedad, total_esperado):
    """Valida consistencia interna y resultado final esperado del cálculo integrado."""
    un_empleado = setup
    total_fc = un_empleado.calcular_sueldo_empleado(hs_trabajadas, antiguedad)

    basico = un_empleado.calcular_sueldo_basico(hs_trabajadas)
    bruto = un_empleado.calcular_sueldo_bruto(basico, antiguedad)
    total_fs = un_empleado.calcular_sueldo_neto(bruto)

    assert total_fc == total_fs
    assert total_fc == total_esperado