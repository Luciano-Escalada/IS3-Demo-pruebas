from behave import given, when, then
from scripts.liquidacion import Liquidacion


@given("un empleado con {horas:d} horas trabajadas y {antiguedad:d} años de antigüedad")
def step_empleado_con_horas_y_antiguedad(context, horas, antiguedad):
    context.horas = horas
    context.antiguedad = antiguedad
    context.liquidacion = Liquidacion()


@when("se calcula la liquidación completa del sueldo")
def step_calcular_liquidacion_completa(context):
    context.resultado = context.liquidacion.calcular_sueldo_empleado(
        context.horas,
        context.antiguedad
    )


@then("el sueldo neto resultante debe ser {esperado:d}")
def step_validar_sueldo_neto(context, esperado):
    assert context.resultado == esperado, (
        f"Se esperaba {esperado}, pero se obtuvo {context.resultado}"
    )