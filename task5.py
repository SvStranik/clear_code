# Задание 3.1
# 1
def SubtractionModulo(firs_input_string,last_input_string):
    if firs_input_string == last_input_string: return '0'
    if int(firs_input_string) < int(last_input_string):
        firs_input_string,last_input_string = last_input_string,firs_input_string 
    last_input_string = last_input_string.rjust(len(firs_input_string),'0')
    resultat_string, temporary_variable = '', 0
    for i in range(len(firs_input_string)-1,-1,-1):
        temporary_index = (10 + int(firs_input_string[i])- temporary_variable - int(last_input_string[i])) % 10
        if int(firs_input_string[i]) < int(last_input_string[i]) : temporary_variable = 1
        if int(firs_input_string[i]) > int(last_input_string[i]) : temporary_variable = 0 
        resultat_string = str(temporary_index) + resultat_string
    if resultat_string[0] == '0': resultat_string = resultat_string[1:]
    return resultat_string

#2
def DeterminingStateDoors(doors_status,closing_door_step):
    for i in range(closing_door_step-1,len(doors_status),closing_door_step):
        if doors_status[i] == '0': doors_status[i] = '1'
        else: doors_status[i] = '0'
    return doors_status
def CalculatingStatusDoors(num_doors,closing_door_step=2):
    if num_doors == 1: return '1' 
    doors_status = ['1'] * num_doors
    while closing_door_step < num_doors:
        DeterminingStateDoors(doors_status,num_doors)
        closing_door_step +=1
    else:
        if doors_status[num_doors-1] == '0': doors_status[num_doors-1] = '1'
        else: doors_status[num_doors-1] = '0'
    return ''.join(doors_status)

#3
def CountingCandidatesVotes(num_candidates,candidates_votes):
    voting_result_string = ['majority winner','minority winner','no winner']
    votes_sorted = sorted(candidates_votes, reverse = True)
    if num_candidates > 1 and votes_sorted[0] == votes_sorted[1]: return voting_result_string[2]
    votes_resultat = round((votes_sorted[0] * 100 / sum(candidates_votes)),3) 
    for i in range(num_candidates):
        if candidates_votes[i] == votes_sorted[0]: position = ' ' + str(i+1)
    if votes_resultat > 50: return voting_result_string[0] + position
    else: return voting_result_string[1] + position

#4
def RotationMatrixElements(matrix_data,number_of_rows,number_of_columns,num_spins):
    for j in range(num_spins):
        matrix_data_copy = matrix_data[:]
        first_counter = 1
        last_counter = 0
        for i in range(number_of_rows):
            matrix_data_temp = ''
            if i+1 < number_of_rows: matrix_data_temp = matrix_data_copy[i+1][:first_counter]
            matrix_data_temp += matrix_data_copy[i][last_counter:number_of_columns - first_counter]
            if i > 0: matrix_data_temp += matrix_data_copy[i-1][number_of_columns - last_counter:] 
            matrix_data[i] = matrix_data_temp
            if i >= number_of_rows - number_of_columns // 2 and i + 1 > number_of_rows // 2:last_counter -= 1
            if last_counter < number_of_columns // 2 and  i + 1 <= number_of_rows // 2: last_counter += 1
            if i+1 >= number_of_rows - number_of_columns //2 and i + 1 >= number_of_rows // 2:first_counter -= 1
            if first_counter < number_of_columns // 2 and  i + 1 < number_of_rows // 2:first_counter += 1

#5
def AmountDiscountPurchaseStore(discount_step,price_purchase_array):
    prices_purchase_sort = sorted(price_purchase_array, reverse = True)
    purchase_discount = 0
    for i in range(discount_step):
        if (i+1) % 3 == 0: purchase_discount += prices_purchase_sort[i]
    return purchase_discount    

# Задание 3.2

class CreatingNode:

    def __init__(self,value_Node):
        self.value = value_Node
        self.next = None 

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def AddTailLinkedList(self,item_linked_list): 
        if self.head is None: self.head = item_linked_list
        else: self.tail.next = item_linked_list
        self.tail = item_linked_list
    
    def DeletingElHeadLinkedList(self):
        if self.head == None: return None
        el_head_delete = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return el_head_delete
        
    def LenLinkedList(self):
        len_linked_list = 0
        node_linked_list = self.head
        while node_linked_list is not None:
            len_linked_list += 1
            node_linked_list = node_linked_list.next
        return len_linked_list
    
    def PrintAllLinkedList(self):
        node_linked_list = self.head
        while node_linked_list != None:
            print(node_linked_list.value)
            node_linked_list = node_linked_list.next

class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def InsertItemEndQueue(self, item_queue):
        self.queue.add_in_tail(CreatingNode(item_queue))

    def IssuingHeadItemQueue(self):
        return self.queue.DeletingElHeadLinkedList()

    def SizeQueue(self):
        return self.queue.len()

