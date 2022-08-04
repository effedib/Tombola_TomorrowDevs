from tombola_td.tombola_helper import TombolaHelper, PrintHelper
from tombola_td.tombola import Tombola


class Start:
    @staticmethod
    def start():
        PrintHelper.print_welcome_text()

        partecipant = TombolaHelper.read_file('partecipants.txt')
        tombola = Tombola(partecipant)
        tombola.get_partecipant_card_numbers()
        tombola.get_extraction()


Start.start()
