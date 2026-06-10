###########################################################################################################
# Test unitarios del caso de Liquidación de sueldos, con pruebas unitarias de las funciones que componen
#   el proceso de liquidación. Se prueba el proceso completo de liquidación, desde el cálculo del sueldo
#   básico, bruto y neto, y se valida que el resultado final sea el esperado.
#
# Se utiliza una instancia de la clase Liquidacion para realizar las pruebas, y se comparan los resultados
#   obtenidos con los resultados esperados, para validar la funcionalidad de la clase.
#
# Se pueden agregar más casos de prueba para validar diferentes escenarios, como por ejemplo empleados
#   con diferentes cantidades de horas trabajadas, diferentes antigüedades, o casos no esperados como
#   valores negativos.
##########################################################################################################

import pytest
import scripts.liquidacion as lq


@pytest.fixture
def setup():
    # Se define en esta clase una instancia de la clase a testear
    instancia = lq.Liquidacion()
    return instancia


def test_instancia_basica(setup):
    """Verifica que la instancia de Liquidacion tenga los valores por defecto esperados."""
    un_empleado = setup
    assert un_empleado.valor_hora == 55000
    assert un_empleado.pct_bonificacion == 8
    assert un_empleado.pct_retenciones == 11
    assert un_empleado.pct_obraSocial == 3


def test_calcular_sueldo_basico(setup):
    """Valida el calculo del sueldo basico para una cantidad fija de horas trabajadas."""
    un_empleado = setup
    hs_trabajadas = 40
    assert un_empleado.calcular_sueldo_basico(hs_trabajadas) == 2200000.00


@pytest.mark.parametrize(
    "valor_a, valor_b, resultado",
    [
        (2200000.00, 3, 2596000.00),
        (2200000.00, 6, 2816000.00),
    ],
)
def test_calcular_sueldo_bruto(setup, valor_a, valor_b, resultado):
    """Comprueba el sueldo bruto en distintos escenarios de antiguedad mediante parametrizacion."""
    un_empleado = setup
    assert un_empleado.calcular_sueldo_bruto(valor_a, valor_b) == resultado



def test_calcular_sueldo_neto(setup):
    """Verifica el calculo del sueldo neto aplicando retenciones y obra social sobre el bruto."""
    un_empleado = setup
    bruto = 2596000.00
    assert un_empleado.calcular_sueldo_neto(bruto) == 2232560.00

