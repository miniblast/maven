from pyparsing import *
from sys import *

funs = {}
vars1 = {}
varn = ""
varv = ""
funn = ""
funv = ""

file = open(sys.argv[0] + ".mvn").read()

def prin(s,l,t):
  print t[0][1:-1]
  
def var1(s,l,t):
  varn = t
  
def var2(s,l,t):
  if varn == "":
    varv = ""
  else:
    varv = varv+t
    vars1[varn] = varv
    varv = ""
    varn = ""
    
def getvar(s,l,t):
  if vars[t]:
    return vars[t]
  else:
    print("Variable not found.")
   
def funct1(s,l,t):
  funn = t
  
def funct2(s,l,t):
  if funn == "":
    funv = ""
  else:
    funv = t
    funs[funn] = funv
    funv = ""
    funn = ""
    
def getfunc(s,l,t):
  if func[t]:
    (pr | dvar | callv | function).parseString(file)
  else:
    print("Function not found.")

def imp(s,l,t):
  return open(t+".mvn","r")
  
num = ("\"" | "'") + Word(nums) + ("\"" | "'")
word = Word(alphas)
pri = Keyword("pri")
semi = Word(";",max=1)
equal = Word("=",max=1)
vars1 = Word("!",max=1)
fgroup = Word("|",max=1)
lpar = Word("(",max=1)
rpar = Word(")",max=1)
va = Word("var")
string = Word("string")
number = Word("number")
as1 = Keyword("as")
func = Keyword("func")
imp = Keyword("imp") 

# Start Parsing
pr = pri + (str1 | str2) + (word | num).SetParseAction() + (str1 | str2)                 # pri "MyString"; pri "100";
dvar = va + " " + word.SetParseAction(var1) + " " + as1 + (string | number) + equal + word.SetParseAction(var2) + semi
callv = vars + word.SetParseAction(getvar)
impor = imp + " " + word.SetParseAction(imp1)
function = func + " " + word.SetParseAction(funct1) + fgroup + OneOrMore(word).SetParseAction(funct) + fgroup

(pr | dvar | callv | function | impor).parseString(file)
