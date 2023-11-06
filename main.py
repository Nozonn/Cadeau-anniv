import time
import pyautogui as pg
import pyperclip as pc

def _workaround_write(text):
    pc.copy(text)
    pg.hotkey('ctrl', 'v')
    pc.copy('')


heure_cible = 11

occ = 0

name = "Enzo"
starting = "Bon Anniversaire"
txt = f"{starting} {name} !!!!"
txt_s = txt.split()

al = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z !"
al = al.split()

word = []

print("Lancement !")

while True:
    heure_actuelle = time.localtime().tm_hour  # Obtenir l'heure actuelle
    
    if heure_actuelle == heure_cible:
        print(f"Il est {heure_cible}h. L'action est en cours d'exécution.")
        time.sleep(5)    
        
        while occ < 100000:
            word = []
            for idx in range(4):
                for i in txt_s[idx]:
                    word.append(" ")
                    for j in al:
                        occ += 1
                        if i == j:
                            word.append(j)
                            _workaround_write("".join(word) + j + f"\nCadeau {occ} !!")
                            pg.press("Enter")
                            break
                        else:
                            _workaround_write("".join(word) + j + f"\nCadeau {occ} !!")
                            print("".join(word) + j)
                            pg.press("Enter")
                        time.sleep(0.5)
                    time.sleep(0.5)
                word.append(" ")
                time.sleep(0.5)
        break
    else:
        time.sleep(60)
