#########################################################################
# Archivo: suma.feature
# Descripción: descripción de casos de prueba para la función de suma de 
#   dos números en formato Gherkin, base para BDD.
# Objetivo: validar la correcta implementación de la función de suma en 
#   diferentes escenarios.
###########################################################################

Feature: Suma de dos números

  Scenario: Sumar dos números positivos
    Given tengo los números 3 y 5
    When los sumo
    Then el resultado debe ser 8

  Scenario: Sumar un número positivo y un número negativo
    Given tengo los números 7 y -2
    When los sumo
    Then el resultado debe ser 5

  Scenario: Sumar dos números negativos
    Given tengo los números -4 y -6
    When los sumo
    Then el resultado debe ser -10