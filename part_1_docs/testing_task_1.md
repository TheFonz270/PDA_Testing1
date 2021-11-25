### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:                        


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
    return "You have a total of" + total # return statement should be outside the loop (-indentation) or total will only = the value of the first card.
                                         # also would need to be str(total) to concatanate this way
  
```
