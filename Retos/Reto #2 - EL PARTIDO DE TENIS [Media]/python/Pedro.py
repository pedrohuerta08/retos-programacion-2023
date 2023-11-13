from enum import Enum
def juego_tenis(lista: list): 
    lista_puntos = ["Love","15","30","40"]
    puntos_p1 = 0
    puntos_p2 = 0
    finished = False
    if not finished:
        for element in lista:
            puntos_p1 += 1 if element == "P1" else 0
            puntos_p2 += 1 if element == "P2" else 0
            if puntos_p1 >= 3 and puntos_p2 >= 3:
                if abs(puntos_p1 -  puntos_p2) < 2:
                    print(f"Deuce" if puntos_p1 == puntos_p2 else "Ventaja P1" if puntos_p2 <
                          puntos_p1 else "Ventaja P2")
                else:
                    print("Ha ganado P1" if puntos_p1 > puntos_p2 else "Ha ganado P2")
                    finished = True
            else:
                print(f"{lista_puntos[puntos_p1]} - {lista_puntos[puntos_p2]}")

juego_tenis(["P1","P1","P2","P2","P1","P2","P1","P2","P2","P2"])
