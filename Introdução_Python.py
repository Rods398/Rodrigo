#%% Codigos essenciais para Introdução ao Python

# Esse script faz referência ao (1) Script Introdução a Python e ao (3) Script Tradutor de Comentários usado nas aula I II III.




#%%                 AULA 1 INTRODUÇÃO AO PYTHON DENTRO DA IDE SPYDER - LINHA 8 a 182

#%% Explicacoes Basicas.

# O elemento #%% utilizado tem o objetivo de organizar o script
# Cria células dentro do script
# Assim, é possível executar o conteúdo daquela célula com "shift + enter"
# Para executar apenas uma linha ou uma seleção, utilize o F9
# Antes de importar pacotes, é importante ter instalado usando pip install e o nome do pacote

#%% Importar os pacotes. Importante importar o pacote antes de rodar o Python.

import pandas as pd
import numpy as np
import math
import seaborn as sns
import plotly
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'browser'
import plotly.graph_objects as go


#%% Pacotes mais complexos.

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.metrics import make_scorer, roc_auc_score
import lightgbm as lgb
import time

#%% Funcoes matematicas basicas.

print(5 + 10)
print(20 - 6)
print(30 * 3)
print(200 / 10)
print(5 ** 3)

# A função math.sqrt() retorna a raiz quadrada e print() printa o resultado.
# Apertar Ctrl I em cima da função pode dar mais detalhes.

print(np.sqrt(144))
print(math.sqrt(144))

#%% Criando objetos. Objetos sao listas criadas para analise. Para criar os objetos utilizamos o indicador = para a atribuicoes.

lista_numeros = [1,2,3,4,5,6,7,8,9,10]

print(lista_numeros)

lista_textos = ['Brasil', 'Argentina', 'Chile', 'Peru', 'Uruguai']

# Somando os elementos que estao dentro da lista criada.

print(lista_numeros[0] + lista_numeros[3])

print(lista_textos[0] + ' e ' + lista_textos[1])

#%% Series - Numerico.

# Sao objetos muito utilizados em analise de dados. 
# As series mais simples sao numericas, de caracteres ou logicas.
# A partir de agora, sempre que usarmos o pandas será com o nome "pd".

numeros = pd.Series([10,20,30,40,50,60,70,80])
print(numeros)

#%% Series - Caracteres.

cores = pd.Series(["Vermelho", "Amarelo", "Azul", "Verde", "Roxo"])
print(cores)

#%% Series - Argumentos logicos.

logico = pd.Series([True, False, True, True, False, False])
print(logico)

#%% Classes (tipos) de objetos.

# Número inteiro ou "int"
print(type(1))

# Número com casas decimais "float"
print(type(2.75))

# Caracteres ou "string"
print(type("Azul"))

# Booleano (verdadeiro ou falso) ou "bool"
print(type(True))

# Uma Series que criamos por meio do pandas
print(type(cores))

#%% Comprimento dos objetos anteriormente criados ou seja, saber quantos "dados" tem dentro do objeto.

print(len(numeros))
print(len(cores))
print(len(logico))
print(len(lista_numeros))

#%% Criando uma sequência de números como o pacote np.

# Note que esta função "arange" inclui o número inicial, mas exclui o final.
# Se atribuir o mesmo nome a outro objeto, o objeto antigo é substituído.

sequencia_1 = np.arange(1, 10)
sequencia_2 = np.arange(1, 10, 0.5)
sequencia_1 = np.arange(1000, 2000)

#%% Series - Variados

# Existem Series que guardam informações de variadas classes.
# Neste caso, a série fica toda identificada como texto.

varios = pd.Series([10, 20, 30, "Azul", "Verde", "Vermelho", False, False, True])
print(varios)

#%% Comparações

# É possível realizar operações com as séries. A seguir, alguns exemplos usando o objeto "numeros":
    
# Igualdade:
print(numeros == 20)

# Multiplicaçao:
print(numeros * 2)

# Multiplicação e criação de objeto:
triplo_numeros = numeros * 3

# Divisão e criação de objeto:
metade_numeros = numeros / 2

#%% Comparando textos (verificando diferença).
print(cores != "Amarelo")

#%% Comparando números (maior).
print(sequencia_2 > 5)

#%% Comparando números (maior ou igual).
print(sequencia_2 >= 4.5)

#%% Comparando números (menor).
print(sequencia_1 < 1010)

#%% Comparando números (menor ou igual).
print(sequencia_1 <= 1003)

#%% Série com dados categórico, vulgo qualitativa.

tipos = pd.Series(["TipoA", "TipoB", "TipoB", "TipoA", "TipoC", "TipoB"], dtype="category")
print(tipos)

#%% Criando dicionario com {}.

dict_uf = {"estado": "SP",
          "regiao": "Sudeste"}

