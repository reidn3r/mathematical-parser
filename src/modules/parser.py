from utils.parser_tree import ParserTree

class Parser():
    def __init__(self):
        self.parentesis = ["(", ")"]
        self.operator = ["+", "-", "*", "/"]
        self.tokens = []
        self.tree = ParserTree()

    def parse2tree(self, tokens):
        self.tokens = [t for t in tokens if t not in self.parentesis]
        root = self.tree.build(self.tokens)
        self.tree.in_order(root)