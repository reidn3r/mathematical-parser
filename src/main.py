from modules.lexer import Lexer
from modules.parser import Parser
from modules.eval_step import Evaluator
from utils.shunting_yard import ParserShuntingYard
from utils.read_io_file import file_stream

def main(path:str):

    lexer = Lexer()
    for t in file_stream(path):
        parser = Parser()
        sy = ParserShuntingYard()
        
        print(t)
        
        t = lexer.run(t)
        q = sy.parse(t)
        tree = parser.parse2tree(q)
        evaluator = Evaluator(tree)
        evaluator.evalTree(tree)

    return

if __name__ == "__main__":
    path:str = "../io/input.txt"
    main(path)