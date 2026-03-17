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
def calcular_puntaje(N, C):
    ...

# Ejercicio 2
def es_primo(x):
    ...

# Ejercicio 2 Variante:
def es_buen_numero(n, lista):
    ...

# Ejercicio 3
def imprimir_parejas(nombres):
    ...

# Ejercicio 3 variante
def obtener_parejas(nombres):
    ...

# Ejercicio 4
def obtener_asiento(nombre):
    ...

# Ejercicio 5
def comprobar_minuto(tiempo, minuto):
    ...

# Ejercicio 6
def es_palindromo(cadena):
    ...

# Ejercicio 7
# Asumimos que N dado es un entero positivo, mayor o igual a 1. (Opcional: comprobar si es entero >= 1)
def generar_fibonacci(N):
    ...

    # Solución 2 (con while):
    # while len(lista) < N:
    #     siguiente = lista[-2] + lista[-1]
    #     lista.append(siguiente)
    # return lista

# Para llamar y comprobar tus funciones
def main():
    print("Ejer 1:")
    print(calcular_puntaje(1.5, 2.5)) # 77.5
    print(calcular_puntaje(1, 0)) # 10
    
    print("\nEjer 2:")
    print(es_primo(1)) # False
    print(es_primo(2)) # True
    print(es_primo(100)) # False
    print(es_primo(101)) # True

    print("\nEjer 2 variante:")
    print(es_buen_numero(6, [2, 3])) # True
    print(es_buen_numero(6, [5, 2, 3])) # False
    print(es_buen_numero(8, [3, 4, 8])) #False
    print(es_buen_numero(120, [2, 3, 6, 7])) # False
    print(es_buen_numero(1, [2, 3])) #False
    print(es_buen_numero(120, [])) # False

    print("\nEjer 3:")
    nombres = ["Ana", "Pablo", "Juan", "Eliana"]
    imprimir_parejas(nombres)

    print("\nEjer 3 Variante:")
    nombres = ["Ana", "Pablo", "Juan", "Eliana"]
    print(obtener_parejas(nombres))

    print("\nEjer 4:")
    print(obtener_asiento("Ana"))
    print(obtener_asiento("Pablo"))
    print(obtener_asiento("Yun")) # Opcional para comprobar
    print(obtener_asiento("ana")) # Opcional para comprobar

    print("\nEjer 5:")
    print(comprobar_minuto("14:02:13", 2)) # True
    print(comprobar_minuto("14:02:13", 22)) # False
    print(comprobar_minuto("14:02:13", 65)) # False
    print(comprobar_minuto("14:02:13", -1)) # False

    print("\nEjer 6:")
    print(es_palindromo("anilina")) # (7 carácteres, minú) True
    print(es_palindromo("AnIlina")) # (7 carácteres, con mayú) True
    print(es_palindromo("reconocer")) # (7 caracteres, con mayú) True
    print(es_palindromo(" dabale arroz a   la zorra el abad ")) # (frase, con espacio) True
    print(es_palindromo("Amor Roma")) # (8 caracteres) True
    print(es_palindromo("hola")) # False

    print("\nEjer 7:")
    print(generar_fibonacci(1)) # [0]
    print(generar_fibonacci(2)) # [0, 1]
    print(generar_fibonacci(3)) # [0, 1, 1]
    print(generar_fibonacci(4)) # [0, 1, 1, 2]
    print(generar_fibonacci(10)) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# No elimines esta parte que es para evitar que se ejecute el código cuando sea importado como un módulo.
if __name__ == "__main__":
    main()