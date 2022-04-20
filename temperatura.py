
def celsius_fahrenheit(celsius):
    return celsius * 9/5 + 32 
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit -32) * 5/9
fahrenheit = float(input("Inserte el valor en grados Celsius: "))
resultado = fahrenheit_celsius (fahrenheit)
print(f'{fahrenheit} °F a °C: {resultado: .2F}')

celsius = float(input("Inserte un valor en grados Fahrenheit: "))
resultado = celsius_fahrenheit(celsius)

print(f'{celsius} °C a °F: {resultado: .2F}')