print(dict_uf["estado"])
print(dict_uf["regiao"])

dict_uf["pais"] = "Brasil"
print(dict_uf)

dict_gay = {"Victor": "Surubeiro",
            "Yuri": "Marmita de Casal",
            "Gui": "Drogado",
            "Luan": "Stalker",
            "Momii": "Trans que só fala bosta"}

print(dict_gay["Momii"])

#%%               AULA 2 INTRODUÇÃO AO PYTHON DENTRO DA IDE SPYDER - LINHA 183 a 616

#%% Criando um DataFrame com o panda. DataFrame sao basicamente uma tabela.

# Note que foi criado um objeto do tipo "DataFrame" no ambiente do Spyder.

dataset_1 = pd.DataFrame({'id':["obs_1", "obs_2", "obs_3"],
                         'idade':[60, 28, 53]})
print(dataset_1)


#%% Criando 3 variáveis para formar o DataFrame.

# Note que criamos um array pelo "numpy" e duas séries do "pandas".
# O None é a indicação do dado "não disponível", isto é, missing value (NA).
# Note que o None não é texto. São valores faltantes.

varA = np.arange(1,11)
varB = pd.Series([1,2,3,4,5,6,7,8,None,None])
varC = pd.Series(["a","b","c","d","e","f","g","h","i","j"])

# Vamos criar o banco de dados com nomes diferentes para as variáveis.

dataset_2 = pd.DataFrame({'variA': varA,
                           'variB' : varB,
                           'variC' : varC})

print (dataset_2)

#%% Importando Excel

# Inicialmente, vamos importar um arquivo em Excel
# Receita anual de vendas para 5 empresas ao longo de 6 anos (Fonte: CVM)
# Note que o pacote relevante para esta função é o pandas "pd"

receita = pd.read_excel("(2) receita_empresas.xlsx")

#%% Importando CSV

# Outro formato bastante comum é o (.csv)
# A seguir, vamos importar dados da OCDE sobre as notas dos países no PISA
# Fonte dos dados: https://pisadataexplorer.oecd.org/ide/idepisa/dataset.aspx
# Os argumentos adicionados nesta função foram:
# O separador (,) e a indicação de decimais (.)

notas_pisa = pd.read_csv("(2) notas_pisa.csv", sep=",", decimal=".")

#%% Link

# Uma ferramenta útil é a coleta dos dados diretamente nos links (APIs)
# Exemplo: Banco Central do Brasil
# Variação mensal do índice nacional de preços ao consumidor amplo (IPCA)
# Argumentos: indicação do link, separador das variáveis (;) e decimais (,)

ipca = pd.read_csv("https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=csv&dataInicial=01/01/2022&dataFinal=30/09/2024",
                   sep=";", decimal=",")

#%% Exportando os dados que foram tratados no Python para Excel ou CSV

# Aqui estamos configurando para exportar sem o index
# Os arquivos serão salvos no Projeto que você está usando no momento

dataset_1.to_csv("dataset1.csv", index=False)

dataset_2.to_excel("dataset2.xlsx", index=False)

#%% Funções e iterações

# Uma função é uma forma de simplificar um código
# É adequada sempre que for necessário repetir o mesmo código várias vezes
# Funções automatizam tarefas que seriam repetitivas
# Funções e iterações são ferramentas que podem facilitar a escrita dos algoritmos

# Reduzir a duplicidade de códigos é importante, pois:
# Facilita a visualização (leitura do código)
# Facilita a mudança do código, caso necessário
# Evita erros durante a duplicação do código

# Para criar uma função, existem três etapas básicas:
# 1. Nomear a função
# 2. Indicar os argumentos (inputs) que são utilizados na função
# 3. Indicar o código que será implementado dentro do corpo da função

#%% Função com input único

# Exemplo: vamos criar uma função que transforme milhas para quilômetros

def converter(milha):
    km = (milha * 1.6093)
    return km

def converter(fahrenheit):
    C = (fahrenheit - 32) * 5 / 9
    return C
          
def converter(celsius):
    F = (celsius * 1.8 ) + 32
    return F

# Testando a função

# A função foi nomeada de "converter" e é assim que a chamaremos
# O input é o que nomeamos de "milha", isto é, o valor que vamos converter
# O "km" é o nome que demos ao código que será implementado
# O "return" é o que queremos que a função faça, retorne o valor convertido

print(converter(60))
print(converter(100))
print(converter(20))
print(converter(30))

#%% É possível criar uma série com todos os valores

# Em seguida, a série entra como input na função para retornar todos os valores

diversos_valores = pd.Series([10,20,30,40,50,60])

print(converter(diversos_valores))

# Podemos armazenar os resultados em um objeto

valores_convertidos = converter(diversos_valores)

