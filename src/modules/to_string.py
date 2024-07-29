from utils.node import Node

class ToString:
    def __init__(self):
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

    def to_expression(self, root: Node, parentesis=False) -> str:
        if root is None:
            return ""
        
        # Se o nó é uma folha, retorna o valor do nó
        if root.left is None and root.right is None:
            return str(root.data)

        if not isinstance(root.left.data, int) and self.precedence[root.left.data] < self.precedence[root.data]:
            left_expr = self.to_expression(root.left, parentesis=True)
        else:
            left_expr = self.to_expression(root.left)

        if not isinstance(root.right.data, int) and self.precedence[root.right.data] < self.precedence[root.data]:
            right_expr = self.to_expression(root.right, parentesis=True)
        else:
            right_expr = self.to_expression(root.right)
        
        # Retornar expressão com parênteses para preservar precedência
        return f"({left_expr} {root.data} {right_expr})" if parentesis else f"{left_expr} {root.data} {right_expr}"