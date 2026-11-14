REESCREVER DEPOIS:





NOX - Mini linguagem de programacao
Autores: Gisele e Dannylo

==================================================
OBJETIVO
==================================================

A NOX e uma linguagem desenvolvida para demonstrar as principais etapas
do processamento de uma linguagem de programacao:

Codigo-fonte
    |
    v
Tokens
    |
    v
AST
    |
    v
Analise semantica
    |
    v
Codigo intermediario TAC
    |
    v
Resultado final

A linguagem possui suporte para:

- Operacoes aritmeticas;
- Comparacoes;
- Variaveis;
- Atribuicoes;
- Chamadas de funcoes;
- Funcoes combinadas;
- Tratamento de erros;
- Geracao de AST;
- Geracao de codigo intermediario TAC.

==================================================
QUESTAO 1 - FUNCAO LIMIT
==================================================

A funcao LIMIT recebe tres argumentos:

LIMIT(valor, minimo, maximo)

Regras:

- Se valor estiver entre minimo e maximo, retorna valor;
- Se valor for menor que minimo, retorna minimo;
- Se valor for maior que maximo, retorna maximo.

Exemplos:

LIMIT(15, 0, 10)

Resultado:

10

LIMIT(-5, 0, 10)

Resultado:

0

LIMIT(7, 0, 10)

Resultado:

7

A funcao exige exatamente tres argumentos.

==================================================
QUESTAO 2 - DIVISAO POR ZERO
==================================================

Antes de realizar uma divisao, o interpretador avalia o operando direito.

Quando o valor do operando direito e zero, a divisao nao e executada.
Nesse caso, a linguagem gera uma excecao propria chamada ErroExecucao.

Exemplo valido:

10 / 2

Resultado:

5

Exemplo invalido:

10 / 0

Mensagem esperada:

Erro: divisao por zero nao e permitida.

A linguagem nao deve apresentar a excecao interna:

ZeroDivisionError

==================================================
QUESTAO 3 - QUANTIDADE DE ARGUMENTOS
==================================================

Cada funcao possui uma quantidade esperada de argumentos.

A funcao LIMIT exige exatamente tres argumentos.

Chamada valida:

LIMIT(5, 0, 10)

Chamada invalida com dois argumentos:

LIMIT(5, 0)

Mensagem esperada:

Erro: funcao 'limit' esperava 3 argumentos,
mas recebeu 2.

Chamada invalida com quatro argumentos:

LIMIT(5, 0, 10, 20)

Mensagem esperada:

Erro: funcao 'limit' esperava 3 argumentos,
mas recebeu 4.

A verificacao ocorre antes da execucao da funcao.

==================================================
QUESTAO 4 - BIBLIOTECA DE FUNCOES
==================================================

A NOX possui as seguintes funcoes obrigatorias:

POTENCIA(base, expoente)
MEDIA(a, b, c)
MEDIANA(a, b, c)
MAIOR(a, b, c)

--------------------------------------------------
POTENCIA
--------------------------------------------------

Recebe dois numeros inteiros e retorna o resultado da potenciacao.

Exemplo:

POTENCIA(2, 5)

Resultado:

32

Outro exemplo:

POTENCIA(3, 3)

Resultado:

27

Para os testes, o expoente deve ser inteiro e nao negativo.

--------------------------------------------------
MEDIA
--------------------------------------------------

Recebe tres valores e retorna a media aritmetica.

Exemplo:

MEDIA(7, 8, 9)

Resultado:

8

Calculo:

(7 + 8 + 9) / 3 = 8

Outro exemplo:

MEDIA(10, 5, 3)

Resultado:

6

--------------------------------------------------
MEDIANA
--------------------------------------------------

Recebe tres valores, organiza-os e retorna o valor central.

Exemplo:

MEDIANA(10, 2, 7)

Valores ordenados:

2, 7, 10

Resultado:

7

Outro exemplo:

MEDIANA(3, 12, 5)

Valores ordenados:

3, 5, 12

Resultado:

5

