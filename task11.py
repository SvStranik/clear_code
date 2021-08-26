class Node:
    def __init__(self, value_node):
        # Делаем приватной переменной класса 
        self._value = value_node
        # Делаем приватной переменной класса 
        self._prev = None
        # Делаем приватной переменной класса 
        self._next = None


class OrderedList:
    def __init__(self, el_sort_ascending=True):
        # Делаем приватной переменной класса (с максимальным уровнем)
        self.__head = None
        # Делаем приватной переменной класса (с максимальным уровнем)
        self.__tail = None
        # Делаем приватной переменной класса (с максимальным уровнем)
        self.__sort_ascending = el_sort_ascending


    def compares_num_values(self, FIRST_VALUES, LAST_VALUES):
        if FIRST_VALUES._value < LAST_VALUES._value: return -1
        elif FIRST_VALUES._value == LAST_VALUES._value: return 0
        else: return 1


    def add_new_node_sorting(self, value_new_node):
        # Создаем константу приватную и ограничиваем ее в пределах функции
        __ITEM_NEW_ORDERED_LIST = Node(value_new_node)
        if self.__sort_ascending: status_ascending = 1
        else: status_ascending = -1
        if self.__head is None:
            self.__head = __ITEM_NEW_ORDERED_LIST
            self.__tail = __ITEM_NEW_ORDERED_LIST
        else:
            if self.compares_num_values(self.__head,__ITEM_NEW_ORDERED_LIST) == status_ascending:
                self.__head._prev = __ITEM_NEW_ORDERED_LIST
                __ITEM_NEW_ORDERED_LIST._next = self.__head
                self.__head = __ITEM_NEW_ORDERED_LIST
            else:
                # Создаем переменную и ограничиваем ее в пределах одного цикла
                node_ordered_list = self.__head
                while node_ordered_list:
                    if self.compares_num_values(node_ordered_list,__ITEM_NEW_ORDERED_LIST) == status_ascending:
                        __ITEM_NEW_ORDERED_LIST._prev = node_ordered_list._prev
                        __ITEM_NEW_ORDERED_LIST._next = node_ordered_list
                        node_ordered_list._prev._next = __ITEM_NEW_ORDERED_LIST
                        node_ordered_list._prev = __ITEM_NEW_ORDERED_LIST
                        __ITEM_NEW_ORDERED_LIST._next = node_ordered_list
                        return
                    node_ordered_list = node_ordered_list._next
                # Обнуляем переменную
                node_ordered_list = None
                __ITEM_NEW_ORDERED_LIST._prev = self.__tail  
                self.__tail._next = __ITEM_NEW_ORDERED_LIST
                self.__tail = __ITEM_NEW_ORDERED_LIST
                # Обнуляем константу
                __ITEM_NEW_ORDERED_LIST = None


    def searches_node_value(self, value_node):
        if self.__sort_ascending: status_ascending = 1
        else: status_ascending = -1
        #Создаем константу непосредственно перед циклом и ограничиваем в пределах этого цикла
        NEW_NODE_TEMP = Node(value_node)
         #Создаем переменную непосредственно перед циклом и ограничиваем в пределах этого цикла
        node_ordered_list = self.__head
        while node_ordered_list:
            result_node_compares = self.compares_num_values(node_ordered_list,NEW_NODE_TEMP)
            if result_node_compares == 0:
                NEW_NODE_TEMP = None 
                return node_ordered_list
            if status_ascending == result_node_compares:
                NEW_NODE_TEMP = None
                node_ordered_list = None 
                return None
            node_ordered_list = node_ordered_list._next

        
    def del_node_by_value(self, value_node,del_all_node=False):
        if self.__head == None: return
        while self.__head._value == value_node:
            if self.__head._next == None:
                self.__head = None
                self.__tail = None
                return
            self.__head._next._prev = None
            self.__head = self.__head._next
            if del_all_node != True: return
        else:
            self.prev = None
        #Создаем переменную непосредственно перед циклом и ограничиваем в пределах этого цикла
        node_ordered_list = self.__head
        while self.__tail != node_ordered_list:
            if node_ordered_list._next._value == value_node:
                if node_ordered_list._next._next == None:
                    node_ordered_list._next = None
                    self.__tail = node_ordered_list
                    node_ordered_list = None
                    return
                node_ordered_list._next._next._prev = node_ordered_list
                node_ordered_list._next = node_ordered_list._next._next
                if del_all_node != True: 
                    node_ordered_list = None
                    return
                continue
            node_ordered_list = node_ordered_list._next

    def clears_order_list(self, el_sort_ascending):
        self.__sort_ascending = el_sort_ascending
        self.__head = None
        self.__tail = None


    def num_nodes_defines(self):
        num_nodes = 0
        #Создаем переменную непосредственно перед циклом и ограничиваем в пределах этого цикла
        node_ordered_list = self.__head
        while node_ordered_list:
            num_nodes += 1
            node_ordered_list = node_ordered_list._next
        node_ordered_list = None
        return num_nodes 


    def generates_list_nodes(self):
        list_nodes = []
        #Создаем переменную непосредственно перед циклом и ограничиваем в пределах этого цикла
        node_ordered_list = self.__head
        while node_ordered_list != None:
            list_nodes.append(node_ordered_list)
            node_ordered_list = node_ordered_list._next
        node_ordered_list = None
        return list_nodes

