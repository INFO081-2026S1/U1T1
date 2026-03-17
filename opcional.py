""" Instrucciones

No cambies las definiciones (nombres y argumentos) de las funciones dadas aquí.
Por ahora, es opcional abordar las excepciones (p.ej., comprobar si el argumento es un número, 
    no una cadena cuando la función es para sumar los argumentos).
    Así que esta pauta no incluye código try-except, pero lo utilizaremos en el futuro.
Esta pauta no implica tipos de datos (p.ej., diccionario), funciones, métodos o cosas que no hayamos
    aprendido en las clases antes de la publicación de esta tarea. Pero las utilizaremos en el futuro 
    para simplificar el código. 
Esta pauta trata de seguir PEP 8 para su estilo.
"""

# Ejercicio 1
def contar_vocales(palabra):
    ...

# Ejercicio 2
# Asumimos que el número dado es un entero positivo.
def calcular_suma_digitos(numero):
    ...

# Ejercicio 3
def calcular_palabras(cadena):
    ...

# Ejercicio 4
def obtener_max_min(lista):
    ...


# Para llamar y comprobar tus funciones
def main():
    print("Ejer 1:")
    print(contar_vocales("")) # 0
    print(contar_vocales("pera")) # 2
    print(contar_vocales(" ZANAORIA!")) # 5
    print(contar_vocales("carácter")) # 3

    print("Ejer 2:")
    print(calcular_suma_digitos(1)) # 1
    print(calcular_suma_digitos(9)) # 9
    print(calcular_suma_digitos(19)) # 10
    print(calcular_suma_digitos(200)) # 2
    print(calcular_suma_digitos(9413)) # 17

    print("Ejer 3:")
    print(calcular_palabras("¿Cachai, Homer Simpson?")) # 3
    print(calcular_palabras(" Cachai,   Yun? ")) # 2
    print(calcular_palabras("")) # 0
    print(calcular_palabras("\tWena!\nGenial!\r")) # 2 (Opcional a comprobar)

    print("Ejer 4:")
    print(obtener_max_min([])) # [] (¡Hay que considerarlo!)
    print(obtener_max_min([1, 2, 5])) # [5, 1]
    print(obtener_max_min([-10, 2.5, -4.7, 9, 0])) # [9, -10]


# No elimines esta parte que es para evitar que se ejecute el código cuando sea importado como un módulo.
if __name__ == "__main__":
    main()