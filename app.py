from flask import Flask, request, render_template
import ctypes
from profiler import profile  

app = Flask(__name__)
lib = ctypes.CDLL('./libcalculator.so')

# restype and argtypes for c functions, for my reference:
# https://docs.python.org/3/library/ctypes.html#ctypes-fundamental-data-types-2
lib.divide.restype = ctypes.c_float
lib.power.restype = ctypes.c_double
lib.power.argtypes = [ctypes.c_double, ctypes.c_double]  # argument types
lib.square_root.restype = ctypes.c_double
lib.square_root.argtypes = [ctypes.c_double]
lib.factorial.restype = ctypes.c_int
lib.factorial.argtypes = [ctypes.c_int]
lib.is_prime.restype = ctypes.c_int
lib.is_prime.argtypes = [ctypes.c_int]

@app.route('/', methods=['GET', 'POST'])
@profile  
def index():
    result = ""
    a = 0
    b = 0
    operation = 'add'

    if request.method == 'POST':
        operation = request.form['operation']
        a = float(request.form['a'])
        b = float(request.form['b']) if 'b' in request.form else None

        if operation == 'add':
            result = lib.add(int(a), int(b))
        elif operation == 'subtract':
            result = lib.subtract(int(a), int(b))
        elif operation == 'multiply':
            result = lib.multiply(int(a), int(b))
        elif operation == 'divide':
            if b != 0:
                result = lib.divide(ctypes.c_float(a), ctypes.c_float(b))
            else:
                result = 'Error: Division by zero'
        elif operation == 'power':
            result = lib.power(ctypes.c_double(a), ctypes.c_double(b))  
        elif operation == 'square_root':
            if a >= 0:
                result = lib.square_root(ctypes.c_double(a)) 
            else:
                result = 'Error: Negative number for square root'
        elif operation == 'factorial':
            if a >= 0 and a == int(a):
                result = lib.factorial(ctypes.c_int(int(a))) 
            else:
                result = 'Error: Non-integer or negative number for factorial'
        elif operation == 'is_prime':
            if a == int(a):
                result = 'Yes' if lib.is_prime(ctypes.c_int(int(a))) else 'No'  
            else:
                result = 'Error: Non-integer for prime check'
        else:
            result = 'Invalid operation'

    return render_template('index.html', result=result, a=a, b=b, operation=operation)

if __name__ == "__main__":
    app.run(debug=True)
