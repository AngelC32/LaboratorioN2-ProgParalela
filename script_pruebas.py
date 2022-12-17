import subprocess
import csv
from time import sleep
from csv import DictWriter

dict= {}
num_of_process = 2
ss_delay = 1


headersCSV = ['Circulos_Python', 'Circulos_Cython','Circulos_Cython_Parallel']
with open('resultados.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headersCSV)
        writer.writeheader()

csvfile.close()


# Iteracion Circulos_Python
lista_Circulos_Python=[]
print("Obteniendo Tiempos de 'Circulos_Python' ")
for i in range(num_of_process):
    proceso = subprocess.run(['python3', 'Circulos_Python_Version/circulos.py'], 
                            capture_output=True, 
                            text=True)
    salto= proceso .stdout.find("\n")

    #guardar tiempos de ejecución
    tiempo= proceso .stdout[0:salto]
    lista_Circulos_Python.append(tiempo)
print('terminado, esperando captura')
sleep(ss_delay)


# Iteracion Circulos_Cython
lista_Circulos_Cython=[]
print("Obteniendo Tiempo de 'Circulos_Cython' ")
for i in range(num_of_process):
    proceso = subprocess.run(['python3', 'Circulos_Cython_Version/circulos_mod.py'], 
                            capture_output=True, 
                            text=True)
    salto= proceso .stdout.find("\n")

    #guardar tiempos de ejecución
    tiempo= proceso .stdout[0:salto]
    lista_Circulos_Cython.append(tiempo)
print('terminado, esperando captura')
sleep(ss_delay)


# Iteracion Circulos_Cython_Parallel
lista_Circulos_Cython_Parallel=[]
print("Obteniendo Tiempo de 'Circulos_Cython_Parallel' ")
for i in range(num_of_process):
    proceso = subprocess.run(['python3', 'Circulos_Cython_Parallel_Version/circulos_mod_parallel.py'], 
                            capture_output=True, 
                            text=True)
    salto= proceso .stdout.find("\n")

    #guardar tiempos de ejecución
    tiempo= proceso .stdout[0:salto]
    dict= {'Paralela':proceso}
    lista_Circulos_Cython_Parallel.append(tiempo)
print('terminado, esperando captura')
sleep(ss_delay)


print('Exportando datos')
for i in range (num_of_process):
        dict= {'Circulos_Python':lista_Circulos_Python[i],'Circulos_Cython':lista_Circulos_Cython[i],
                'Circulos_Cython_Parallel':lista_Circulos_Cython_Parallel[i]
        }       
         #guardar en el archivo resultados
        with open('resultados.csv', 'a', newline='') as f_object:
                dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
                dictwriter_object.writerow(dict)
        f_object.close()
print('Datos exportados')
 