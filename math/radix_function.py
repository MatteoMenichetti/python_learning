import math
from symbol import return_stmt

def bisection(f, a, b, tol):
    """ bisection(f, a, b, tol)

    Parameters
    __________
    - f, function (lambda or function, eg (lambda x: x**2))
    - a, b, interval
    - tol, tolerance

    Returns
    _________
    - x, zero of f
    """

    #tbd: controllare condizioni < 0

    if a - b == 0 or a > b: print('intervallo non valido', a, b); return 'None'

    if tol<= 0: print('tolleranza', tol, 'non valida'); return 'None';

    n = math.ceil(math.log2(abs(b-a)) - math.log2(tol))

    fa = f(a); fb = f(b)

    for i in range(n):
        x = (a + b) / 2

        fx = f(x)

        if b-a == 0: print('b-a == 0', a, b); return 'None'

        f1x = abs((fa - fb) / (b - a))

        if fx == 0:
            return [x,n]

        if f1x == 0: print('metodo non convergente'); return 'None'

        if abs(fx) <= f1x * tol: return [x,i]

        if fa * fx < 0: b = x; fb = fx

        elif fb * fx < 0: a = x; fa = fx

        if abs(fx) > f1x * tol: print('metodo non convergente'); return 'None'
    return [x,n]

def newton(f, f1, x, tol = 1e-15, itmax = 1000):
    """ newton(f, a, b, tol, itmax)

    Parameters
    __________
    - f, function (lambda or function, eg (lambda x: x**2))
    - f1, derivate of f
    - x, starting point
    - tol, tolerance (default 1e-15)
    - itmax, max number of iterations (default=1000)
    """

    if tol <= 0: print('tolleranza', tol, 'non valida'); return None;

    if itmax <= 0: print('itmax', itmax, 'non valida'); return None;

    for i in range(itmax):

        f1x = f1(x)

        if f1x == 0: print('f1x == 0'); return None

        x1 = x - f(x)/f1x

        if abs(x1-x) <= tol: return [x,i]

        x = x1
    if abs(x1-x) > tol: print('metodo non convergente'); return None
    return [x, itmax]

def aitken(f, f1, x, tol = 1e-15, itmax = 1000):
    """ aitken(f, f1, x, tol, itmax)

        Parameters
        __________
        - f, function (lambda or function, eg (lambda x: x**2))
        - f1, derivate of f
        - x, starting point
        - tol, tolerance (default 1e-15)
        - itmax, max number of iterations (default=1000)
    """

    if tol <= 0: print('tolleranza', tol, 'non valida'); return None;

    if itmax <= 0: print('itmax', itmax, 'non valida'); return None

    for i in range(itmax):

        fx = f(x); f1x = f1(x)

        if abs(fx) <= abs(f1x) * tol: return [x, i]

        if f1x == 0: print('metodo non covergente'); return ''

        x1 = x - fx/f1x #x_i

        fx = f(x); f1x = f1(x)

        if f1x == 0: print('metodo non covergente'); return ''

        x2 = x - fx/f1x #x_i+1

        x = (x * x2 - x1**2)/(x + x2 -2*x1)

    if abs(fx) > abs(f1x) * tol: print('metodo non covergente'); return ''

    return [x, itmax]