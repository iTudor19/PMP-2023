import random
import matplotlib.pyplot as plt

# Functie ce returneaza 0 sau 1 in functie de prob monedei
def arunca_moneda(probabilitate):
    return random.choices([0, 1], weights=[1 - probabilitate, probabilitate])[0]

numar_simulari=20000

def simuleaza_joc(numar_simulari):
    castiguri_p0 = 0
    castiguri_p1 = 0

# Pornim jocul
    for _ in range(numar_simulari):
        steme_p0= 0
        steme_p1= 0
        jucator_curent = random.choice([0, 1])

        # Daca incepe p0
        if jucator_curent == 0:
            steme_p0 = arunca_moneda(1/3)
            if steme_p0 == 1:
                ct=steme_p0 + 1
                while ct>0:
                    steme_p1 += arunca_moneda(1/2)
                    ct=ct-1
            # Vedem cin castiga meciul 
            if(steme_p0>=steme_p1):
                castiguri_p0+=1
            else:
                castiguri_p1+=1

        # Daca incepe p1
        else:
            
            steme_p1 = arunca_moneda(1/2)
            if steme_p1 == 1:
                ct=steme_p1 + 1
                while ct>0:
                    steme_p0 += arunca_moneda(1/3)
                    ct=ct-1
            # Vedem cin castiga meciul        
            if(steme_p1>=steme_p0):
                castiguri_p1+=1
            else:
                castiguri_p0+=1

    # Returnam jucatorul cu mai multe victorii
    if castiguri_p0>castiguri_p1:
        print("p0")
    else:
        print("p1")        

simuleaza_joc(numar_simulari)