A ordem dos argumentos nao altera o resultado.

--------------------------------------------------
MAIOR
--------------------------------------------------

Recebe tres valores e retorna o maior deles.

Exemplo:

MAIOR(4, 15, 8)

Resultado:

15

Outro exemplo:

MAIOR(20, 7, 13)

Resultado:

20

--------------------------------------------------
FUNCOES COMBINADAS
--------------------------------------------------

As funcoes podem ser utilizadas dentro de outras operacoes
ou chamadas de funcao.

Exemplo:

POTENCIA(MEDIA(2, 4, 6), 2)

Processamento:

MEDIA(2, 4, 6) -> 4

POTENCIA(4, 2) -> 16

Resultado:

16

Outro exemplo:

MEDIA(MAIOR(4, 15, 8), MEDIANA(10, 2, 7), 6)

Resultado:

9.333333333333334

==================================================
FUNCOES PRESERVADAS
==================================================

A linguagem tambem preserva as funcoes existentes anteriormente:

FATORIAL(numero)
CHAVE(numero)
SEN(graus)
COS(graus)
PRINT(valor)
MINIMO(valores)
MAXIMO(valores)
TAMANHO(texto)

==================================================
AST E CODIGO INTERMEDIARIO
==================================================

Para cada teste executado, o programa apresenta:

- Entrada;
- Arvore Sintatica Abstrata;
- Codigo intermediario TAC;
- Resultado final ou erro controlado.

Exemplo:

Entrada:

POTENCIA(MEDIA(2, 4, 6), 2)

AST:

FunctionCall(
    name='POTENCIA',
    args=[
        FunctionCall(
            name='MEDIA',
            args=[Number(2), Number(4), Number(6)]
        ),
        Number(2)
    ]
)

Codigo intermediario TAC:

t1 = MEDIA(2, 4, 6)
t2 = POTENCIA(t1, 2)

Resultado final:

16.0

==================================================
ESTRUTURA DOS ARQUIVOS
==================================================

tokens.py:

Define os tipos de tokens.

ast_nodes.py:

Define os nos da AST.

lexer.py:

Transforma o codigo-fonte em tokens.

parser.py:

Verifica a estrutura dos tokens e constroi a AST.

semantic.py:

Realiza a analise semantica, verificando:

- Variaveis;
- Tipos;
- Quantidade de argumentos;
- Funcoes existentes;
- Argumentos validos.

funcoes.py:

Implementa as funcoes internas da linguagem.

interpreter.py:

Executa a AST e gera o resultado final.

tac.py:

Gera o codigo intermediario Three-Address Code.

main.py:

Executa a linguagem e apresenta:

- AST;
- Codigo intermediario;
- Resultado final.

tests.py:

Contem os testes separados por questao:

- Questao 1;
- Questao 2;
- Questao 3;
- Questao 4.

==================================================
TRATAMENTO DE ERROS
==================================================

A linguagem possui erros proprios para impedir que excecoes internas
do Python sejam apresentadas diretamente ao usuario.

Exemplos:

Divisao por zero:

10 / 0

Resultado:

Erro: divisao por zero nao e permitida.

Quantidade incorreta de argumentos:

LIMIT(5, 0)

Resultado:

Erro: funcao 'LIMIT' esperava 3 argumentos,
mas recebeu 2.

Funcao inexistente:

MAGICA(10)

Resultado:

Erro: funcao 'MAGICA' nao existe.

Variavel nao definida:

variavel_inexistente + 1

Resultado:

Erro: variavel 'variavel_inexistente' nao foi definida.

==================================================
COMO EXECUTAR
==================================================

Para iniciar a linguagem:

python main.py

Para executar os testes:

python tests.py

Ao executar o main.py, digite uma expressao no terminal.

Exemplo:

>>> limit(15, 0, 10)

O programa apresentara:

- A AST;
- O codigo intermediario;
- O resultado final.

Para encerrar o programa:

sair

ou:

exit


==================================================
ALTERACOES REALIZADAS PARA ESTA PROVA
==================================================

