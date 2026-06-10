# Demo Pruebas

Este repositorio esta armado como practica guiada para el tema de pruebas de software.
El objetivo es aprender como evoluciona el codigo cuando se trabaja con tests (que pueden ser automatizados).

## Cátedras y carreras

Ingeniería de Software III / Actualidad Informática  
Lic. en Sistemas de Información / Analista en Sistemas de Computación  
FCEQyN | UNaM

## Parte 1 - Tests unitarios y TDD

- `scripts/calculos.py`: implementacion de funciones de suma en distintas versiones.
- `test/test_calculos.py`: pruebas unitarias para observar comportamiento esperado y fallos.

### Objetivo de aprendizaje (modulo calculos)

La idea de `suma_v1`, `suma_v2` y `suma_v3` no es solo tener tres funciones distintas.
La progresion esta pensada para mostrar como se trabaja bajo TDD:

1. Se escribe un test que describe el comportamiento esperado.
2. El test falla (fase **Red**).
3. Se cambia el codigo para que pase (fase **Green**).
4. Se mejora la solucion manteniendo tests en verde (fase **Refactor**).

En esta practica, cada version representa una respuesta a nuevos casos que aparecen al ejecutar pruebas.

### Progresion de versiones en `calculos.py`

#### `suma_v1(a, b)`

- Implementacion minima: retorna `a + b`.
- Sirve para pasar casos basicos con enteros.
- Limite intencional: si se pasan strings numericos, Python concatena (`"2" + "3" -> "23"`).

Aprendizaje TDD: la version inicial suele ser pequena y suficiente para el primer set de tests.

#### `suma_v2(a, b)`

- Agrega validacion/conversion con `int()`.
- Introduce manejo de errores con `try/except`.
- Devuelve `None` ante entradas invalidas.

Aprendizaje TDD: cuando aparecen tests que revelan entradas no previstas, el codigo evoluciona para cubrirlas.

#### `suma_v3(a, b)`

- Extiende el comportamiento a decimales usando `float()`.
- Mantiene manejo de errores para no romper ante datos no numericos.
- Devuelve `None` cuando no puede convertir entradas.

Aprendizaje TDD: se agregan capacidades de forma incremental, guiadas por nuevos tests.


## Parte 2 - Tests unitarios y de integración

- `scripts/liquidacion.py`: implementacion de funciones de liquidación básica de sueldos.
- `test/test_u_liquidacion.py`: pruebas unitarias para observar comportamiento esperado y fallos de cada método / función.
- `test/test_i_liquidacion.py`: pruebas de integración (internas ya que no se utilizan servicios externos) para la clase y funcionalidad de liquidación.

### Objetivo de aprendizaje (modulo liquidación)

La idea de `Liquidacion` como clase es tener un ejemplo más elaborado aunque sin tantos detalles como sería en el mundo real.
La propuesta en este caso se basa en:

1. Observar la implementación de los tests y el código como parte de TDD.
2. Avanzar sobre la implmenetación de varios casos de pruebas unitarias.
3. Observar una aproximación a pruebas de integración para este caso.

En esta practica, cada test tiene su objetivo y es lograr cobertura de pruebas para toda la aplicación en este flujo operativo.


## Parte 3 - Introducción a BDD

TODO:reescribir
- `scripts/liquidacion.py`: implementacion de funciones de liquidación básica de sueldos.
- `test/test_u_liquidacion.py`: pruebas unitarias para observar comportamiento esperado y fallos de cada método / función.
- `test/test_i_liquidacion.py`: pruebas de integración (internas ya que no se utilizan servicios externos) para la clase y funcionalidad de liquidación.

### Objetivo de aprendizaje (modulo liquidación)

La idea de `Liquidacion` como clase es tener un ejemplo más elaborado aunque sin tantos detalles como sería en el mundo real.
La propuesta en este caso se basa en:

1. Observar la implementación de los tests y el código como parte de TDD.
2. Avanzar sobre la implmenetación de varios casos de pruebas unitarias.
3. Observar una aproximación a pruebas de integración para este caso.

En esta practica, cada test tiene su objetivo y es lograr cobertura de pruebas para toda la aplicación en este flujo operativo.


## Como replicar la practica

1. Instalar `uv` (si no lo tenes instalado):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Sincronizar dependencias del proyecto:

```bash
uv sync
```

3. Ejecutar tests:

```bash
uv run pytest -q
```

4. Generar reportes individuales (librería: pytest-html):
```bash
uv run pytest --html=docs/reporte_calculos.html --self-contained-html test/test_calculos.py
```

5. Generar reportes de covertura de tests (librería: pytest-cov):
```bash
uv run pytest --cov=scripts --cov-report=html:docs/coverage
```

## Observaciones

En este repositorio, la coexistencia de `suma_v1`, `suma_v2` y `suma_v3` es deliberada para mostrar los ejemplos.
En un proyecto productivo, normalmente se mantiene una sola implementacion consolidada.
Para el caso de liquidación, una observación similar es que la complejidad del cálculo está minimizada a fines de que se comprendan los conceptos aplicables y no es exactamente fiel a la normativa aplicable.

### Material extra:

* [Tutorial](https://realpython.com/pytest-python-testing/)