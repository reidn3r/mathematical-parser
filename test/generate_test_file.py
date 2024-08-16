import random
import re

def generate_number():
    """Gera um número aleatório como string."""
    return str(random.randint(1, 100))

def generate_operator():
    """Gera um operador aleatório."""
    return random.choice(['+', '-', '*'])

def generate_expression(depth=0):
    """Gera uma expressão matemática válida com profundidade variável."""
    if depth > 3 or random.choice([True, False]):
        # Cria uma expressão simples
        expr = f"{generate_number()} {generate_operator()} {generate_number()}"
    else:
        # Cria uma expressão mais complexa com parênteses
        expr = f"({generate_expression(depth + 1)}) {generate_operator()} ({generate_expression(depth + 1)})"
    
    return expr

def generate_valid_expressions(num_expressions):
    """Gera um número especificado de expressões válidas e longas."""
    expressions = []
    for _ in range(num_expressions):
        expr_length = random.randint(10, 100)  # Comprimento da expressão
        expr = generate_expression().replace(' ', '')  # Remove espaços para aumentar o comprimento
        while len(expr) < expr_length:
            expr = generate_expression().replace(' ', '')
        expressions.append(expr)
    
    return expressions

def save_expressions_to_file(expressions, filename):
    """Salva as expressões geradas em um arquivo .txt."""
    with open(filename, 'w') as file:
        for expr in expressions:
            file.write(expr + '\n')

# Gerar e salvar expressões
num_expressions = 100000
expressions = generate_valid_expressions(num_expressions)
save_expressions_to_file(expressions, 'valid_expressions.txt')

print(f"{num_expressions} expressões válidas foram salvas em 'valid_expressions.txt'.")