#%% Função com vários inputs

# Vamos criar uma função que calcule a área de um retângulo 
# Os dois inputs necessários são a base (b) e a altura (h) em metros
# O f e o m² = ( Alt + Ctrl + 2 ) é só para florear o resultado

def calcular_area(b, h):
  area = (b * h)
  return area

# Testando a função

print(f"{calcular_area(10, 10)}m²")
print(f"{calcular_area(20, 15)}m²")
print(f"{calcular_area(50, 30)}m²")

#%% Criando condicoes com If.

# Neste contexto de funções, as condições "if, elif e else" são importantes
# Primeiramente, estabelecemos a condição
# Logo após, no primeiro print() vamos estabelecer o resultado caso if == TRUE
# Na sequência, estabelecemos o else, ou seja, o restante caso if == FALSE
# Assim, o segundo print() indica o que retornar se a condição não for atendida

valor = 100

if valor == 10**2:
    print("Valor Correto")
else:
    print("Valor Incorreto")

# Multiplos if + elif

salario = 2500

if salario <= 1412:
  print("Até 1 salário mínimo")
elif salario > 1412 and salario <= 4236:
  print("Entre de 1 e 3 salários mínimos")
elif salario > 4236 and salario <= 7060:
  print("Entre 3 e 5 salários mínimos")
else:
  print("Mais de 5 salários mínimos")
  
# Exemplo Allan

from datetime import datetime

data_e_hora_atuais = datetime.now()
data_atual = date.today()

import datetime

dia = datetime.date.today().day
ano = datetime.date.today().year
mês = datetime.date.today().month
dia_semana = datetime.date.today().isoweekday()

print(dia_semana)
 
if dia_semana == 0:
  print("Provavelmente Namorando")
elif dia_semana == 2:
  print("Início do Término")
elif dia_semana == 4:
  print("Provavelmente Solteiro")
elif dia_semana == 6:
  print("Pensando em tentar fazer dar certo DE NOVO")
else:
  print("Namorando mas com DR")

#%% Funções e condições

# É possível integrar condições ("if") às funções apresentadas anteriormente
# Voltando ao exemplo, vamos calcular a quantidade exata de salários mínimos
# Porém, a função só retornará o valor exato até o limite de 10 salários
# Acima deste limite, a função indicará uma mensagem

# Adicionamos o if (condição) e o que retornar quando for satisfeita
# Na sequência, o else e o que retornar quando NÃO for satisfeita

def quantidade_salarios(salario):
    
    quantidade = (salario/1412)
    
    if quantidade <= 10:
        return quantidade
    else:
        return("Mais de 10 salários mínimos")
    
# Testando a função

print(quantidade_salarios(1412))
print(quantidade_salarios(3000))
print(quantidade_salarios(14120))
print(quantidade_salarios(15000))    

#%% Vários inputs e múltiplas condições

def nova_area(b, h):
    
    calculo_area = (b * h) # inserir b e h em metros
    
    if calculo_area <= 10000:
        return calculo_area, "Até 1 hectare"
    elif calculo_area > 10000 and calculo_area <= 50000:
        return calculo_area, "Entre 1 e 5 hectares"
    else:
        return calculo_area, "Mais de 5 hectares"

# Testando a função

print(nova_area(300, 25))
print(nova_area(200,100))
print(nova_area(500, 300))    

#%% Integrando novas funções e códigos existentes

# Vamos criar uma função que calcula o coeficiente de variação da variável
# Std = Desvio Padrao, Mean = Média

def coef_var(x):
  coeficiente = (np.std(x) / np.mean(x)) * 100
  return np.round(coeficiente, decimals=3)

# Calculando a média de um objeto e criando um objeto com o resultado

print(np.mean(variavel_cv))

media_variavel_cv = np.mean(variavel_cv)

# Pegando a variável de um dos DataFrames e aplicando o coef_var

coef_var(receita['receita'])
print(np.mean(receita['receita']))

# Extraindo o Dataframe receita para verificar se o média foi calculada
# Ao exportar em xlsx as colunas já vem separadas ao contrário de csv

receita.to_csv("receita.csv", index=False)
receita.to_excel("receita.xlsx", index=False)

# Testando a função

variavel_cv = pd.Series([10, 25, 40, 35, 15, 28, 31])

print(f"{coef_var(variavel_cv)}%")

#%% Iterações: "for"

# Na conversão de milhas para quilômetros, podemos usar o "for" em uma série

lista_conversao = pd.Series([60, 100, 20, 30])

# Gerando uma lista vazia para os resultados

lista_km = []

# Desenvolvendo a iteração

for i in lista_conversao:
    lista_km.append(i * 1.6093)
    
# Esta função faz a conversão de valores e guarda na lista que estava vazia

print(lista_km)

#%% Iterações: "while"

