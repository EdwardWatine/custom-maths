import itertools, re
import mathSupport

class mymath(Exception):
    pass
class parsingError(mymath):
    pass
class syntaxError(mymath):
    pass
    
def simplify(expr):
    
    symbols = ["(", ")", "^", "/", "*", "+", "-"]
    expr = re.sub(r"[^()^/*+\-a-z0-9]", "", expr)
    expr = re.sub(r"(?<![0-9])
    openB = [x.start() for x in re.finditer(r"\(", expr)]
    closeB = [x.start() for x in re.finditer(r"\)", expr)]
    if len(openB) != len(closeB) or openB[0] > closeB[0] or openB[-1] > closeB[-1]:
        raise parsingError("Bracket error!")
    
    x = 0
    braks = []
    while openB:
        cpos, opos = closeB[0], openB[x]
        if (x != len(openB)-1 and cpos < openB[x+1]) or x == len(openB)-1:
            braks.append(collect
        openB = [x.start() for x in re.finditer(r"\(", expr)]
        closeB = [x.start() for x in re.finditer(r"\)", expr)]
        x += 1    
                
                
    
   
simplify("")        