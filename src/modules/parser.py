from utils.parser_tree import ParserTree

class Parser():
    def __init__(self):
        self.tree = ParserTree()

    def parse2tree(self, queue):
        root = self.tree.parse(queue)
        return root
    
    def print_tree(self):
        root = self.tree.root
        if root is not None:
            self.tree.in_order(root)