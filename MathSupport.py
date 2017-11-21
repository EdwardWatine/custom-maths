import fractions, itertools
import simplify
class algebra:

    class expression:
    
        def __init__(self, expr):
        
            self.expr = simplify.simplify(expr)
            return self.expr
            
        def __add__(a, b):
        
            return algebra.add(a, b)
            
        def __radd__(b, a):
        
            return algebra.add(a, b)
            
        def __sub__(a, b):
        
            return algebra.add(a, -b)
            
        def __rsub__(b, a):
        
            return algebra.add(a, -b)
            
        def __mul__(a, b):
            
            return algebra.mul(a, b)

        def __rmul__(b, a):

            return algebra.mul(a, b)

        def __div__(a, b):

            return algebra.div(a, b)

        def __rdiv__(b, a):

            return algebra.div(a, b)

while True:
    exec(raw_input())