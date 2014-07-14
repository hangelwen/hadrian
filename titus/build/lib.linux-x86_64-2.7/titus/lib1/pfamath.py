#!/usr/bin/env python

import math

from titus.fcn import Fcn
from titus.fcn import LibFcn
from titus.signature import Sig
from titus.signature import Sigs
from titus.datatype import *
from titus.errors import *
from titus.lib1.core import checkForOverflow
import titus.P as P

provides = {}
def provide(fcn):
    provides[fcn.name] = fcn

prefix = "m."

#################################################################### constants (0-arity side-effect free functions)

class Pi(LibFcn):
    name = prefix + "pi"
    sig = Sig([], P.Double())
    def genpy(self, paramTypes, args):
        return "math.pi"
    def __call__(self, state, scope, paramTypes):
        return math.pi
provide(Pi())

class E(LibFcn):
    name = prefix + "e"
    sig = Sig([], P.Double())
    def genpy(self, paramTypes, args):
        return "math.e"
    def __call__(self, state, scope, paramTypes):
        return math.e
provide(E())

#################################################################### functions (alphabetical order)

anyNumber = set([AvroInt(), AvroLong(), AvroFloat(), AvroDouble()])

class Abs(LibFcn):
    name = prefix + "abs"
    sig = Sig([{"x": P.Wildcard("A", anyNumber)}], P.Wildcard("A"))
    def __call__(self, state, scope, paramTypes, x):
        return checkForOverflow(paramTypes, abs(x))
provide(Abs())

class ACos(LibFcn):
    name = prefix + "acos"
    sig = Sig([{"x": P.Double()}], P.Double())
    def __call__(self, state, scope, paramTypes, x):
        try:
            return math.acos(x)
        except ValueError:
            return float("nan")
provide(ACos())

class ASin(LibFcn):
    name = prefix + "asin"
    sig = Sig([{"x": P.Double()}], P.Double())
    def __call__(self, state, scope, paramTypes, x):
        try:
            return math.asin(x)
        except ValueError:
            return float("nan")
provide(ASin())

class ATan(LibFcn):
    name = prefix + "atan"
    sig = Sig([{"x": P.Double()}], P.Double())
    def genpy(self, paramTypes, args):
        return "math.atan({})".format(*args)
    def __call__(self, state, scope, paramTypes, x):
        return math.atan(x)
provide(ATan())

class ATan2(LibFcn):
    name = prefix + "atan2"
    sig = Sig([{"y": P.Double()}, {"x": P.Double()}], P.Double())
    def genpy(self, paramTypes, args):
        return "math.atan2({}, {})".format(*args)
    def __call__(self, state, scope, paramTypes, x, y):
        return math.atan2(x, y)
provide(ATan2())

class Ceil(LibFcn):
    name = prefix + "ceil"
    sig = Sig([{"x": P.Double()}], P.Double())
    def genpy(self, paramTypes, args):
        return "math.ceil({})".format(*args)
    def __call__(self, state, scope, paramTypes, x):
        return math.ceil(x)
provide(Ceil())

class CopySign(LibFcn):
    name = prefix + "copysign"
    sig = Sig([{"mag": P.Wildcard("A", anyNumber)}, {"sign": P.Wildcard("A")}], P.Wildcard("A"))
    def __call__(self, state, scope, paramTypes, mag, sign):
        return abs(mag) * (-1 if sign < 0 else 1)
provide(CopySign())

class Cos(LibFcn):
    name = prefix + "cos"
    sig = Sig([{"x": P.Double()}], P.Double())
    def genpy(self, paramTypes, args):
        return "math.cos({})".format(*args)
    def __call__(self, state, scope, paramTypes, x):
        return math.cos(x)
provide(Cos())

class CosH(LibFcn):
    name = prefix + "cosh"
    sig = Sig([{"x": P.Double()}], P.Double())
    def genpy(self, paramTypes, args):
        return "math.cosh({})".format(*args)
    def __call__(self, state, scope, paramTypes, x):
        return math.cosh(x)
provide(CosH())

class Exp(LibFcn):
    name = prefix + "exp"
    sig = Sig([{"x": P.Double()}], P.Double())
    def genpy(self, paramTypes, args):
        return "math.exp({})".format(*args)
    def __call__(self, state, scope, paramTypes, x):
        return math.exp(x)
provide(Exp())

class ExpM1(LibFcn):
    name = prefix + "expm1"
    sig = Sig([{"x": P.Double()}], P.Double())
    def genpy(self, paramTypes, args):
        return "(math.exp({}) - 1.0)".format(*args)
    def __call__(self, state, scope, paramTypes, x):
        return math.exp(x) - 1.0
