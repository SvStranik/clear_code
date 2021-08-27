def MassVote(NUM_CANDIDATES,CANDIDATES_VOTES):
    # Константа "VOTINGN_RESULT_STRING" содержит вывод текста результатов голосов. М данном примере 
    # можно было бы обойтись и без данной константы и в результате сразу вписать данные строки, но
    # в случае если надо поправить текст строк, то удобнее будет через константу 
    VOTINGN_RESULT_STRING = ['majority winner','minority winner','no winner']
    # Константа "VOTES_SORTED" содержит сортированный список голосов по возрастанию, константа написана
    # для удобства и наглядности, чтения кода. В данном примере можно было бы обойтись и без константы 
    VOTES_SORTED = sorted(CANDIDATES_VOTES, reverse = True)
    equality_first_votes = VOTES_SORTED[0] == VOTES_SORTED[1]
    if NUM_CANDIDATES > 1 and equality_first_votes: return VOTINGN_RESULT_STRING[2]
    try:
        VOTES_RESULTAT = round((VOTES_SORTED[0] * 100 / sum(CANDIDATES_VOTES)),3) 
    except ZeroDivisionError:
        return 'division by zero'
    for i in range(NUM_CANDIDATES):
        if CANDIDATES_VOTES[i] == VOTES_SORTED[0]: position = ' ' + str(i+1)
    VOTES_SORTED = "None"
    if VOTES_RESULTAT > 50: return VOTINGN_RESULT_STRING[0] + position
    else: return VOTINGN_RESULT_STRING[1] + position


def LineAnalysis(CHARACTER_STRING):
    is_Found = False
    # Константа "REFERENCE_SYMBOL", по ней данный пример делает форматирование (сравнение) входящих
    # строк. Данную константу можно опустить, но тогда в случае если мы захотим форматировать (сравнивать)
    # строки, нам придется в тексте кода выискива символ форматирования, что не удобно.
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
    for i in range(len(last_formated_str)-1):
        if last_formated_str[i] != last_formated_str[i+1]: return is_Found
    is_Found = True
    first_formated_str,last_formated_str = "***ERROR***","***ERROR***"

def codeEncripted(source_string):
    merged_string = source_string.replace(' ','')
    # Константа "SQUARE_ROOT_STRING", ее можно было бы сразу привести к целому числу
    # "SQUARE_ROOT_STRING = int(pow(len(merged_string),0.5))", тогда мы можем убрать в части кода преодразование
    # "int", но учитывая что мы имеем дело с деление и чтобы не путаться, константу мы не приводим к целому числу
    # а по тексту кода делаем приводим переменные к "int"
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
    for i in range(number_of_matrix_columns):
        temporary_array = []
        for j in range(number_of_rows_of_the_matrix):
            if array_counter == len(merged_string): break
            temporary_array.append(merged_string[array_counter])
            array_counter += 1
        array_of_encrypted_data.append(temporary_array)
    encrypted_string = ''
    for i in range(number_of_rows_of_the_matrix):
        for j in range(number_of_matrix_columns):
            if i < len(array_of_encrypted_data[j]):
                encrypted_string += array_of_encrypted_data[j][i]
        encrypted_string += ' '
    encrypted_string =  encrypted_string.strip()
    return encrypted_string
