# Dictionary of card value
# Aces care currently only one

# Hearts
ace_hearts = "Ace of Hearts"
two_hearts = "2 of Hearts"
three_hearts = "3 of Hearts"
four_hearts = "4 of Hearts"
five_hearts = "5 of Hearts"
six_hearts = "6 of Hearts"
seven_hearts = "7 of Hearts"
eights_hearts = "8 of Hearts"
nine_hearts = "9 of Hearts"
ten_hearts = "10 of Hearts"
jack_hearts = "Jack of Hearts"
queen_hearts = "Queen of Hearts"
king_hearts = "King of Hearts"

# Spades

ace_spades = "Ace of Spades"
two_spades = "2 of Spades"
three_spades = "3 of Spades"
four_spades = "4 of Spades"
five_spades = "5 of Spades"
six_spades = "6 of Spades"
seven_spades = "7 of Spades"
eights_spades = "8 of Spades"
nine_spades = "9 of Spades"
ten_spades = "10 of Spades"
jack_spades = "Jack of Spades"
queen_spades = "Queen of Spades"
king_spades = "King of Spades"


#Clubs
ace_clubs = "Ace of Clubs"
two_clubs = "2 of Clubs"
three_clubs = "3 of Clubs"
four_clubs = "4 of Clubs"
five_clubs = "5 of Clubs"
six_clubs = "6 of Clubs"
seven_clubs = "7 of Clubs"
eights_clubs = "8 of Clubs"
nine_clubs = "9 of Clubs"
ten_clubs = "10 of Clubs"
jack_clubs = "Jack of Clubs"
queen_clubs = "Queen of Clubs"
king_clubs = "King of Clubs"

ace_diamonds = "Ace of Diamonds"
two_diamonds = "2 of Diamonds"
three_diamonds = "3 of Diamonds"
four_diamonds = "4 of Diamonds"
five_diamonds = "5 of Diamonds"
six_diamonds = "6 of Diamonds"
seven_diamonds = "7 of Diamonds"
eights_diamonds = "8 of Diamonds"
nine_diamonds = "9 of Diamonds"
ten_diamonds = "10 of Diamonds"
jack_diamonds = "Jack of Diamonds"
queen_diamonds = "Queen of Diamonds"
king_diamonds = "King of Diamonds"

card_values = {ace_hearts: 1,
        two_hearts: 2,
        three_hearts: 3,
        four_hearts: 4,
        five_hearts: 5,
        six_hearts: 6,
        seven_hearts: 7,
        eights_hearts: 8,
        nine_hearts: 9,
        ten_hearts: 10,
        jack_hearts: 10,
        queen_hearts: 10, 
        king_hearts: 10,
        ace_diamonds: 1,
        two_diamonds: 2,
        three_diamonds: 3,
        four_diamonds: 4,
        five_diamonds: 5,
        six_diamonds: 6,
        seven_diamonds: 7,
        eights_diamonds: 8,
        nine_diamonds: 9,
        ten_diamonds: 10,
        jack_diamonds: 10,
        queen_diamonds: 10, 
        king_diamonds: 10,
        ace_spades: 1,
        two_spades: 2,
        three_spades: 3,
        four_spades: 4,
        five_spades: 5,
        six_spades: 6,
        seven_spades: 7,
        eights_spades: 8,
        nine_spades: 9,
        ten_spades: 10,
        jack_spades: 10,
        queen_spades: 10, 
        king_spades: 10,
        ace_clubs: 1,
        two_clubs: 2,
        three_clubs: 3,
        four_clubs: 4,
        five_clubs: 5,
        six_clubs: 6,
        seven_clubs: 7,
        eights_clubs: 8,
        nine_clubs: 9,
        ten_clubs: 10,
        jack_clubs: 10,
        queen_clubs: 10, 
        king_clubs: 10,
         }


hand_value = card_values[ace_hearts] + card_values[two_hearts] + card_values[jack_hearts] + card_values[ace_diamonds] + card_values[king_diamonds]

print(two_hearts, ace_hearts, jack_hearts, ace_diamonds, king_diamonds)

print(hand_value)

