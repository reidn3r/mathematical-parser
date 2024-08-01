from modules.lexer import Lexer
from modules.parser import Parser
from modules.eval_step import EvalStep
from modules.to_string import ToString
from utils.shunting_yard import ParserShuntingYard
from utils.read_io_file import file_stream

class Evaluator:
    def __init__(self, path:str):
        self.path = path

    def execute(self):
        lexer = Lexer()
        for i, t in enumerate(file_stream(self.path)):
            t = t[:-1] if t[-1] == '\n' else t # Tira o breakLine (\n) do final da linha lida do arquivo
            tokens = lexer.run(t)

            sy, parser, tostr = ParserShuntingYard(), Parser(), ToString()
            
            queue = sy.parse(tokens)
            tree = parser.parse2tree(queue)
            evaluator = EvalStep(tree)

            print(f"> {(tostr.to_expression(tree))}")
            while(not isinstance(tree.data, int)):
                evaluator.evalStep()
                print(f"{(tostr.to_expression(tree))}")