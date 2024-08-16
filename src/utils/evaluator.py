from modules.lexer import Lexer
from modules.parser import Parser
from modules.eval_step import EvalStep
from modules.to_string import ToString
from utils.shunting_yard import ParserShuntingYard
from utils.read_io_file import file_stream

import re

class Evaluator:
    def __init__(self, path:str):
        self.path = path

    def execute(self):
        lexer = Lexer()
        for i, t in enumerate(file_stream(self.path)):
            t = t[:-1] if t[-1] == '\n' else t # Tira o breakLine (\n) do final da linha lida do arquivo

            if not is_valid_expression(t):
                print(f'> {t}\t[Expressão inválida] ')
                continue

            tokens = lexer.run(t)

            sy, parser, tostr = ParserShuntingYard(), Parser(), ToString()
            
            queue = sy.parse(tokens)
            tree = parser.parse2tree(queue)
            evaluator = EvalStep(tree)

            print(f"> {(tostr.to_expression(tree))}")
            while(not isinstance(tree.data, int)):
                evaluator.evalStep()
                print(f"{(tostr.to_expression(tree))}")

def is_valid_expression(expr):
    # Remove espaços em branco
    expr = expr.replace(" ", "")
    
    # Define padrões para detecção de erros comuns
    invalid_patterns = [
        r'[^0-9+\-*/() ]',   # Caracteres inválidos (como @)
        r'[+\-*/]{3}',
        r'[+\-*/]{2,}$',     # Operadores no final da expressão
        r'^[+\-*/]{2,}',     # Operadores no início da expressão
        r'\(\)',             # Parênteses vazios (ex: ())
        #r'\)[^\-*/)]',       # Parênteses fechados seguidos por número ou '(' sem operador (ex: )55)
        #r'\([^\-*/(]',       # Parênteses abertos seguidos por número ou ')' sem operador (ex: (55)
        #r'[+\-*/]\)',        # Operador seguido de parêntese fechando
        #r'\([+\-*/]',        # Parêntese abrindo seguido de operador
    ]
    
    
    for pattern in invalid_patterns:
        if re.search(pattern, expr):
            return False
    
    
    # Verifica se os parênteses estão balanceados
    balance = 0
    for char in expr:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:
            return False
    if balance != 0:
        return False

    return True
