# Receptor_Ligantes_Caixas
# N_N_N_ Loop
# PART 1

#from openbabel import openbabel, pybel
import os
import re
import shutil
import openbabel
import subprocess
import pandas as pd

caminho_da_receptors = "/home/osvaldinojunior/Documents/Computational_Biology_Lab/all_molec/Multi_Recep" 
# caminho da pasta com os receptores

dirligs = "/home/osvaldinojunior/Documents/Computational_Biology_Lab/all_molec/10_mol"
# caminho da pasta com os melhores candidatos a ligantes

diresultados = "/home/osvaldinojunior/Documents/Computational_Biology_Lab/all_molec/10_multiple_results_"                     
# saída dos resultados para o usuário


# -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------
# POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------#POLICE LINE DO NOT CROSS#
# -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------
# POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------#POLICE LINE DO NOT CROSS#
# -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------
# POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------#POLICE LINE DO NOT CROSS#
# -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------
# POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------#POLICE LINE DO NOT CROSS#
# -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------
# POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------#POLICE LINE DO NOT CROSS#
# -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------
# POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------#POLICE LINE DO NOT CROSS#
# -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------
# POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------#POLICE LINE DO NOT CROSS#
# POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------#POLICE LINE DO NOT CROSS#
# -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------
# POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------#POLICE LINE DO NOT CROSS#
# -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------
# POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------#POLICE LINE DO NOT CROSS#
# -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------
# POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------#POLICE LINE DO NOT CROSS#
# -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------
# POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------#POLICE LINE DO NOT CROSS#
# -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------
# POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------#POLICE LINE DO NOT CROSS#
# -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------
# POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##-------  POLICE LINE DO NOT CROSS -------#POLICE LINE DO NOT CROSS#

#input para gerar opcional o arquivo de sessão do pymol
Pymol_session = input("deseja receber imagens dos resultados? (s/n) = ").strip().lower()
if Pymol_session == ("n"):
    no_yes_pymol = ""
elif Pymol_session == ("s"):
    no_yes_pymol = "-y"

