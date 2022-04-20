''' 
Script en Python que permite 
calcular el tiempo actual
'''

import datetime

ahora = datetime.datetime.now()
print(ahora.strftime("%d/%m/%Y %H:%M:%S"))