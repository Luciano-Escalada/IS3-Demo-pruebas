#########################################################################
# Script: suma_steps.py
# Descripción: Archivo con los pasos definidos para las pruebas BDD de
#   la función suma que está definida en el módulo calculos.py, utilizando
#   el framework Behave que toma como base suma.feature.
# Objetivo: Definir los pasos necesarios para ejecutar las pruebas BDD de
#   la función suma, validando su correcta implementación.
###########################################################################

from behave import given, when, then
# Se importa la función suma_v3 para realizar las pruebas, 
#   se puede cambiar a suma_v1 o suma_v2 según se necesite.
from scripts.calculos import suma_v3 as suma 


@given("tengo los números {a} y {b}")
def step_given_tengo_los_numeros(context, a, b):
    """ Función para el paso de "tengo los números"

    Args:
        context (behave.runner.Context): objeto de contexto de Behave para compartir datos entre pasos
        a (str): primer número como cadena
        b (str): segundo número como cadena
    """
    context.a = int(a)
    context.b = int(b)


@when("los sumo")
def step_when_los_sumo(context):
    """ Función para el paso de "los sumo"

    Args:
        context (behave.runner.Context): objeto de contexto de Behave para compartir datos entre pasos
    """
    context.resultado = suma(context.a, context.b)


@then("el resultado debe ser {esperado:d}")
def step_then_el_resultado_debe_ser(context, esperado):
    """ Función para el paso de "el resultado debe ser"

    Args:
        context (behave.runner.Context): objeto de contexto de Behave para compartir datos entre pasos
        esperado (int): resultado esperado
    """
    assert context.resultado == esperado, (
        f"Esperado {esperado}, pero fue {context.resultado}"
    )
