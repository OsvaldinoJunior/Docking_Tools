from rdkit import Chem,  DataStructs

from rdkit.DataStructs import cDataStructs

################################################################################

def generate_rdkit_plif(residue_list, plif_list_all):

    #generates RDKit plif given list of residues in binding site and list of interacting residues

    plif_rdkit = DataStructs.ExplicitBitVect(len(residue_list), False)

    for index, res in enumerate(residue_list):

        if res in plif_list_all:

            print ('here')

            plif_rdkit.SetBit(index)

        else:

            continue

    return plif_rdkit
#########################################################################

plif_m006 = generate_rdkit_plif(residue_list, plif_list_m006)

plif_m009 = generate_rdkit_plif(residue_list, plif_list_m009)

plif_m004 = generate_rdkit_plif(residue_list, plif_list_m004)

