import random
suites=["Hearts","Diamonds","Spades","Clubs"]
cardFaces=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]


def pickACard():
    cardFace=random.choice(cardFaces)
    cardSuite=random.choice(suites)
    card=cardFace+" of %s"%(cardSuite)
    return card

hand=[]
for i in range(5):
    card=pickACard()
    if card not in hand:
        hand.append(card)
print(hand)

