# num_doors - количесвто дверей(задается по условию и будет не изменяемой) 
def shiftDoor(doors_status,closing_door_step):
    for i in range(closing_door_step-1,len(doors_status),closing_door_step):
        if doors_status[i] == '0': doors_status[i] = '1'
        else: doors_status[i] = '0'
    return doors_status
def Keymaker(NUM_DOORS,closing_door_step=2):
    if NUM_DOORS == 1: return '1' 
    doors_status = ['1'] * NUM_DOORS
    while closing_door_step < NUM_DOORS:
        shiftDoor(doors_status,NUM_DOORS)
        closing_door_step +=1
    else:
        if doors_status[NUM_DOORS-1] == '0': doors_status[NUM_DOORS-1] = '1'
        else: doors_status[NUM_DOORS-1] = '0'
    return ''.join(doors_status)

# charcter_string - дается по условию и является не изменным параметром
# reference_symbol = '*' - параметр по которому происходит сравнение и является не изменной
def LineAnalysis(CHARACTER_STRING):
    is_Found = False
    REFERENCE_SYMBOL = '*'
    if CHARACTER_STRING == REFERENCE_SYMBOL * len(CHARACTER_STRING): 
        is_Found = True
        return is_Found
    if (CHARACTER_STRING[0] != REFERENCE_SYMBOL or 
        CHARACTER_STRING[len(CHARACTER_STRING)-1] != REFERENCE_SYMBOL):
        return is_Found
    first_formated_str = CHARACTER_STRING[1:len(CHARACTER_STRING)-1]
    last_formated_str = (first_formated_str.replace('*',',')).split(',')
    for i in range(len(last_formated_str)-1):
        if last_formated_str[i] != last_formated_str[i+1]: return is_Found
    is_Found = True
    return is_Found

# num_candidates - количество кондидатов, будет не изменной и задается по условию
# candidates_votes - голоса кандидатов, также не изменяемая
# voting_result_string - строки результатов голосования, не изменяемо
# votes_sorted - отсортированные голоса, не изменятся
# votes_resultat - результат голосов, не изменяется
def MassVote(NUM_CANDIDATES,CANDIDATES_VOTES):
    VOTINGN_RESULT_STRING = ['majority winner','minority winner','no winner']
    VOTES_SORTED = sorted(CANDIDATES_VOTES, reverse = True)
    if NUM_CANDIDATES > 1 and VOTES_SORTED[0] == VOTES_SORTED[1]: return VOTINGN_RESULT_STRING[2]
    VOTES_RESULTAT = round((VOTES_SORTED[0] * 100 / sum(CANDIDATES_VOTES)),3) 
    for i in range(NUM_CANDIDATES):
        if CANDIDATES_VOTES[i] == VOTES_SORTED[0]: position = ' ' + str(i+1)
    if VOTES_RESULTAT > 50: return VOTINGN_RESULT_STRING[0] + position
    else: return VOTINGN_RESULT_STRING[1] + position

# number_of_rows, number_of_columns,num_spins кол-во строк, столбцов, вращений является не изменной
def MatrixTurn(matrix_data,NUMBER_OF_ROWS,NUMBER_OF_COLUMNS,NUM_SPINS):
    for j in range(NUM_SPINS):
        matrix_data_copy = matrix_data[:]
        first_counter = 1
        last_counter = 0
        for i in range(NUMBER_OF_ROWS):
            matrix_data_temp = ''
            if i+1 < NUMBER_OF_ROWS: 
                matrix_data_temp = matrix_data_copy[i+1][:first_counter]
            matrix_data_temp += matrix_data_copy[i][last_counter:NUMBER_OF_COLUMNS - first_counter]
            if i > 0: 
                matrix_data_temp += matrix_data_copy[i-1][NUMBER_OF_COLUMNS - last_counter:] 
            matrix_data[i] = matrix_data_temp
            if i >= NUMBER_OF_ROWS - NUMBER_OF_COLUMNS // 2 and i + 1 > NUMBER_OF_ROWS // 2:
                last_counter -= 1
            if last_counter < NUMBER_OF_COLUMNS // 2 and  i + 1 <= NUMBER_OF_ROWS // 2: 
                last_counter += 1
            if i+1 >= NUMBER_OF_ROWS - NUMBER_OF_COLUMNS //2 and i + 1 >= NUMBER_OF_ROWS // 2:
                first_counter -= 1
            if first_counter < NUMBER_OF_COLUMNS // 2 and  i + 1 < NUMBER_OF_ROWS // 2:
                first_counter += 1   

# discount_step - указывает на каждую бесплатную вещь, не изменяется
# price_purchase_array - список цен покупок вещей, не изменен
def MaximumDiscount(DISCOUNT_STEP,PRICE_PURCHASE_ARRAY):
    prices_purchase_sort = sorted(PRICE_PURCHASE_ARRAY, reverse = True)
    purchase_discount = 0
    for i in range(DISCOUNT_STEP):
        if (i+1) % 3 == 0: purchase_discount += prices_purchase_sort[i]
    return purchase_discount

# text_data - задается текст, не изменяется
# text_symbol_print, cost_symbol_print - параметры программы не изменяемы
def PrintingCosts(TEXT_DATA):
    TEXT_SYMBOL_PRINT = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',',
                        '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8',
                        '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D',
                        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
                        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\',
                        ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                        'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
    COST_SYMBOL_PRINT = [0,9,6,24,29,22,24,3,12,12,17,13,7,7,4,10,22,19,22,23,21,27,26,16,
                        23,26,8,11,10,14,10,15,32,24,29,20,26,26,20,25,25,18,18,21,16,
                        28,25,26,23,31,28,25,16,23,19,26,18,14,22,18,10,18,7,8,3,23,25,
                        17,25,23,18,30,21,15,20,21,16,22,18,20,25,25,13,21,17,17,13,19,
                        13,24,19,18,12,18,9]    
    
    printing_costs = 0
    for i in range(len(TEXT_DATA)):
        if TEXT_DATA[i] in TEXT_SYMBOL_PRINT:
            printing_costs += COST_SYMBOL_PRINT[TEXT_SYMBOL_PRINT.index(TEXT_DATA[i])]
        else:
            printing_costs += 23
    return printing_costs
