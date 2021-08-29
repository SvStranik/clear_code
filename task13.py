def MassVote(NUM_CANDIDATES,CANDIDATES_VOTES):
    VOTINGN_RESULT_STRING = ['majority winner','minority winner','no winner']
    VOTES_SORTED = sorted(CANDIDATES_VOTES, reverse = True)
    equality_first_votes = VOTES_SORTED[0] == VOTES_SORTED[1]
    if NUM_CANDIDATES > 1 and equality_first_votes: return VOTINGN_RESULT_STRING[2]
    try:
        VOTES_RESULTAT = round((VOTES_SORTED[0] * 100 / sum(CANDIDATES_VOTES)),3) 
    except ZeroDivisionError:
        return 'division by zero'
    # Сдесь мы можем поменять условие цикла for и уйти от произвольношо доступа к моссиву
    # Было    
    #for i in range(NUM_CANDIDATES):
    #    if CANDIDATES_VOTES[i] == VOTES_SORTED[0]: position = ' ' + str(i+1)
    # Стало
    for counter,num_votes in enumerate(CANDIDATES_VOTES): 
        if num_votes == VOTES_SORTED[0]: position = ' ' + str(counter+1)
    # Также чтобы не запутаться с "i,j" даем им названия    
    VOTES_SORTED = "None"
    if VOTES_RESULTAT > 50: return VOTINGN_RESULT_STRING[0] + position
    else: return VOTINGN_RESULT_STRING[1] + position

def codeEncripted(source_string):
    merged_string = source_string.replace(' ','')
    SQUARE_ROOT_STRING = pow(len(merged_string),0.5) 
    equality_square_root = int(SQUARE_ROOT_STRING //1) >= int(SQUARE_ROOT_STRING % 1 * 10)
    if equality_square_root:
        number_of_rows_of_the_matrix = int(SQUARE_ROOT_STRING % 1 * 10)
        number_of_matrix_columns = int(SQUARE_ROOT_STRING // 1)
    else: 
        number_of_rows_of_the_matrix = int(SQUARE_ROOT_STRING // 1)
        number_of_matrix_columns = int(SQUARE_ROOT_STRING % 1 * 10)
    
    while number_of_rows_of_the_matrix * number_of_matrix_columns < len(merged_string):
        number_of_rows_of_the_matrix += 1
    array_of_encrypted_data = []
    array_counter = 0
    # В данном примере в цикле for мы работает с масивом без выполнения прямой индексации
    for i in range(number_of_matrix_columns):
        temporary_array = []
        for j in range(number_of_rows_of_the_matrix):
            if array_counter == len(merged_string): break
            temporary_array.append(merged_string[array_counter])
            array_counter += 1
        array_of_encrypted_data.append(temporary_array)
    encrypted_string = ''
    # В данном приемере чтобы не путаться с "i,j" можно дать им имена
    for rows in range(number_of_rows_of_the_matrix):
        for columns in range(number_of_matrix_columns):
            if rows < len(array_of_encrypted_data[columns]):
                encrypted_string += array_of_encrypted_data[columns][rows]
        encrypted_string += ' '
    encrypted_string =  encrypted_string.strip()
    return encrypted_string

def LineAnalysis(CHARACTER_STRING):
    is_Found = False
    REFERENCE_SYMBOL = '*'
    equality_el_string = CHARACTER_STRING == REFERENCE_SYMBOL * len(CHARACTER_STRING)
    if equality_el_string: 
        is_Found = True
        return is_Found
    equality_el_string = "***ERROR***"
    equality_first_el = CHARACTER_STRING[0] != REFERENCE_SYMBOL
    equality_last_one_el = CHARACTER_STRING[len(CHARACTER_STRING)-1] != REFERENCE_SYMBOL
    if equality_first_el or equality_last_one_el:
        return is_Found
    equality_first_el, equality_last_one_el = "***ERROR***","***ERROR***"
    first_formated_str = CHARACTER_STRING[1:len(CHARACTER_STRING)-1]
    last_formated_str = (first_formated_str.replace('*',',')).split(',')
    # Возможно чтобы не запутаться в индексации, можем определить сразу две строки и сравнить их елемены
    """for i in range(len(last_formated_str)-1):
        if last_formated_str[i] != last_formated_str[i+1]: """
    first_str = last_formated_str[:-1]
    last_str = last_formated_str[1:]
    for i in range(len(first_str)):
        if first_str[i] != last_str[i]:
            return is_Found
    is_Found = True
    first_formated_str,last_formated_str = "***ERROR***","***ERROR***"

def MaximumDiscount(DISCOUNT_STEP,PRICE_PURCHASE_ARRAY):
    prices_purchase_sort = sorted(PRICE_PURCHASE_ARRAY, reverse = True)
    purchase_discount = 0
    # В данной задаче мы также можем передать список в цикл for и пробежаться по данным
    # и не обращаясь по индексации произвести расчеты
    for i,j in enumerate(prices_purchase_sort):
        if (i+1) % DISCOUNT_STEP == 0: 
            purchase_discount += j
    """for i in range(DISCOUNT_STEP):
        if (i+1) % 3 == 0: purchase_discount += prices_purchase_sort[i]"""
    prices_purchase_sort = None
    return purchase_discount