Em comparacao com a versao final do trabalho anterior, foram realizadas
as seguintes alteracoes na linguagem NOX:

1. Inclusao da funcao LIMIT

Foi adicionada a funcao interna:

LIMIT(valor, minimo, maximo)

A funcao retorna o proprio valor quando ele esta dentro do intervalo.
Quando o valor e menor que o minimo, retorna o minimo. Quando o valor e
maior que o maximo, retorna o maximo.

Exemplos:

LIMIT(15, 0, 10) -> 10
LIMIT(-5, 0, 10) -> 0
LIMIT(7, 0, 10) -> 7

A funcao exige exatamente tres argumentos.

2. Tratamento proprio para divisao por zero

O interpretador passou a verificar o valor do operando direito antes de
realizar uma divisao. Se o valor for zero, a operacao e interrompida e a
linguagem gera a excecao propria ErroExecucao.

Exemplo:

10 / 0

Mensagem apresentada:

Erro: divisao por zero nao e permitida.

Dessa forma, o usuario nao recebe a excecao interna do Python:

ZeroDivisionError

3. Validacao da quantidade de argumentos

Foi incluida uma verificacao da quantidade de argumentos recebidos por
cada funcao. A quantidade recebida e comparada com a quantidade esperada
antes da execucao.

A funcao LIMIT exige tres argumentos.

Chamada valida:

LIMIT(5, 0, 10)

Chamada invalida com dois argumentos:

LIMIT(5, 0)

Mensagem esperada:

Erro: funcao 'LIMIT' esperava 3 argumentos, mas recebeu 2.

Chamada invalida com quatro argumentos:

LIMIT(5, 0, 10, 20)

Mensagem esperada:

Erro: funcao 'LIMIT' esperava 3 argumentos, mas recebeu 4.

4. Inclusao das funcoes MEDIA, MEDIANA e MAIOR

Foram adicionadas novas funcoes internas para ampliar a biblioteca da
linguagem.

MEDIA(a, b, c):

Retorna a media aritmetica dos tres valores.

Exemplo:

MEDIA(7, 8, 9) -> 8

MEDIANA(a, b, c):

Organiza os tres valores e retorna o valor central.

Exemplo:

MEDIANA(10, 2, 7) -> 7

MAIOR(a, b, c):

Retorna o maior dos tres valores.

Exemplo:

MAIOR(4, 15, 8) -> 15

As tres funcoes exigem exatamente tres argumentos numericos.

5. Suporte a funcoes combinadas

As funcoes podem ser utilizadas como argumentos de outras funcoes ou
em expressoes.

Exemplo:

POTENCIA(MEDIA(2, 4, 6), 2)

Resultado:

16

Outro exemplo:

MAIOR(MEDIANA(20, 5, 11), 8, 15)

Resultado:

15

6. Exibicao da AST e do codigo intermediario

A execucao das funcoes passou a apresentar as etapas intermediarias
do processamento:

- Entrada;
- Arvore Sintatica Abstrata;
- Codigo intermediario TAC;
- Resultado final ou erro controlado.

Exemplo de TAC para uma chamada combinada:

POTENCIA(MEDIA(2, 4, 6), 2)

t1 = MEDIA(2, 4, 6)
t2 = POTENCIA(t1, 2)

7. Organizacao dos testes

O arquivo tests.py foi reorganizado de acordo com as questoes da prova:

- QUESTAO 1 - Funcao LIMIT;
- QUESTAO 2 - Divisao por zero;
- QUESTAO 3 - Quantidade de argumentos;
- QUESTAO 4 - Biblioteca de funcoes.

Os testes tambem incluem chamadas combinadas e exibem a AST, o TAC e
o resultado de cada caso valido.

8. Funcoes anteriores preservadas

As funcoes que ja existiam no trabalho anterior foram mantidas:

- POTENCIA;
- FATORIAL;
- CHAVE;
- SEN;
- COS;
- PRINT;
- MINIMO;
- MAXIMO;
- TAMANHO.