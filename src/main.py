from modules.lexer import Lexer
from modules.parser import Parser

def main():
    lexer = Lexer()
    parser = Parser()

    t = lexer.run("1 + 3 * 4 + 1")
    print(t)
    parser.parse2tree(t)
    parser.print_tree()

    print("\n\n")

    t = lexer.run("1 + 3 * (4 + 1)")
    print(t)
    parser.parse2tree(t)
    parser.print_tree()
    return;

if __name__ == "__main__":
    main()