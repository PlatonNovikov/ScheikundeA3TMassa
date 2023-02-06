def Count(el):
    listtotal = []
    while True:
        input1 = input("Will you add a element?")
        if input1.lower() == "y":
            elin = el[input("which one?")]
            howmuch = input("how much")
            listel = [elin] * int(howmuch)
            listtotal.extend(listel)
        else:
            break
    return listtotal



elements1 = {"H":1.008, "Li":6.941, "Na":22.99, "K":39.10, "Rb":85.47, "Cs":132.9, "Fr":223}
elements2 = {"Be":9.012, "Mg":24.31, "Ca":40.08, "Sr":87.62, "Ba":137.3, "Ra":226}
elements3 = {"Sc":44.96, "Y":88.91, "La":138.9, "Ac":227}
elements4 = {"Ti":47.87, "Zr":91.22, "Hf":178.5, "Rf":267}
elements5 = {"V":50.94, "Nb":92.91, "Ta":180.9, "Db":268}
elements6 = {"Cr":52.00, "Mo":95.94, "W":183.8, "Sg":269}
elements7 = {"Mn":54.94, "Tc":98, "Re":186.2, "Bh":270}
elements8 = {"Fe":55.85, "Ru":101.1, "Os":190.2, "Hs":269}
elements9 = {"Co":58.93, "Rh":102.9, "Ir":192.2, "Mt":278}
elements10 = {"Ni":58.69, "Pd":106.4, "Pt":195.1, "Ds":281}
elements11 = {"Cu":63.55, "Ag":107.4, "Au":197.0, "Rg":281}
elements12 = {"Zn":65.38, "Cd":112.4, "Hg":200.6, "Cn":285}
elements13 = {"B":10.81, "Al":26.98, "Ga":69.72, "In":114.8, "Ti":204.4, "Uut":286}
elements14 = {"C":12.01, "Si":28.09, "Ge":72.64, "Sn":118.7, "Pb":207.2, "Fl":289}
elements15 = {"N":14.01, "P":30.97, "As":74.92, "Sb":121.8, "Bi":209.0, "Uup":288}
elements16 = {"O":16.00, "S":32.06, "Se":88.96, "Te":127.6, "Po":209, "Lv":293}
elements17 = {"F":19.00, "Cl":35.45, "Br":79.90, "I":126.9, "At":210, "Uus":294}
elements18 = {"He":4.003, "Ne":20.18, "Ar":39.95, "Kr":83.80, "Xe":131.3, "Rn":222, "Uuo":294}
elements = elements1 | elements2 | elements3 | elements4 | elements5 | elements6 | elements7 | elements8 | elements9 | elements10 | elements11 | elements12 | elements13 | elements14 | elements15 | elements16 | elements17 | elements18
massa = Count(elements)
print (sum(massa))