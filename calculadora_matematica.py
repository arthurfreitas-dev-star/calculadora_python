import math

def linha(char="─", n=54):
    print(char * n)

def cabecalho(titulo, subtitulo=""):
    print()
    linha("═")
    print(f"  {titulo}")
    if subtitulo:
        print(f"  {subtitulo}")
    linha("═")

def secao(titulo):
    print()
    linha()
    print(f"  {titulo}")
    linha()

def formatar(n):
    """Formata número: inteiro se possível, float sem zeros desnecessários."""
    if isinstance(n, float) and n.is_integer():
        return str(int(n))
    if isinstance(n, float):
        return f"{n:.10g}"
    return str(n)

def ler_float(prompt):
    while True:
        try:
            return float(input(f"  {prompt}: ").replace(",", "."))
        except ValueError:
            print("    Valor inválido. Tente novamente.")

def ler_int(prompt, minimo=None, maximo=None):
    while True:
        try:
            v = int(input(f"  {prompt}: "))
            if minimo is not None and v < minimo:
                print(f"    Valor mínimo: {minimo}")
                continue
            if maximo is not None and v > maximo:
                print(f"    Valor máximo: {maximo}")
                continue
            return v
        except ValueError:
            print("    Insira um número inteiro.")

def ler_lista_floats(prompt):
    while True:
        entrada = input(f"    {prompt}: ").replace(",", " ")
        try:
            nums = [float(x) for x in entrada.split() if x]
            if nums:
                return nums
            print("   Insira ao menos um número.")
        except ValueError:
            print("    Formato inválido. Separe os números por espaço ou vírgula.")

def pausar():
    input("\n  [Enter] para voltar ao menu...")


def soma():
    cabecalho("SOMA", "Some dois ou mais números")
    nums = ler_lista_floats("Números (separados por espaço ou vírgula)")
    total = sum(nums)
    expressao = " + ".join(formatar(n) for n in nums)
    secao("Resultado")
    print(f"  {expressao}")
    print(f"  = {formatar(total)}")
    pausar()


def subtracao():
    cabecalho("SUBTRAÇÃO", "Subtraia dois números")
    a = ler_float("Minuendo (A)")
    b = ler_float("Subtraendo (B)")
    resultado = a - b
    secao("Resultado")
    print(f"  {formatar(a)} − {formatar(b)} = {formatar(resultado)}")
    pausar()


def multiplicacao():
    cabecalho("MULTIPLICAÇÃO", "Multiplique dois ou mais números")
    nums = ler_lista_floats("Números (separados por espaço ou vírgula)")
    produto = 1
    for n in nums:
        produto *= n
    expressao = " × ".join(formatar(n) for n in nums)
    secao("Resultado")
    print(f"  {expressao}")
    print(f"  = {formatar(produto)}")
    pausar()



def divisao():
    cabecalho("DIVISÃO", "Divida dois números")
    a = ler_float("Dividendo (A)")
    b = ler_float("Divisor  (B)")
    if b == 0:
        print("\n   Erro: divisão por zero é indefinida.")
        pausar()
        return
    quociente   = a / b
    q_inteiro   = int(a) // int(b) if a == int(a) and b == int(b) else math.trunc(a / b)
    resto       = a % b
    secao("Resultado")
    print(f"  {formatar(a)} ÷ {formatar(b)} = {formatar(quociente)}")
    print(f"  Quociente inteiro : {q_inteiro}")
    print(f"  Resto             : {formatar(resto)}")
    pausar()



def media():
    cabecalho("MÉDIA ARITMÉTICA", "Calcule a média de uma lista de números")
    nums = ler_lista_floats("Números (separados por espaço ou vírgula)")
    total = sum(nums)
    med   = total / len(nums)
    secao("Resultado")
    print(f"  Números    : {', '.join(formatar(n) for n in nums)}")
    print(f"  Quantidade : {len(nums)}")
    print(f"  Soma       : {formatar(total)}")
    print(f"  Média      : {formatar(med)}")
    pausar()



