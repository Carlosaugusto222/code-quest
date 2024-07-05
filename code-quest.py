# Nível 1: Variáveis
def nivel_variaveis():
    print("Bem-vindo ao Nível 1 - Variáveis!")
    print("Neste nível, você aprenderá sobre variáveis e operações básicas.")
    
    # Exemplo de variáveis e operações
    quantidade_macas = 5
    quantidade_peras = 3
    total_frutas = quantidade_macas + quantidade_peras
    
    # Exibição dos resultados
    print("Quantidade de maçãs:", quantidade_macas)
    print("Quantidade de peras:", quantidade_peras)
    print("Total de frutas:", total_frutas)

# Nível 2: Condicionais
def nivel_condicionais():
    print("\nBem-vindo ao Nível 2 - Condicionais!")
    print("Neste nível, você aprenderá sobre condicionais (if, elif, else).")
    
    # Exemplo de condicional
    porta_escolhida = "vermelha"
    if porta_escolhida == "vermelha":
        print("Você escolheu a porta vermelha.")
    else:
        print("Você escolheu uma porta diferente.")

# Nível 3: Loops
def nivel_loops():
    print("\nBem-vindo ao Nível 3 - Loops!")
    print("Neste nível, você aprenderá sobre loops (while e for).")
    
    # Exemplo de loop while
    contador = 0
    while contador < 3:
        print("Contador:", contador)
        contador += 1
    
    # Exemplo de loop for
    ingredientes = ["olho de sapo", "asas de morcego", "lágrimas de fênix"]
    for ingrediente in ingredientes:
        print("Adicionando", ingrediente)

# Nível 4: Funções
def nivel_funcoes():
    print("\nBem-vindo ao Nível 4 - Funções!")
    print("Neste nível, você aprenderá sobre funções em Python.")
    
    # Exemplo de função simples
    def calcular_area_retangulo(comprimento, largura):
        area = comprimento * largura
        return area
    
    # Testando a função
    sala1 = calcular_area_retangulo(5, 3)
    sala2 = calcular_area_retangulo(4, 2)
    print("Área da sala 1:", sala1)
    print("Área da sala 2:", sala2)

# Nível 5: Desafios Avançados
def nivel_desafios_avancados():
    print("\nBem-vindo ao Nível 5 - Desafios Avançados!")
    print("Neste nível, você enfrentará desafios integrados e complexos.")
    
    # Exemplo de desafio integrado
    def criar_pocao(ingredientes):
        # Simulação da criação de poção com base nos ingredientes
        if "olho de sapo" in ingredientes and "asas de morcego" in ingredientes:
            print("Você criou uma poção mágica!")
        else:
            print("Não foi possível criar a poção. Ingredientes insuficientes.")

    # Testando a função
    ingredientes_poção = ["olho de sapo", "asas de morcego"]
    criar_pocao(ingredientes_poção)

# Função principal para iniciar o jogo
def iniciar_jogo():
    print("Bem-vindo ao Code Quest - Jogo de Programação!")
    print("Prepare-se para embarcar em uma jornada de aprendizado e desafios.")
    
    # Chamando cada nível sequencialmente
    nivel_variaveis()
    nivel_condicionais()
    nivel_loops()
    nivel_funcoes()
    nivel_desafios_avancados()
    
    print("\nParabéns! Você concluiu todos os níveis do Code Quest.")
    print("Você se tornou um mestre na arte da programação em Python!")

# Chamando a função principal para iniciar o jogo
iniciar_jogo()
