class Lexer:
    def __init__(self):
        self

    def run(self, string) -> 'list[str]':
        return self.__string2tokens__(string);

    def __string2tokens__(self, string:str) -> 'list[str]':
        '''
            1. Primeiro if: Trata constantes com parênteses aberto
                - Primeiro é add. ao array o char '('
                - Em seguida é add. ao array a parte numerica

            2. Segundo if: Trata constantes com parênteses fechado
                - Primeiro é add. ao array a parte numerica
                - Em seguida é add. ao array o char ')'

            3. Terceiro if: Trata constantes e operadores, sem parênteses
        '''

        parts, tokens = string.split(' '), []
        for part in parts:
            open_idx, close_idx = part.find('('), part.find(')')
            if(open_idx != -1):
                tokens.append(part[open_idx])
                tokens.append(int(part[1:]))
                continue
            
            if(close_idx != -1):
                tokens.append(int(part[:close_idx]))
                tokens.append(part[close_idx])
                continue

            else:
                try:
                    tokens.append(int(part)) 
                    #Tenta converter para int, se falhar não é número
                except ValueError:
                    tokens.append(part) if part != '' else None
        return tokens
    