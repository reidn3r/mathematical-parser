from utils.node import Node

class ParserTree:
    def __init__(self):
        self.operator = ["+", "-", "*", "/"]
        self.root = None
        self.stack = []

    def parse(self, queue):
        self.__build__(self.root, queue)
        return self.root


    def __build__(self, root, queue):
        if not queue:
            return None
        
        for token in queue:
            if token not in self.operator:
                self.stack.append(Node(token))
            else:
                sub_tree = Node(token)
                sub_tree.right = self.stack.pop()
                sub_tree.left = self.stack.pop()
                self.stack.append(sub_tree)

        root, self.root = self.stack[0], self.stack[0]
        for subtree in self.stack[1:]:
            root.left = subtree
            root = subtree
        
        return self.root

    def in_order(self, root:Node):
        if root is not None:
            if root.left:
                self.in_order(root.left)

            print(root.data)
            
            if root.right:
                self.in_order(root.right)
