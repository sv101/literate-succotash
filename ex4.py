# Operator Overloading

class line_vector():
    def __init__(self, lv):
        self.lv = lv
        
    def __mul__(self, other):
        out = []
        for i in self.lv:
            out.append(i * other)        
        return line_vector(out)

# Method Overriding
    
    
    