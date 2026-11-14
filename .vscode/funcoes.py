import math

def potencia(base, expoente):
    return base ** expoente

def raiz(numero):
    if numero < 0:
        raise ValueError("Raíz aceita somente números não negativos")
    
    return math.sqrt(numero)

#  ************************

def formatar(n):
    if float(n).is_integer():
        return str(int(n))
    return str(round(n, 4))

# BHASKARA/DELTA

def montar_etapas(a, b, c):
    if a == 0:
        raise ValueError("Não é uma equação de 2º grau se 'a' for igual a 0")
    
    delta = b ** 2 - 4 * a * c
    etapas = [
        f"Equação: a = {a}, b = {b}, c = {c}",
        "Fórmula do Delta: Δ = b² - 4.a.c",
        f"Valores no lugar: Δ = ({b}²) - 4.{a}.{c}",
        f"A conta: Δ = {b ** 2} - {4 * a * c} = {delta}",
    ]
    
    if delta < 0:
        etapas.append("Se delta (Δ) é menor que 0, não existem raízes reais")
        return etapas, [] # para aqui e não haverá mais etapas
    
    raiz = math.sqrt(delta)
    x1 = (-b + raiz) / (2 * a)
    x2 = (-b - raiz) / (2 * a)
    etapas += [
        "Se Δ é maior ou igual a 0, existem raízes reais",
        f"Raíz do Delta: √{delta} = {formatar(raiz)}",
        "Fórmula das raízes: x = (-b ± √Δ) / 2a",
        f"Valores no lugar: x = ({-b} ± √{delta}) / {2 * a}",
    ]
    
    if delta == 0:
        etapas.append(f"Como Δ = 0, as duas raízes são iguais: x = {formatar(x1)}")
    else:
        etapas.append(f"Resultado: x1 = {formatar(x1)} e x2 = {formatar(x2)}")
       
    return etapas, [x1, x2]


def bhaskara(a, b, c):
    etapas, raizes = montar_etapas(a, b, c)
    for etapa in etapas:
        print(etapa)        
    return raizes

#  ************************




FUNCOES = {
    "POTENCIA": (2, potencia),
    "RAIZ": (1, raiz),
    "BHASKARA": (3, bhaskara)
}

if __name__ == "__main__":
    for a, b, c in [(1, -3, 2), (1, -2, 1), (1, 2, 5)]:
        etapas, raizes = montar_etapas(a, b, c)
        print(f"\n--- a={a}, b={b}, c={c} ---")
        for etapa in etapas:
            print(etapa)