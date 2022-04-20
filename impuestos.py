'''
Script en Python donde se tiene que calcular montos con y sin
impuesto a través de una calculadora :v
'''


def calcular_total(pago_sin_impuesto):
    return pago_sin_impuesto+pago_sin_impuesto * (impuesto/100)
pago_sin_impuesto = float(input("Proporcione el pago sin impuestos: "))
impuesto = float(input("Proporcione el monto del impuesto: "))
pago_con_impuesto = calcular_total(pago_sin_impuesto, impuesto)
print(f'pago con impuesto: {pago_con_impuesto}')