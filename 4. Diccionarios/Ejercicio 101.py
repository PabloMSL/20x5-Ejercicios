def accion_sumar(a, b): return a + b
def accion_restar(a, b): return a - b
def accion_multiplicar(a, b): return a * b

operaciones = {
    '+': accion_sumar,
    '-': accion_restar,
    '*': accion_multiplicar
}
operador = '+'
num1 = 10
num2 = 5
if operador in operaciones:
    resultado = operaciones[operador](num1, num2)
    print(f"\nSimulación de switch/case: {num1} {operador} {num2} = {resultado}")
else:
    print(f"\nOperador '{operador}' no válido.")