def bhaskara():
    cabecalho("EQUAÇÃO DE 2° GRAU", "ax² + bx + c = 0  ·  Fórmula de Bhaskara")
    a = ler_float("Coeficiente A")
    if a == 0:
        print("\n    'a' não pode ser zero (seria equação de 1° grau).")
        pausar()
        return
    b = ler_float("Coeficiente B")
    c = ler_float("Coeficiente C")

    sinal_b = "+" if b >= 0 else "-"
    sinal_c = "+" if c >= 0 else "-"

    delta = b**2 - 4*a*c

    secao("Resolução")
    print(f"  Equação : {formatar(a)}x² {sinal_b} {formatar(abs(b))}x {sinal_c} {formatar(abs(c))} = 0")
    print(f"  Δ = b² − 4ac")
    print(f"  Δ = {formatar(b)}² − 4·{formatar(a)}·{formatar(c)}")
    print(f"  Δ = {formatar(delta)}")

    if delta < 0:
        print("\n  Δ < 0 → Sem raízes reais (raízes complexas)")
        parte_real = -b / (2*a)
        parte_img  = math.sqrt(-delta) / (2*a)
        print(f"  x₁ = {formatar(parte_real)} + {formatar(parte_img)}i")
        print(f"  x₂ = {formatar(parte_real)} − {formatar(parte_img)}i")
    elif delta == 0:
        x = -b / (2*a)
        print(f"\n  Δ = 0 → Uma raiz real (dupla)")
        print(f"  x = {formatar(x)}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"\n  Δ > 0 → Duas raízes reais distintas")
        print(f"  x₁ = (−({formatar(b)}) + √{formatar(delta)}) / {formatar(2*a)} = {formatar(x1)}")
        print(f"  x₂ = (−({formatar(b)}) − √{formatar(delta)}) / {formatar(2*a)} = {formatar(x2)}")
    pausar()




def fatorial():
    cabecalho("FATORIAL", "Calcule n! para inteiros não-negativos")
    n = ler_int("Número (n)", minimo=0)
    resultado = math.factorial(n)

    secao("Resultado")
    if n <= 12:
        passos = " × ".join(str(i) for i in range(1, n+1)) if n > 0 else "1"
        print(f"  {n}! = {passos}")
    else:
        print(f"  {n}! = {str(resultado)[:60]}..." if len(str(resultado)) > 60 else f"  {n}! = {resultado}")
    print(f"\n  Resultado completo: {resultado}")
    print(f"  Dígitos          : {len(str(resultado))}")
    pausar()

CONVERSOES = {
    "1": {
        "nome": "Comprimento",
        "unidades": {
            "1": ("Metro",       "m",   1.0),
            "2": ("Quilômetro",  "km",  1000.0),
            "3": ("Centímetro",  "cm",  0.01),
            "4": ("Milímetro",   "mm",  0.001),
            "5": ("Milha",       "mi",  1609.344),
            "6": ("Pé",          "ft",  0.3048),
            "7": ("Polegada",    "in",  0.0254),
        }
    },
    "2": {
        "nome": "Massa",
        "unidades": {
            "1": ("Quilograma",  "kg",  1.0),
            "2": ("Grama",       "g",   0.001),
            "3": ("Miligrama",   "mg",  0.000001),
            "4": ("Tonelada",    "t",   1000.0),
            "5": ("Libra",       "lb",  0.453592),
            "6": ("Onça",        "oz",  0.0283495),
        }
    },
    "3": {
        "nome": "Temperatura",
        "unidades": {
            "1": ("Celsius",    "°C", None),
            "2": ("Fahrenheit", "°F", None),
            "3": ("Kelvin",     "K",  None),
        }
    },
    "4": {
        "nome": "Velocidade",
        "unidades": {
            "1": ("Metro/segundo",   "m/s",  1.0),
            "2": ("Quilômetro/hora", "km/h", 1/3.6),
            "3": ("Milha/hora",      "mph",  0.44704),
            "4": ("Nó",              "kn",   0.514444),
        }
    },
}

def converter_temperatura(valor, de, para):
   
    if de == para:
        return valor
   
    if de == "°F":
        celsius = (valor - 32) * 5/9
    elif de == "K":
        celsius = valor - 273.15
    else:
        celsius = valor
    
    if para == "°F":
        return celsius * 9/5 + 32
    elif para == "K":
        return celsius + 273.15
    return celsius

def conversao():
    cabecalho("CONVERSÃO DE UNIDADES", "Comprimento · Massa · Temperatura · Velocidade")

   
    print()
    for k, v in CONVERSOES.items():
        print(f"  [{k}] {v['nome']}")
    print()
    while True:
        cat = input("    Categoria: ").strip()
        if cat in CONVERSOES:
            break
        print("      Opção inválida.")

    dados = CONVERSOES[cat]
    unidades = dados["unidades"]


    print()
    for k, (nome, sigla, _) in unidades.items():
        print(f"  [{k}] {nome} ({sigla})")

    print()
    while True:
        de_key = input("  De (número): ").strip()
        if de_key in unidades:
            break
        print("    Opção inválida.")

    while True:
        para_key = input("    Para (número): ").strip()
        if para_key in unidades:
            break
        print("    Opção inválida.")

    valor = ler_float("Valor")

    nome_de,  sigla_de,  fator_de  = unidades[de_key]
    nome_para, sigla_para, fator_para = unidades[para_key]

    if cat == "3":  # Temperatura
        resultado = converter_temperatura(valor, sigla_de, sigla_para)
    else:
        resultado = valor * fator_de / fator_para

    secao("Resultado")
    print(f"  {formatar(valor)} {sigla_de}  →  {formatar(resultado)} {sigla_para}")
    print(f"  ({nome_de} → {nome_para})")
    pausar()



def tabuada():
    cabecalho("TABUADA", "Gere a tabuada completa de qualquer número")
    n   = ler_float("Número")
    ate = ler_int("Até (padrão 10)", minimo=1)

    secao(f"Tabuada de {formatar(n)}")
    for i in range(1, ate + 1):
        r = n * i
        print(f"  {formatar(n):>8} × {str(i):>3} = {formatar(r)}")
    pausar()



def fibonacci():
    cabecalho("SEQUÊNCIA DE FIBONACCI", "Gere os primeiros N termos")
    n = ler_int("Quantidade de termos", minimo=1, maximo=1000)

    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b

    secao(f"Fibonacci — {n} termo{'s' if n > 1 else ''}")
    for i, v in enumerate(seq):
        print(f"  F({str(i).rjust(4)}) = {v}")

    print()
    print(f"  Último termo : {seq[-1]}")
    print(f"  Dígitos      : {len(str(seq[-1]))}")
    pausar()


OPERACOES = {
    "1":  ("Soma",                  soma),
    "2":  ("Subtração",             subtracao),
    "3":  ("Multiplicação",         multiplicacao),
    "4":  ("Divisão",               divisao),
    "5":  ("Média Aritmética",      media),
    "6":  ("Equação de 2° Grau",    bhaskara),
    "7":  ("Fatorial",              fatorial),
    "8":  ("Conversão de Unidades", conversao),
    "9":  ("Tabuada",               tabuada),
    "10": ("Fibonacci",             fibonacci),
    "0":  ("Sair",                  None),
}

def menu():
    while True:
        cabecalho("CALCULADORA MATEMÁTICA", "Selecione uma operação")
        print()
        for k, (nome, _) in OPERACOES.items():
            if k == "0":
                print()
                print(f"  [{k:>2}] {nome}")
            else:
                print(f"  [{k:>2}] {nome}")
        print()
        linha()
        opcao = input("  Opção: ").strip()
        linha()

        if opcao not in OPERACOES:
            print("    Opção inválida. Tente novamente.")
            continue

        nome, func = OPERACOES[opcao]

        if opcao == "0":
            print()
            print("  Até logo! ")
            print()
            break

        func()

if __name__ == "__main__":
    menu()
