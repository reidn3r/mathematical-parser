from modules.lexer import Lexer
from modules.parser import Parser
from modules.eval_step import Evaluator
from utils.shunting_yard import ParserShuntingYard

def main():
    lexer = Lexer()
    parser = Parser()
    sy = ParserShuntingYard()

    # t = lexer.run("(10 / 3 + 23) * (1 - 4)")
    # t = lexer.run("4+18/(9-3)")
    t = lexer.run("(1 + 2 + 3) * 4") #rever a geração de árvore
    # t = lexer.run("31*(4+10)")
    print(t)

    # print(q)
    q = sy.parse(t)
    tree = parser.parse2tree(q)
    parser.print_tree()

    print("\n")

    evaluator = Evaluator(tree)
    evaluator.evalStep() 
    evaluator.evalStep() 
    evaluator.evalStep() 


    return

if __name__ == "__main__":
    main()