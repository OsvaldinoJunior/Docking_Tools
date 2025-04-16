import os

def remove_parenteses(diretorio):
    # Listar arquivos no diretório
    arquivos = os.listdir(diretorio)

    for nome_arquivo in arquivos:
        # Construir o caminho completo do arquivo
        caminho_atual = os.path.join(diretorio, nome_arquivo)

        # Verificar se é um arquivo
        if os.path.isfile(caminho_atual):
            # Remover parênteses do nome do arquivo
            novo_nome = nome_arquivo.replace("(", "").replace(")", "")

            # Construir o novo caminho do arquivo
            novo_caminho = os.path.join(diretorio, novo_nome)

            # Renomear o arquivo
            os.rename(caminho_atual, novo_caminho)

if __name__ == "__main__":
    # Substitua 'caminho/do/seu/diretorio' pelo caminho real do seu diretório
    caminho_do_diretorio = '/home/instala/Documentos/Osvaldino/docking_plip/1_recep_n_lig_1_caixa/melhores_candidatos_ligs'
    remove_parenteses(caminho_do_diretorio)