# Loop para iterar sobre os arquivos na pasta
for nome_do_arquivo in os.listdir(caminho_da_receptors):
    caminho_recep_loop = os.path.join(caminho_da_receptors, nome_do_arquivo)

    # Verifica se o caminho é um arquivo (não é um diretório)
    if os.path.isfile(caminho_recep_loop):
        print(f"Executando código para o arquivo: {nome_do_arquivo}")
        
        dirrec = caminho_recep_loop
        
        criando_saida_results = os.path.join(diresultados, "RUNNING_PLIP_SETUP_WAIT_A_MOMENT")
        os.makedirs(criando_saida_results, exist_ok=True)

        criando_saida_convert = os.path.join(diresultados, f"{nome_do_arquivo}")
        os.makedirs(criando_saida_convert, exist_ok=True)

        def combinar_receptor_e_ligantes(dirrec, dirlig, diresultados):
            # Ler o conteúdo do arquivo receptor
            with open(os.path.join(dirrec), 'r') as receptor_file:
                conteudo_receptor = receptor_file.readlines()

            # Iterar sobre todas as pastas de ligantes no diretório
            for pasta_ligantes in os.listdir(dirlig):
                caminho_pasta_ligantes = os.path.join(dirlig, pasta_ligantes)

                if os.path.isdir(caminho_pasta_ligantes):
                    ligantes = [f for f in os.listdir(caminho_pasta_ligantes) if f.endswith('.pdbqt')]

                    for ligante in ligantes:
                        caminho_ligante = os.path.join(caminho_pasta_ligantes, ligante)

                        with open(caminho_ligante, 'r') as ligante_file:
                            conteudo_ligante = ligante_file.readlines()

                        conteudo_combinado = conteudo_ligante + conteudo_receptor

                        nome_pasta_saida = f"{pasta_ligantes}_{ligante.replace('.pdbqt', '')}"
                        caminho_pasta_saida = os.path.join(criando_saida_results, nome_pasta_saida)
                        os.makedirs(caminho_pasta_saida, exist_ok=True)

                        caminho_saida = os.path.join(caminho_pasta_saida, f"{pasta_ligantes}_{ligante}")

                        # Escrever o conteúdo combinado no arquivo de saída
                        with open(caminho_saida, 'w') as saida_file:
                            saida_file.writelines(conteudo_combinado)

        if __name__ == "__main__":
        
            caminho_do_diretorio_receptor = dirrec
            caminho_do_diretorio_ligantes = dirligs
            caminho_do_diretorio_saida = criando_saida_results

            combinar_receptor_e_ligantes(caminho_do_diretorio_receptor, caminho_do_diretorio_ligantes, caminho_do_diretorio_saida)

        ########################################################################################################################################
        ########################################################################################################################################
        ########################################################################################################################################

        # PART 2

        ########################################################################################################################################
        ########################################################################################################################################
        ########################################################################################################################################

        # Renomear removendo parênteses para conversão


        def remover_parenteses(nome):
            return nome.replace("(", "").replace(")", "")

        def renomear_pastas_e_arquivos(diretorio):
            
            pastas = [nome for nome in os.listdir(diretorio) if os.path.isdir(os.path.join(diretorio, nome))]

            for pasta in pastas:
                
                caminho_pasta = os.path.join(diretorio, pasta)

                novo_nome_pasta = remover_parenteses(pasta)
                novo_caminho_pasta = os.path.join(diretorio, novo_nome_pasta)

                os.rename(caminho_pasta, novo_caminho_pasta)

                arquivos = [nome for nome in os.listdir(novo_caminho_pasta) if os.path.isfile(os.path.join(novo_caminho_pasta, nome))]

                for arquivo in arquivos:
                    caminho_arquivo = os.path.join(novo_caminho_pasta, arquivo)

                    novo_nome_arquivo = remover_parenteses(arquivo)
                    novo_caminho_arquivo = os.path.join(novo_caminho_pasta, novo_nome_arquivo)

                    os.rename(caminho_arquivo, novo_caminho_arquivo)

        if __name__ == "__main__":
            caminho_do_diretorio = os.path.join(diresultados, criando_saida_results) 
            renomear_pastas_e_arquivos(caminho_do_diretorio)

        ########################################################################################################################################
        ########################################################################################################################################
        ########################################################################################################################################

        # PART 3

        ########################################################################################################################################
        ########################################################################################################################################
        ########################################################################################################################################

        # Tratamento de Dados

        def read_pdbqt(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()

            ligands = []
            current_model = []

            for line in lines:
                if line.startswith('MODEL'):
                    current_model = [line]
                elif line.startswith('ENDMDL'):
                    current_model.append(line)
                    ligands.append(current_model.copy())
                else:
                    current_model.append(line)

            return ligands

        def write_pdbqt(output_path, model):
            with open(output_path, 'w') as file:
                file.writelines(model)

        def add_receptor(lines, receptor_lines):
            return receptor_lines + lines

        def process_files_in_directory(directory):
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith('.pdbqt'):
                        file_path = os.path.join(root, file)
                        ligands = read_pdbqt(file_path)

                        # Extrair o modelo do receptor (o primeiro modelo)
                        receptor_model = ligands[0]

                        # Iterar sobre os ligantes e salvar cada combinação receptor + ligante
                        for i, ligand_model in enumerate(ligands[:]):  # Ignorar o primeiro modelo (receptor)
                            # Construir o nome do arquivo de saída
                            ligand_filename = f'{file.replace(".pdbqt", "")}_ligand_{i + 1}.pdbqt'
                            ligand_path = os.path.join(root, ligand_filename)

                            # Adicionar as linhas do receptor no início do modelo do ligante
                            combined_model = add_receptor(ligand_model, receptor_model)

                            # Salvar a combinação receptor + ligante em um novo arquivo PDBQT
                            write_pdbqt(ligand_path, combined_model)

        directory_path = criando_saida_results
        process_files_in_directory(directory_path)

        ########################################################################################################################################
        ########################################################################################################################################
        ########################################################################################################################################

        # PART 4

        ########################################################################################################################################
        ########################################################################################################################################
        ########################################################################################################################################

        # Separar ligantes

        def add_receptor_to_files(directory, receptor_path):
            with open(receptor_path, 'r') as receptor_file:
                receptor_lines = receptor_file.readlines()

            # Itera sobre todos os arquivos PDBQT no diretório
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith('.pdbqt'):
                        file_path = os.path.join(root, file)

                        with open(file_path, 'r') as pdbqt_file:
                            pdbqt_lines = pdbqt_file.readlines()

                        # Combina as linhas do receptor com as do arquivo PDBQT
                        combined_lines = receptor_lines + pdbqt_lines

                        # Salva o resultado no mesmo arquivo ou em um novo
                        with open(file_path, 'w') as output_file:
                            output_file.writelines(combined_lines)

        directory_path = criando_saida_results

        receptor_path = dirrec

        add_receptor_to_files(directory_path, receptor_path)

                                # Ajuste de um arquivo, tratamento 2

        def remove_model_sections(file_path):
            with open(file_path, 'r') as file:
                content = file.read()

            # Remova todos os blocos "MODEL 1" - "ENDMDL"
            pattern = re.compile(r'MODEL 1.*?ENDMDL', re.DOTALL)
            content = re.sub(pattern, '', content, count=1)

            with open(file_path, 'w') as file:
                file.write(content)

        def process_files_in_directory(directory):
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith('.pdbqt'):
                        file_path = os.path.join(root, file)
                        remove_model_sections(file_path)

        directory_path = criando_saida_results
        process_files_in_directory(directory_path)


        ########################################################################################################################################
        ########################################################################################################################################
        ########################################################################################################################################

        # PART 5

        ########################################################################################################################################
        ########################################################################################################################################
        ########################################################################################################################################

        # Organizar pastas I
        #import os
        #import shutil

        def copy_folders(source_directory, destination_directory):
            try:
                # Itera sobre os diretórios no diretório de origem
                for folder_name in os.listdir(source_directory):
                    source_folder = os.path.join(source_directory, folder_name)
                    
                    if os.path.isdir(source_folder):
                        destination_folder = os.path.join(destination_directory, folder_name)
                        
                        # Copia o conteúdo da pasta de origem para a pasta de destino
                        shutil.copytree(source_folder, destination_folder)
                        print(f"Pasta '{source_folder}' copiada para '{destination_folder}' com sucesso.")
            except Exception as e:
                print(f"Erro ao copiar pastas: {e}")

        source_directory = criando_saida_results
        destination_directory = criando_saida_convert

        copy_folders(source_directory, destination_directory)

        ########################################################################################################################################
        ########################################################################################################################################
        ########################################################################################################################################

        # PART 6

        ########################################################################################################################################
        ########################################################################################################################################
        ########################################################################################################################################

        # convert_obabel

        def convert_pdbqt_to_pdb(input_file, output_directory):
            conv = openbabel.OBConversion()
            conv.SetInAndOutFormats("pdbqt", "pdb")
            # Cria os moléculas de entrada e saída
            mol = openbabel.OBMol()

            conv.ReadFile(mol, input_file)

            base_name = os.path.splitext(os.path.basename(input_file))[0]

            output_file = os.path.join(output_directory, base_name + '.pdb')

            # Escreve a molécula convertida para o arquivo PDB
            conv.WriteFile(mol, output_file)

        def process_files_in_directory(input_directory, output_parent_directory):
            for root, dirs, files in os.walk(input_directory):
                for file in files:
                    if file.endswith('.pdbqt') or file.endswith('out.pdb'):
                        file_path = os.path.join(root, file)

                        # Obtém o nome do diretório pai
                        parent_directory_name = os.path.basename(os.path.dirname(file_path))

                        # Cria um diretório de saída dentro do diretório pai
                        output_directory = os.path.join(output_parent_directory, parent_directory_name)

                        # Chama a função para converter e salvar
                        convert_pdbqt_to_pdb(file_path, output_directory)
                        if file.endswith('.pdbqt') or file.endswith('out.pdb'):
                            os.remove(file_path)

        input_directory = criando_saida_results

        output_parent_directory = criando_saida_convert

        process_files_in_directory(input_directory, output_parent_directory)


    #import shutil
        pasta_a_apagar = criando_saida_results
        shutil.rmtree(pasta_a_apagar)

        ########################################################################################################################################
        ########################################################################################################################################
        ########################################################################################################################################

        # PART 7

        ########################################################################################################################################
        ########################################################################################################################################
        ########################################################################################################################################

        # organizar pastas II

        #import os
        #import shutil

        def remove_unwanted_files(directory):
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith('.pdbqt') or file.endswith('out.pdb'):
                        file_path = os.path.join(root, file)
                        os.remove(file_path)

        def create_folders_for_files(directory):
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith('.pdb'):
                        file_path = os.path.join(root, file)

                        # Obtém o nome do arquivo sem extensão
                        base_name = os.path.splitext(file)[0]

                        # Cria o diretório com o mesmo nome do arquivo, se não existir
                        target_directory = os.path.join(directory, base_name)
                        os.makedirs(target_directory, exist_ok=True)

                        shutil.move(file_path, os.path.join(target_directory, file))

        def process_output_directory(directory):
            # Itera sobre as pastas no diretório de saída
            for folder in os.listdir(directory):
                folder_path = os.path.join(directory, folder)
                
                remove_unwanted_files(folder_path)

                create_folders_for_files(folder_path)

        directory_to_process = criando_saida_convert

        process_output_directory(directory_to_process)

########################################################################################################################################
########################################################################################################################################
########################################################################################################################################

# PART 8

########################################################################################################################################
########################################################################################################################################
########################################################################################################################################

# Using PLIP

#import os
#import subprocess

criando_saida_convert = diresultados

def run_plip_for_directory(directory):
    # Itera sobre todos os diretórios e subdiretórios
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.pdb'):
                pdb_path = os.path.join(root, file)

                # Mude o diretório de trabalho para onde o arquivo .pdb está localizado
                os.chdir(root)

                plip_command = f'plip -f {file} -x -t {no_yes_pymol} --nohydro --nofixfile --nofix'

                subprocess.run(plip_command, shell=True)

directory_to_process = criando_saida_convert

# Chama a função para executar o PLIP em cada arquivo PDB, considerando diretórios dinâmicos
run_plip_for_directory(directory_to_process)

#Rename pasta
#import os

def rename_folders(directory):
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)

        if os.path.isdir(folder_path) and folder_name.endswith(".pdbqt"):
            new_folder_name = folder_name[:-6] + "_Receptor"  # Remove ".pdbqt" e adiciona "_Receptor"
            new_folder_path = os.path.join(directory, new_folder_name)

            os.rename(folder_path, new_folder_path)
            print(f"Pasta concluída: {folder_name} -> {new_folder_name}")

