from flask import Flask, request, render_template

app = Flask(__name__)


# Esta función no es una ruta sino que la uso para calcular el facto
def calcular_factorial(n):
    # aqui valido si el numero es negativo
    if n < 0:
        return "Error: El factorial no esta definido para numeros negativos"
    # Caso base: 0! = 1
    elif n == 0:
        return 1
    # Calculo factorial para n > 0
    else:
        factorial = 1
        # Multiplicando desde 1 hasta n
        for i in range(1, n + 1):
            factorial *= i
        return factorial

# Aqui si estaran las utas de la aplicación 

# Ruta principal - Método GET
# Esta ruta muestra el formulario HTML inicial
@app.route('/', methods=['GET'])
def mostrar_formulario():
    return render_template('index.html')

@app.route('/factorial', methods=['POST'])
def procesar_factorial():
    numero_str = request.form.get('number')

    # Valido si se recibió un número en el post
    if not numero_str:
        # Si no hay número, mpongo un mensaje de error simple
        resultado_mensaje = "Error: No se recibió ningún número."
        return(resultado_mensaje)

    try:
        # Intentar convertir la entrada a un número entero por si las moscas
        numero_int = int(numero_str)

        # Calculo el factorial con la fucnios del inicio
        resultado_factorial = calcular_factorial(numero_int)
        return render_template('resultado_factorial.html', numero=numero_int, resultado=resultado_factorial)

    except ValueError:
        # Si la conversión falla (no es un número válido)
        resultado_mensaje = "Error: La entrada no es un numero entero válido."
        return render_template('resultado_factorial.html', numero=numero_str, resultado=resultado_mensaje)





if __name__ == '__main__':
    app.run(debug=True)