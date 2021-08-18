#Задача 1
class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1.value < v2.value: return -1
        elif v1.value == v2.value: return 0
        else: return 1

    def add(self, value):
        item = Node(value)
        if self.__ascending is True: status = 1
        else: status = -1
        if self.head is None:
            self.head = item
            self.tail = item
        else:
            if self.compare(self.head,item) == status:
                self.head.prev = item
                item.next = self.head
                self.head = item
            else:
                node = self.head
                while node:
                    if self.compare(node,item) == status:
                        item.prev = node.prev
                        item.next = node
                        node.prev.next = item
                        node.prev = item
                        item.next = node
                        return
                    node = node.next
                item.prev = self.tail  
                self.tail.next = item
                self.tail = item


    def find(self, val):
        item = Node(val)
        node = self.head
        if self.__ascending is True: status = 1
        else: status = -1
        while node:
            per = self.compare(node,item)
            if per == 0: return node
            if status == per: return None
            node = node.next
        
        
    def delete(self, val,all=False):
        if self.head == None: return
        while self.head.value == val:
            if self.head.next == None:
                self.head = None
                self.tail = None
                return
            self.head.next.prev = None
            self.head = self.head.next
            if all != True: return
        else:
            self.prev = None
        node = self.head
        while self.tail != node:
            if node.next.value == val:
                if node.next.next == None:
                    node.next = None
                    self.tail = node
                    return
                node.next.next.prev = node
                node.next = node.next.next
                if all != True: return
                continue
            node = node.next


    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None


    def len(self):
        resultat = 0
        node = self.head
        while node:
            resultat += 1
            node = node.next
        return resultat 


    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

# сделано по заданию

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        if v1.value.rstrip().lstrip() < v2.value.rstrip().lstrip(): return -1
        elif v1.value.rstrip().lstrip() == v2.value.rstrip().lstrip(): return 0
        else: return 1

class Node:
    def __init__(self, value_node):
        self.value = value_node
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, el_sort_ascending=True):
        self.head = None
        self.tail = None
        self.__sort_ascending = el_sort_ascending

    def compares_num_values(self, first_values, last_values):
    # функция сравнивает числовые значения
        if first_values.value < last_values.value: return -1
        elif first_values.value == last_values.value: return 0
        else: return 1

    def add_new_node_by_sorting(self, value_new_node):
        # функция добовляет новый узел по сортировке
        item_new_ordered_list = Node(value_new_node)
        if self.__sort_ascending is True: status_ascending = 1
        else: status_ascending = -1
        if self.head is None:
            self.head = item_new_ordered_list
            self.tail = item_new_ordered_list
        else:
            if self.compares_num_values(self.head,item_new_ordered_list) == status_ascending:
                self.head.prev = item_new_ordered_list
                item_new_ordered_list.next = self.head
                self.head = item_new_ordered_list
            else:
                node_ordered_list = self.head
                while node_ordered_list:
                    if self.compares_num_values(node_ordered_list,item_new_ordered_list) == status_ascending:
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
        # функция ищет узел по значению
        new_node_temp = Node(value_node)
        node_ordered_list = self.head
        if self.__sort_ascending is True: status_ascending = 1
        else: status_ascending = -1
        while node_ordered_list:
            result_node_compares = self.compares_num_values(node_ordered_list,new_node_temp)
            if result_node_compares == 0: return node_ordered_list
            if status_ascending == result_node_compares: return None
            node_ordered_list = node_ordered_list.next
        
        
    def del_node_by_value(self, value_node,del_all_node=False):
        if self.head == None: return
        while self.head.value == value_node:
            if self.head.next == None:
                self.head = None
                self.tail = None
                return
            self.head.next.prev = None
            self.head = self.head.next
            if del_all_node != True: return
        else:
            self.prev = None
        node_ordered_list = self.head
        while self.tail != node_ordered_list:
            if node_ordered_list.next.value == value_node:
                if node_ordered_list.next.next == None:
                    node_ordered_list.next = None
                    self.tail = node_ordered_list
                    return
                node_ordered_list.next.next.prev = node_ordered_list
                node_ordered_list.next = node_ordered_list.next.next
                if del_all_node != True: return
                continue
            node_ordered_list = node_ordered_list.next


    def clears_order_list(self, el_sort_ascending):
        # функция очищает OrderedList
        self.__sort_ascending = el_sort_ascending
        self.head = None
        self.tail = None


    def num_nodes_defines(self):
        # функция определяет количество узлов
        num_nodes = 0
        node_ordered_list = self.head
        while node_ordered_list:
            num_nodes += 1
            node_ordered_list = node_ordered_list.next
        return num_nodes 


    def generates_list_nodes(self):
        # функция формирует список узлов
        list_nodes = []
        node_ordered_list = self.head
        while node_ordered_list != None:
            list_nodes.append(node_ordered_list)
            node_ordered_list = node_ordered_list.next
        return list_nodes


class OrderedStringList(OrderedList):
    def __init__(self, el_sort_ascending):
        super(OrderedStringList, self).__init__(el_sort_ascending)

    def compares_string_val(self, first_values, last_values):
        # функция сравнивает строковые значения
        if first_values.value.rstrip().lstrip() < last_values.value.rstrip().lstrip(): return -1
        elif first_values.value.rstrip().lstrip() == last_values.value.rstrip().lstrip(): return 0
        else: return 1
#__________________________________________________________________________________________________

#Задача 2
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

# сделано по заданию
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def adds_new_node_tail(self,item_linked_list): 
        # функция добавляет новый узел в хвост
        if self.head is None: self.head = item_linked_list
        else: self.tail.next = item_linked_list
        self.tail = item_linked_list
    
    def removes_node_in_head(self):
        # функция удаляет узел с головы
        if self.head == None: return None
        el_head_delete = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return el_head_delete
        
    def num_nodes_linkedlist(self):
        # функция определяет количество узлов
        len_linked_list = 0
        node_linked_list = self.head
        while node_linked_list is not None:
            len_linked_list += 1
            node_linked_list = node_linked_list.next
        return len_linked_list
    
    def prints_all_nodes(self):
        # функция печатает все узлы
        node_linked_list = self.head
        while node_linked_list != None:
            print(node_linked_list.value)
            node_linked_list = node_linked_list.next
