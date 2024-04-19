def guardar_arquivo(nome): #Guarda o nome do último arquivo .txt criado
    arq = open('GuardarArquivo.txt', 'w')
    arq.write(nome)
    return nome


def escrever(txt=''): #Escreve o que desejar no último arquivo .txt criado
    arq = open(f'{nome_arquivo()}', 'r')
    analise = arq.readlines()
    analise = len(analise)
    arq = open(f'{nome_arquivo()}', 'a+t')
    if analise > 0:
        arq.write(f'\n{txt}')
    else:
        arq.write(txt)


def criar_arq(name): #Cria o arquivo com o nome .txt escolhido
    arq = open(f'{name}.txt', 'w')
    guardar_arquivo(name)
    return True


def nome_arquivo():#Pega o nome do último arquivo .txt criado
    try:
        arq = open('GuardarArquivo.txt', 'r+t')
        dados = arq.readlines()
        dados = ''.join(dados)
        try:
            dados = dados.replace('\n', '')
        except:
            dados = dados
        return F'{dados}.txt'
    except:
        arq = open('GuardarArquivo.txt', 'w+')
        dados = arq.readlines()
        dados = ''.join(dados)
        try:
            dados = dados.replace('\n', '')
        except:
            dados = dados
        return F'{dados}.txt'


def mostrar_arq(): #Retorna os itens de dentro do último arquivo .txt criado.
    try:
        arq = open(f'{nome_arquivo()}', 'r+')
        dados = arq.readlines()
        dados = ''.join(dados)
        return dados
    except:
        return 'Arquivo não encontrado'


def apagar(indicie): #Apaga um item no índicie escolhido
    arq = open(f'{nome_arquivo()}', 'r')
    info = arq.readlines()
    palavra_apagar = info.pop(indicie)
    guardar_apagado(palavra_apagar)
    arq.close()
    arq = open(f'{nome_arquivo()}', 'w+')
    for i in info:
        arq.write(i)
    return palavra_apagar


def guardar_apagado(item=None, reescrever=False): # Guarda as palavras apagadas e reescreve-as quando desejado enquanto a janela não for fechada.
    if reescrever is False:
        try:
            arq = open('reescrever.txt', 'r+')
        except:
            arq = open('reescrever.txt', 'w+')
            arq.close()
            arq = open('reescrever.txt', 'r+')
        analise = arq.readlines()
        analise = len(analise)
        if analise > 0:
            arq.write(f'\n{item}')
        else:
            arq.write(item)
        return None
    else:
        try:
            arq = open('reescrever.txt', 'r+')
        except:
            arq = open('reescrever.txt', 'w+')
            arq.close()
            arq = open('reescrever.txt', 'r+')
        analise = arq.readlines()

        try:
            palavra = analise.pop()
            arq.close()
            arq = open('reescrever.txt', 'w+')
            for i in analise:
                i = i.replace('\n', '')
                arq.write(i)
            arq.close()
            palavra = palavra.replace('\n', '')
            escrever(palavra)
            return palavra
        except:
            return None
