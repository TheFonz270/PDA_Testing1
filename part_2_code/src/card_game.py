### Testing task 2 code:

# Carry out dynamic testing on the code below.

# Correct the errors below that you spotted in task 1.

class CardGame:

#   def check_for_ace(self, card):
#     if card.value == 1:
#       return True
#     else:
#       return False
   

#   def highest_card(self, card1, card2):
#     if card1.value > card2.value:
#       return card1
#     else:
#       return card2

#   def cards_total(self, cards):
#     total = 0
#     for card in cards:
#       total += card.value
#     return "You have a total of" + str(total)

  def check_for_ace(self, card):
      if card.value = 1:                 # = should be ==, to compare rather than set the value.
        return True
      else                               # this line needs a : after else.
        return False
    

    dif highest_card(self, card1 card2): # dif should be def, and a comma is missing from after card1.
    if card1.value > card2.value:        # if should be indented (increasing indentation of everything below by 1 tab)
      return card                        # Should be return card1.
    else:
      return card2
    


  def cards_total(self, cards):          # missing indentation (increasing indentation of everything below by 1 tab)
    total                                # total should be defined as zero, variable is not initialised here.
    for card in cards:
      total += card.value
      return "You have a total of" + total
