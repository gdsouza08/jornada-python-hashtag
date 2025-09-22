import pyautogui as pa
import pandas as pd
import time

# Passo 1: Entrar no sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
time.sleep(2)
pa.press('win')
pa.write('google chorme')
time.sleep(2)
pa.press('enter')
time.sleep(2)
pa.hotkey('win', 'up')
pa.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pa.press('enter')
time.sleep(3)

# Passo 2: Fazer login
pa.click(x=851, y=499)
pa.write('teste@teste.com')
time.sleep(1)
pa.press('tab')
pa.write('minhasenhaforteaqui')
time.sleep(1)
pa.press('tab')
pa.press('enter')
time.sleep(2)

# Passo 3: Importar a base de dados
tabela = pd.read_csv('automacao\produtos.csv')
print(tabela)

# Passo 4: Cadastrar 1 produto  e # Passo 5: Repetir para todos os produtos
for linha in tabela.index: # para cada linha dentro das linhas da minha tabela
    pa.click(x=952, y=360)

    codigo = str(tabela.loc[linha, 'codigo'])
    pa.write(codigo)
    time.sleep(1)
    pa.press('tab')
    marca = str(tabela.loc[linha, 'marca'])
    pa.write(marca)
    time.sleep(1)
    pa.press('tab')
    tipo = str(tabela.loc[linha, 'tipo'])
    pa.write(tipo)
    time.sleep(1)
    pa.press('tab')
    categoria = str(tabela.loc[linha, 'categoria'])
    pa.write(categoria)
    time.sleep(1)
    pa.press('tab')
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pa.write(preco_unitario)
    time.sleep(1)
    pa.press('tab')
    custo = str(tabela.loc[linha, 'custo'])
    pa.write(custo)
    time.sleep(1)
    pa.press('tab')
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pa.write(obs)
    time.sleep(1)
    pa.press('tab')
    pa.press('enter')

    pa.scroll(10000)


