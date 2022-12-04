# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask (__name__)

@app.route('/add')
def add_func():
    """Add a and b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a,b)
    return str(result)

@app.route('/sub')
def sub_func():
    """Substract b from a."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a,b)
    return str(result)  

@app.route('/mult')
def mult_func():
    """Multiply a and b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a,b)
    return str(result) 

@app.route('/div')
def div_func():
    """Divide a by b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a,b)
    return str(result)


# BONUS
funcs = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}
@app.route('/math/<funcs>')
def math_func(operator):
    """Function with 4 operations"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = funcs[operator](a,b)
    return str(result)