class TombolaHelper:

    @staticmethod
    def read_file(filename):
        """
        Method that read the content of a file
        
        :param filename: the path of the partecipants file
        :return: list of all names in the file
        """
        with open(filename, 'r') as file:
            partecipants = [line.strip().title() for line in file]
            return partecipants


class PrintHelper:

    @staticmethod
    def print_welcome_text():
        welcome_text = 'Ｗｅｌｃｏｍｅ ｔｏ\nＴｏｍｏｒｒｏｗｄｅｖｓ Ｔｏｍｂｏｌａ\n'
        print(welcome_text)

    @staticmethod
    def print_winner(number, winner, award):
        winner = """
        ╔══════════════════════════════════╗
        ║       Tombola TomorrowDevs       ║  
        ╠══════════════════════════════════╣
        ║ Winner: {:^20}     ║
        ║ Number: {:^20}     ║
        ║ Award : {:^20}     ║
        ╚══════════════════════════════════╝
          """.format(winner, number, award)

        print(winner)
    
    @staticmethod
    def print_residual_awards(awards):
        print("NO MORE NUMBERS!\n")
        
        residual_small_awards = [a for a in awards.small_awards if awards.small_awards[a] > 0]

        if len(residual_small_awards) > 0:
          print("Residual small awards:")
          for award, quantity in awards.small_awards.items():
            if quantity > 0:
              print(f'{award}, quantity: {quantity}')
        
        residual_big_awards = [a for a in awards.big_awards if awards.big_awards[a] > 0]
        if len(residual_big_awards) > 0:
            print("\nResidual big awards:")
            for award, quantity in awards.big_awards.items():
              if quantity > 0:
                print(f'{award}, quantity: {quantity}')


    @staticmethod
    def print_partecipants_awards(partecipants):
        print()
        for partecipant in partecipants:
          print(f'{partecipant.name}:')
          for a in partecipant.awards:
            print(f'-{a}')
            #print(a, end= ' ')
          print('\n')
      