# O while permite que seja adicionada a condição do tipo "enquanto" à iteração
# Vamos avaliar a evolução de R$100 investidos à taxa de juros de 10% aa
# A capitalização ocorrerá até quando o montante capitalizado for menor que R$10.000

saldo_investimento = 100

# Gerando uma lista vazia para os resultados

lista_invest = []
    
while saldo_investimento < 10000:
    saldo_investimento = (saldo_investimento*1.10)
    lista_invest.append(saldo_investimento)

print(lista_invest)

# Apenas para ajustar a lista com o valor inicial do investimento

lista_invest.insert(0, 100)

#%% Tradução de Textos

pip install googletrans==4.0.0-rc1

from googletrans import Translator
import time

#%% Indicar o texto que deverá ser traduzido

# Nota: manter as aspas (""") no início e fim (o texto deve ficar entre elas)

translator = Translator()

code = """

#%% Numérico

# Na função a seguir, note que é comum atribuir apelidos aos pacotes "pd"
# A partir de agora, sempre que usarmos o pandas será com o nome "pd"
# Na sequência, indicamos a função "Series" que está no pacote "pd"

numeros = pd.Series([10,20,30,40,50,60,70,80])

print(numeros)

"""
#%% Definindo a função (se necessário, alterar o idioma destino na linha 36)

def translate_comment(comment, translator, retries=5, delay=2):
    for attempt in range(retries):
        try:
            translated_comment = translator.translate(comment,
                                                      src='portuguese', dest='japanese').text
            return translated_comment
        except Exception as e:
            print(f"Erro ao traduzir: {e}. Tentativa {attempt + 1} de {retries}.")
            time.sleep(delay)
    return comment

def translate_comments(code, translator):
    lines = code.split('\n')
    translated_code = []
    for line in lines:
        if '#' in line:
            code_part, comment_part = line.split('#', 1)
            translated_comment = translate_comment(comment_part.strip(), translator)
            translated_code.append(f"{code_part.strip()} # {translated_comment}")
        else:
            translated_code.append(line)
    return '\n'.join(translated_code)

#%% Gerando a tradução

translated_code = translate_comments(code, translator)
print(translated_code)

#%% Outra forma de tradução

pip install deep-translator

from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source="pt", target="chinese")

texto = "Oi idiotas"

traducao = tradutor.translate(texto)

#%% Importando um banco de dados

# Na grande maioria dos casos, as bases de dados precisam ser preparadas
# Vamos utilizar a base de dados com notas do PISA (Programa Internacional de Avaliação de Alunos)
# Fonte: https://pisadataexplorer.oecd.org/ide/idepisa/report.aspx

pisa = pd.read_csv("(2) notas_pisa.csv", delimiter=",")

#%% Visualizar os dados

# Vamos olhar apenas a parte inicial do banco de dados (5 primeiras linhas)
print(pisa.head(5))

# Quais são os nomes das variáveis disponíveis?
print(pisa.columns)
lista_variaveis = pisa.columns

# Informações mais detalhadas das variáveis do banco de dados
print(pisa.info())

#%% Tamanho do banco de dados

# Quantas observações (linhas) existem no banco de dados
print(pisa.shape[0])

# Quantas variáveis (colunas) existem no banco de dados
print(pisa.shape[1])

# Quantas observações e variáveis existem no banco de dados
print(pisa.shape)

#%% Selecionando variáveis

# Vamos especificar nomes de variáveis do banco de dados
print(pisa['country'])

# Podemos armazenar a variável especificada em um novo objeto
paises_pisa = pisa['country']

# Também poderíamos armazenar mais de uma variável em um novo objeto
pisa_reading_2018 = pisa[['country', 'reading_2018']]

#%% Removendo variáveis sem uso

# Por exemplo, supondo que não vamos avaliar as variáveis no ano de 2018
pisa_2022 = pisa.drop(columns=['mathematics_2018', 'reading_2018', 'science_2018'])

# O argumento inplace=True pode ser usado para reescrever o objeto existente
pisa_2022.drop(columns=['group'], inplace=True)

# Para remover um objeto do ambiente, pode ser feito da seguinte forma
del pisa_reading_2018


#%%               AULA 3 INTRODUÇÃO AO PYTHON DENTRO DA IDE SPYDER - LINHA 617 a 1109

#%% Identificando elementos específicos por posição

# O primeiro argumento é o número da linha (index)
# O segundo argumento é a posição da coluna
# Nota: tanto o index quanto as colunas começam contagem do zero no pandas

# Qual é a nota de matemática em 2022 para o Brasil?
print(pisa.iloc[46, 2])

# Quais são os valores de todas as variáveis para o Japão?
print(pisa.iloc[19,])