if __name__ == "__main__":
    source_directory = diresultados
    
    rename_folders(source_directory)

#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#                                            Tabelas
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#                                            Tabelas
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#                                            Tabelas
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#


import xml.etree.ElementTree as ET
import csv
import os
import pandas as pd

rename_xml = diresultados

#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#                                            HB
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#

# Função para extrair dados de ligação de hidrogênio
def extract_hydrogen_bond_data(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    hydrogen_bond_data = []

    filename_tag = root.find('filename')
    filename = filename_tag.text if filename_tag is not None else 'Unknown'

    for bindingsite in root.findall('bindingsite'):
        site_id = bindingsite.get('id')

        # Extraindo interações de hidrogênio
        hydrogen_bonds = bindingsite.find('interactions/hydrogen_bonds')
        if hydrogen_bonds is not None:
            for bond in hydrogen_bonds.findall('hydrogen_bond'):
                resnr = bond.find('resnr').text if bond.find('resnr') is not None else None
                restype = bond.find('restype').text if bond.find('restype') is not None else None
                reschain = bond.find('reschain').text if bond.find('reschain') is not None else None
                resnr_lig = bond.find('resnr_lig').text if bond.find('resnr_lig') is not None else None
                restype_lig = bond.find('restype_lig').text if bond.find('restype_lig') is not None else None
                reschain_lig = bond.find('reschain_lig').text if bond.find('reschain_lig') is not None else None
                dist_h_a = bond.find('dist_h-a').text if bond.find('dist_h-a') is not None else None
                dist_d_a = bond.find('dist_d-a').text if bond.find('dist_d-a') is not None else None
                don_angle = bond.find('don_angle').text if bond.find('don_angle') is not None else None
                protisdon = bond.find('protisdon').text if bond.find('protisdon') is not None else None
                donoridx = bond.find('donoridx').text if bond.find('donoridx') is not None else None
                donortype = bond.find('donortype').text if bond.find('donortype') is not None else None
                acceptoridx = bond.find('acceptoridx').text if bond.find('acceptoridx') is not None else None
                acceptortype = bond.find('acceptortype').text if bond.find('acceptortype') is not None else None
                sidechain = bond.find('sidechain').text if bond.find('sidechain') is not None else None

                # Coordenadas do ligante
                ligcoo = bond.find('ligcoo')
                if ligcoo is not None:
                    x_lig = ligcoo.find('x').text if ligcoo.find('x') is not None else None
                    y_lig = ligcoo.find('y').text if ligcoo.find('y') is not None else None
                    z_lig = ligcoo.find('z').text if ligcoo.find('z') is not None else None
                else:
                    x_lig, y_lig, z_lig = None, None, None

                # Coordenadas do protótipo
                protcoo = bond.find('protcoo')
                if protcoo is not None:
                    x_prot = protcoo.find('x').text if protcoo.find('x') is not None else None
                    y_prot = protcoo.find('y').text if protcoo.find('y') is not None else None
                    z_prot = protcoo.find('z').text if protcoo.find('z') is not None else None
                else:
                    x_prot, y_prot, z_prot = None, None, None

                # Adicionar os dados à lista de interações de hidrogênio
                hydrogen_bond_data.append({
                    'Binding Site ID': site_id,
                    'Residue Number': resnr,
                    'Residue Type': restype,
                    'Residue Chain': reschain,
                    'Ligand Residue Number': resnr_lig,
                    'Ligand Residue Type': restype_lig,
                    'Ligand Residue Chain': reschain_lig,
                    'Distance H-A': dist_h_a,
                    'Distance D-A': dist_d_a,
                    'Donor Angle': don_angle,
                    'Prot is Donor': protisdon,
                    'Donor Index': donoridx,
                    'Donor Type': donortype,
                    'Acceptor Index': acceptoridx,
                    'Acceptor Type': acceptortype,
                    'Sidechain': sidechain,
                    'Ligand Coordinates': f'({x_lig}, {y_lig}, {z_lig})',
                    'Protein Coordinates': f'({x_prot}, {y_prot}, {z_prot})',
                    'Filename': filename,
                })

    # Salvando os dados em CSV
    if hydrogen_bond_data:
        csv_filename = os.path.join(os.path.dirname(xml_file), 'Hydrogen_Summary_Interations.csv')
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=hydrogen_bond_data[0].keys())
            writer.writeheader()
            writer.writerows(hydrogen_bond_data)

# Função para percorrer diretórios e processar todos os arquivos XML
def process_all_xml_files(root_directory):
    for dirpath, _, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('.xml'):
                xml_file_path = os.path.join(dirpath, filename)
                print(f"Processing file: {xml_file_path}")
                extract_hydrogen_bond_data(xml_file_path)

root_directory = rename_xml
process_all_xml_files(root_directory)

#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#                                      #hidrophobic
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#


import os
import xml.etree.ElementTree as ET
import csv

