from modules.lexer import Lexer
from modules.parser import Parser
from modules.eval_step import Evaluator
from modules.to_string import ToString
from utils.shunting_yard import ParserShuntingYard
from utils.read_io_file import file_stream

def main(path:str):

    lexer = Lexer()
    for i, t in enumerate(file_stream(path)):
        t = t[:-1] if t[-1] == '\n' else t # Tira o breakLine (\n) do final da linha lida do arquivo

        print('-='*10)
        print(f'linha {i} do arquivo:\t{t}')

        l = lexer.run(t)
        print(f'Tokens identificados:\t{l}')

        sy = ParserShuntingYard()
        q = sy.parse(l)

        parser = Parser()
        tree = parser.parse2tree(q)
        print('Árvore in ordem:\t', end='')
        parser.print_tree()

        tostr = ToString()
        print(f'Árvore para string:\t{tostr.to_expression(tree)}')

        evaluator = Evaluator(tree)
        evaluator.evalTree(tree)

    return

if __name__ == "__main__":
    path:str = "io/input.txt"
    main(path)