#Actividad Integradora Paralelismo de Analizador Sintactico
#Por Harumi Manzano & Sebastian Mora
from SyntaxAnalizer import syntaxAnalize

import os
import sys
import time
import multiprocessing
from distutils.dir_util import copy_tree

def chunker(lista, chunks):
    return list((lista[i::chunks] for i in range(chunks)))

def secuencial(archivos):
  for name in archivos:
    syntaxAnalize(name)
    os.remove(name)


def paralela(archivos,cores):
  pool = multiprocessing.Pool()
  pool = multiprocessing.Pool(processes=cores)
  inputs = chunker(archivos,cores)
  pool.map(secuencial,inputs)
  




if __name__ == '__main__':
  print(" * Actividad Integradora Final * ")
  print("Creando la carpeta de Output ...")
  copy_tree('./Input','./Output')
  print("Listo !!!")

  path =r'./Output'
  archivos = []
  for root, dirs, files in os.walk(path):
    for file in files:
      if file.endswith('.txt'):
        archivos.append(os.path.join(root,file))

  print("- Prueba Secuencial ----------")
  start = time.time()
  secuencial(archivos)
  end = time.time()
  print("Tiempo aproximado de ejecucion secuencial: ", end-start)

  print("- Prueba Paralela -----------")
  start = time.time()
  paralela(archivos,2)
  end = time.time()
  print("Tiempo aproximado de ejecucion paralela: ", end-start)