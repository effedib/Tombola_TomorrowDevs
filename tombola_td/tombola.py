
import random

from tombola_td.tombola_awards import Awards
from tombola_td.tombola_card import Card
from tombola_td.tombola_partecipant import Partecipant
from tombola_td.tombola_helper import PrintHelper


class Tombola:

    def __init__(self, partecipant):
        self.partecipants = partecipant
        self.numbers = random.sample(range(1, len(self.partecipants) * 3 + 1), len(self.partecipants) * 3)


    def get_partecipant_card_numbers(self):

        """
        Method assigning 3 numbers (one card) for each participant
        """
        count = 0

        # assigns 3 numbers from the list for each participant
        for index, name in enumerate(self.partecipants):
            user_num = self.numbers[count:count + 3]  # increment the list index
            user_card = Card()
            user_card.n1 = user_num[0]
            user_card.n2 = user_num[1]
            user_card.n3 = user_num[2]

            partecipant = Partecipant(name, user_card)
            self.partecipants[index] = partecipant
            count += 3


    def __retrieve_winner(self, number):
        """
        Method that get the winner for the chosen number

        Search among all participants who owns the number extracted

        :param number: the extracted number
        :return: The winning participant as object
        """
        for partecipant in self.partecipants:
            if number in [partecipant.card.n1, partecipant.card.n2, partecipant.card.n3]:
                return partecipant


    def __assign_award(self, award, winner):
        """
        Method that awards a prize to the winner

        :param award: the choosen award to assign 
        :param winner: the participant to whom the prize is awarded as object
        """
        for partecipant in self.partecipants:
            if partecipant.name == winner.name:
                partecipant.awards.append(award)
                break


    def get_extraction(self):

        random.shuffle(self.numbers)  # shuffle the actual random numbers list

        for number in self.numbers:
            user_input = ''#input('Enter blank to extract a number: ')

            if not user_input:  # if enter blank
                winner = self.__retrieve_winner(number)  # get the winner

                award = Awards().get_award(winner)

                # assign award to the winner
                self.__assign_award(award, winner)
                PrintHelper.print_winner(number, winner.name, award)

            elif user_input == 'exit':
                return -1

        PrintHelper().print_residual_awards(Awards())
        PrintHelper().print_partecipants_awards(self.partecipants)