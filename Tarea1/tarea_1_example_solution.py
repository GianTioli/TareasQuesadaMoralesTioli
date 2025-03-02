# tarea_1_example_solution.py

def separa_letras(cadena):
    """
    Separa las letras de la cadena en mayúsculas y minúsculas,
    retornando códigos de error o éxito según indicado en tarea_1_testing.py
    Códigos esperados:
      - -100: No es un string
      - -200: Carácter no válido
      - -300: String vacío
       0: Éxito
    """

    # 1. Verifica si la entrada es un string
    if not isinstance(cadena, str):
        return (-100, None, None)

    # 2. Verifica si la cadena es vacía
    if cadena == "":
        return (-300, None, None)

    # 3. Verifica que la cadena contenga únicamente letras válidas
    letras_mayusculas = [chr(i) for i in range(65, 91)] + ["Ñ"]
    letras_minusculas = [chr(i) for i in range(97, 123)] + ["ñ"]
    letras_validas = set(letras_mayusculas + letras_minusculas)

    for letra in cadena:
        if letra not in letras_validas:
            return (-200, None, None)

    # 4. Construye las cadenas de mayúsculas y minúsculas
    mayus = "".join(letra for letra in cadena if letra in letras_mayusculas)
    minus = "".join(letra for letra in cadena if letra in letras_minusculas)

    # 5. Éxito
    return (0, mayus, minus)


def potencia_manual(base, potencia):
    """
    Calcula la potencia (base ^ potencia) sin usar el operador '*',
    retornando códigos de error o éxito según indicado en tarea_1_testing.py.
    Códigos esperados:
    - -400: Base o potencia son strings
    0: Éxito
    """

    # 1. Verifica si base o potencia son strings
    if isinstance(base, str) or isinstance(potencia, str):
        return (-400, None)

    # Función auxiliar para multiplicar sin usar '*'
    def multiplica(a, b):
        resultado = 0
        negativo = False
        if a < 0:
            a = -a
            negativo = not negativo
        if b < 0:
            b = -b
            negativo = not negativo
        for _ in range(b):
            resultado += a
        if negativo:
            resultado = -resultado
        return resultado

    # 2. Manejo de la potencia
    # El test no especifica más validaciones (ej.potencia negativa),
    # solo verifica que no sea string. Aun así, podemos manejar potencia 0:
    if potencia == 0:
        return (0, 1)

    # 3. Calcula la potencia manualmente
    resultado = 1
    for _ in range(potencia):
        resultado = multiplica(resultado, base)

    # 4. Éxito
    return (0, resultado)


# Ejemplo rápido para probar manualmente en consola antes de correr pytest:
if __name__ == "__main__":
    print(separa_letras("HolaMUndoÑ"))
    print(separa_letras(7))
    print(potencia_manual(3, 3))
    print(potencia_manual("3", 4))
