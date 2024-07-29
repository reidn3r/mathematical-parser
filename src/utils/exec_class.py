from modules.lexer import Lexer
from modules.parser import Parser
from modules.eval_step import Evaluator
from modules.to_string import ToString
from utils.shunting_yard import ParserShuntingYard
from utils.read_io_file import file_stream

class execution:
    def __init__(self, path:str):
        self.path = path

    def exec(self):
        lexer = Lexer()
        for i, t in enumerate(file_stream(self.path)):
            t = t[:-1] if t[-1] == '\n' else t # Tira o breakLine (\n) do final da linha lida do arquivo

            l = lexer.run(t)

            sy = ParserShuntingYard()
            q = sy.parse(l)

            parser = Parser()
            tree = parser.parse2tree(q)

            tostr = ToString()

            evaluator = Evaluator(tree)

            print(f"> {(tostr.to_expression(tree))}")

            while(not isinstance(tree.data, int)):
                evaluator.evalStep()
                print(f"{(tostr.to_expression(tree))}")