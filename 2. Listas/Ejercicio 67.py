expresion_postfija = ["3", "4", "+", "2", "*", "1", "-"]
pila_evaluacion = []
for token in expresion_postfija:
    if token.isdigit():
        pila_evaluacion.append(int(token))
    else:
        # Usando pop() para sacar del final (comportamiento de pila)
        operando2 = pila_evaluacion.pop()
        operando1 = pila_evaluacion.pop()
        if token == "+":
            resultado = operando1 + operando2
        elif token == "-":
            resultado = operando1 - operando2
        elif token == "*":
            resultado = operando1 * operando2
        elif token == "/":
            resultado = operando1 / operando2
        pila_evaluacion.append(resultado)
print(f"Resultado de la expresión postfija ({' '.join(expresion_postfija)}): {pila_evaluacion[0]}")