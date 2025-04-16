import os
import pymol

def vina_results_to_pymol(molecule_file, receptor_file, output_pdb_file):
    # Inicialize o PyMOL
    print("step0")
    pymol.finish_launching()
    print("step1")
    # Carregue a molécula e o receptor no PyMOL
    pymol.cmd.load(molecule_file, '1iep_ligand.pdbqt')
    pymol.cmd.load(receptor_file, 'plip_1iep.pdb')
    print("step2")
    # Crie um complexo da molécula e receptor
    pymol.cmd.create('complex', 'receptor or ligand')
    print("step3")
    # Salve o complexo em um arquivo PDB
    pymol.cmd.save(output_pdb_file, 'complex')
    print("step4")
    # Feche o PyMOL
    pymol.cmd.quit()
    print("step5")
if __name__ == "__main__":
    # Substitua os caminhos pelos seus arquivos de entrada e saída
    molecule_file = '/home/instala/Documentos/Osvaldino/Validacao/CASF2016/Alvo1/Docking/1_Receptor_5Lig/tutoras/docking/1iep_receptor/1iep_ligand.pdbqt'
    receptor_file = '/home/instala/Documentos/Osvaldino/Validacao/CASF2016/Alvo1/Docking/1_Receptor_5Lig/tutoras/recep/1iep_receptor.pdbqt'
    output_pdb_file = '/home/instala/Documentos/Osvaldino/Validacao/CASF2016/Alvo1/Docking/1_Receptor_5Lig/tutoras/docking/1iep_receptor/plipython_1iep.pdb'

    # Chame a função para criar o complexo e salvar o arquivo PDB
    vina_results_to_pymol(molecule_file, receptor_file, output_pdb_file)
