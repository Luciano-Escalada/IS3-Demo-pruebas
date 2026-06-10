from scripts.calculos import suma_v1, suma_v2, suma_v3

###########################################################################################################
# Test versión 1.0
# Pruebas básicas con números enteros, sin validaciones ni manejo de errores.
# Esto falla y se tiene que refactorizar la función para manejar casos no esperados.
##########################################################################################################

def test_suma_v1():
    """ En este caso se hacen pruebas básicas con números enteros
    """
    assert suma_v1(2, 3) == 5
    assert suma_v1(-1, 1) == 0
    assert suma_v1(0, 0) == 0
    # Pero qué pasa si le paso un string? No hay validaciones, entonces se rompe
    assert suma_v1("2", "3") == 5, "Error: la función no maneja strings, debería devolver un error o manejar la conversión"


###########################################################################################################
# Test versión 2.0
# Pruebas básicas con números enteros, pero también se prueban casos no esperados
# Se agregan validaciones para manejar errores y casos no esperados, pero no se maneja el caso de los 
# decimales, lo que hace que la función no sea tan robusta y fallan los test.
##########################################################################################################

def test_suma_v2():
    """ En este caso se hacen pruebas básicas con números enteros, pero también se prueban casos no esperados
    """
    assert suma_v2(2, 3) == 5
    assert suma_v2(-1, 1) == 0
    assert suma_v2(0, 0) == 0
    # Ahora si le paso un string, no se rompe, hace la conversión y devuelve el resultado correcto
    assert suma_v2("2", "3") == 5
    assert suma_v2("2", 3) == 5
    assert suma_v2(2, "3") == 5
    # Si le paso algo que no se puede convertir a número, devuelve None
    assert suma_v2("dos", "tres") is None
    # Pero si paso un decimal, se rompe porque lo convierte a entero y el resultado no es el esperado
    assert suma_v2(2.5, 3.5) == 6, "Error: la función no maneja decimales, debería devolver 6.0 en lugar de 6"



###########################################################################################################
# Test versión 3.0
# Pruebas más completas con números enteros y decimales, pero también se prueban casos no esperados
# Se usan valores float para poder manejar decimales, lo que hace que la función sea más robusta 
#   y se manejan casos no esperados, lo que hace que los test sean más completos y la función más confiable.
###########################################################################################################
def test_suma_v3():
    """ En este caso se hacen pruebas básicas con números enteros y decimales, pero también se prueban casos no esperados
    """
    assert suma_v3(2, 3) == 5
    assert suma_v3(-1, 1) == 0
    assert suma_v3(0, 0) == 0  
    assert suma_v3("2", "3") == 5
    assert suma_v3(2, "3") == 5
    assert suma_v3("dos", "tres") is None
    # Ahora si le paso un float hace la operación correctamente
    assert suma_v3(2.5, 3.5) == 6.0
    assert suma_v3("2.5", "3.5") == 6.0
    assert suma_v3("2.5", 3.5) == 6.0
    assert suma_v3(2.5, "3.5") == 6.0


###########################################################################################################
# Test versión 3.1
# Pruebas más completas donde se valida la captura de errores en la función suma_v3, con casos no esperados 
# como None o objetos que no se pueden convertir a números.
###########################################################################################################
def test_suma_v3_con_casos_no_esperados():
    """ En este caso se prueban casos no esperados para la función suma_v3
    """
    # Si le paso None, devuelve None
    assert suma_v3(None, None) is None
    assert suma_v3(None, 2) is None
    assert suma_v3(2, None) is None
    # Si le paso un objeto que no se puede convertir a número, devuelve None
    class Objeto:
        pass

    assert suma_v3(Objeto(), Objeto()) is None
    assert suma_v3(Objeto(), 2) is None
    assert suma_v3(2, Objeto()) is None


#######################################################################################################
# Función suma version 3.2
# Pytest tiene una funcionalidad llamada parametrize que permite ejecutar el mismo test con diferentes 
# conjuntos de datos, lo que hace que los test sean más completos y fáciles de mantener.
# Se agregan pruebas con diferentes combinaciones de valores, incluyendo casos no esperados, lo
#######################################################################################################

import pytest # Esto debería ir arriba en el archivo

@pytest.mark.parametrize(
    "valor_a, valor_b, resultado",
    [
        (2, 3, 5),           
        (-1, 1, 0), # suma de un entero negativo           
        (0, 5, 5),
        ("2.5", "3.5", 6.0),
        ('2', 5, 7),
        (2, suma_v3(2, 2), 6), # Propiedad asociativa
        (None, None, None),
        (None, 2, None),
        (2, None, None),
        (suma_v3(2, 3), suma_v3(4, 5), 14) # Propiedad distributiva
    ]
)
def test_varios_casos(valor_a, valor_b, resultado):
    assert suma_v3(valor_a, valor_b) == resultado