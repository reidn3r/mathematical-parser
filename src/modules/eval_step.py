from utils.parser_tree import ParserTree
from utils.node import Node

class EvalStep:
    def __init__(self, root_node: Node):
        self.root = root_node

    def evalStep(self):
        if not isinstance(self.root.data, int):
            self.__lowerOperationNode__(self.root)
        else:
            print(self.root.data) # se a árvore só tem um nó (raiz), printa o conteúdo desse nó


    def __lowerOperationNode__(self, root:Node):
        
        # desce in-order para a direita até achar o nó folha mais baixo
        # se achar um nó folha descendo para direita e ainda tem operadores no nó da esquerda
        # vai para a esquerda e desce in-order dnv
        if isinstance(root.right.data, str):
            self.__lowerOperationNode__(root.right)
        elif isinstance(root.left.data, str):
            self.__lowerOperationNode__(root.left)
        else:
            # atualiza o nó
            result = self.__valueOperate__(root.left.data, root.right.data, root.data)
            root.data = result
            root.left = None
            root.right = None
            # print(root.data) # printando para ver se deu o resultado esperado
            return

    def __valueOperate__(self, left, right, op):
       operations = {
          '+':lambda x, y: x + y,
          '-':lambda x, y: x - y,
          '/':lambda x, y: x / y,
          '*':lambda x, y: x * y
       }
       
       return int(operations[op](left, right))


    # função para verificar o valor final da expressão da árvore
    # decidi não fazer privada para testarmos depois o valor final das árvores que montarmos
    def evalTree(self, root_node:ParserTree):
        
        if isinstance(root_node.data, int):
            return root_node.data
        
        if isinstance(root_node.data, str): # str = op
           right_operator = self.evalTree(root_node.right)
           operation = root_node.data
           left_operator = self.evalTree(root_node.left)

           print(f"left: {left_operator}, right: {right_operator}, operation: {operation}", end=' ')
           print(f'-> {self.__valueOperate__(left_operator, right_operator, operation)}')

           return self.__valueOperate__(left_operator, right_operator, operation)
           