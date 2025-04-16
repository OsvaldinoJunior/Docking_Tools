import os
import numpy as np

# Pasta de entrada contendo arquivos PDB ou PDBQT
input_folder = "/home/osvaldinojunior/Documents/scripts_vscode_notebook/blind_docking_automaton/"
# Pasta de saída para os arquivos de parâmetros da caixa de docking
output_folder = "/home/osvaldinojunior/Documents/scripts_vscode_notebook/blind_docking_automaton/grid_box"

def read_coordinates_from_pdb_or_pdbqt(pdb_file):
    with open(pdb_file, 'r') as file:
        lines = file.readlines()
    
    # Filtra apenas as linhas que contêm coordenadas de átomos (ATOM para PDB, ATOM/HETATM para PDBQT)
    atom_lines = [line.strip().split() for line in lines if line.startswith('ATOM') or line.startswith('HETATM')]
    
    # Extrai as coordenadas x, y e z de cada átomo
    coordinates = np.array([[float(atom[6]), float(atom[7]), float(atom[8])] for atom in atom_lines])
    
    return coordinates

def get_extreme_coordinates_and_center(coordinates):
    # Calcula as coordenadas mais extremas (mínimas e máximas) em cada dimensão (x, y, z)
    min_coords = np.min(coordinates, axis=0)
    max_coords = np.max(coordinates, axis=0)
    
    # Calcula o centroide das coordenadas
    center = np.mean(coordinates, axis=0)
    
    return min_coords, max_coords, center

def get_docking_box_dimensions(pdb_file, margin=0.4):
    # Lê as coordenadas do arquivo PDB ou PDBQT
    coordinates = read_coordinates_from_pdb_or_pdbqt(pdb_file)
    
    # Obtém as coordenadas extremas e o centroide
    min_coords, max_coords, center = get_extreme_coordinates_and_center(coordinates)
    
    # Calcula as dimensões da caixa
    dimensions = max_coords - min_coords + margin
    
    return min_coords, max_coords, center, dimensions

def write_docking_box_parameters(pdb_file, output_folder):
    # Obtém o nome do arquivo sem a extensão
    filename = os.path.splitext(os.path.basename(pdb_file))[0]
    
    # Cria o nome do arquivo de saída
    output_file = os.path.join(output_folder, filename + '_blinding_docking_box.txt')
    
    # Obtém as dimensões da caixa de docking com uma margem de 0.4
    min_coords, max_coords, center, box_dimensions = get_docking_box_dimensions(pdb_file, margin=0.4)
    
    # Escreve as coordenadas e dimensões no arquivo de saída
    with open(output_file, 'w') as file:
        file.write(f"center_x = {center[0]:.3f}\n")
        file.write(f"center_y = {center[1]:.3f}\n")
        file.write(f"center_z = {center[2]:.3f}\n")
        file.write(f"size_x = {box_dimensions[0]:.1f}\n")
        file.write(f"size_y = {box_dimensions[1]:.1f}\n")
        file.write(f"size_z = {box_dimensions[2]:.1f}\n")

def process_files_in_folder(input_folder, output_folder):
    # Cria a pasta de saída se ela não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Processa cada arquivo na pasta de entrada
    for filename in os.listdir(input_folder):
        # Verifica se o arquivo é um arquivo PDB ou PDBQT
        if filename.endswith(".pdb") or filename.endswith(".pdbqt"):
            pdb_file = os.path.join(input_folder, filename)
            # Escreve os parâmetros da caixa de docking no arquivo de saída
            write_docking_box_parameters(pdb_file, output_folder)

# Processa os arquivos na pasta de entrada e escreve os parâmetros da caixa de docking na pasta de saída
process_files_in_folder(input_folder, output_folder)

print("Parâmetros da caixa de docking foram salvos em:", output_folder)
