# p7 : To read a card as input and output if the card is lucky or not.

c=input("Enter Any Suit with Card : ")

suit,card=c.split()

if(suit=='diamond' or (suit=='spade' and card=='ace') or card=='king'):
  print("Card is Lucky")
else:
  print("Please,try next time")