# Função para extrair dados de interações hidrofóbicas
def extract_hydrophobic_interaction_data(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    hydrophobic_interaction_data = []

    filename_tag = root.find('filename')
    filename = filename_tag.text if filename_tag is not None else 'Unknown'

    for bindingsite in root.findall('bindingsite'):
        site_id = bindingsite.get('id')

        # Extraindo interações hidrofóbicas
        hydrophobic_interactions = bindingsite.find('interactions/hydrophobic_interactions')
        if hydrophobic_interactions is not None:
            for interaction in hydrophobic_interactions.findall('hydrophobic_interaction'):
                resnr = interaction.find('resnr').text if interaction.find('resnr') is not None else None
                restype = interaction.find('restype').text if interaction.find('restype') is not None else None
                reschain = interaction.find('reschain').text if interaction.find('reschain') is not None else None
                resnr_lig = interaction.find('resnr_lig').text if interaction.find('resnr_lig') is not None else None
                restype_lig = interaction.find('restype_lig').text if interaction.find('restype_lig') is not None else None
                reschain_lig = interaction.find('reschain_lig').text if interaction.find('reschain_lig') is not None else None
                dist = interaction.find('dist').text if interaction.find('dist') is not None else None
                ligcarbonidx = interaction.find('ligcarbonidx').text if interaction.find('ligcarbonidx') is not None else None
                protcarbonidx = interaction.find('protcarbonidx').text if interaction.find('protcarbonidx') is not None else None
                ligcoo = interaction.find('ligcoo')
                if ligcoo is not None:
                    x_lig = ligcoo.find('x').text if ligcoo.find('x') is not None else None
                    y_lig = ligcoo.find('y').text if ligcoo.find('y') is not None else None
                    z_lig = ligcoo.find('z').text if ligcoo.find('z') is not None else None
                else:
                    x_lig, y_lig, z_lig = None, None, None

                # Coordenadas do protótipo
                protcoo = interaction.find('protcoo')
                if protcoo is not None:
                    x_prot = protcoo.find('x').text if protcoo.find('x') is not None else None
                    y_prot = protcoo.find('y').text if protcoo.find('y') is not None else None
                    z_prot = protcoo.find('z').text if protcoo.find('z') is not None else None
                else:
                    x_prot, y_prot, z_prot = None, None, None

                # Adicionar os dados à lista de interações hidrofóbicas
                hydrophobic_interaction_data.append({
                    'Binding Site ID': site_id,
                    'Residue Number': resnr,
                    'Residue Type': restype,
                    'Residue Chain': reschain,
                    'Ligand Residue Number': resnr_lig,
                    'Ligand Residue Type': restype_lig,
                    'Ligand Residue Chain': reschain_lig,
                    'Distance H-A': dist,
                    'Ligand Carbon Index': ligcarbonidx,
                    'Protein Carbon Index': protcarbonidx,
                    'Ligand Coordinates': f'({x_lig}, {y_lig}, {z_lig})',
                    'Protein Coordinates': f'({x_prot}, {y_prot}, {z_prot})',
                    'Filename': filename,
                })

    # Salvando os dados em CSV no mesmo diretório do arquivo XML
    if hydrophobic_interaction_data:
        csv_filename = os.path.join(os.path.dirname(xml_file), 'Hydrophobic_Summary_Interations.csv')
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=hydrophobic_interaction_data[0].keys())
            writer.writeheader()
            writer.writerows(hydrophobic_interaction_data)

# Função para percorrer diretórios e processar todos os arquivos XML em subdiretórios
def process_all_xml_files(root_directory):
    for dirpath, _, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('.xml'):
                xml_file_path = os.path.join(dirpath, filename)
                print(f"Processing file: {xml_file_path}")
                extract_hydrophobic_interaction_data(xml_file_path)

root_directory = rename_xml
process_all_xml_files(root_directory)

#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#                                          halogen
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#

import os
import xml.etree.ElementTree as ET
import csv

# Função para extrair dados de interações de ligação de halogênio
def extract_halogen_bond_data(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    halogen_bond_data = []

    filename_tag = root.find('filename')
    filename = filename_tag.text if filename_tag is not None else 'Unknown'

    for bindingsite in root.findall('bindingsite'):
        site_id = bindingsite.get('id')

        # Extraindo interações de ligação de halogênio
        halogen_bonds = bindingsite.find('interactions/halogen_bonds')
        if halogen_bonds is not None:
            for bond in halogen_bonds.findall('halogen_bond'):
                resnr = bond.find('resnr').text if bond.find('resnr') is not None else None
                restype = bond.find('restype').text if bond.find('restype') is not None else None
                reschain = bond.find('reschain').text if bond.find('reschain') is not None else None
                resnr_lig = bond.find('resnr_lig').text if bond.find('resnr_lig') is not None else None
                restype_lig = bond.find('restype_lig').text if bond.find('restype_lig') is not None else None
                reschain_lig = bond.find('reschain_lig').text if bond.find('reschain_lig') is not None else None
                sidechain = bond.find('sidechain').text if bond.find('sidechain') is not None else None
                dist = bond.find('dist').text if bond.find('dist') is not None else None
                don_angle = bond.find('don_angle').text if bond.find('don_angle') is not None else None
                acc_angle = bond.find('acc_angle').text if bond.find('acc_angle') is not None else None
                don_idx = bond.find('don_idx').text if bond.find('don_idx') is not None else None
                donortype = bond.find('donortype').text if bond.find('donortype') is not None else None
                acc_idx = bond.find('acc_idx').text if bond.find('acc_idx') is not None else None
                acceptortype = bond.find('acceptortype').text if bond.find('acceptortype') is not None else None

                # Coordenadas do ligante
                ligcoo = bond.find('ligcoo')
                if ligcoo is not None:
                    x_lig = ligcoo.find('x').text if ligcoo.find('x') is not None else None
                    y_lig = ligcoo.find('y').text if ligcoo.find('y') is not None else None
                    z_lig = ligcoo.find('z').text if ligcoo.find('z') is not None else None
                else:
                    x_lig, y_lig, z_lig = None, None, None

                # Coordenadas da proteína
                protcoo = bond.find('protcoo')
                if protcoo is not None:
                    x_prot = protcoo.find('x').text if protcoo.find('x') is not None else None
                    y_prot = protcoo.find('y').text if protcoo.find('y') is not None else None
                    z_prot = protcoo.find('z').text if protcoo.find('z') is not None else None
                else:
                    x_prot, y_prot, z_prot = None, None, None

                # Adicionar os dados à lista de interações de halogênio
                halogen_bond_data.append({
                    'Binding Site ID': site_id,
                    'Residue Number': resnr,
                    'Residue Type': restype,
                    'Residue Chain': reschain,
                    'Ligand Residue Number': resnr_lig,
                    'Ligand Residue Type': restype_lig,
                    'Ligand Residue Chain': reschain_lig,
                    'Sidechain': sidechain,
                    'Distance H-A': dist,
                    'Donor Angle': don_angle,
                    'Acceptor Angle': acc_angle,
                    'Donor Index': don_idx,
                    'Donor Type': donortype,
                    'Acceptor Index': acc_idx,
                    'Acceptor Type': acceptortype,
                    'Ligand Coordinates': f'({x_lig}, {y_lig}, {z_lig})',
                    'Protein Coordinates': f'({x_prot}, {y_prot}, {z_prot})',
                    'Filename': filename,
                })

    # Salvando os dados em CSV no mesmo diretório do arquivo XML
    if halogen_bond_data:
        csv_filename = os.path.join(os.path.dirname(xml_file), 'Halogen_Bond_Summary_Interations.csv')
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=halogen_bond_data[0].keys())
            writer.writeheader()
            writer.writerows(halogen_bond_data)

# Função para percorrer diretórios e processar todos os arquivos XML em subdiretórios
def process_all_xml_files(root_directory):
    for dirpath, _, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('.xml'):
                xml_file_path = os.path.join(dirpath, filename)
                print(f"Processing file: {xml_file_path}")
                extract_halogen_bond_data(xml_file_path)

