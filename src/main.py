from modules.lexer import Lexer
from modules.parser import Parser
from modules.eval_step import Evaluator

def main():
    lexer = Lexer()
    parser = Parser()

    t = lexer.run("(10 / 3 + 23) * (1 - 4)")
    # t = lexer.run("(1 + 2 + 3) * 4") rever a geração de árvore
    print(t)
    tree = parser.parse2tree(t)
    parser.print_tree()

    evaluator = Evaluator(tree)
    evaluator.evalStep() 
    evaluator.evalStep() 
    evaluator.evalStep()
    evaluator.evalStep()


    return

if __name__ == "__main__":
    main()