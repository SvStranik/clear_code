def MassVote(NUM_CANDIDATES,CANDIDATES_VOTES):
    VOTINGN_RESULT_STRING = ['majority winner','minority winner','no winner']
    VOTES_SORTED = sorted(CANDIDATES_VOTES, reverse = True)
    equality_first_votes = VOTES_SORTED[0] == VOTES_SORTED[1]
    if NUM_CANDIDATES > 1 and equality_first_votes: return VOTINGN_RESULT_STRING[2]
    try:
        VOTES_RESULTAT = round((VOTES_SORTED[0] * 100 / sum(CANDIDATES_VOTES)),3) 
    except ZeroDivisionError:
        return 'division by zero'
    for i in range(NUM_CANDIDATES):
        if CANDIDATES_VOTES[i] == VOTES_SORTED[0]: position = ' ' + str(i+1)
    # Завершение работы с переменной
    VOTES_SORTED = "None"
    if VOTES_RESULTAT > 50: return VOTINGN_RESULT_STRING[0] + position
    else: return VOTINGN_RESULT_STRING[1] + position


def LineAnalysis(CHARACTER_STRING):
    is_Found = False
    REFERENCE_SYMBOL = '*'
    equality_el_string = CHARACTER_STRING == REFERENCE_SYMBOL * len(CHARACTER_STRING)
    if equality_el_string: 
        is_Found = True
        return is_Found
    # Завершение работы с переменной
    equality_el_string = "***ERROR***"
    equality_first_el = CHARACTER_STRING[0] != REFERENCE_SYMBOL
    equality_last_one_el = CHARACTER_STRING[len(CHARACTER_STRING)-1] != REFERENCE_SYMBOL
    if equality_first_el or equality_last_one_el:
        return is_Found
    # Завершение работы с переменной
    equality_first_el, equality_last_one_el = "***ERROR***","***ERROR***"
    first_formated_str = CHARACTER_STRING[1:len(CHARACTER_STRING)-1]
    last_formated_str = (first_formated_str.replace('*',',')).split(',')
    for i in range(len(last_formated_str)-1):
        if last_formated_str[i] != last_formated_str[i+1]: return is_Found
    is_Found = True
    # Завершение работы с переменной
    first_formated_str,last_formated_str = "***ERROR***","***ERROR***"


def codeEncripted(source_string):
    merged_string = source_string.replace(' ','')
    square_root_string = pow(len(merged_string),0.5)
    # Завершение работы с переменной
    merged_string = "***ERROR***"
    equality_square_root = int(square_root_string //1) >= int(square_root_string % 1 * 10)
    if equality_square_root:
        number_of_rows_of_the_matrix = int(square_root_string % 1 * 10)
        number_of_matrix_columns = int(square_root_string // 1)
    else: 
        number_of_rows_of_the_matrix = int(square_root_string // 1)
        number_of_matrix_columns = int(square_root_string % 1 * 10)
    # Завершение работы с переменной
    square_root_string = -1
    equality_square_root = None
    while number_of_rows_of_the_matrix * number_of_matrix_columns < len(merged_string):
        number_of_rows_of_the_matrix += 1
    array_of_encrypted_data = []
    array_counter = 0
    for i in range(number_of_matrix_columns):
        temporary_array = []
        for j in range(number_of_rows_of_the_matrix):
            if array_counter == len(merged_string): break
            temporary_array.append(merged_string[array_counter])
            array_counter += 1
        array_of_encrypted_data.append(temporary_array)
    # Завершение работы с переменной
    array_counter = -1
    temporary_array = ["***ERROR***"]

    encrypted_string = ''
    for i in range(number_of_rows_of_the_matrix):
        for j in range(number_of_matrix_columns):
            if i < len(array_of_encrypted_data[j]):
                encrypted_string += array_of_encrypted_data[j][i]
        encrypted_string += ' '
    encrypted_string =  encrypted_string.strip()
    # Завершение работы с переменной
    number_of_rows_of_the_matrix = -1
    number_of_matrix_columns = -1
    array_of_encrypted_data = None
    return encrypted_string


def MaximumDiscount(DISCOUNT_STEP,PRICE_PURCHASE_ARRAY):
    prices_purchase_sort = sorted(PRICE_PURCHASE_ARRAY, reverse = True)
    purchase_discount = 0
    for i in range(DISCOUNT_STEP):
        if (i+1) % 3 == 0: purchase_discount += prices_purchase_sort[i]
    # Завершение работы с переменной
    prices_purchase_sort = None
    return purchase_discount


def MatrixTurn(matrix_data,NUMBER_OF_ROWS,NUMBER_OF_COLUMNS,NUM_SPINS):
    for j in range(NUM_SPINS):
        matrix_data_copy = matrix_data[:]
        # переменные инициализированны непосредственно перед циклом
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
         # Завершение работы с переменной  
        matrix_data_temp = "***ERROR***"
    # Завершение работы с переменной
    first_counter = -1
    last_counter = -1
    matrix_data_copy = "***ERROR***"
