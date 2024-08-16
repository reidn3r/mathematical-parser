class Lexer:
    def __init__(self):
        pass

    def run(self, string) -> 'list[str]':
        # Método público que chama o método privado __string2tokens__ para analisar a string e retornar uma lista de tokens
        return self.__string2tokens__(string)

    def __string2tokens__(self, string: str) -> 'list[str]':
        # Método privado que realiza a análise léxica da string fornecida
        tokens = []
        current_position = 0

        while current_position < len(string):
            current_char = string[current_position]

            if current_char.isspace():
                # Ignora espaços em branco e avança para o próximo caractere
                current_position += 1
                continue

            # Um número inteiro pode ser positivo ou negativo
            # Para se reconhecer um número negativo, primeiro verifica-se se o caracter atual é '-'
            # Se for o caso, temos duas possibilidades de ser um número negativo: ser o começo da expressão ou o token anterior ser '+-*/('
            # Para o segundo caso, verifica-se se existem tokens, se o último adicionado foi uma string, e se pertence a '+-*/(' respectivamente
            elif current_char.isdigit() or (current_char == '-' and (
                    current_position == 0 or
                    (tokens and isinstance(tokens[-1], str) and tokens[-1] in '+-*/('))):
                # Reconhece números inteiros e números negativos
                start_position = current_position
                if current_char == '-':
                    current_position += 1

                while current_position < len(string) and string[current_position].isdigit():
                    current_position += 1

                tokens.append(int(string[start_position:current_position]))

            elif current_char in '+-*/':
                # Reconhece operadores aritméticos
                tokens.append(current_char)
                current_position += 1

            elif current_char == '(':
                # Reconhece parêntese esquerdo
                tokens.append(current_char)
                current_position += 1

            elif current_char == ')':
                # Reconhece parêntese direito
                tokens.append(current_char)
                current_position += 1

            else:
                # Levanta uma exceção para caracteres inesperados
                #raise RuntimeError(f'Caractere inesperado: {current_char}')
                print(f'Caractere inesperado: {current_char}')
                current_position += 1

        return tokens