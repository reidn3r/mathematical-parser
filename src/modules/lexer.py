class Lexer:
    def __init__(self):
        self

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

            elif current_char.isdigit():
                # Reconhece números inteiros
                start_position = current_position
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
                raise RuntimeError(f'Caractere inesperado: {current_char}')
        
        return tokens
