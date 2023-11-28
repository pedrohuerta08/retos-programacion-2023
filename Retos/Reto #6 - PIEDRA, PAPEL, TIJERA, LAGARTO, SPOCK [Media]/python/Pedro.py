#  Crea un programa que calcule quien gana más partidas al piedra,
#  * papel, tijera, lagarto, spock.
#  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#  * - La función recibe un listado que contiene pares, representando cada jugada.
#  * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#  *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
#  * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
#  * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
#  */
def pipatilasp(partida):
    tijeras_gana = ["🦎", "📄"]

    papel_gana = ["🗿","🖖"]

    piedra_gana = ["✂️","🦎"]

    lagarto_gana = ["📄","🖖"]

    spock_gana = ["🗿","✂️"]

    contador_p1 = 0
    contador_p2 = 0
    for i in range(0,len(partida)):
        if partida[i][0] == "✂️":
            if partida[i][1] in tijeras_gana:
                contador_p1 += 1
            elif partida[i][1] == partida[i][0]:
                contador_p1 += 1
                contador_p2 += 1
            else:
                contador_p2 += 1
        elif partida[i][0] == "📄":
            if partida[i][1] in papel_gana:
                contador_p1 += 1
            elif partida[i][1] == partida[i][0]:
                contador_p1 += 1
                contador_p2 += 1
            else:
                contador_p2 += 1
        elif partida[i][0] == "🗿":
            if partida[i][1] in piedra_gana:
                contador_p1 += 1
            elif partida[i][1] == partida[i][0]:
                contador_p1 += 1
                contador_p2 += 1
            else:
                contador_p2 += 1
        elif partida[i][0] == "🦎":
            if partida[i][1] in lagarto_gana:
                contador_p1 += 1
            elif partida[i][1] == partida[i][0]:
                contador_p1 += 1
                contador_p2 += 1
            else:
                contador_p2 += 1
        elif partida[i][0] == "🖖":
            if partida[i][1] in spock_gana:
                contador_p1 += 1
            elif partida[i][1] == partida[i][0]:
                contador_p1 += 1
                contador_p2 += 1
            else:
                contador_p2 += 1
        else:
            print("No has metido un elemento del juego")
    if contador_p1 > contador_p2:
        print("Ha ganado P1")
    elif contador_p2 > contador_p1:
        print("Ha ganado P2")
    else:
        print("Empate")

pipatilasp(partida= [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")])               



def piedra_papel_tijeras_lagarto_spock(games):
    rules = { "✂️" : ["🦎", "📄"], 
             "📄":["🗿","🖖"],
             "🗿":["✂️","🦎"],
             "🦎":["📄","🖖"],
             "🖖":["🗿","✂️"]
    }
    points_p1 = 0
    points_p2 = 0
    for game in games:
        if game[1] in rules[game[0]]:
            points_p1 +=1
        elif game[0] == game[1]:
            points_p1 += 1
            points_p2 += 1
        else:
            points_p2 += 1
    print("Player1" if points_p1 > points_p2 else "Player2" if points_p2 > points_p1 else "Tie")


piedra_papel_tijeras_lagarto_spock(games= [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")])   