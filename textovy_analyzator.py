"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Zuzana Soudná
email: zuza.soudna@gmail.com
discord: Zuzana S.#3996
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

uzivatele_hesla = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
odrazka = "-"

username = input("username: ")
password = input("password: ")
print(odrazka * 30)

if username in uzivatele_hesla.keys():
   if password in uzivatele_hesla.get(username):
      print("Welcome to the app,", username)
      print("We have 3 texts to be analyzed.") 
      print(odrazka * 30)
      selected_text_number = input("Enter a number btw. 1 and 3 to select: ")
      print(odrazka * 30)

      if selected_text_number.isdigit() and int(selected_text_number) in range(1,3):
         vybrany_text_c = TEXTS[int(selected_text_number) - 1]
         list_slov_z_vybraneho_textu = vybrany_text_c.split()
         
         list_slov_bez_interpunkce = []
         for kazde_slovo in list_slov_z_vybraneho_textu:
            slovo_bez_interpunkce = kazde_slovo.strip(".,!?")
            # list_slov_bez_interpunkce = [] NELZE, jinak se tu pořád zapisuje znovu prázdný!!!
            list_slov_bez_interpunkce.append(slovo_bez_interpunkce)
         #print(list_slov_bez_interpunkce)
   
         celkovy_pocet_slov = 0
         pocet_cisel = 0
         soucet_cisel = 0
         

         for kazde_slovo in list_slov_bez_interpunkce:
               celkovy_pocet_slov = celkovy_pocet_slov + 1   

         for kazde_slovo in list_slov_bez_interpunkce:      #!!!musí tu být znovu, jinak počítá bez těch číslic
               if kazde_slovo.isdigit() == True:
                  pocet_cisel = pocet_cisel + 1
                  #list_cisel.append(kazde_slovo)
                  soucet_cisel= soucet_cisel + int(kazde_slovo)
                  list_bez_cisel = list_slov_bez_interpunkce
                  list_bez_cisel.remove(kazde_slovo)
               
         
         print(celkovy_pocet_slov)
         pocet_slov_malymi_pismeny = 0
         pocet_slov_s_velkym_pismenem = 0
         pocet_slov_velkymi_pismeny = 0
         for kazde_slovo in list_bez_cisel:
            if kazde_slovo == kazde_slovo.lower():
               pocet_slov_malymi_pismeny = pocet_slov_malymi_pismeny + 1 
            elif kazde_slovo == kazde_slovo.title():   
               pocet_slov_s_velkym_pismenem = pocet_slov_s_velkym_pismenem + 1
            elif kazde_slovo == kazde_slovo.upper():
               pocet_slov_velkymi_pismeny = pocet_slov_velkymi_pismeny + 1
            
         #print(pocet_slov_malymi_pismeny)
         #print(pocet_slov_s_velkym_pismenem)
         #print(pocet_slov_velkymi_pismeny)
                    
         #print(list_bez_cisel)         
         
         #print(list_cisel)
         #print(soucet_cisel)
         print("There are ", celkovy_pocet_slov, "words in the selected text.")
         print("There are ", pocet_slov_s_velkym_pismenem, "titlecase words.")
         print("There are ", pocet_slov_velkymi_pismeny, "uppercase words.")
         print("There are ", pocet_slov_malymi_pismeny, "lowercase words.")
         print("There are ", pocet_cisel, "numeric strings.")
         print("The sum of all the numbers ", soucet_cisel)

         #_____________________________________________________________________________________
         list_slov_bez_interpunkce2 = []
         for kazde_slovo in list_slov_z_vybraneho_textu:
            slovo_bez_interpunkce2 = kazde_slovo.strip(".,!?")
            #list_slov_bez_interpunkce = [] NELZE, jinak se tu pořád zapisuje znovu prázdný!!!
            list_slov_bez_interpunkce2.append(slovo_bez_interpunkce2)
         #print(list_slov_bez_interpunkce)
         
         list_cetnosti = []
         #print(list_slov_bez_interpunkce)

         for kazde_slovo in list_slov_bez_interpunkce2:
            delka_slova = len(kazde_slovo)
            list_cetnosti.append(delka_slova)

         #print(list_cetnosti)
         list_cetnosti.sort()
         #print(list_cetnosti)

         list_cetnosti.reverse()
         max_pocet_pismen = list_cetnosti[0]
         #print(max_pocet_pismen)

         list_cislic = []

         for cislo in range(1,max_pocet_pismen + 1):
            list_cislic.append(cislo)

         #print(list_cislic)

         print(odrazka * 30)
         print("LEN| OCCURENCES |NR.")
         print(odrazka * 30)
         for cislo_x in list_cislic:
            cetnost_cisla_x = list_cetnosti.count(cislo_x) 
            if cetnost_cisla_x != 0:
               print(cislo_x, "|", "*" * cetnost_cisla_x,"|", cetnost_cisla_x )  

      else:
         print("Entered number not in range or not number")
  
else:
   print("unregistered user, terminating the program..")

print(odrazka * 30)


