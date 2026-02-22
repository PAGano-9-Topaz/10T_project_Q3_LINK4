from pyscript import display, document

def intrams(e):

    document.getElementById('output1').innerHTML=" "
    Section = document.getElementById("Select2").value

    TP = ["Abdullah, Abeleda, Arce, Arias, Bonzon, Cajucom, Catimbang, Cotioco, Choi, Daradal, Enriquez, Escobar, Espina, Gano, Garcia, Kaur, Ong, Rufo, Sanchez, Santos, Tan, Vilale, Yao, Zosa"]
    SP = "Unfortunately we are lacking information about Sapphire. In the meantime, look at the other sections."
    RB = ["Agena, Ala, Baring, Baylon, Brodhagen, Cabatingan, Cañete, Dimaculangan, Evangelista, Galang, Garbles, Gonzales, Jamet, Ledesma, Nacino, Nardo, Oliveros, Oldmedo, Ong, Rebadulla, Reyes, Sangreo, Villafuerte, Villegas, Yao"]
    EM = ["Ibay, Barrientos, Sidhu, Coeli, Dellejero, Franzeska-Delacruz, Lan-Delacruz, Gozum, Precones, De mata, Antes, Yvonne Casal, Mamauag, Apostol, David, Ramos, Lozano, Zaragoza, Tiu, Villamayor, Fukuda, Navarro"]
    
    

    if Section == 'TPZ':
        for topaz in TP:
            display(topaz, target='output1')
    elif Section == 'SPE':
            display(SP, target='output1')
    if Section == 'RBY':
        for ruby in RB:
            display(ruby, target='output1')
    if Section == 'EMD':
        for emerald in EM:
            display(emerald, target='output1')

    