root_directory = rename_xml
process_all_xml_files(root_directory)

import os
import xml.etree.ElementTree as ET
import csv

#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#                                        Pi Stack
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#

def extract_pi_stack_data(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    pi_stack_data = []

    filename_tag = root.find('filename')
    filename = filename_tag.text if filename_tag is not None else 'Unknown'

    for bindingsite in root.findall('bindingsite'):
        site_id = bindingsite.get('id')

        # Extraindo interações de pi stack
        pi_stacks = bindingsite.find('interactions/pi_stacks')
        if pi_stacks is not None:
            for stack in pi_stacks.findall('pi_stack'):
                resnr = stack.find('resnr').text if stack.find('resnr') is not None else None
                restype = stack.find('restype').text if stack.find('restype') is not None else None
                reschain = stack.find('reschain').text if stack.find('reschain') is not None else None
                resnr_lig = stack.find('resnr_lig').text if stack.find('resnr_lig') is not None else None
                restype_lig = stack.find('restype_lig').text if stack.find('restype_lig') is not None else None
                reschain_lig = stack.find('reschain_lig').text if stack.find('reschain_lig') is not None else None
                centdist = stack.find('centdist').text if stack.find('centdist') is not None else None
                angle = stack.find('angle').text if stack.find('angle') is not None else None
                offset = stack.find('offset').text if stack.find('offset') is not None else None
                type_stack = stack.find('type').text if stack.find('type') is not None else None

                # Listas de índices do protótipo e ligante
                prot_idx_list = ', '.join(idx.text for idx in stack.find('prot_idx_list').findall('idx')) if stack.find('prot_idx_list') is not None else None
                lig_idx_list = ', '.join(idx.text for idx in stack.find('lig_idx_list').findall('idx')) if stack.find('lig_idx_list') is not None else None

                # Coordenadas do ligante
                ligcoo = stack.find('ligcoo')
                if ligcoo is not None:
                    x_lig = ligcoo.find('x').text if ligcoo.find('x') is not None else None
                    y_lig = ligcoo.find('y').text if ligcoo.find('y') is not None else None
                    z_lig = ligcoo.find('z').text if ligcoo.find('z') is not None else None
                else:
                    x_lig, y_lig, z_lig = None, None, None

                # Coordenadas do protótipo
                protcoo = stack.find('protcoo')
                if protcoo is not None:
                    x_prot = protcoo.find('x').text if protcoo.find('x') is not None else None
                    y_prot = protcoo.find('y').text if protcoo.find('y') is not None else None
                    z_prot = protcoo.find('z').text if protcoo.find('z') is not None else None
                else:
                    x_prot, y_prot, z_prot = None, None, None

                # Adicionar os dados à lista de interações de pi stack
                pi_stack_data.append({
                    'Binding Site ID': site_id,
                    'Residue Number': resnr,
                    'Residue Type': restype,
                    'Residue Chain': reschain,
                    'Ligand Residue Number': resnr_lig,
                    'Ligand Residue Type': restype_lig,
                    'Ligand Residue Chain': reschain_lig,
                    'Distance H-A': centdist,
                    'Donor Angle': angle,
                    'Offset': offset,
                    'Type': type_stack,
                    'Ligand Index List': lig_idx_list,
                    'Protein Index List': prot_idx_list,
                    'Ligand Coordinates': f'({x_lig}, {y_lig}, {z_lig})',
                    'Protein Coordinates': f'({x_prot}, {y_prot}, {z_prot})',
                    'Filename': filename,
                })

    # Salvando os dados em CSV no mesmo diretório do arquivo XML
    if pi_stack_data:
        csv_filename = os.path.join(os.path.dirname(xml_file), 'Pi_Stack_Summary_Interations.csv')
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=pi_stack_data[0].keys())
            writer.writeheader()
            writer.writerows(pi_stack_data)

# Função para percorrer diretórios e processar todos os arquivos XML em subdiretórios
def process_all_xml_files(root_directory):
    for dirpath, _, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('.xml'):
                xml_file_path = os.path.join(dirpath, filename)
                print(f"Processing file: {xml_file_path}")
                extract_pi_stack_data(xml_file_path)

root_directory = rename_xml
process_all_xml_files(root_directory)

#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#                                        Pi cation
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#

import os
import xml.etree.ElementTree as ET
import csv

# Função para extrair dados de interações pi-cátion
def extract_pi_cation_data(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    pi_cation_data = []

    filename_tag = root.find('filename')
    filename = filename_tag.text if filename_tag is not None else 'Unknown'

    for bindingsite in root.findall('bindingsite'):
        site_id = bindingsite.get('id')

        # Extraindo interações pi-cátion
        pi_cation_interactions = bindingsite.find('interactions/pi_cation_interactions')
        if pi_cation_interactions is not None:
            for interaction in pi_cation_interactions.findall('pi_cation_interaction'):
                resnr = interaction.find('resnr').text if interaction.find('resnr') is not None else None
                restype = interaction.find('restype').text if interaction.find('restype') is not None else None
                reschain = interaction.find('reschain').text if interaction.find('reschain') is not None else None
                resnr_lig = interaction.find('resnr_lig').text if interaction.find('resnr_lig') is not None else None
                restype_lig = interaction.find('restype_lig').text if interaction.find('restype_lig') is not None else None
                reschain_lig = interaction.find('reschain_lig').text if interaction.find('reschain_lig') is not None else None
                distance = interaction.find('dist').text if interaction.find('dist') is not None else None
                offset = interaction.find('offset').text if interaction.find('offset') is not None else None
                protcharged = interaction.find('protcharged').text if interaction.find('protcharged') is not None else None
                lig_group = interaction.find('lig_group').text if interaction.find('lig_group') is not None else None

                # Listas de índices do protótipo e ligante
                prot_idx_list = ', '.join(idx.text for idx in interaction.find('prot_idx_list').findall('idx')) if interaction.find('prot_idx_list') is not None else None
                lig_idx_list = ', '.join(idx.text for idx in interaction.find('lig_idx_list').findall('idx')) if interaction.find('lig_idx_list') is not None else None

                # Coordenadas do ligante
                ligcoo = interaction.find('ligcoo')
                if ligcoo is not None:
                    x_lig = ligcoo.find('x').text if ligcoo.find('x') is not None else None
                    y_lig = ligcoo.find('y').text if ligcoo.find('y') is not None else None
                    z_lig = ligcoo.find('z').text if ligcoo.find('z') is not None else None
                else:
                    x_lig, y_lig, z_lig = None, None, None

                # Coordenadas do protótipo
                protcoo = interaction.find('protcoo')
                if protcoo is not None:
                    x_prot = protcoo.find('x').text if protcoo.find('x') is not None else None
                    y_prot = protcoo.find('y').text if protcoo.find('y') is not None else None
                    z_prot = protcoo.find('z').text if protcoo.find('z') is not None else None
                else:
                    x_prot, y_prot, z_prot = None, None, None

                # Adicionar os dados à lista de interações pi-cátion
                pi_cation_data.append({
                    'Binding Site ID': site_id,
                    'Residue Number': resnr,
                    'Residue Type': restype,
                    'Residue Chain': reschain,
                    'Ligand Residue Number': resnr_lig,
                    'Ligand Residue Type': restype_lig,
                    'Ligand Residue Chain': reschain_lig,
                    'Distance H-A': distance,
                    'Offset': offset,
                    'Protein Charged': protcharged,
                    'Ligand Group': lig_group,
                    'Ligand Index List': lig_idx_list,
                    'Protein Index List': prot_idx_list,
                    'Ligand Coordinates': f'({x_lig}, {y_lig}, {z_lig})',
                    'Protein Coordinates': f'({x_prot}, {y_prot}, {z_prot})',
                    'Filename': filename,
                })

    # Salvando os dados em CSV no mesmo diretório do arquivo XML
    if pi_cation_data:
        csv_filename = os.path.join(os.path.dirname(xml_file), 'Pi_Cation_Summary_Interations.csv')
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=pi_cation_data[0].keys())
            writer.writeheader()
            writer.writerows(pi_cation_data)

