#Actividad Integradora Paralelismo de Analizador Sintactico
#Por Harumi Manzano & Sebastian Mora
from SyntaxAnalizer import syntaxAnalize

import os
from distutils.dir_util import copy_tree


if __name__ == '__main__':
  print("Copying the original Input folder ...")
  copy_tree('./Input','./Output')
  path =r'./Output'
  list_of_files = []

  for root, dirs, files in os.walk(path):
    for file in files:
      list_of_files.append(os.path.join(root,file))
  print("Analyzing all files ...")
  for name in list_of_files:
    syntaxAnalize(name)
    os.remove(name)
  print("Read!")