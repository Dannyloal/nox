from ast_nodes import (
    Number,
    Texto,
    BinOp,
    UnaryOp,
    Var,
    Assignment,
    FunctionCall,
)

class ErroSemantico(Exception):
    pass

class Semantica:
    def __init__(self):
        self.variaveis = {}

    def analisar(self, node):
        if isinstance(node, Number):
            return "numero"

        if isinstance(node, Texto):
            return "texto"

        if isinstance(node, Var):
            if node.value not in self.variaveis:
                raise ErroSemantico(f"Erro semantico: variavel '{node.value}' nao declarada.")

            return self.variaveis[node.value]

        if isinstance(node, Assignment):
            nome = node.left.value
            tipo = self.analisar(node.value)

            if (
                nome in self.variaveis
                and self.variaveis[nome] != tipo
            ):
                raise ErroSemantico(f"Erro semantico: a variavel '{nome}' nao pode receber um valor do tipo {tipo}.")

            self.variaveis[nome] = tipo
            return tipo

        if isinstance(node, UnaryOp):
            tipo = self.analisar(node.right)

            if tipo != "numero":
                raise ErroSemantico("Erro semantico: operador unario exige um numero.")

            return "numero"

        if isinstance(node, BinOp):
            esquerda = self.analisar(node.left)
            direita = self.analisar(node.right)

            if (
                esquerda != "numero"
                or direita != "numero"
            ):
                raise ErroSemantico("Erro semantico: a operacao exige valores numericos.")

            return "numero"

        if isinstance(node, FunctionCall):
            nome = node.name.upper()

            tipos = [
                self.analisar(argumento)
                for argumento in node.args
            ]

            quantidade_funcoes = {
                "POTENCIA": 2,
                "RAIZ": 1,
                "BHASKARA": 3
            }

            if nome not in quantidade_funcoes:
                raise ErroSemantico(f"Erro semantico: funcao '{node.name}' nao existe.")

            esperada = quantidade_funcoes[nome]
            recebida = len(tipos)

            if recebida != esperada:
                raise ErroSemantico(f"Erro: funcao '{node.name}' esperava {esperada} argumentos, mas recebeu {recebida}.")

            if any(tipo != "numero" for tipo in tipos):
                raise ErroSemantico(f"Erro semantico: funcao '{node.name}' exige argumentos numericos.")

            return "numero"

        raise ErroSemantico(f"No semantico desconhecido: {type(node).__name__}.")