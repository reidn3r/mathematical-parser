<h2 align="center"> Avaliador de Expressões Matemáticas </h2>
<p align="justify"> Implementação de um avaliador de expressões aritméticas. O trabalho inclui o desenvolvimento de um lexer, parser, e um avaliador passo a passo, com foco na facilidade de leitura, confiabilidade e custo de execução.</p>

<p align="center"> <a href="https://malbarbo.pro.br/ensino/2019/9795/trabalho-comp/" target="_blank"> Enunciado Completo </a> </p>

<hr>

# Arquitetura Geral:
<p align="center">
    <img src="./assets/architecture.png" alt="Software Architecture">
</p>

### Lexer:
<p align="center">
    <p> Recebe expressão como entrada e retorna array de tokens</p>
    <img src="./assets/lexer.png" alt="Lexer Architecture">
</p>

### Parser:
<p align="center">
    <p> Recebe array de tokens como entrada e constrói uma árvore sintática que representa a expressão inicial</p>
    <img src="./assets/parser.png" alt="Parser Architecture">
</p>

### Eval Step:
<p align="center">
    <p> Percorre a árvore da expressão seguindo a abordagem bottom-up, e resolve a expressão toda por partes, avaliando resultados inferidos por sub-árvores</p>
    <img src="./assets/eval-step.png" alt="Eval Step">
</p>

### To String:
<p align="center">
    <p> Percorre a árvore e imprime o estado atual da expressão</p>
</p>


## Feito por:
* <a href="https://github.com/reidn3r" target="_blank">Reidner</a>
* <a href="https://github.com/Vitor-Padovani" target="_blank">Vitor Padovani</a>
* <a href="https://github.com/Hudson-H" target="_blank">Hudson da Silva</a>