<h2 align="center"> Mathematical Expression Evaluator </h2>
<p align="justify"> Implementation of an arithmetic expression evaluator. The work includes the development of a lexer, parser, and a step-by-step evaluator, focusing on readability, reliability, and execution cost.</p>

<p align="center"> <a href="https://malbarbo.pro.br/ensino/2019/9795/trabalho-comp/" target="_blank"> Full Assignment (pt-br) </a> </p>

<hr>

# Overall Architecture:
<p align="center">
    <img src="./assets/architecture.png" alt="Software Architecture">
</p>

### Lexer:
<p align="center">
    <p> Receives the expression as input and returns an array of tokens</p>
    <img src="./assets/lexer.png" alt="Lexer Architecture">
</p>

### Parser:
<p align="center">
    <p> Receives an array of tokens as input and builds a syntax tree that represents the original expression</p>
    <img src="./assets/parser.png" alt="Parser Architecture">
</p>

### Eval Step:
<p align="center">
    <p> Traverses the expression tree following a bottom-up approach, resolving the entire expression in parts by evaluating results inferred by subtrees</p>
    <img src="./assets/eval-step.png" alt="Eval Step">
</p>

### To String:
<p align="center">
    <p> Traverses the tree and prints the current state of the expression</p>
</p>

## Created by:
* <a href="https://github.com/reidn3r" target="_blank">Reidner</a>
* <a href="https://github.com/Vitor-Padovani" target="_blank">Vitor Padovani</a>
* <a href="https://github.com/Hudson-H" target="_blank">Hudson da Silva</a>
