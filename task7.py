# Я не очень понял, что требуется по заданию, сделал переназначение методов с указанием
# что метод работает со строкой

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
        if first_values.value < last_values.value: return -1
        elif first_values.value == last_values.value: return 0
        else: return 1


    def add_new_node_sorting(self, value_new_node):
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
        self.__sort_ascending = el_sort_ascending
        self.head = None
        self.tail = None


    def num_nodes_defines(self):
        num_nodes = 0
        node_ordered_list = self.head
        while node_ordered_list:
            num_nodes += 1
            node_ordered_list = node_ordered_list.next
        return num_nodes 


    def generates_list_nodes(self):
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
        if first_values.value.rstrip().lstrip() < last_values.value.rstrip().lstrip(): return -1
        elif first_values.value.rstrip().lstrip() == last_values.value.rstrip().lstrip(): return 0
        else: return 1

    def add__string_node(self,value_new_node):
        value_node_str = value_new_node.rstrip().lstrip()
        OrderedList.add_new_node_sorting(value_node_str)

    def deleting_string_node(self,value_node,del_all_node=False):
        value_node_str = value_node.rstrip().lstrip()
        self.del_node_by_value(value_node_str,del_all_node)

