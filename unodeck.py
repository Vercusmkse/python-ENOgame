import random

def buildDeck():
    deck = []
    colours = ["Red", "Green", "Yellow", "Blue"]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw Two", "Skip", "Reverse"]
    wilds = ["Wild", "Wild Draw Four"]
    
    for colour in colours:
        for value in values:
            cardVal = "{} {}".format(colour, value)
            deck.append(cardVal)
            if value != 0:
                deck.append(cardVal)
    
    for i in range(4):
        deck += wilds
    return deck

def draw_Cards(numCards):
    cardsDrawn = []
    for x in range (numCards):
        cardsDrawn.append(uno_deck.pop(0))
    return cardsDrawn

def showHand(player, playerHand):
    print("player {}'s Turn".format(player+1))
    print("your Hand")
    print("----------")
    y = 1
    for card in playerHand:
        print("{}) {}".format(y, card))
        y += 1
    print("")

def valid(colour, value, playerHand):
    for card in playerHand:
        if "Wild" in card:
            return True
        elif colour in card or value in card:
            return True
    return False

uno_deck = buildDeck()
random.shuffle(uno_deck)
discards = []

players = [] #List to store player cards
playerNames = [] #List to store player names
colours = ["Blue", "Red", "Green", "Yellow"]
num_Players = None
print("Enter --help to display the rules of the game\n")

num_Players = int(input("how many players?"))
if num_Players == "--help" or num_Players == "--resume":
    input(num_Players)
else:
    num_Players = int(num_Players)
    while len(playerNames) < num_Players:
        tempName = input("Enter player's name: ")
        if tempName == "--help" or tempName == "--resume":
            input(tempName)
        else:
            playerNames.append(tempName)
            players.append(draw_Cards(7))


print("The cards are:")
for (x,y) in zip(playerNames, players):
    print("Player {} has {}".format(x, y))
print("")

player_Turn = 0
colours = ["Red", "Green", "Yellow", "Blue"]
Direction = 1
playing = True
discards.append(uno_deck.pop(0))
split_Card = discards[0].split(" ", 1)
current_colour = split_Card[0]
if current_colour != "Wild":
    card_Val = split_Card[1]
else:
    card_Val = "any"

while playing:
    showHand(player_Turn,players[player_Turn])
    print("card on top of discard pile: {}".format(discards[-1]))
    if valid(current_colour, card_Val,players[player_Turn]):
        card_chosen = int(input("which card do you want to play? "))
        while not valid(current_colour, card_Val,[players[player_Turn][card_chosen-1]]):
            card_chosen = int(input("Not a valid card. which card do you want to play? "))
        print("you play {}".format(players[player_Turn][card_chosen-1]))
        discards.append(players[player_Turn].pop(card_chosen-1))
    else:
        print("you can't play. you have to draw a card.")
        players[player_Turn].extend(draw_Cards(1))
    print("")
    
    #check if the player won
    if len(players[player_Turn]) == 0:
        playing = False
        winner = "player {}".format(player_Turn+1)
    #check specail cards
    split_Card = discards[-1].split(" ", 1)
    current_colour = split_Card[0]
    if len(split_Card) == 1:
        card_Val = "Any"
    else:
        card_Val = split_Card[1]
    if current_colour == "Wild":
        for x in range(len(colours)):
            print("{}) {}".format(x+1, colours[x]))
        newColour = int(input("what colour would you like to choose? "))
        while newColour < 1 or newColour > 4:
            newColour = int(input("Invalid option. what colour would you like to choose? "))
        current_colour = colours[newColour-1]
    if card_Val == "Reverse":
        Direction = Direction * -1
    elif card_Val == "Skip":
        player_Turn += Direction
        if player_Turn >= num_Players:
            player_Turn = 0
        elif player_Turn < 0:
            player_Turn = num_Players-1
    elif card_Val == "Draw Two":
        playerDraw = player_Turn + Direction
        if player_Turn == num_Players:
            player_Turn = 0
        elif player_Turn < 0:
            player_Turn = num_Players-1
        players[player_Turn].extend(draw_Cards(4))
    elif card_Val == "Wild Draw Four ":
        playerDraw = player_Turn + Direction
        if player_Turn == num_Players:
            player_Turn = 0
        elif player_Turn < 0:
            player_Turn = num_Players-1
        players[player_Turn].extend(draw_Cards(4))
        print("")


    player_Turn += Direction
    if player_Turn >= num_Players:
        player_Turn = 0
    elif player_Turn < 0:
        player_Turn = num_Players-1

print("Game over")
print("{} is the Winner!".format(winner))