# Quais são os valores de todas as variáveis para os países de index de 0 a 6?
print(pisa.iloc[0:7, ])

# Selecionar as variáveis que estão nas posições 0, 2 e 5
pisa_matematica = pisa.iloc[:, [0,2,5]]

# Selecionar as variáveis que estão nas posições de 0 até 2. Necessário adicionar uma posição a mais no final!
pisa_matematica = pisa.iloc[:, 0:3]

#%% Reorganizando a posição das variáveis

# Vamos selecionar algumas variáveis e trocar a ordem delas. Axis = 1 é alteração nas colunas.
pisa_2022_ajuste = pisa.reindex(['group','country', 'science_2022', 'mathematics_2022', 'reading_2022'], axis=1)

#%% Excluindo algumas observações com base no index

# Supondo que não vamos analisar os países de index 38 até 95. Lembrando de adicionar uma posição a mais no final
pisa_ocde = pisa.drop(pisa.index[38:96])

#%% Detalhando as manipulações de dados

# O banco de dados em análise tem um problema:
# As variáveis de notas, que deveriam ser métricas, estão como textos "object"

# Ajustando variáveis:
# Neste caso, utilizaremos a função "to_numeric"
# Os missings serão ajustados pelo coerce e serão substituídos por nan

pisa['mathematics_2022'] = pd.to_numeric(pisa['mathematics_2022'], errors='coerce')
pisa['reading_2022'] = pd.to_numeric(pisa['reading_2022'], errors='coerce')
pisa['science_2022'] = pd.to_numeric(pisa['science_2022'], errors='coerce')

pisa['mathematics_2018'] = pd.to_numeric(pisa['mathematics_2018'], errors='coerce')
pisa['reading_2018'] = pd.to_numeric(pisa['reading_2018'], errors='coerce')
pisa['science_2018'] = pd.to_numeric(pisa['science_2018'], errors='coerce')

print(pisa.info())

#%% Excluindo linhas com dados faltantes

# É possível eliminar as observações que apresentem valores faltantes
pisa_na = pisa.dropna()

# Pegando só o Brasil
brazil = pisa.iloc[46,]

#%% Gerando estatísticas descritivas

# Tabela de estatísticas descritivas para variáveis QUANTITATIVAS
pisa[['mathematics_2022', 'reading_2022', 'science_2022']].describe()

# Tabela de frequências para variável QUALITATIVAS
pisa['group'].value_counts()

#%% Filtrando observações por meio de operadores

# É possível filtrar observações por meio dos operadores:
# Alguns operadores úteis para realizar filtros:

# "== igual"
# "> maior"
# ">= maior ou igual"
# "< menor"
# "<= menor ou igual"
# "!= diferente"
# "& indica e"
# "| indica ou"

#%% Exemplos de Filtros:

# Nota de matemática no ano de 2022 maior do que 437
print(pisa[pisa['mathematics_2022'] > 437])
acima_media_mat_2022 = pisa[pisa['mathematics_2022'] > 437] # salvando objeto

# Somente países no grupo da OECD
print(pisa[pisa['group'] == 'OECD'])

# Países no grupo da OECD e com nota em ciências no ano de 2022 menor ou igual a 493
print(pisa[(pisa['group'] == 'OECD') & (pisa['science_2022'] <= 493)])

# Países que não sejam classificados no grupo da OECD
print(pisa[pisa['group'] != 'OECD'])

# Nota em leitura no ano de 2022 menor do que 386 ou maior do que 480
print(pisa[(pisa['reading_2022'] < 386) | (pisa['reading_2022'] > 480)])
extremos_leitura = (pisa[(pisa['reading_2022'] < 386) | (pisa['reading_2022'] > 480)])

#%% Agrupamento dos dados por algum critério

# Agrupando os dados pelo método groupby
pisa_grupo = pisa.groupby(by=['group'])

# O pisa_grupo está agrupado e não pode mais ser manipulado como antes
# As informações serão extraídas com base no critério de agrupamento

pisa_grupo.describe().T # o comando .T apenas fez a transposição da tabela


#%% Organizando o dataset com base em critérios

# É possível ordenar as observações com base nos valores das variáveis

# Em ordem decrescente
sort_matem = pisa.sort_values(by=['mathematics_2022'], ascending=False)

# Em ordem crescente
sort_ciencias = pisa.sort_values(by=['science_2022'], ascending=True)


#%% Também poderíamos alterar os nomes das variáveis

nomes = ["pais",
         "grupo",
         "matematica_2022",
         "leitura_2022",
         "ciencias_2022",
         "matematica_2018",
         "leitura_2018",
         "ciencias_2018"]

pisa.columns = nomes
print(pisa.info())

# Para trocar apenas um nome:
pisa = pisa.rename(columns={'grupo':'grupo_paises'})
print(pisa.info())

