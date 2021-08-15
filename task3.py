# Задание 7.1
# 1
def LineAnalysis(line):
    bool = False
    symbol = '*'
    if line == symbol * len(line): 
        bool = True
        return bool
    if line[0] != symbol or line[len(line)-1] != symbol:
        return bool
    convertedLine = line[1:len(line)-1]
    convertedLine1 = (convertedLine.replace('*',',')).split(',')
    for i in range(len(convertedLine1)-1):
        if convertedLine1[i] != convertedLine1[i+1]: return bool
    bool = True
    return bool
#_________________________________________________________________
def LineAnalysis(line):
    is_Found = False
    symbol = '*'
    if line == symbol * len(line): 
        is_Found = True
        return is_Found
    if line[0] != symbol or line[len(line)-1] != symbol:
        return is_Found
    convertedLine = line[1:len(line)-1]
    convertedLine1 = (convertedLine.replace('*',',')).split(',')
    for i in range(len(convertedLine1)-1):
        if convertedLine1[i] != convertedLine1[i+1]: return is_Found
    is_Found = True
    return is_Found

# 2
def SherlockValidString(s):
    step = 0
    string = sorted(s)
    per1 = string.count(string[0])
    per2 = string.count(string[per1])
    if per1 > per2 and per1-1 == per2:
            per1 = per2
    pos = per1
    bool = True
    while pos < len(string):
        quantityElements = string.count(string[pos])
        if per1 != quantityElements: 
            if (per1 + 1 == quantityElements or quantityElements == 1) and step == 0:
                step = 1
            else:
                bool = False
                return bool
        pos +=quantityElements
    return bool
#__________________________________________________________________________________________
def SherlockValidString(s):
    step = 0
    string = sorted(s)
    per1 = string.count(string[0])
    per2 = string.count(string[per1])
    if per1 > per2 and per1-1 == per2:
            per1 = per2
    pos = per1
    Found = True
    while pos < len(string):
        quantityElements = string.count(string[pos])
        if per1 != quantityElements: 
            if (per1 + 1 == quantityElements or quantityElements == 1) and step == 0:
                step = 1
            else:
                Found = False
                return Found
        pos +=quantityElements
    return Found    
# 3
def Football(F,N):                                                            
    resultat = False
    i = -1
    while i != len(F)-2 and len(F) > 1:
        i += 1
        if F[i] > F[i+1] and resultat == False:
            if len(F) - i == 2:
                return True
            elif F[i+1] < F[i+2]:
                counter = i+1
                while F[counter] < F[counter+1]:
                    counter += 1
                    if counter == len(F)-1: 
                        break
                else:
                    F[i],F[counter+1] = F[counter+1],F[i]
            else:
                counter = i
                while counter != len(F)-1 and F[counter] > F[counter+1]:
                        counter += 1
                else:
                    F[i:counter+1] = list(reversed(F[i:counter+1]))                                    
            resultat = True
            i = 0
        if F[i] > F[i+1] and resultat == True:
            return False
    return resultat
#________________________________________________________________________
def Football(F,N):                                                            
    status_football = False
    i = -1
    while i != len(F)-2 and len(F) > 1:
        i += 1
        if F[i] > F[i+1] and status_football == False:
            if len(F) - i == 2:
                return True
            elif F[i+1] < F[i+2]:
                counter = i+1
                while F[counter] < F[counter+1]:
                    counter += 1
                    if counter == len(F)-1: 
                        break
                else:
                    F[i],F[counter+1] = F[counter+1],F[i]
            else:
                counter = i
                while counter != len(F)-1 and F[counter] > F[counter+1]:
                        counter += 1
                else:
                    F[i:counter+1] = list(reversed(F[i:counter+1]))                                    
            status_football = True
            i = 0
        if F[i] > F[i+1] and status_football == True:
            return False
    return True

# 4
def ichecking_data(data_string):
    bool = False
    if not isinstance(data_string, str):
        return bool
    else: return True
#_________________________________________________________________________________
def ichecking_data(data_string):
    error = False
    if not isinstance(data_string, str):
        return error
    else: return True

