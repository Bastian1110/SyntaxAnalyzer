def createHtml(data,outname):
  begin = ["<!DOCTYPE html>",
           " <html>",
           "    <head>",
           "      <title>Actividad integradora</title>",
           '      <link rel="stylesheet" href="style.css">',
           "    </head>",
           "    <body>"
          ]
  end =   ["    </body>", "</html>"]
  for i in data:
    line = '<p' 
    if i[1]:
      line = line + '>'
      for t in i[0]:
        line = line + ' <i class="' + t[1] + '"> ' + t[0] + ' </i> ' 
    else:
      line = line + ' class="wrong">'
      for t in i[0]:
        line = line + t[0] 
    line = line + "</p>"
    begin = begin + ["    " + line]
    
  html = begin + end
  htmlFile = open(outname + ".html","w")
  for i in html:
    htmlFile.write(i + '\n')
  htmlFile.close()