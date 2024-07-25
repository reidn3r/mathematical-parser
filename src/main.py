from modules.lexer import Lexer
from modules.parser import Parser

def main():
    lexer = Lexer()
    parser = Parser()

    t = lexer.run("3*(2-(1/(3+2))*3)")
    # t = lexer.run("(4+3)*(5/(2+3)+6)") #Montando a árvore incorretamente
    print(t)
    parser.parse2tree(t)
    parser.print_tree()
    return;

if __name__ == "__main__":
    main()