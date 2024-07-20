from modules.lexer import Lexer
from modules.parser import Parser

def main():
    lexer = Lexer()
    parser = Parser()

    t = lexer.run("31 * (4  + 10)")
    parser.parse2tree(t)
    return;

if __name__ == "__main__":
    main()