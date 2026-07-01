import pytest
from scripts.liquidacion import Liquidacion


@pytest.fixture
def liquidacion():
    return Liquidacion()


def test_luciano_calcular_sueldo_basico_45_horas(liquidacion):
    """
    Prueba unitaria:
    valida únicamente el método calcular_sueldo_basico.
    """
    resultado = liquidacion.calcular_sueldo_basico(45)

    assert resultado == 2475000.00