# Função para percorrer diretórios e processar todos os arquivos XML em subdiretórios
def process_all_xml_files(root_directory):
    for dirpath, _, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('.xml'):
                xml_file_path = os.path.join(dirpath, filename)
                print(f"Processing file: {xml_file_path}")
                extract_pi_cation_data(xml_file_path)

root_directory = rename_xml
process_all_xml_files(root_directory)


import os
import xml.etree.ElementTree as ET
import csv

#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#                                       metal-complex
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#

def extract_metal_complex_data(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    metal_complex_data = []

    # Capturando o nome do arquivo
    filename_tag = root.find('filename')
    filename = filename_tag.text if filename_tag is not None else 'Unknown'

    for bindingsite in root.findall('bindingsite'):
        site_id = bindingsite.get('id')

        # Extraindo interações de complexos metálicos
        metal_complexes = bindingsite.find('interactions/metal_complexes')
        if metal_complexes is not None:
            for metal_complex in metal_complexes.findall('metal_complex'):
                resnr = metal_complex.find('resnr').text if metal_complex.find('resnr') is not None else None
                restype = metal_complex.find('restype').text if metal_complex.find('restype') is not None else None
                reschain = metal_complex.find('reschain').text if metal_complex.find('reschain') is not None else None
                resnr_lig = metal_complex.find('resnr_lig').text if metal_complex.find('resnr_lig') is not None else None
                restype_lig = metal_complex.find('restype_lig').text if metal_complex.find('restype_lig') is not None else None
                reschain_lig = metal_complex.find('reschain_lig').text if metal_complex.find('reschain_lig') is not None else None
                metal_idx = metal_complex.find('metal_idx').text if metal_complex.find('metal_idx') is not None else None
                metal_type = metal_complex.find('metal_type').text if metal_complex.find('metal_type') is not None else None
                target_idx = metal_complex.find('target_idx').text if metal_complex.find('target_idx') is not None else None
                target_type = metal_complex.find('target_type').text if metal_complex.find('target_type') is not None else None
                coordination = metal_complex.find('coordination').text if metal_complex.find('coordination') is not None else None
                dist = metal_complex.find('dist').text if metal_complex.find('dist') is not None else None
                location = metal_complex.find('location').text if metal_complex.find('location') is not None else None
                rms = metal_complex.find('rms').text if metal_complex.find('rms') is not None else None
                geometry = metal_complex.find('geometry').text if metal_complex.find('geometry') is not None else None
                complexnum = metal_complex.find('complexnum').text if metal_complex.find('complexnum') is not None else None

                # Coordenadas do metal
                metalcoo = metal_complex.find('metalcoo')
                if metalcoo is not None:
                    x_metal = metalcoo.find('x').text if metalcoo.find('x') is not None else None
                    y_metal = metalcoo.find('y').text if metalcoo.find('y') is not None else None
                    z_metal = metalcoo.find('z').text if metalcoo.find('z') is not None else None
                else:
                    x_metal, y_metal, z_metal = None, None, None

                # Coordenadas do alvo
                targetcoo = metal_complex.find('targetcoo')
                if targetcoo is not None:
                    x_target = targetcoo.find('x').text if targetcoo.find('x') is not None else None
                    y_target = targetcoo.find('y').text if targetcoo.find('y') is not None else None
                    z_target = targetcoo.find('z').text if targetcoo.find('z') is not None else None
                else:
                    x_target, y_target, z_target = None, None, None

                # Adicionar os dados à lista de interações de complexos metálicos
                metal_complex_data.append({
                    'Binding Site ID': site_id,
                    'Residue Number': resnr,
                    'Residue Type': restype,
                    'Residue Chain': reschain,
                    'Ligand Residue Number': resnr_lig,
                    'Ligand Residue Type': restype_lig,
                    'Ligand Residue Chain': reschain_lig,
                    'Metal Index': metal_idx,
                    'Metal Type': metal_type,
                    'Target Index': target_idx,
                    'Target Type': target_type,
                    'Coordination Number': coordination,
                    'Distance H-A': dist,
                    'Location': location,
                    'RMS': rms,
                    'Geometry': geometry,
                    'Complex Number': complexnum,
                    'Metal Coordinates': f'({x_metal}, {y_metal}, {z_metal})',
                    'Target Coordinates': f'({x_target}, {y_target}, {z_target})',
                    'Filename': filename,
                })

    # Salvando os dados em CSV no mesmo diretório do arquivo XML
    if metal_complex_data:
        csv_filename = os.path.join(os.path.dirname(xml_file), 'Metal_Complex_Summary_Interations.csv')
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=metal_complex_data[0].keys())
            writer.writeheader()
            writer.writerows(metal_complex_data)

# Função para percorrer diretórios e processar todos os arquivos XML em subdiretórios
def process_all_xml_files(root_directory):
    for dirpath, _, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('.xml'):
                xml_file_path = os.path.join(dirpath, filename)
                print(f"Processing file: {xml_file_path}")
                extract_metal_complex_data(xml_file_path)

root_directory = rename_xml
process_all_xml_files(root_directory)

import os
import xml.etree.ElementTree as ET
import csv

#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#                                         ponte de água
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#