# 5
def TankRush(H1, W1, S1, H2, W2, S2):
    equal = False
    for i in range(len(S1)-W1):
        counter = i
        equal = True
        for j in range(len(S2)):
            if S2[j] == ' ':
                counter = counter + W1 - j + 1
                continue
            if S1[counter] == S2[j]:counter += 1
            else:
                equal = False
                break            
        if equal: return equal
    return equal
#___________________________________________________________________________
def TankRush(H1, W1, S1, H2, W2, S2):
    is_Done = False
    for i in range(len(S1)-W1):
        counter = i
        is_Done = True
        for j in range(len(S2)):
            if S2[j] == ' ':
                counter = counter + W1 - j + 1
                continue
            if S1[counter] == S2[j]:counter += 1
            else:
                is_Done = False
                break            
        if is_Done: return is_Done
    return is_Done

# Задание 7.2
def TankRush(H1, W1, S1, H2, W2, S2):
    is_Done = False
    for i in range(len(S1)-W1):
        counter = i
        is_Done = True
        for j in range(len(S2)):
            if S2[j] == ' ':
                counter = counter + W1 - j + 1
                continue
            if S1[counter] == S2[j]:counter += 1
            else:
                is_Done = False
                break            
        if is_Done: return is_Done
    return is_Done

def LineAnalysis(line):
    is_Found = False
    symbol = '*'
    if line == symbol * len(line): 
        is_Found = True
        return is_Found
    if line[0] != symbol or line[len(line)-1] != symbol:
        return is_Found
    convertedLine = line[1:len(line)-1]
    convertedLine1 = (convertedLine.replace('*',',')).split(',')
    for i in range(len(convertedLine1)-1):
        if convertedLine1[i] != convertedLine1[i+1]: return is_Found
    is_Found = True
    return is_Found

# Задание 7.3

class DynArray:
    

    def __init__(self):
        ...
    def __len__(self):
        ...
    def make_array(self, new_volume_DynArray):
        ...
    def __getitem__(self,border_index):
        ...
    def resize(self, new_volume_DynArray):
        ...
    def append(self, app_new_elements):
        ...
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

# Задание 7.4
def sort_key(j):
        return int(j[1])
def ShopOLAP(N,items):
    if N == 1: return items
    first_items = []
    last_items = []
    for j in items:
        first_items.append(j.split())
    first_items = sorted(first_items)
    for i in range(len(first_items)-1):
        if first_items[i][0] == first_items[i+1][0]:
            first_items[i+1][1] = str(int(first_items[i][1]) + int(first_items[i+1][1]))
        else:
            last_items.append(first_items[i])
    last_items.append(first_items[i+1])
    sortItems = sorted(last_items, reverse = True, key=sort_key)
    resultat = []
    for y in range(len(sortItems)):
        per = sortItems[y][0] + ' ' + sortItems[y][1]
        resultat.append(per)
    return resultat

def Transform(input_array):
    output_array = []
    for i in range(len(input_array)):
        for j in range(len(input_array)-i):
            k = i + j
            output_array.append(max(input_array[j:k+1]))
    return output_array
def TransformTransform(input_array,N):
    input_array = Transform(input_array)
    output_array = Transform(input_array)
    if sum(output_array) % 2 == 0: return True
    else: return False

# Задание 7.5

"""def UFO(N,data,octal):
    if octal == True: degree = 8
    else: degree = 16
    result = []
    for i in data:
        I = str(i)
        per = len(I)
        summ = 0
        for j in range(len(I)):
            summ = summ + (int(I[j]) * degree ** (per-1))
            per -= 1
        result.append(summ)
    return result"""

def UFO(N,data,octal):
    degree = (8 if octal == True else 16)
    result = []
    for number_data in data:
        temp_summ_result = 0
        for position in range(len(str(number_data))):
            temp_summ_result += (int(str(number_data)[position]) * 
                                degree ** (len(str(number_data))-position-1))
        result.append(temp_summ_result)
    return result
