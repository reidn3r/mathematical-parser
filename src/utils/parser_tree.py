from utils.node import Node

class ParserTree:
    def __init__(self):
        self.root = None
        self.operator = ["+", "-", "*", "/"]
        self.tokens = []


    def build(self, tokens):
        self.tokens = tokens;
        if self.root is None:
            root_data = self.__find_first_operator__()
            if(root_data):
                self.root = Node(root_data)
                self.tokens.remove(root_data)
            else:
                print("raiz:operador nao encontrado")
                return

        root = self.root
        while(len(self.tokens) > 0):
            t = self.tokens[0]
            if(root.left is None):
                root.left = Node(t)
                self.tokens.remove(t)
                continue
            
            else:
                node_data = self.__find_first_operator__()
                if(node_data is not None):
                    root.right = Node(node_data)
                    self.tokens.remove(node_data)
                    root = root.right
                else:
                    root.right = Node(t)
                    self.tokens.remove(t)
        return self.root


    def in_order(self, root:Node):
        if root is not None:
            if root.left:
                self.in_order(root.left)

            print(root.data)
            
            if root.right:
                self.in_order(root.right)

    def __find_first_operator__(self):
        for t in self.tokens:
            if(t in self.operator):
                return t