provide(ExpM1())

class Floor(LibFcn):
    name = prefix + "floor"
    sig = Sig([{"x": P.Double()}], P.Double())
    def genpy(self, paramTypes, args):
        return "math.floor({})".format(*args)
    def __call__(self, state, scope, paramTypes, x):
        return math.floor(x)
provide(Floor())

class Hypot(LibFcn):
    name = prefix + "hypot"
    sig = Sig([{"x": P.Double()}, {"y": P.Double()}], P.Double())
    def __call__(self, state, scope, paramTypes, x, y):
        return math.sqrt(x**2 + y**2)
provide(Hypot())

class Ln(LibFcn):
    name = prefix + "ln"
    sig = Sig([{"x": P.Double()}], P.Double())
    def __call__(self, state, scope, paramTypes, x):
        if x < 0.0:
            return float("nan")
        elif x == 0.0:
            return float("-inf")
        else:
            return math.log(x)
provide(Ln())

class Log10(LibFcn):
    name = prefix + "log10"
    sig = Sig([{"x": P.Double()}], P.Double())
    def __call__(self, state, scope, paramTypes, x):
        if x < 0.0:
            return float("nan")
        elif x == 0.0:
            return float("-inf")
        else:
            return math.log10(x)
provide(Log10())

class Log(LibFcn):
    name = prefix + "log"
    sig = Sig([{"x": P.Double()}, {"base": P.Int()}], P.Double())
    def __call__(self, state, scope, paramTypes, x, base):
        if base <= 0:
            raise PFARuntimeException("base must be positive")
        if x < 0.0:
            return float("nan")
        elif x == 0.0:
            return float("-inf")
        else:
            return math.log(x, base)
provide(Log())

class Ln1p(LibFcn):
    name = prefix + "ln1p"
    sig = Sig([{"x": P.Double()}], P.Double())
    def __call__(self, state, scope, paramTypes, x):
        if x < -1.0:
            return float("nan")
        elif x == -1.0:
            return float("-inf")
        else:
            return math.log(1 + x)
provide(Ln1p())

class Round(LibFcn):
    name = prefix + "round"
    sig = Sigs([Sig([{"x": P.Float()}], P.Int()),
                Sig([{"x": P.Double()}], P.Long())])
    def __call__(self, state, scope, paramTypes, x):
        return checkForOverflow(["long"], long(math.floor(x + 0.5)))
provide(Round())

class RInt(LibFcn):
    name = prefix + "rint"
    sig = Sig([{"x": P.Double()}], P.Double())
    def __call__(self, state, scope, paramTypes, x):
        up, down = math.ceil(x), math.floor(x)
        if up - x < x - down:
            return up
        elif up - x > x - down:
            return down
        elif int(up) % 2 == 0:
            return up
        else:
            return down
            
provide(RInt())

class Signum(LibFcn):
    name = prefix + "signum"
    sig = Sig([{"x": P.Double()}], P.Int())
    def __call__(self, state, scope, paramTypes, x):
        if x == 0:
            return 0
        elif x > 1:
            return 1
        else:
            return -1
provide(Signum())

class Sin(LibFcn):
    name = prefix + "sin"
    sig = Sig([{"x": P.Double()}], P.Double())
    def genpy(self, paramTypes, args):
        return "math.sin({})".format(*args)
    def __call__(self, state, scope, paramTypes, x):
        return math.sin(x)
provide(Sin())

class SinH(LibFcn):
    name = prefix + "sinh"
    sig = Sig([{"x": P.Double()}], P.Double())
    def genpy(self, paramTypes, args):
        return "math.sinh({})".format(*args)
    def __call__(self, state, scope, paramTypes, x):
        return math.sinh(x)
provide(SinH())

class Sqrt(LibFcn):
    name = prefix + "sqrt"
    sig = Sig([{"x": P.Double()}], P.Double())
    def __call__(self, state, scope, paramTypes, x):
        try:
            return math.sqrt(x)
        except ValueError:
            return float("nan")
provide(Sqrt())

class Tan(LibFcn):
    name = prefix + "tan"
    sig = Sig([{"x": P.Double()}], P.Double())
    def genpy(self, paramTypes, args):
        return "math.tan({})".format(*args)
    def __call__(self, state, scope, paramTypes, x):
        return math.tan(x)
provide(Tan())

class TanH(LibFcn):
    name = prefix + "tanh"
    sig = Sig([{"x": P.Double()}], P.Double())
    def genpy(self, paramTypes, args):
        return "math.tanh({})".format(*args)
    def __call__(self, state, scope, paramTypes, x):
        return math.tanh(x)
provide(TanH())