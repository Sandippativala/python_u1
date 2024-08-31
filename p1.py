# p1 : A card is drawn at random from a deck of well-suffled.find the probability 
#      of if being neither a king nor a spade.

Total_card=52
Kings=4
Spades= 13
neither_king_nor_spade=Total_card-Kings-Spades+1
probability=neither_king_nor_spade/Total_card
print("------------probability------------")
print("The Probability of drawing a card that is neither a king nor a spade is :",probability)
print("-----------------------------------")