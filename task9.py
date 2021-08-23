def MassVote(NUM_CANDIDATES,CANDIDATES_VOTES):
    # Использование констант
    # Локализация текстового сообщения (в самом начале программы)
    VOTINGN_RESULT_STRING = ['majority winner','minority winner','no winner']
    VOTES_SORTED = sorted(CANDIDATES_VOTES, reverse = True)
    # Использование логической переменной для повышения читабельности
    equality_first_votes = VOTES_SORTED[0] == VOTES_SORTED[1]
    if NUM_CANDIDATES > 1 and equality_first_votes: return VOTINGN_RESULT_STRING[2]
    # Проверяем деление на "0"
    try:
        VOTES_RESULTAT = round((VOTES_SORTED[0] * 100 / sum(CANDIDATES_VOTES)),3) 
    except ZeroDivisionError:
        return 'division by zero'
    for i in range(NUM_CANDIDATES):
        if CANDIDATES_VOTES[i] == VOTES_SORTED[0]: position = ' ' + str(i+1)
    if VOTES_RESULTAT > 50: return VOTINGN_RESULT_STRING[0] + position
    else: return VOTINGN_RESULT_STRING[1] + position
#_________________________________________________________________________________________________________
import ctypes

class DynArray:
    
    def __init__(self):
        ...
    def __len__(self):
        ...
    def make_array(self, new_capacity):
        ...
    def __getitem__(self,i):
        ...
    def resize(self, new_capacity):
        ...
    def append(self, itm):
        ...
    def insert(self, item_insert_position, insert_element):
        ...
    def delete(self, position_deletion):
        self.__getitem__(position_deletion)
        del_new_DynArray = self.make_array(self.volume_DynArray)
        del_ndepend_counter = 0
        for position in range(self.count_el_DynArray):
            if position == position_deletion: 
                continue
            del_new_DynArray[del_ndepend_counter] = self.location_el_DynArray[position]
            del_ndepend_counter += 1
        self.location_el_DynArray = del_new_DynArray
        self.count_el_DynArray -= 1
        if self.count_el_DynArray < self.volume_DynArray // 2:
            # приведение вещественного числа к целому
            if int(self.volume_DynArray / 1.5) <= 16:
                new_volume_DynArray = 16
            else:
                # приведение вещественного числа к целому
                new_volume_DynArray = int(self.volume_DynArray / 1.5)
            self.resize(new_volume_DynArray)

#__________________________________________________________________________________________________________

class Node:
    ...

class OrderedList:
    ...
    def compares_num_values(self, first_values, last_values):
        ...
    def add_new_node_by_sorting(self, value_new_node):
        item_new_ordered_list = Node(value_new_node)
        if self.__sort_ascending is True: status_ascending = 1
        else: status_ascending = -1
        if self.head is None:
            self.head = item_new_ordered_list
            self.tail = item_new_ordered_list
        else:
            # Использование логической переменной для повышения читабельности
            found_num_values = (self.compares_num_values(self.head,item_new_ordered_list) == 
                                                         status_ascending)
            if found_num_values:
                self.head.prev = item_new_ordered_list
                item_new_ordered_list.next = self.head
                self.head = item_new_ordered_list
            else:
                node_ordered_list = self.head
                while node_ordered_list:
                    # Использование логической переменной для повышения читабельности
                    found_num_values = (self.compares_num_values(node_ordered_list,item_new_ordered_list) == 
                                                                 status_ascending)
                    if found_num_values:
                        item_new_ordered_list.prev = node_ordered_list.prev
                        item_new_ordered_list.next = node_ordered_list
                        node_ordered_list.prev.next = item_new_ordered_list
                        node_ordered_list.prev = item_new_ordered_list
                        item_new_ordered_list.next = node_ordered_list
                        return
                    node_ordered_list = node_ordered_list.next
                item_new_ordered_list.prev = self.tail  
                self.tail.next = item_new_ordered_list
                self.tail = item_new_ordered_list


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
class OrderedStringList(OrderedList):
    def __init__(self, el_sort_ascending):
        ...
    def compares_string_val(self, first_values, last_values):
        ...
#_________________________________________________________________________________________________________

def LineAnalysis(CHARACTER_STRING):
    is_Found = False
    REFERENCE_SYMBOL = '*'
    # Использование логической переменной для повышения читабельности
    # Проверка промежуточных результатов
    equality_el_string = CHARACTER_STRING == REFERENCE_SYMBOL * len(CHARACTER_STRING)
    if equality_el_string: 
        is_Found = True
        return is_Found
    # Использование логической переменной для повышения читабельности
    # Проверка промежуточных результатов
    equality_first_el = CHARACTER_STRING[0] != REFERENCE_SYMBOL
    equality_last_one_el = CHARACTER_STRING[len(CHARACTER_STRING)-1] != REFERENCE_SYMBOL
    if equality_first_el or equality_last_one_el:
        return is_Found
    first_formated_str = CHARACTER_STRING[1:len(CHARACTER_STRING)-1]
    last_formated_str = (first_formated_str.replace('*',',')).split(',')
    for i in range(len(last_formated_str)-1):
        if last_formated_str[i] != last_formated_str[i+1]: return is_Found
    is_Found = True
#________________________________________________________________________________________________________________
def codeEncripted(source_string):
    merged_string = source_string.replace(' ','')
    square_root_string = pow(len(merged_string),0.5) 
    # Использование логической переменной для повышения читабельности
    # приводим к целым числам, исключаем остаток
    equality_square_root = int(square_root_string //1) >= int(square_root_string % 1 * 10)
    if equality_square_root:
        number_of_rows_of_the_matrix = int(square_root_string % 1 * 10)
        # приводим к целым числам, исключаем остаток
        number_of_matrix_columns = int(square_root_string // 1)
    else: 
        # приводим к целым числам, исключаем остаток
        number_of_rows_of_the_matrix = int(square_root_string // 1)
        number_of_matrix_columns = int(square_root_string % 1 * 10)
    
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
