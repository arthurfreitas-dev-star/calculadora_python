#  Calculadora Matemática

Calculadora matemática interativa para o terminal, desenvolvida em Python. Reúne em um único menu operações básicas, equação de 2° grau, fatorial, conversão de unidades, tabuada e sequência de Fibonacci. O programa não precisa de nenhuma instalação extra, basta ter o Python e executar.

---

##  Tecnologias utilizadas

- **[Python 3](https://www.python.org/)** — linguagem principal do projeto
- **`math`** — módulo da biblioteca padrão do Python (raiz quadrada, fatorial e truncamento)

> Nenhuma dependência externa é necessária. Não há `pip install` nem `requirements.txt`.

---

##  Como instalar e executar

### Pré-requisitos

- **Python 3.6 ou superior** instalado na sua máquina.

Para verificar se o Python já está instalado, abra o terminal e digite:

```bash
python --version
```

Caso o comando não funcione, tente `python3 --version`. Se o Python não estiver instalado, baixe-o em [python.org/downloads](https://www.python.org/downloads/).

### Passo a passo

**1. Clone o repositório**

```bash
git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
```

**2. Entre na pasta do projeto**

```bash
cd NOME-DO-REPOSITORIO
```

**3. Execute o programa**

```bash
python calculadora_matematica.py
```

No Linux ou macOS, caso `python` não seja reconhecido:

```bash
python3 calculadora_matematica.py
```

**4. Use o menu**

Digite o número da operação desejada e pressione `Enter`. Ao final de cada operação, pressione `Enter` novamente para voltar ao menu. Para encerrar, escolha a opção `0`.

>  **Dica:** você pode usar vírgula ou ponto como separador decimal (`3,5` ou `3.5`). Nas operações com várias entradas, separe os números por espaço ou vírgula.

###  Funcionalidades

| Opção | Operação | Descrição |
|:-----:|----------|-----------|
| 1 | Soma | Soma dois ou mais números |
| 2 | Subtração | Subtrai dois números |
| 3 | Multiplicação | Multiplica dois ou mais números |
| 4 | Divisão | Retorna quociente, quociente inteiro e resto (com tratamento de divisão por zero) |
| 5 | Média Aritmética | Calcula a média de uma lista de números |
| 6 | Equação de 2° Grau | Resolve ax² + bx + c = 0 pela fórmula de Bhaskara, inclusive com raízes complexas |
| 7 | Fatorial | Calcula n! para inteiros não negativos |
| 8 | Conversão de Unidades | Comprimento, massa, temperatura e velocidade |
| 9 | Tabuada | Gera a tabuada de qualquer número até o limite escolhido |
| 10 | Fibonacci | Gera os primeiros N termos da sequência (até 1000) |
| 0 | Sair | Encerra o programa |

---

##  Exemplo de uso

### Menu principal

```text
══════════════════════════════════════════════════════
  CALCULADORA MATEMÁTICA
  Selecione uma operação
══════════════════════════════════════════════════════

  [ 1] Soma
  [ 2] Subtração
  [ 3] Multiplicação
  [ 4] Divisão
  [ 5] Média Aritmética
  [ 6] Equação de 2° Grau
  [ 7] Fatorial
  [ 8] Conversão de Unidades
  [ 9] Tabuada
  [10] Fibonacci

  [ 0] Sair

──────────────────────────────────────────────────────
  Opção:
```

### Soma

```text
══════════════════════════════════════════════════════
  SOMA
  Some dois ou mais números
══════════════════════════════════════════════════════
    Números (separados por espaço ou vírgula): 10 25,5 4

──────────────────────────────────────────────────────
  Resultado
──────────────────────────────────────────────────────
  10 + 25.5 + 4
  = 39.5
```

### Divisão

```text
══════════════════════════════════════════════════════
  DIVISÃO
  Divida dois números
══════════════════════════════════════════════════════
  Dividendo (A): 17
  Divisor  (B): 5

──────────────────────────────────────────────────────
  Resultado
──────────────────────────────────────────────────────
  17 ÷ 5 = 3.4
  Quociente inteiro : 3
  Resto             : 2
```

### Equação de 2° Grau (Bhaskara)

```text
══════════════════════════════════════════════════════
  EQUAÇÃO DE 2° GRAU
  ax² + bx + c = 0  ·  Fórmula de Bhaskara
══════════════════════════════════════════════════════
  Coeficiente A: 1
  Coeficiente B: -5
  Coeficiente C: 6

──────────────────────────────────────────────────────
  Resolução
──────────────────────────────────────────────────────
  Equação : 1x² - 5x + 6 = 0
  Δ = b² − 4ac
  Δ = -5² − 4·1·6
  Δ = 1

  Δ > 0 → Duas raízes reais distintas
  x₁ = (−(-5) + √1) / 2 = 3
  x₂ = (−(-5) − √1) / 2 = 2
```

### Fatorial

```text
══════════════════════════════════════════════════════
  FATORIAL
  Calcule n! para inteiros não-negativos
══════════════════════════════════════════════════════
  Número (n): 5

──────────────────────────────────────────────────────
  Resultado
──────────────────────────────────────────────────────
  5! = 1 × 2 × 3 × 4 × 5

  Resultado completo: 120
  Dígitos          : 3
```

### Conversão de unidades

```text
══════════════════════════════════════════════════════
  CONVERSÃO DE UNIDADES
  Comprimento · Massa · Temperatura · Velocidade
══════════════════════════════════════════════════════

  [1] Comprimento
  [2] Massa
  [3] Temperatura
  [4] Velocidade

    Categoria: 3

  [1] Celsius (°C)
  [2] Fahrenheit (°F)
  [3] Kelvin (K)

  De (número): 1
    Para (número): 2
  Valor: 100

──────────────────────────────────────────────────────
  Resultado
──────────────────────────────────────────────────────
  100 °C  →  212 °F
  (Celsius → Fahrenheit)
```

### Tabuada

```text
══════════════════════════════════════════════════════
  TABUADA
  Gere a tabuada completa de qualquer número
══════════════════════════════════════════════════════
  Número: 7
  Até (padrão 10): 5

──────────────────────────────────────────────────────
  Tabuada de 7
──────────────────────────────────────────────────────
         7 ×   1 = 7
         7 ×   2 = 14
         7 ×   3 = 21
         7 ×   4 = 28
         7 ×   5 = 35
```

### Sequência de Fibonacci

```text
══════════════════════════════════════════════════════
  SEQUÊNCIA DE FIBONACCI
  Gere os primeiros N termos
══════════════════════════════════════════════════════
  Quantidade de termos: 8

──────────────────────────────────────────────────────
  Fibonacci — 8 termos
──────────────────────────────────────────────────────
  F(   0) = 0
  F(   1) = 1
  F(   2) = 1
  F(   3) = 2
  F(   4) = 3
  F(   5) = 5
  F(   6) = 8
  F(   7) = 13

  Último termo : 13
  Dígitos      : 2
```

---

##  Autor e contato

<!--  Edite os campos abaixo com as suas informações -->

**Desenvolvido por:** Arthur Victor Couto Freitas 

-  **LinkedIn:** https://www.linkedin.com/in/arthurvictorfreitas/
-  **E-mail:** arthurfreitas082007@outlook.com
-  **GitHub:** https://github.com/arthurfreitas-dev-star

---

⭐ Se este projeto foi útil para você, considere deixar uma estrela no repositório!