def extract_water_bridge_data(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    water_bridge_data = []

    # Capturando o nome do arquivo
    filename_tag = root.find('filename')
    filename = filename_tag.text if filename_tag is not None else 'Unknown'

    for bindingsite in root.findall('bindingsite'):
        site_id = bindingsite.get('id')

        # Extraindo interações de ponte de água
        water_bridges = bindingsite.find('interactions/water_bridges')
        if water_bridges is not None:
            for bridge in water_bridges.findall('water_bridge'):
                resnr = bridge.find('resnr').text if bridge.find('resnr') is not None else None
                restype = bridge.find('restype').text if bridge.find('restype') is not None else None
                reschain = bridge.find('reschain').text if bridge.find('reschain') is not None else None
                resnr_lig = bridge.find('resnr_lig').text if bridge.find('resnr_lig') is not None else None
                restype_lig = bridge.find('restype_lig').text if bridge.find('restype_lig') is not None else None
                reschain_lig = bridge.find('reschain_lig').text if bridge.find('reschain_lig') is not None else None
                dist_a_w = bridge.find('dist_a-w').text if bridge.find('dist_a-w') is not None else None
                dist_d_w = bridge.find('dist_d-w').text if bridge.find('dist_d-w') is not None else None
                don_angle = bridge.find('don_angle').text if bridge.find('don_angle') is not None else None
                water_angle = bridge.find('water_angle').text if bridge.find('water_angle') is not None else None
                protisdon = bridge.find('protisdon').text if bridge.find('protisdon') is not None else None
                donor_idx = bridge.find('donor_idx').text if bridge.find('donor_idx') is not None else None
                donortype = bridge.find('donortype').text if bridge.find('donortype') is not None else None
                acceptor_idx = bridge.find('acceptor_idx').text if bridge.find('acceptor_idx') is not None else None
                acceptortype = bridge.find('acceptortype').text if bridge.find('acceptortype') is not None else None
                water_idx = bridge.find('water_idx').text if bridge.find('water_idx') is not None else None

                # Coordenadas do ligante
                ligcoo = bridge.find('ligcoo')
                if ligcoo is not None:
                    x_lig = ligcoo.find('x').text if ligcoo.find('x') is not None else None
                    y_lig = ligcoo.find('y').text if ligcoo.find('y') is not None else None
                    z_lig = ligcoo.find('z').text if ligcoo.find('z') is not None else None
                else:
                    x_lig, y_lig, z_lig = None, None, None

                # Coordenadas da proteína
                protcoo = bridge.find('protcoo')
                if protcoo is not None:
                    x_prot = protcoo.find('x').text if protcoo.find('x') is not None else None
                    y_prot = protcoo.find('y').text if protcoo.find('y') is not None else None
                    z_prot = protcoo.find('z').text if protcoo.find('z') is not None else None
                else:
                    x_prot, y_prot, z_prot = None, None, None

                # Coordenadas da água
                watercoo = bridge.find('watercoo')
                if watercoo is not None:
                    x_water = watercoo.find('x').text if watercoo.find('x') is not None else None
                    y_water = watercoo.find('y').text if watercoo.find('y') is not None else None
                    z_water = watercoo.find('z').text if watercoo.find('z') is not None else None
                else:
                    x_water, y_water, z_water = None, None, None

                # Adicionar os dados à lista de interações de ponte de água
                water_bridge_data.append({
                    'Binding Site ID': site_id,
                    'Residue Number': resnr,
                    'Residue Type': restype,
                    'Residue Chain': reschain,
                    'Ligand Residue Number': resnr_lig,
                    'Ligand Residue Type': restype_lig,
                    'Ligand Residue Chain': reschain_lig,
                    'Distance H-A': dist_a_w,
                    'Distance D-W': dist_d_w,
                    'Donor Angle': don_angle,
                    'Water Angle': water_angle,
                    'Prot is Donor': protisdon,
                    'Donor Index': donor_idx,
                    'Donor Type': donortype,
                    'Acceptor Index': acceptor_idx,
                    'Acceptor Type': acceptortype,
                    'Water Index': water_idx,
                    'Ligand Coordinates': f'({x_lig}, {y_lig}, {z_lig})',
                    'Protein Coordinates': f'({x_prot}, {y_prot}, {z_prot})',
                    'Water Coordinates': f'({x_water}, {y_water}, {z_water})',
                    'Filename': filename,
                })

    # Salvando os dados em CSV no mesmo diretório do arquivo XML
    if water_bridge_data:
        csv_filename = os.path.join(os.path.dirname(xml_file), 'Water_Bridge_Summary_Interations.csv')
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=water_bridge_data[0].keys())
            writer.writeheader()
            writer.writerows(water_bridge_data)

# Função para percorrer diretórios e processar todos os arquivos XML em subdiretórios
def process_all_xml_files(root_directory):
    for dirpath, _, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('.xml'):
                xml_file_path = os.path.join(dirpath, filename)
                print(f"Processing file: {xml_file_path}")
                extract_water_bridge_data(xml_file_path)

root_directory = rename_xml
process_all_xml_files(root_directory)
import os
import xml.etree.ElementTree as ET
import csv

#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#                             interações de ponte de sal
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#

def extract_salt_bridge_data(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    salt_bridge_data = []

    # Capturando o nome do arquivo
    filename_tag = root.find('filename')
    filename = filename_tag.text if filename_tag is not None else 'Unknown'

    for bindingsite in root.findall('bindingsite'):
        site_id = bindingsite.get('id')

        # Extraindo interações de ponte de sal
        salt_bridges = bindingsite.find('interactions/salt_bridges')
        if salt_bridges is not None:
            for bridge in salt_bridges.findall('salt_bridge'):
                resnr = bridge.find('resnr').text if bridge.find('resnr') is not None else None
                restype = bridge.find('restype').text if bridge.find('restype') is not None else None
                reschain = bridge.find('reschain').text if bridge.find('reschain') is not None else None
                resnr_lig = bridge.find('resnr_lig').text if bridge.find('resnr_lig') is not None else None
                restype_lig = bridge.find('restype_lig').text if bridge.find('restype_lig') is not None else None
                reschain_lig = bridge.find('reschain_lig').text if bridge.find('reschain_lig') is not None else None
                dist = bridge.find('dist').text if bridge.find('dist') is not None else None
                protispos = bridge.find('protispos').text if bridge.find('protispos') is not None else None
                lig_group = bridge.find('lig_group').text if bridge.find('lig_group') is not None else None

                # Índices da proteína
                prot_idx_list = [idx.text for idx in bridge.findall('prot_idx_list/idx')]

                # Índices do ligante
                lig_idx_list = [idx.text for idx in bridge.findall('lig_idx_list/idx')]

                # Coordenadas do ligante
                ligcoo = bridge.find('ligcoo')
                if ligcoo is not None:
                    x_lig = ligcoo.find('x').text if ligcoo.find('x') is not None else None
                    y_lig = ligcoo.find('y').text if ligcoo.find('y') is not None else None
                    z_lig = ligcoo.find('z').text if ligcoo.find('z') is not None else None
                else:
                    x_lig, y_lig, z_lig = None, None, None

                # Coordenadas da proteína
                protcoo = bridge.find('protcoo')
                if protcoo is not None:
                    x_prot = protcoo.find('x').text if protcoo.find('x') is not None else None
                    y_prot = protcoo.find('y').text if protcoo.find('y') is not None else None
                    z_prot = protcoo.find('z').text if protcoo.find('z') is not None else None
                else:
                    x_prot, y_prot, z_prot = None, None, None

                # Adicionar os dados à lista de interações de ponte de sal
                salt_bridge_data.append({
                    'Binding Site ID': site_id,
                    'Residue Number': resnr,
                    'Residue Type': restype,
                    'Residue Chain': reschain,
                    'Ligand Residue Number': resnr_lig,
                    'Ligand Residue Type': restype_lig,
                    'Ligand Residue Chain': reschain_lig,
                    'Distance H-A': dist,
                    'Protein is Positive': protispos,
                    'Ligand Group': lig_group,
                    'Protein Index List': ','.join(prot_idx_list),
                    'Ligand Index List': ','.join(lig_idx_list),
                    'Ligand Coordinates': f'({x_lig}, {y_lig}, {z_lig})',
                    'Protein Coordinates': f'({x_prot}, {y_prot}, {z_prot})',
                    'Filename': filename,
                })

    # Salvando os dados em CSV no mesmo diretório do arquivo XML
    if salt_bridge_data:
        csv_filename = os.path.join(os.path.dirname(xml_file), 'Salt_Bridge_Summary_Interations.csv')
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=salt_bridge_data[0].keys())
            writer.writeheader()
            writer.writerows(salt_bridge_data)

