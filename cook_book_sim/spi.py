from inspect import Signature, Parameter, signature

def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
            for name in names]
    return Signature(parms)

class Structure:
    __signature__ = make_sig()
    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Point(Structure):
    __signature__ = make_sig('x', 'y')

print(signature(Point))
p1 = Point(1, 7)
print(p1.x)

