#########################################################################
# Script: calculos.py
# Descripción: Funciones para realizar cálculos matemáticos
# Objetivo: Revisar evolución del código al refactorizar post-tests
###########################################################################

"""
    Script con funciones para realizar cálculos matemáticos, 
    utilizado para realizar pruebas unitarias y TDD.
"""

############################################################
# Función suma version 1.0
# Suma y no mucho más, sin validaciones ni manejo de errores
#############################################################

def suma_v1(a, b):
    """ Función que realiza una suma 
        de dos argumentos

    Args:
        a (int/float): argumento a
        b (int/float): argumento b

    Returns:
        int/float: resultado de la suma
    """
    return a + b

####################################################################
# Función suma version 2.0
# Se agregan validaciones para manejar errores y casos no esperados
####################################################################

def suma_v2(a, b):
    """ Función que realiza una suma 
        de dos argumentos

    Args:
        a (int/float): argumento a
        b (int/float): argumento b

    Returns:
        int/float: resultado de la suma
    """
    try:
        num_a = int(a)
        num_b = int(b)
        return num_a + num_b
    except (TypeError, ValueError):
        return  None

##############################################################
# Función suma version 3.0
# Se agregan validaciones para manejar errores y casos no esperados
# Se agrega manejo de decimales y se mejora la documentación
##############################################################  

def suma_v3(a, b):
    """ Función que realiza una suma 
        de dos argumentos, con manejo de errores y decimales

    Args:
        a (int/float): argumento a
        b (int/float): argumento b  

    Returns:
        int/float: resultado de la suma, o None si hay un error
    """
    try:
        num_a = float(a)
        num_b = float(b)
        return num_a + num_b
    except (TypeError, ValueError):
        return  None