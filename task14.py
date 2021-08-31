# Функция высчитывает кол-во тонера требуемого для его печати. Используется таблица 
# раскладки символов ASCII. В случае неучтенного символа в "TEXT_SYMBOL_PRINT" 
# используется значение "23"

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

# Функция, подсчитывает количество голосов "CANDIDATES_VOTES", кондидатов "NUM_CANDIDATES"
# Выводит результат победителя "VOTINGN_RESULT_STRING"

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
    VOTES_SORTED = "None"
    if VOTES_RESULTAT > 50: return VOTINGN_RESULT_STRING[0] + position
    else: return VOTINGN_RESULT_STRING[1] + position


# Функция определяет максимальную скидку при покупке товаров. Получаем на вход "DISCOUNT_STEP"
# аукционный товар и список цен на те товары которые необходимо преобрести "PRICE_PURCHASE_ARRAY"
def MaximumDiscount(DISCOUNT_STEP,PRICE_PURCHASE_ARRAY):
    prices_purchase_sort = sorted(PRICE_PURCHASE_ARRAY, reverse = True)
    purchase_discount = 0
    for i,j in enumerate(prices_purchase_sort):
        if (i+1) % DISCOUNT_STEP == 0: 
            purchase_discount += j
    prices_purchase_sort = None
    return purchase_discount


# Функция распознает закономерность в тексте изображений точек и звездочек. При 
# правильной закономерности текст считаестя корректным. 
# На вход получаем строку "CHARACTER_STRING"

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
    first_str = last_formated_str[:-1]
    last_str = last_formated_str[1:]
    for i in range(len(first_str)):
        if first_str[i] != last_str[i]:
            return is_Found
    is_Found = True
    first_formated_str,last_formated_str = "***ERROR***","***ERROR***"


# Функция вращает елементы матрици по часовой стрелке относительно ее центра.  
# Получает на вход (по ссылке!) массив строк "matrix_data" и вращает ее на "NUMBER_OF_ROWS"
# Минимальное значение "NUMBER_OF_COLUMNS, NUM_SPINS" обязательно четное!

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
        matrix_data_temp = "***ERROR***"
    first_counter = -1
    last_counter = -1
    matrix_data_copy = "***ERROR***"


# Функция вычисляет заранее двери которые будут открыты по завершению работы мастера ключей.
# На вход получаем количество дверей "NUM_DOORS", не обязательный пораметр "closing_door_step"
# шаг закрытых дверей и выводим список-результат функции "doors_status"

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


class Node:
    def __init__(self, value_node):
        self.value = value_node
        self.prev = None
        self.next = None


class OrderedList:
    ...

    def compares_num_values(self, first_values, last_values):
        ...

    def add_new_node_sorting(self, value_new_node):
        ...

    def searches_node_value(self, value_node):
        ...        
        
    def del_node_by_value(self, value_node,del_all_node=False):
        ...

    def clears_order_list(self, el_sort_ascending):
        ...

    def num_nodes_defines(self):
        ...

    def generates_list_nodes(self):
        ...

# Наследник текущего класса, который работает только со строковым типом.

class OrderedStringList(OrderedList):
    def __init__(self, el_sort_ascending):
        super(OrderedStringList, self).__init__(el_sort_ascending)

    def compares_string_val(self, first_values, last_values):
        if first_values.value.rstrip().lstrip() < last_values.value.rstrip().lstrip(): return -1
        elif first_values.value.rstrip().lstrip() == last_values.value.rstrip().lstrip(): return 0
        else: return 1
