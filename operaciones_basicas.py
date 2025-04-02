"""Este script contiene clases y funciones para realizar operaciones matemáticas
   básicas y calcular el promedio de una lista de números.

Clases:
    - OperacionesBasicas: Realiza operaciones de suma y resta.
    - CalculadoraPromedio: Calcula el promedio de una lista de valores.

Variables globales:
    - NUMEROS: Lista de números para el cálculo del promedio.
    - NUM1, NUM2: Números utilizados en las operaciones básicas.
"""


# pylint: disable=too-few-public-methods

class OperacionesBasicas:
    """Clase para realizar operaciones matemáticas básicas como suma y resta."""

    def __init__(self):
        """Inicializa la clase con un atributo resultado en 0."""
        self.resultado = 0

    def sumar(self, a, b):
        """Suma dos números y almacena el resultado.

        Args:
            a (int o float): Primer número.
            b (int o float): Segundo número.
        """
        self.resultado = a + b

    def restar(self, a, b):
        """Resta dos números y almacena el resultado.

        Args:
            a (int o float): Primer número.
            b (int o float): Segundo número.
        """
        self.resultado = a - b

    def obtener_resultado(self):
        """Obtiene el resultado de la última operación realizada.

        Returns:
            int o float: Resultado de la operación matemática.
        """
        return self.resultado


class CalculadoraPromedio:
    """Clase para calcular el promedio de una lista de valores."""

    def __init__(self, valores):
        """Inicializa la clase con una lista de valores.

        Args:
            valores (list): Lista de números para calcular el promedio.
        """
        self.valores = valores

    def calcular_promedio(self):
        """Calcula el promedio de los valores proporcionados.

        Returns:
            float: El promedio de la lista de valores.
        """
        suma = sum(self.valores)
        resultado_promedio = suma / len(self.valores)
        return resultado_promedio


# Variables globales
NUMEROS = [1, 2, 3, 4, 5]  # Lista de números para el cálculo del promedio
NUM1 = 10  # Primer número para operaciones básicas
NUM2 = 20  # Segundo número para operaciones básicas

# Ejecución principal
if __name__ == "__main__":
    # Usar la clase OperacionesBasicas
    operaciones = OperacionesBasicas()
    operaciones.sumar(NUM1, NUM2)
    print(f"El resultado de la suma es: {operaciones.obtener_resultado()}")

    operaciones.restar(NUM1, NUM2)
    print(f"El resultado de la resta es: {operaciones.obtener_resultado()}")

    # Usar la clase CalculadoraPromedio
    calculadora_promedio = CalculadoraPromedio(NUMEROS)
    resultado_promedio = calculadora_promedio.calcular_promedio()
    print(f"El promedio de los números es: {resultado_promedio}")
