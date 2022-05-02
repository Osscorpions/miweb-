'''
nombre_archivo: edad.py
Script en Python para saber si una persona es mayor a 18 años y que puede hacer.
autor: Oscar Salgado
'''

def mayoria_edad(edad):
    edad = int(input("Escriba su edad: "))
    if edad < 0: 
        print("Wait, that's illegal")
    elif edad > 100:
        print("Tu no deberías estar vivo, si lo estás es un milagro")

    elif edad < 18:
        print("Aún no eres legal")
    else: 
        print("Ya eres mayor de edad, puedes sacar tu INE")
    return edad

mayoria_edad(None)