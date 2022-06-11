from Lexer import lexLuthor 
from Parser import parse
from WebInterface import createHtml

def readFile(path):  #Funcion que lee todos los caracteres de input.txt
  file = open(path,'r')
  data = [line.strip() for line in file]
  return data

  

 #Creacion de un objeto tipo Lexer con las reglas del lenguaje

def generateTokens(lex,dat):
  result = []
  for i in dat:
    if(i):
      tokens = []
      for j in lex.tokenize(i):
        tokens.append(j)
      result.append(tokens)
  return result

def prepareForParse(tokens):
  out = []
  operations = ['add','sub','multi','power','divi']
  for line in tokens:
    outLine = []
    for i in line:
      if i[1] in operations:
        outLine.append('operation')
      else:
        outLine.append(i[1])
    out.append(outLine)
  return out

def parseFile(tokens,prepare):
  out = []
  for i in range(len(tokens)):
    out.append([tokens[i],parse(prepare[i])])
  return out

def syntaxAnalize(inputPath):
  data = readFile(inputPath)
  tokens = generateTokens(lexLuthor,data)
  prepare = prepareForParse(tokens)
  finalOut = parseFile(tokens,prepare)
  createHtml(finalOut,inputPath[:-4])
  
