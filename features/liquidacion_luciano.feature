Feature: Liquidación de sueldo de empleado

  Scenario: Luciano Escalada liquida sueldo con 45 horas y 8 años de antigüedad
    Given un empleado con 45 horas trabajadas y 8 años de antigüedad
    When se calcula la liquidación completa del sueldo
    Then el sueldo neto resultante debe ser 2724480