# Função para percorrer diretórios e processar todos os arquivos XML em subdiretórios
def process_all_xml_files(root_directory):
    for dirpath, _, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('.xml'):
                xml_file_path = os.path.join(dirpath, filename)
                print(f"Processing file: {xml_file_path}")
                extract_salt_bridge_data(xml_file_path)

root_directory = rename_xml
process_all_xml_files(root_directory)

# Organizando nomes

import os

def rename_files_in_subdirectories(root_directory):
    for dirpath, _, filenames in os.walk(root_directory):
        folder_name = os.path.basename(dirpath)
        
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if filename.endswith('.txt') or filename.endswith('.xml'):
                new_name = f"{folder_name}{os.path.splitext(filename)[1]}"  # Mantém a extensão
                new_path = os.path.join(dirpath, new_name)
                os.rename(file_path, new_path)
                print(f"Renamed: {file_path} to {new_path}")
            elif filename.endswith('.csv'):
                # Adicionando _{nome_da_pasta} ao final dos arquivos .csv
                new_name = f"{os.path.splitext(filename)[0]}_{folder_name}.csv"
                new_path = os.path.join(dirpath, new_name)
                os.rename(file_path, new_path)
                print(f"Renamed: {file_path} to {new_path}")

root_directory = rename_xml
rename_files_in_subdirectories(root_directory)


#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#                                     Unindo as tabelas
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#

import os
import pandas as pd


# Caminho do diretório raiz para busca
root_dir = diresultados 


# Função para criar a tabela dinâmica
def create_dynamic_table(df, output_file):
    
    # Lista de aminoácidos
    amino_acids = [
        "ALA", "ARG", "ASN", "ASP", "CYS", "GLN", "GLU", "GLY", 
        "HIS", "ILE", "LEU", "LYS", "MET", "PHE", "PRO", "SER", 
        "THR", "TRP", "TYR", "VAL"
    ]

    # Verificar se a coluna "Donor Angle" existe no DataFrame
    has_donor_angle = "Donor Angle" in df.columns

    # Criar um DataFrame vazio para a tabela dinâmica
    columns = ["Filename", "Residue Type", "Distance"]
    if has_donor_angle:
        columns.append("Donor Angle")
    columns.extend(amino_acids)

    dynamic_table = pd.DataFrame(columns=columns)

    # Iterar sobre cada linha do DataFrame
    for index, row in df.iterrows():
        filename = row["Filename"]
        restype = row["Residue Type"]
        distance = row["Distance H-A"]

        # Verificar se o tipo de resíduo está na lista de aminoácidos
        if restype in amino_acids:
            # Criar uma nova linha para a tabela dinâmica
            new_row = {
                "Filename": filename,
                "Residue Type": restype,
                "Distance": distance,
            }

            # Adicionar o Donor Angle, se existir
            if has_donor_angle:
                new_row["Donor Angle"] = row["Donor Angle"]

            # Preencher as colunas de aminoácidos
            for aa in amino_acids:
                new_row[aa] = distance if restype == aa else ""

            # Criar um DataFrame temporário para a nova linha
            temp_df = pd.DataFrame([new_row])

            # Remover colunas vazias ou totalmente NA antes de concatenar
            temp_df = temp_df.dropna(axis=1, how="all")

            # Adicionar a nova linha ao DataFrame dinâmico
            dynamic_table = pd.concat([dynamic_table, temp_df], ignore_index=True)

    # Salvar a tabela dinâmica em um arquivo CSV
    dynamic_table.to_csv(output_file, index=False)
    print(f"Tabela dinâmica criada e salva em: {output_file}")

# Função principal para processar o diretório
def process_directory(root_dir, file_patterns):
    
    # Dicionário para armazenar DataFrames separados por padrão
    data_by_pattern = {pattern: [] for pattern in file_patterns}

    # Percorrer o diretório e subdiretórios
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Procurar arquivos que correspondam aos padrões fornecidos
        for filename in filenames:
            for pattern in file_patterns:
                if pattern in filename:
                    file_path = os.path.join(dirpath, filename)
                    print(f"Processando arquivo: {file_path}")

                    try:
                        # Ler o arquivo CSV
                        df = pd.read_csv(file_path)

                        # Verificar se o arquivo contém as colunas necessárias
                        required_columns = ["Filename", "Residue Type", "Distance H-A"]
                        if all(column in df.columns for column in required_columns):
                            data_by_pattern[pattern].append(df)
                        else:
                            print(f"Erro: O arquivo {file_path} não contém as colunas necessárias: {required_columns}")
                    except Exception as e:
                        print(f"Erro ao processar o arquivo {file_path}: {e}")
                    break  # Parar de verificar outros padrões após encontrar uma correspondência

    # Criar uma tabela dinâmica para cada padrão
    for pattern, data_list in data_by_pattern.items():
        if data_list:
            # Combinar todos os DataFrames do mesmo padrão
            combined_df = pd.concat(data_list, ignore_index=True)
            print(f"Total de linhas combinadas para o padrão '{pattern}': {len(combined_df)}")

            # Caminho do arquivo de saída para o padrão atual
            output_file = os.path.join(diresultados, f"Dynamic_{pattern}_tab.csv")

            # Criar a tabela dinâmica
            create_dynamic_table(combined_df, output_file)
        else:
            print(f"Nenhum arquivo encontrado para interações '{pattern}'.")


# Lista de padrões de nomes de arquivos para buscar
file_patterns = [
    "Hydrogen_Summary_Interations",
    "Hydrophobic_Summary_Interations",
    "Halogen_Bond_Summary_Interations",
    "Pi_Stack_Summary_Interations",
    "Pi_Cation_Summary_Interations",
    "Metal_Complex_Summary_Interations",
    "Water_Bridge_Summary_Interations",
    "Salt_Bridge_Summary_Interations",
]

process_directory(root_dir, file_patterns)
