
"""
Ester Pereira Martins
Atividade 07 - Projeto Integrador

"""

# 1 - Em comentarios , explique o cada comando faz

5 + 5       # soma de 5 mais 5
8 - 6       # subtracao de 8 menos 6  
12 * 5      # multiplicacao de 12 vezes 5
4**2        # exponencial de 4 elevado ao quadrado
27**(1/3)   # calcula a raíz cúbica de 27
27 / 3      # divisao de 27 por 3
27 // 4     # retorna o quociente inteiro da divisão de 27 por 4
27 % 4      # retorna o resto da divisão de 27 por 4

print('Este exercício é muito legal!')  # printa na tela Este exercício é muito legal!
x = 7   # atribui o valor 7 ao objeto x
print('O exercício ' + str(x) + ' é muito fácil!')  # printa na tela O exercício 7 é muito fácil!, convertendo o 7 da variável x para sting
x, y = 5, 6     # atribui 5 ao x e 6 ao y
print(x, y) # printa na tela os valores de x e y, separados por um espaço
print('Aprendi na escola que o {} vem antes do {}'.format(x, y))    # printa na tela Aprendi na escola que o 5 vem antes do 6, usando o método format para atribuir seus argumentos dentro das chaves na string

meuNome = 'Neylson Crepalde'    # define o objeto meuNome como Neylson Crepalde
print(meuNome[:8])  # retorna as letras do meuNome desde o início até o elemento 7 (começando do 0)
print(meuNome[8:])  # retorna as letras do meuNome desde o elemento 8 até o final

galera = ['Neylson', 'Edésio', 'Layla', 'Gerson', 'Iago','Ester', 'Juliany', 'Marcos', 'Patrick', 
          'Bia', 'Fabiano', 'Larissa', 'Sávio', 'Túlio', 'Vanessa', 'Numiá', 'Adelvan', 'Nelson', 
          'Warley', 'Vladimir'] # cria uma lista com esses nomes
          
galera[1]   # retorna o 2º elemento da lista (Edesio)
galera[0]   # retorna o 1º elemento da lista (Neylson)
galera[:5]  # retorna os 5 primeiros elementos da lista
galera[10:] # retorna desde o 11º elemento até o final desta lista
galera[6:15]    # retorna desde o 7º elemento até o 15º elemento da lista

# 2 - Crie três listas. A primeira deve conter o nome de 5 amigos de infância.
# A segunda deve conter o nome e 5 animais de estimação. A terceira deve conter 
# três pratos que você adora comer (use a criatividade). Exiba o conteúdo das listas.

amigosInfancia = ['Suellen', 'Sarah', 'Isabelle', 'Thiago', 'Matheus']
animaisEstimacao = ['Jack','Kira', 'Stuartt', 'Pitucha', 'Bruce Wayne']
pratos = ['Stroganoff', 'Sushi', 'Pizza', 'Coxinha', 'Yakisoba']

print(amigosInfancia, animaisEstimacao, pratos)

# 3 - Printe o nome do terceiro amigo da lista.
print(amigosInfancia[2])

# 4 - Bole uma frase bonitinha para chamar um bicho e insira nesse frase o nome do último bicho de estimação. Printe a frase na tela.
print(f'Vamos salvar a cidade Batman!! {animaisEstimacao[-1]} !!')

# 5 - Exiba na tela uma frase perguntando o que você quer comer no jantar essa noite e dê três opções: o segundo, terceiro e quarto pratos.
print(f'Boa noite ! \n \
temos três opções no menu desta noite: \n \
1){pratos[1]} \n \
2){pratos[2]} \n \
3){pratos[3]} \n \
Qual opção você deseja ?')

# 6 - Crie um objeto chamado nomeCompleto e atribua a ele o seu nome completo como uma string.
nomeCompleto = 'Ester Pereira Martins'

# 7 - Usando apenas slices (subsettings de um dado de texto) exiba apenas seu primeiro nome, apenas seu nome do meio e apenas seu sobrenome, um por vez.
print(nomeCompleto[:5])
print(nomeCompleto[6:13])
print(nomeCompleto[13:])

# 8 - Crie um dicionário com dados sobre a sua casa. 
# Pense em dados que seriam interessantes de serem usados numa pesquisa de 
# verdade - quantidade de moradores, bairro de localização, nomes das pessoas que moram, idade, cor, sexo, tipo de moradia (casa ou apartamento) e mais quatro campos. 
casa = {'quantidade de moradores': 5,
        'bairro': 'Concordia',
        'nomes': ['Ester', 'Fred', 'Alessandra', 'Lucymary', 'Kennedy'],
        'idades': ['18', '30', '45', '53', '53'],
        'cor': ['Branco', 'Branco', 'Branco', 'Parda', 'Branco'],
        'sexo': ['Feminino','Masculino', 'Feminino', 'Feminino', 'Masculino'],
        'tipo de moradia': ['Casa'],
        'viajou para outro pais': ['Nao', 'Sim', 'Sim', 'Nao', 'Nao'],
        'gostaria de morar em outro pais': [True, True, True, True, True],
        'estado civil': ['Solteira','Solteiro','Solteira','Casada', 'Casado'],
        'possui animal de estimacao':['Sim', 'Nao', 'Sim', 'Sim', 'Sim']}

# 9 - Exiba apenas as chaves do dicionário. Exiba apenas os valores do dicionário.
casa.keys()
casa.values()

# 10 - Exiba apenas o nome da segunda pessoa que mora na sua casa.
casa['nomes'][1]

# 11 - Escolha mais duas informações relevantes e exiba no console.
casa['viajou para outro pais'][1]
casa['estado civil'][4]


