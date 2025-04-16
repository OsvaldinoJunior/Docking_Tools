def similarity_plifs(plif_1, plif_2):

    sim = DataStructs.TanimotoSimilarity(plif_1, plif_2)

    print sim

    return sim
###################################################################

print similarity_plifs(plif_m006, plif_m009)

print similarity_plifs(plif_m006, plif_m004)

print similarity_plifs(plif_m009, plif_m004)