#%%                                                   GRÁFICOS

#%% Gráfico de barras para contagem

# Para a análise, vamos importar o banco de dados de uma empresa comercial
# Fonte: adaptado de https://www.kaggle.com/datasets/apoorvaappz/global-super-store-dataset
comercio = pd.read_excel("(2) comercio_global.xlsx")

# Vamos iniciar por uma variável qualitativa, o mercado onde ocorreu a venda 
# Como é variável categórica, vamos criar um gráfico de contagem (countplot)
# Neste caso, o gráfico apresentará a contagem em cada categoria da variável
plt.figure(figsize=(15,9), dpi = 600)
sns.countplot(data=comercio, x="market")

# Podemos escolher a ordem de apresentação reorganizando os níveis da variável
plt.figure(figsize=(15,9), dpi = 600)
sns.countplot(data=comercio, x="market", order=["APAC", "LATAM", "EU", "US", "Africa", "EMEA", "Canada"])

# Vamos adicionar algumas formatações ao gráfico básico
plt.figure(figsize=(15,9), dpi = 600)
sns.countplot(data=comercio, x="market", order=["APAC", "LATAM", "EU", "US", "Africa", "EMEA", "Canada"])
plt.title("Análise por Mercado",fontsize=20)
plt.xlabel('Mercado',fontsize=15)
plt.ylabel('Conatgem',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Podemos trocar as cores das barras
plt.figure(figsize=(15,9), dpi = 600)
sns.countplot(data=comercio, x="market", order=["APAC", "LATAM", "EU", "US", "Africa", "EMEA", "Canada"], color="blue")
plt.title("Análise por Mercado",fontsize=20)
plt.xlabel('Mercado',fontsize=15)
plt.ylabel('Conatgem',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Conhecendo algumas paletas de cores do seaborn

# Paleta bright
palette = sns.color_palette("bright")
sns.palplot(palette)

# Paleta viridis
palette = sns.color_palette("viridis")
sns.palplot(palette)

# Paleta Paired
palette = sns.color_palette("Paired")
sns.palplot(palette)

# Paleta Rocket
palette = sns.color_palette("rocket")
sns.palplot(palette)

# Vamos alterar o tema do gráfico e adicionar as contagens
# Argumento hue coloca cor em cada mercado e palette para escolher as paletas
# Ax container serve pra mostrar os números em cima da barra
plt.figure(figsize=(15,9), dpi = 600)
ax = sns.countplot(data=comercio, x="market", hue="market", order=["APAC", "LATAM", "EU", "US", "Africa", "EMEA", "Canada"], palette='viridis', legend=False)
for container in ax.containers: ax.bar_label(container, fontsize=12)
plt.title("Análise por Mercado",fontsize=20)
plt.xlabel('Mercado',fontsize=15)
plt.ylabel('Conatgem',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Também poderíamos apresentar o gráfico com os eixos invertidos (var no Y)
plt.figure(figsize=(15,9), dpi = 600)
ax = sns.countplot(data=comercio, y="market", hue="market",
                   order = comercio['market'].value_counts(ascending=False).index,
                   palette = 'viridis', legend=False)
for container in ax.containers: ax.bar_label(container, padding=1, fontsize=12)
plt.title("Análise por Mercado",fontsize=20)
plt.xlabel('Contagem',fontsize=15)
plt.ylabel('Mercado',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Vamos ajustar os dados de interesse gerando uma média por grupo
comercio_agrupado = comercio[['category', 'profit']].groupby(by=['category']).mean()
comercio_agrupado = comercio_agrupado.sort_values(by=['profit'], ascending=False).reset_index()

# Gerando o gráfico de barras
# Padding é a distancia do numero pra barrae % 2f é a porcentagem com quantas casas decimais quer.
plt.figure(figsize=(15,9), dpi = 600)
ax1 = sns.barplot(data=comercio_agrupado, x='category', y='profit', hue='category', palette='rocket')
for container in ax1.containers: ax1.bar_label(container, fmt='%.2f', padding=3, fontsize=12)
plt.title("Lucro Médio por Categoria",fontsize=20)
plt.xlabel('Categorias',fontsize=15)
plt.ylabel('Lucro',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

#%% Gráfico Pizza de Setores

# Gerando os dados de interesse. Normalize tranforma freq absoluta em relati totalizando 100%.
pizza = pd.crosstab(index = comercio['segment'], columns = 'segmento', normalize = True).sort_values('segmento', ascending = False)

# Plotando o gráfico
plt.figure(figsize=(15,9), dpi = 600)
plt.pie(pizza['segmento'], 
        labels = pizza.index, 
        colors = sns.color_palette('pastel'), 
        autopct='%.0f%%', # nº de casas decimais 
        textprops={'fontsize': 20}, # tamanho da fonte
        pctdistance = 0.6) # posição dos percentuais
plt.title('Análise por Segmento',fontsize=20)
plt.show()

#%% Histograma

# A seguir, vamos elaborar o histograma do valor das vendas
plt.figure(figsize=(15,9), dpi = 600)
sns.histplot(data=comercio, x="sales", bins=50)
plt.xlabel('Valor das Vendas',fontsize=15)
plt.ylabel('Frequência',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Visualizando apenas um trecho da distribuição da variável
hist_vendas = comercio[comercio['sales'] < 1000]

plt.figure(figsize=(15,9), dpi = 600)
sns.histplot(data=hist_vendas, x="sales", bins=30)
plt.xlabel('Valor das Vendas',fontsize=15)
plt.ylabel('Frequência',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Detalhando um pouco mais o gráfico
# bins=range significa q o gráfico vai de 0 a 1000 variando de 100 em 100
plt.figure(figsize=(15,9), dpi = 600)
ax2 = sns.histplot(data = hist_vendas, x = "sales", bins=range(0,1100,100), color='blue', alpha=0.6, kde=True)
ax2.bar_label(ax2.containers[0], fontsize=12)
plt.xlabel('Valor das Vendas',fontsize=15)
plt.xticks(ticks=np.arange(0,1100,100))
plt.ylabel('Frequência',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

#%% Gráfico de pontos - Scatterplot

# Vamos elaborar um gráfico de dispersão dos pontos
# Os dados são do atlas ambiental sobre distritos da cidade de São Paulo
atlas_ambiental = pd.read_excel("(2) atlas_ambiental.xlsx")

# Iniciando com o gráfico básico (scatterplot)
# Neste caso, devemos especificar as variáveis dos eixos x e y
plt.figure(figsize=(15,9), dpi = 600)
sns.scatterplot(data=atlas_ambiental, x="renda", y="escolaridade")

# Como há variáveis nos dois eixos, podemos adicionar outras variáveis:
# Na forma de tamanho dos pontos ("size")
plt.figure(figsize=(15,9), dpi = 600)
sns.scatterplot(data=atlas_ambiental, x="renda", y="escolaridade", size="idade")
plt.title("Indicadores dos Distritos do Município de São Paulo",fontsize=20)
plt.xlabel('Renda',fontsize=15)
plt.ylabel('Escolaridade',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Vamos criar uma nova variável indicando "favel" acima ou abaixo da média
print(atlas_ambiental['favel'].mean())

atlas_ambiental.loc[atlas_ambiental['favel']<5.93, "indica_favel"] = "Abaixo"
atlas_ambiental.loc[atlas_ambiental['favel']>=5.93, "indica_favel"] = "Acima"

# Vamos adicionar a variável que será indicada pela cor dos pontos ("hue")
plt.figure(figsize=(15,9), dpi = 600)
sns.scatterplot(data=atlas_ambiental, x="renda", y="escolaridade", size="idade", hue="indica_favel")
plt.title("Indicadores dos Distritos do Município de São Paulo",fontsize=20)
plt.xlabel('Renda',fontsize=15)
plt.ylabel('Escolaridade',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Vamos criar outra variável indicando "mortalidade" acima ou abaixo da média
print(atlas_ambiental['mortalidade'].mean())

atlas_ambiental.loc[atlas_ambiental['mortalidade'] < 15.99, "mort"] = "Abaixo"
atlas_ambiental.loc[atlas_ambiental['mortalidade'] >= 15.99, "mort"] = "Acima"

# Vamos adicionar a variável que será indicada pelo tipo dos pontos ("style")
plt.figure(figsize=(15,9), dpi = 600)
sns.scatterplot(data=atlas_ambiental, x="renda", y="escolaridade", size="idade", hue="indica_favel", style="mort")
plt.title("Indicadores dos Distritos do Município de São Paulo",fontsize=20)
plt.xlabel('Renda',fontsize=15)
plt.ylabel('Escolaridade',fontsize=15)
plt.legend(bbox_to_anchor=(1,1), fontsize=9)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Caso queira verificar graficamente o ajuste linear à nuvem de pontos
plt.figure(figsize=(15,9), dpi = 600)
sns.regplot(data=atlas_ambiental, x="renda", y="escolaridade", ci=None)
plt.title("Indicadores dos Distritos do Município de São Paulo",fontsize=20)
plt.xlabel('Renda',fontsize=15)
plt.ylabel('Escolaridade',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

#%% Gráfico de linhas

# Vamos elaborar um gráfico de linhas (lineplot) para dados ao longo do tempo
# Vamos utilizar o banco de dados com as receitas de vendas das empresas
receita = pd.read_excel("(2) receita_empresas.xlsx")

# Como temos 5 empresas no banco de dados, vamos implementar o seguinte gráfico
# Vamos separar cada empresa por meio da cor da linha
plt.figure(figsize=(15,9), dpi = 600)
sns.lineplot(data=receita, x="ano", y="receita", hue="id_empresa")

# Vamos formatar um pouco mais o gráfico
plt.figure(figsize=(15,9), dpi = 600)
sns.lineplot(data=receita, x="ano", y="receita", hue="id_empresa", marker="o")
plt.title("Receita de Vendas",fontsize=20)
plt.xlabel('Ano',fontsize=15)
plt.ylabel('Receita Anual de Vendas',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(title='Empresa', loc='upper left', fontsize=12)
plt.show()

# A seguir, vamos elaborar um gráfico interativo
# Elaborando o gráfico

fig_line = px.line(receita, 
                   x='ano', 
                   y='receita', 
                   color='id_empresa', 
                   markers=True, 
                   title='Receita de Vendas',
                   labels={"ano": "Ano",
                           "receita": "Receita Anual de Vendas",
                           "id_empresa": "Empresa"})

fig_line.show()

# Salvando a figura
fig_line.write_html('grafico_linhas.html')

#%% Gráfico de calor

# Vamos gerar um gráfico de calor que distingue informações por meio de cores
# O banco de dados contém informações sobre a quantidade vendida em 3 produtos
vendas_regional = pd.read_excel("(2) vendas_regiao.xlsx")

# Inicialmente, vamos selecionar as variáveis quantitativas do banco de dados
vendas_reg = vendas_regional[['produtoA','produtoB','produtoC']]

# Vamos gerar o gráfico de calor no contexto das correlações entre variáveis
# Portanto, primeiramente, vamos criar a matriz de correlações de Pearson
# Lembrando: selecionar apenas as variáveis quantitativas da base de dados
corr = vendas_reg.corr()

# Vamos elaborar um gráfico de calor (heatmap) com o plotly
fig_heat = go.Figure()

fig_heat.add_trace(
    go.Heatmap(
        x = corr.columns,
        y = corr.index,
        z = np.array(corr),
        text=corr.values,
        texttemplate='%{text:.2f}',
        colorscale='ice'))

fig_heat.update_layout(
    height = 600,
    width = 600)

fig_heat.show()

# Salvando a figura
fig_heat.write_html('grafico_calor.html')

# Algumas opções de colorscale:
    # solar
    # viridis
    # speed
    # blues
    # oranges

#%% Gráficos Boxplot

# O boxplot apresenta medidas de posição das variáveis
# Mínimo, máximo, 1º quartil, mediana e 3º quartil
# Vemos a distribuição dos dados nas variáveis e eventuais outliers univariados
# Inicialmente, vamos apresentar o boxplot de uma única variável

# Importando o banco de dados
vendas_regional = pd.read_excel("(2) vendas_regiao.xlsx")

plt.figure(figsize=(15,9), dpi = 600)
sns.boxplot(data=vendas_regional, y='produtoA', width = 0.5, color = "lightblue")
plt.xlabel('Produto A',fontsize=15)
plt.ylabel('Valores',fontsize=15)
plt.show()

# Poderíamos fazer vários boxplot em um mesmo gráfico
var_boxplot = vendas_regional[['produtoA', 'produtoB', 'produtoC']]

plt.figure(figsize=(15,9), dpi = 600)
sns.boxplot(data=var_boxplot, width = 0.6, palette='rocket')
plt.xlabel('Produtos',fontsize=15)
plt.ylabel('Valores',fontsize=15)
plt.show()

# Vamos torná-lo mais informativo
fig_box = px.box(var_boxplot,
                 width = 900)

fig_box.update_layout(title='BOXPLOT',
                      xaxis_title='Produtos',
                      yaxis_title='Valores',
                      plot_bgcolor='lightblue')

fig_box.show()

# Salvando a figura

fig_box.write_html('grafico_boxplot.html')

#%% Pairplot

# O pairplot permite analisar relações entre pares de variáveis
# O resultado é uma matriz de gráficos
# Importando o banco de dados
atlas_ambiental = pd.read_excel("(2) atlas_ambiental.xlsx")

sns.set(rc={"figure.dpi":600})
sns.pairplot(data=atlas_ambiental.iloc[:,[2,4,5]])

# Poderíamos adicionar uma variável categórica por meio de cores:
atlas_ambiental.loc[atlas_ambiental['mortalidade'] < 15.99, "mort"] = "Abaixo"
atlas_ambiental.loc[atlas_ambiental['mortalidade'] >= 15.99, "mort"] = "Acima"

sns.set(rc={"figure.dpi":600})
sns.pairplot(data=atlas_ambiental.iloc[:,[2,4,5,11]], hue='mort')
plt.savefig('grafico_pairplot.png')