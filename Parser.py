def V():
  if tokens[t] == 'name':
    match('name')
    match('equal')
    E()
    Vp()
  elif tokens[t] == 'comment':
    match('comment')
    Vp()
  else:
    raise Exception

def Vp():
  if t >= len(tokens):
    return
  else:
    if tokens[t] == 'comment':
      match('comment')
    else:
      return

def E():
  if tokens[t] == 'int':
    match('int')
    Ep()
  elif tokens[t] == 'float':
    match('float')
    Ep()
  elif tokens[t] == 'name':
    match('name')
    Ep()
  elif tokens[t] == 'open':
    match('open')
    E()
    match('close')
    Ep()
  else:
    raise Exception

def Ep():
  if t >= len(tokens):
    return
  else :
    if tokens[t] == 'operation':
      match('operation')
      E()
      Ep()
    else:
      return

def match(c):
    global t
    if tokens[t] == c:
        t += 1
    else:
        raise Exception

def parse(line):
  global tokens
  global t
  t = 0
  tokens = []
  try:
    tokens = line
    V()
    if t < len(tokens):
      raise Exception
    return True
    
  except Exception:
    return False