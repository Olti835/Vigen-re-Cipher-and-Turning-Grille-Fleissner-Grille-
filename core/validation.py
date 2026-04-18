def mode(choose_mode):
    choose_mode = choose_mode.lower()

    if choose_mode in ('enc', 'dec'):
        return True, '\nContinue'
    
    return False, "\nInvalid input. Use enc or dec."


def alg_validation(algorithm):
    algorithm = algorithm.lower()

    if algorithm in ('v', 't'):
        return True, "Good. \n"

    return False, "\nInvalid input. Use V or T."
 

# def continue_():
#     question = input('\nDo you want to continue(yes/no): ')
#     question = question.lower()

#     if question == 'yes':
#         print('\nContinue')
#         return True
#     else:
#         print('\nHava a good day!')
#         return False
