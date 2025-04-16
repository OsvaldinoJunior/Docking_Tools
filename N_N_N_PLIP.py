# Receptor Loop
# PART 1

#from openbabel import openbabel, pybel
import os
import re
import shutil
import openbabel
import subprocess



# Caminho para a pasta contendo os arquivos do Receptor
caminho_da_receptors = "/home/osvaldinojunior/Documents/Osvaldino_PLIP_Filtro/recep/"

# Caminho para a pasta contendo os arquivos do Ligant
dirligs = "/home/osvaldinojunior/Documents/Osvaldino_PLIP_Filtro/ligs/"

# Caminho para a pasta contendo os arquivos de saída
diresultados = "/home/osvaldinojunior/Documents/Osvaldino_PLIP_Filtro/result"

# Deseja receber o arquivo de imagem do pymol?
Pymol_session = input("deseja receber imagens dos resultados? (s/n) = ").strip().lower()
if Pymol_session == ("n"):
    no_yes_pymol = ""
elif Pymol_session == ("s"):
    no_yes_pymol = "-y"

#------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------#
#------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------#
#------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------#
#------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------#
#------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------#
#------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------#
#------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------#
#------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------#
#------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------#
#------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------#
#------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------#
#------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------#
#------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------#
#------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------#
#------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------#
#------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------#
#------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------#
#------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------##------- POLICE LINE DO NOT CROSS -------#

# Loop para iterar sobre os arquivos na pasta
for nome_do_arquivo in os.listdir(caminho_da_receptors):
    caminho_recep_loop = os.path.join(caminho_da_receptors, nome_do_arquivo)

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
            
            for pasta_ligantes in os.listdir(dirlig):
                caminho_pasta_ligantes = os.path.join(dirlig, pasta_ligantes)

                if os.path.isdir(caminho_pasta_ligantes):
                    ligantes = [f for f in os.listdir(caminho_pasta_ligantes) if f.endswith('.pdbqt')]

                    # Iterar sobre os arquivos ligantes
                    for ligante in ligantes:
                        caminho_ligante = os.path.join(caminho_pasta_ligantes, ligante)

                        with open(caminho_ligante, 'r') as ligante_file:
                            conteudo_ligante = ligante_file.readlines()

                        conteudo_combinado = conteudo_ligante + conteudo_receptor

                        # Criar uma pasta para cada arquivo combinado
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

        # Renomear para conversão

        # PART 2

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

            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith('.pdbqt'):
                        file_path = os.path.join(root, file)

                        with open(file_path, 'r') as pdbqt_file:
                            pdbqt_lines = pdbqt_file.readlines()

                        combined_lines = receptor_lines + pdbqt_lines

                        with open(file_path, 'w') as output_file:
                            output_file.writelines(combined_lines)
 
        directory_path = criando_saida_results

        receptor_path = dirrec

        add_receptor_to_files(directory_path, receptor_path)

        # Tratamento 2 pequenos ajustes

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

            # Obtém o nome do arquivo sem extensão
            base_name = os.path.splitext(os.path.basename(input_file))[0]

            output_file = os.path.join(output_directory, base_name + '.pdb')

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

                        # Remove os arquivos .pdbqt e out.pdb
                        if file.endswith('.pdbqt') or file.endswith('out.pdb'):
                            os.remove(file_path)

        input_directory = criando_saida_results

        output_parent_directory = criando_saida_convert

        process_files_in_directory(input_directory, output_parent_directory)

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

                        base_name = os.path.splitext(file)[0]

                        target_directory = os.path.join(directory, base_name)
                        os.makedirs(target_directory, exist_ok=True)

                        shutil.move(file_path, os.path.join(target_directory, file))

        def process_output_directory(directory):
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
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.pdb'):
                pdb_path = os.path.join(root, file)

                os.chdir(root)

                plip_command = f'plip -f {file} -x -t {no_yes_pymol} --nohydro --nofixfile --nofix'

                subprocess.run(plip_command, shell=True)

directory_to_process = criando_saida_convert

run_plip_for_directory(directory_to_process)

#Rename pasta
#import os

def rename_folders(directory):
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)

        if os.path.isdir(folder_path) and folder_name.endswith(".pdbqt"):
            new_folder_name = folder_name[:-6] + "_Receptor" 
            new_folder_path = os.path.join(directory, new_folder_name)

            os.rename(folder_path, new_folder_path)
            print(f"Pasta concluída: {folder_name} -> {new_folder_name}")

if __name__ == "__main__":
    source_directory = diresultados
    
    rename_folders(source_directory)


######################################################################################################
######################################################################################################
######################################################################################################



######################################################################################################
######################################################################################################
######################################################################################################
