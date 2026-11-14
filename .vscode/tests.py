from math import isclose
from lexer import Lexer
from parser import Parser
from semantic import Semantica, ErroSemantico
from interpreter import Interpreter, ErroExecucao
from tac import TAC
from main import formatar_ast

def analisar(
    codigo,
    semantico=None,
    interpretador=None,
):
    semantico = semantico or Semantica()
    interpretador = interpretador or Interpreter()

    tokens = Lexer(codigo).tokenizar()
    arvore = Parser(tokens).parse()

    semantico.analisar(arvore)

    gerador = TAC()
    gerador.gerar(arvore)

    resultado = interpretador.avaliar(arvore)

    return resultado, arvore, gerador.codigo

def mostrar(
    codigo,
    resultado,
    arvore,
    codigo_tac,
):
    print(f"\nEntrada: {codigo}")

    print("\nAST:")
    print(formatar_ast(arvore))

    print("\nCodigo intermediario TAC:")

    if codigo_tac:
        print("\n".join(codigo_tac))
    else:
        print("(nenhuma instrucao)")

    print("\nResultado:")
    print(resultado)


def testar(
    codigo,
    esperado,
    semantico=None,
    interpretador=None,
    tolerancia=None,
):
    resultado, arvore, codigo_tac = analisar(
        codigo,
        semantico,
        interpretador,
    )

    mostrar(
        codigo,
        resultado,
        arvore,
        codigo_tac,
    )

    if tolerancia is None:
        correto = resultado == esperado
    else:
        correto = isclose(
            resultado,
            esperado,
            abs_tol=tolerancia,
        )

    if not correto:
        raise AssertionError(f"Resultado incorreto para {codigo}. Esperado: {esperado}. Recebido: {resultado}.")
    print("[OK]")

def testar_erro(codigo, tipo_esperado):
    try:
        resultado, arvore, codigo_tac = analisar(
            codigo
        )

        mostrar(
            codigo,
            resultado,
            arvore,
            codigo_tac,
        )

        raise AssertionError(f"{codigo} deveria produzir erro.")

    except tipo_esperado as erro:
        print(f"\nEntrada: {codigo}")
        print(f"Erro controlado: {erro}")
        print("[OK ERRO]")


print("=" * 60)
print("POTÊNCIA")
print("=" * 60)

testar("potencia(2, 5)", 32)
testar("potencia(3, 3)", 27)

#

print("=" * 60)
print("RAÍZ")
print("=" * 60)

testar("raiz(16)", 4.0)
testar("raiz(9)", 3.0)
testar_erro("raiz(-4)", ErroExecucao)

#

print("=" * 60)
print("BHASKARA")
print("=" * 60)

testar("bhaskara(1, -3, 2)", [2.0, 1.0])
testar("bhaskara(1, -2, 1)", [1.0, 1.0])
testar("bhaskara(1, 2, 5)", [])
testar_erro("bhaskara(0, 2, 1)", ErroExecucao)

print("\nTESTES DA PROVA CONCLUÍDOS.")