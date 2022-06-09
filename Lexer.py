import re #Libreria de expresiones regulares de python

class Lexer(object):
    def __init__(self, rules): #Constructor de la clase Lexer con las reglas
        idx = 1
        regex_parts = []
        self.group_type = {}

        for regex, type in rules:
            groupname = 'GROUP%s' % idx
            regex_parts.append('(?P<%s>%s)' % (groupname, regex))
            self.group_type[groupname] = type  #Juntamos todas la reglas en una sola ER
            idx += 1

        self.regex = re.compile('|'.join(regex_parts))
        self.re_ws_skip = re.compile('\S')

    def getToken(self):
        if self.pos >= len(self.buf):  #Verificiamos si no hemos llegado al final del input
            return None
        else:
            m = self.re_ws_skip.search(self.buf, self.pos) 

            if m:
              self.pos = m.start()     #Si encontramos un espacion, lo ignoramos
            else:
              return None

            m = self.regex.match(self.buf, self.pos)
            if m:
                groupname = m.lastgroup
                tok_type = self.group_type[groupname] #Cuando encontremos un token valido, checamos de que tipo es y lo regresamos
                tok = [m.group(groupname),tok_type]
                self.pos = m.end()
                return tok

    def tokenize(self,buf):
        self.buf = buf
        self.pos = 0
        out = []
        while 1:
            tok = self.getToken()  #Usamos la funcion getToken para todo el input (buf)
            if tok is None:
              break
            else:
              out.append(tok)
        return out


def createLexer():
  rules = [
    ('([0-9]*[.])+[0-9]+',         'float'),
    ('\d+',                        'int'),
    ('[a-zA-Z0-9_]+',                 'name'),
    ('\+',                         'add'),
    ('\-',                         'sub'),
    ('\*',                         'multi'),
    ('\^',                         'power'),
    ('\(',                         'open'),
    ('\)',                         'close'),
    ('=',                          'equal'),
    ('\/\/[^\n\r]+',               'comment'),
    ('\/',                         'divi'),
  ]

  l = Lexer(rules)
  return l


lexLuthor = createLexer()