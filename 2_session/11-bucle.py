#veremos como se usa la estructura repetitiva while  en python
#el programa  simulará  el despegue de un cohete

import time

contador=10
while contador>=0:
    time.sleep(.5)
    print(contador, end=" ", flush=True)
    contador-=1
print(f'El coehete se despega')
