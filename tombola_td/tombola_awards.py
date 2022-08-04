import random
import sys

class Awards:
  # Class that handle the Tombola awards
  small_awards = {"Sticker TD": 40, "Portachiavi TD": 10, 'Spilletta TD': 50, "Calamita TD": 50, "Quaderno TD": 10}
  
  big_awards = {"Coupon early bird Git - Github Fundamentals by Fabio Biondi": 2, "Biglietto online omaggio IDI Incontro DevOps Italia": 1, "Biglietto omaggio CssDay": 1, "Biglietto omaggio JsDay": 1, "Biglietto omaggio phpDay": 1, "Biglietto omaggio ContainerDay": 1, "Biglietto omaggio rubyday 2022": 1, "Biglietto omaggio vueday 2022": 1, "Biglietto omaggio reactjsday 2022": 1, "Biglietto omaggio angularday 2022": 1, "Treedom": 2, "Ebook a scelta su Packt": 5, "Tshirt TD": 5, "Cappellino TD": 5,  "Borraccia TD": 5, "Tazza TD": 5}


  def __is_awards_available(self, awards):
    """
    Method that check if there are available awards in a specifc dict

    :param awards: awards dict to check [small_awards|big_awards]
    :return: boolean
    """

    for quantity in awards.values():
      if quantity > 0:
        return True
    return False



  def __decrease_award_quantity(self, chosen_award, awards):
      """
      Method that given an available award decreases its available quantity

      :param chosen_award: the award for which the available quantity should be reduced
      """
      awards[chosen_award] = awards[chosen_award] - 1  


  def get_award(self, winner):
    """
    Method that chooses random a prize among those available

    :return: an available award
    """
    # create a list with only the available awards
    # if there are 2 awards, chose between big awards
    if len(winner.awards) == 2:
      awards = self.big_awards   
    elif len(winner.awards) <= 2:   # if not, between small awards
      awards = self.small_awards
      
    # if there are awards available
    if self.__is_awards_available(awards):
      
      available_awards = [a for a in awards if awards[a] > 0]
    
      # given the winner awards, create a list with the prizes you have not yet received so that you can choose a random only among those you have not yet
      available_awards_for_user = list(set(available_awards) - set(winner.awards))

      # generates the choice of an award among those available
      if available_awards_for_user:
        choosen_awards = random.choice(available_awards_for_user)
        self.__decrease_award_quantity(choosen_awards, awards)
      else:
        print("No available awards")
        sys.exit(1)

      return choosen_awards

    else:
      print("There are no more awards available")
      sys.exit(1)
