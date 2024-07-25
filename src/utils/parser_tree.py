from utils.node import Node

class ParserTree:
    def __init__(self):
        self.root = None
        self.operator = ["+", "-", "*", "/"]
        self.tokens = []

    def parse(self, tokens):
        self.tokens = tokens;
        self.__build__(self.root, tokens)
        return self.root


    def __build__(self, root, tokens):
        '''
            - Metodo recursivo que monta a árvore sintática
            - Se possível, diminuir o tamanho do método
            - Testar com mais expressões
        '''
        if not tokens:
            return None
        
        if self.root is None:
            '''
                1. Determina apenas a RAIZ da árvore
            '''
            root_data, op_index = self.__find_best_operator__(tokens)
            if(root_data):
                self.root = Node(root_data)
                left_idx = tokens[:op_index]
                right_idx = tokens[op_index+1:]

                self.root.left = self.__build__(self.root.left, left_idx)
                self.root.right = self.__build__(self.root.right, right_idx)

        if root is None:
            '''
                2. Repetição do if acima,
                !!FAZER FUNÇÃO QUE REAPROVEITA O CÓDIGO ANTERIOR!!
            '''
            root_data, op_index = self.__find_best_operator__(tokens)
            if(root_data):
                root = Node(root_data)
                left_idx = tokens[:op_index]
                right_idx = tokens[op_index+1:]

                root.left = self.__build__(root.left, left_idx)
                root.right = self.__build__(root.right, right_idx)
            else:
                root_data = self.__find_value__(tokens)
                if(root_data is not None):
                    root = Node(root_data)
                else:
                    print("Error")
                    return None

        return root

    def in_order(self, root:Node):
        if root is not None:
            if root.left:
                self.in_order(root.left)

            print(root.data)
            
            if root.right:
                self.in_order(root.right)


    def __find_best_operator__(self, tokens):
        parentesis_count = 0
        operator_index, min_precedence_op, min_precedence = -1, "", 3

        precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

        if(tokens[0] == "("):
            last_token_idx = len(tokens) - 1
            if(tokens[last_token_idx] == ")"):
                tokens.pop(0), tokens.pop()

        for idx, t in enumerate(tokens):
            if t == '(':
                parentesis_count += 1
            if t == ')':
                parentesis_count -= 1

            if parentesis_count == 0 and t in self.operator:
                if(precedence[t] < min_precedence):
                    min_precedence_op, min_precedence = t, precedence[t]
                    operator_index = idx
        
        if(parentesis_count != 0):
            raise ValueError("Syntax Error: ) or ( used incorrectly")

        return min_precedence_op, operator_index
    
    def __find_value__(self, tokens):
        for t in tokens:
            if t not in self.operator and t not in ["(", ")"]:
                return t



