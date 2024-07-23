from sympy import symbols, diff, solve, simplify

def resolver_equacao(equacao):
    x = symbols('x')
    solucao = solve(equacao, x)
    return solucao

def calcular_derivada(expressao, x):
    derivada = diff(expressao, x)
    return derivada

def main():
    x = symbols('x')

    equacao = x**2 - 4
    expressao = x**2 - 4*x + 4

    solucao = resolver_equacao(equacao)
    print(f"Soluçao da equaçao {equacao}: {solucao}")

    derivada = calcular_derivada(expressao, x)
    print(f"Derivada de {expressao}: {derivada}")
    
    expressao_simplificada = simplify(expressao)
    print(f"Expressao Simplificada de {expressao}: {expressao_simplificada}")

if __name__ == "__main__":
    main()


