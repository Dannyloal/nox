from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
from semantic import Semantica
from tac import TAC

from ast_nodes import (
    Number,
    BinOp,
    UnaryOp,
    FunctionCall,
    Var,
    Assignment,
    Texto,
)

def formatar_ast(node, nivel=0):
    espaco = "    " * nivel

    if isinstance(node, Number):
        return f"Number({node.value})"

    if isinstance(node, Texto):
        return f'Texto("{node.value}")'

    if isinstance(node, Var):
        return f"Var({node.value})"

    if isinstance(node, BinOp):
        esquerda = formatar_ast(
            node.left,
            nivel + 1,
        )

        direita = formatar_ast(
            node.right,
            nivel + 1,
        )

        return (
            "BinOp(\n"
            f"{espaco}    left={esquerda},\n"
            f"{espaco}    op='{node.op.valor}',\n"
            f"{espaco}    right={direita}\n"
            f"{espaco})"
        )

    if isinstance(node, UnaryOp):
        direita = formatar_ast(
            node.right,
            nivel + 1,
        )

        return (
            "UnaryOp(\n"
            f"{espaco}    op='{node.op.valor}',\n"
            f"{espaco}    right={direita}\n"
            f"{espaco})"
        )

    if isinstance(node, Assignment):
        esquerda = formatar_ast(
            node.left,
            nivel + 1,
        )

        valor = formatar_ast(
            node.value,
            nivel + 1,
        )

        return (
            "Assignment(\n"
            f"{espaco}    left={esquerda},\n"
            f"{espaco}    value={valor}\n"
            f"{espaco})"
        )

    if isinstance(node, FunctionCall):
        argumentos = ", ".join(
            formatar_ast(
                argumento,
                nivel + 1,
            )
            for argumento in node.args
        )

        return (
            "FunctionCall(\n"
            f"{espaco}    name='{node.name}',\n"
            f"{espaco}    args=[{argumentos}]\n"
            f"{espaco})"
        )

    return (
        f"<No desconhecido: "
        f"{type(node).__name__}>"
    )


def analisar_codigo(
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

    return (
        resultado,
        arvore,
        gerador.codigo,
    )


def processar(
    linha,
    semantico,
    interpretador,
):
    resultado, arvore, codigo_tac = analisar_codigo(
        linha,
        semantico,
        interpretador,
    )

    print("\nArvore sintatica abstrata:\n")
    print(formatar_ast(arvore))

    print("\nCodigo intermediario TAC:\n")

    if codigo_tac:
        print("\n".join(codigo_tac))
    else:
        print("(nenhuma instrucao)")

    print("\nResultado final:\n")
    print(resultado)
    print()


def executar(
    codigo,
    semantico=None,
    interpretador=None,
):
    resultado, _, _ = analisar_codigo(
        codigo,
        semantico,
        interpretador,
    )

    return resultado


def repl():
    print("NOX iniciada.")
    print("Digite 'sair' para encerrar.\n")

    semantico = Semantica()
    interpretador = Interpreter()

    while True:
        codigo = input(">>> ").strip()

        if codigo.lower() in ("sair", "exit"):
            print("Programa encerrado.")
            break

        if not codigo:
            continue

        try:
            processar(
                codigo,
                semantico,
                interpretador,
            )

        except Exception as erro:
            print(f"{erro}\n")


if __name__ == "__main__":
    repl()