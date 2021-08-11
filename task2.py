"""import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i != self.count:
            self.__getitem__(i)
        if self.count + 1 > self.capacity:
            new_capacity = (2 * self.capacity)
            self.resize(new_capacity)
        new_array = self.make_array(self.capacity)
        new_count = 0
        for j in range(self.count+1):
            if i == j:
                new_array[j] = itm
                continue
            new_array[j] = self.array[new_count]
            new_count += 1
        self.array = new_array
        self.count += 1

    def delete(self, i):
        self.__getitem__(i)
        new_array = self.make_array(self.capacity)
        per = 0
        for j in range(self.count):
            if j == i: 
                continue
            new_array[per] = self.array[j]
            per += 1
        self.array = new_array
        self.count -= 1
        if self.count < self.capacity // 2:
            if int(self.capacity / 1.5) <= 16:
                new_capacity = 16
            else:
                new_capacity = int(self.capacity / 1.5)
            self.resize(new_capacity)"""

# Задание 6.1

# self.count                            => self.number_elements_DynArray 
# self.capacity                         => self.volume_DynArray
# self.array                            => self.reference_to_the_DynArray 
# def make_array(self, new_capacity)    => def make_array(self, new_volume_DunArray)
# def resize(self, new_volume_DunArray):
#     ...new_array...                   => new_resize_DynArray
#def insert(self, i, itm):              => def insert(self, item_insert_position, itm): 

# Задание 6.2

# self.capacity                         => self.buffer_size_DynArray
# self.array                            => self.storing_PyObject_elements
# def __getitem__(self,i):              => def __getitem__(self,index):
#    if i < 0 or i >= self.count:       =>      if index < 0 or index >= self.count:
#        raise IndexError('Index is out of bounds')
#    return self.array[i]               => return self.array[index]
# def resize(self, new_capacity):       => def resize(self, buffer_size):

# Задание 6.3
#
#  def insert(self, item_insert_position, insert_element):
#  ... 
#  independent_counter = 0              => ins_independ_counter = 0  

#  def delete(self, position_deletion):
#  ... 
#  independent_counter = 0              => del_independ_counter = 0

# def resize(self, new_capacity):
#    new_array = self.make_array(new_capacity) => res_new_DynArray
#    for i in range(self.count):
#       new_array[i] = self.array[i]           => res_new_DynArray[i] = self.array[i]
#    self.array = new_array                    => self.array = res_new_DynArray
#    self.capacity = new_capacity

# Задание 6.4

# self.number_elements_DynArray              => self.count_el_DynArray
# self.reference_to_the_DynArray             => self.location_el_DynArray
# def __getitem__(self,index):               => border_index
# def resize(self, new_volume_DynArray):
# ... i (заменяем) ...                       => position
# def append(self, itm):                     => def append(self, app_new_elements): 

import ctypes

class DynArray:
    

    def __init__(self):
        self.count_el_DynArray = 0
        self.volume_DynArray = 16
        self.location_el_DynArray = self.make_array(self.volume_DynArray)


    def __len__(self):
        return self.count_el_DynArray


    def make_array(self, new_volume_DynArray):
        return (new_volume_DynArray * ctypes.py_object)()


    def __getitem__(self,border_index):
        if border_index < 0 or border_index >= self.count_el_DynArray:
            raise IndexError('Index is out of bounds')
        return self.location_el_DynArray[border_index]


    def resize(self, new_volume_DynArray):
        res_new_DynArray = self.make_array(new_volume_DynArray)
        for position in range(self.count_el_DynArray):
            res_new_DynArray[position] = self.location_el_DynArray[position]
        self.location_el_DynArray = res_new_DynArray
        self.volume_DynArray = new_volume_DynArray


    def append(self, app_new_elements):
        if self.count_el_DynArray == self.volume_DynArray:
            self.resize(2*self.volume_DynArray)
        self.location_el_DynArray[self.count_el_DynArray] = app_new_elements
        self.count_el_DynArray += 1


    def insert(self, item_insert_position, insert_element):
        if item_insert_position != self.count_el_DynArray:
            self.__getitem__(item_insert_position)
        if self.count_el_DynArray + 1 > self.volume_DynArray:
            new_volume_DynArray = (2 * self.volume_DynArray)
            self.resize(new_volume_DynArray)
        temporary_array= self.make_array(self.volume_DynArray)
        ins_independ_counter = 0
        for position in range(self.count_el_DynArray + 1):
            if item_insert_position == position:
                temporary_array[position] = insert_element
                continue
            temporary_array[position] = self.location_el_DynArray[ins_independ_counter]
            ins_independ_counter += 1
        self.location_el_DynArray = temporary_array
        self.count_el_DynArray += 1


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
            if int(self.volume_DynArray / 1.5) <= 16:
                new_volume_DynArray = 16
            else:
                new_volume_DynArray = int(self.volume_DynArray / 1.5)
            self.resize(new_volume_DynArray)
            