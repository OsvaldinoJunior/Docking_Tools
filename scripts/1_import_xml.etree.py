import xml.etree.ElementTree as ET
################################################################################

def generate_plif_lists(report_file, residue_list, lig_ident):

    
    #uses report.xml from PLIP to return list of interacting residues and update list of residues in binding site

        plif_list_all = []

        tree = ET.parse(report_file)

        report_file = ('m004/report.xml', 'm006/report.xml', 'm009/report.xml')

        root = tree.getroot()

        #list of residue keys that form an interaction

        for binding_site in root.findall('bindingsite'):

                nest = binding_site.find('identifiers')

                lig_code = nest.find('hetid')

                if str(lig_code.text) == str(lig_ident):

                        #get the plifs stuff here

                        nest_residue = binding_site.find('bs_residues')

                        residue_list_tree = nest_residue.findall('bs_residue')

                        for residue in residue_list_tree:

                                res_id = residue.text

                                dict_res_temp = residue.attrib

                                if res_id not in residue_list:

                                        residue_list.append(res_id)

                                if dict_res_temp['contact'] == 'True':

                                        if res_id not in plif_list_all:

                                                plif_list_all.append(res_id)

        return plif_list_all, residue_list

residue_list =[]
###############################################################################

plif_list_m006, residue_list = generate_plif_lists('m006/report.xml', residue_list, 'EDO')

plif_list_m009, residue_list = generate_plif_lists('m009/report.xml', residue_list, 'EDO')

plif_list_m004, residue_list = generate_plif_lists('m004/report.xml', residue_list, 'EDO')

print(plif_list_m004)
print(plif_list_m006)
print(plif_list_m009)
print(residue_list)

print("SUCESSFULLLLLLLLLLLLLLL")