def calculadora(operacao):
    def soma(a, b):
        return a + b
    
    def sub(a, b):
        return a - b

    def div(a, b):
        return a / b

    def mul(a, b):
        return a * b
        
    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "/":
            return div
        case "*":
            return mul
        
op = calculadora("+")
print(op(2,2))
calculadora("-")(3,1)
print(calculadora("*")(5,5))
