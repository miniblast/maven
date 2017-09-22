from pyparsing import *
from sys import *

vars = {}
varn = ""
varv = ""

file = open(sys.argv[0] + ".mvn").read()

def prin(s,l,t):
  print(t)
  
def var1(s,l,t):
  varn = t
  
def var2(s,l,t):
  if varn == "":
    varv = ""
  else:
    varv = t
    vars[varn] = varv
    varv = ""
    varn = ""
    
def getvar(s,l,t):
  if vars[t]:
    return vars[t]
  else:
    print("Variable not found.")
  

num = Word(nums)
word = Word(alphas)
pri = Keyword("pri")
semi = Word(";",max=1)
equal = Word("=",max=1)
vars = Word("!",max=1)
va = Word("var")
string = Word("string")
number = Word("number")
as = Keyword(as)

# Start Parsing
pr = pri + " " + (word | num).SetParseAction() + semi                 # pri MyString; pri 100;
dvar = va + " " + word.SetParseAction(var1) + " " + as + (string | number) + equal + word.SetParseAction(var2) + semi
callv = vars + word.SetParseAction(getvar)

(pr).parseFile(file)
