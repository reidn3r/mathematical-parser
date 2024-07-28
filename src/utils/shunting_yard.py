
class ParserShuntingYard:

    def __init__(self):
        self.operators = ["+", "-", "/", "*"]
        self.parentesis = ["(", ")"]

        self.queue = []
            #Primeiro da fila: primeiro elemento

        self.operator_stack = []
            #Topo da pilha: ultimo elemento (self.operator_stack[-1])

    def parse(self, tokens):
        self.__build__(tokens)
        return self.queue

    def __build__(self, tokens):
        precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

        for token in tokens:
            if token not in self.operators and token not in self.parentesis:
                self.queue.append(token)
            
            elif token in self.operators:
                while (len(self.operator_stack) > 0 and 
                        self.operator_stack[-1] != "(" and 
                        precedence[self.operator_stack[-1]] >= precedence[token]):
                    top_operator = self.operator_stack.pop()
                    self.queue.append(top_operator)
                self.operator_stack.append(token)

            elif token == "(":
                self.operator_stack.append(token)
            
            elif token == ")":
                while len(self.operator_stack) > 0 and self.operator_stack[-1] != "(":
                    top_operator = self.operator_stack.pop()
                    self.queue.append(top_operator)
                self.operator_stack.pop() 
        
        while(len(self.operator_stack) > 0):
            top_operator = self.operator_stack.pop()
            self.queue.append(top_operator)
