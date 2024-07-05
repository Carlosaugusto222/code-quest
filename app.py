from flask import Flask, render_template

app = Flask(__name__)

# Funções para os níveis do jogo
def nivel_variaveis():
    return """
    <h2>Nível 1 - Variáveis</h2>
    <p>Aqui você aprende sobre variáveis em Python.</p>
    <p>Exemplo:</p>
    <pre>
    quantidade_macas = 5
    quantidade_peras = 3
    total_frutas = quantidade_macas + quantidade_peras
    print("Total de frutas:", total_frutas)
    </pre>
    """

def nivel_condicionais():
    return """
    <h2>Nível 2 - Condicionais</h2>
    <p>Aqui você aprende sobre condicionais em Python.</p>
    <p>Exemplo:</p>
    <pre>
    porta_escolhida = "vermelha"
    if porta_escolhida == "vermelha":
        print("Você escolheu a porta vermelha.")
    else:
        print("Você escolheu uma porta diferente.")
    </pre>
    """

def nivel_loops():
    return """
    <h2>Nível 3 - Loops</h2>
    <p>Aqui você aprende sobre loops em Python.</p>
    <p>Exemplo:</p>
    <pre>
    contador = 0
    while contador < 3:
        print("Contador:", contador)
        contador += 1
    </pre>
    """

def nivel_funcoes():
    return """
    <h2>Nível 4 - Funções</h2>
    <p>Aqui você aprende sobre funções em Python.</p>
    <p>Exemplo:</p>
    <pre>
    def calcular_area_retangulo(comprimento, largura):
        area = comprimento * largura
        return area

    sala1 = calcular_area_retangulo(5, 3)
    sala2 = calcular_area_retangulo(4, 2)
    print("Área da sala 1:", sala1)
    print("Área da sala 2:", sala2)
    </pre>
    """

def nivel_desafios_avancados():
    return """
    <h2>Nível 5 - Desafios Avançados</h2>
    <p>Aqui você enfrenta desafios integrados e complexos.</p>
    <p>Exemplo:</p>
    <pre>
    def criar_pocao(ingredientes):
        if "olho de sapo" in ingredientes and "asas de morcego" in ingredientes:
            print("Você criou uma poção mágica!")
        else:
            print("Não foi possível criar a poção. Ingredientes insuficientes.")

    ingredientes_poção = ["olho de sapo", "asas de morcego"]
    criar_pocao(ingredientes_poção)
    </pre>
    """

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para cada nível do jogo
@app.route('/nivel1')
def nivel1():
    return nivel_variaveis()

@app.route('/nivel2')
def nivel2():
    return nivel_condicionais()

@app.route('/nivel3')
def nivel3():
    return nivel_loops()

@app.route('/nivel4')
def nivel4():
    return nivel_funcoes()

@app.route('/nivel5')
def nivel5():
    return nivel_desafios_avancados()

if __name__ == '__main__':
    app.run(debug=True)
