# Задание 7

# 1
def BiggerGreater(string):
    for i in range(len(string)-1,0,-1):
        if string[i] > string[i-1]:
            string2 = list(string[i-1:])
            stringMax = sorted(string2)
            element = stringMax[stringMax.index(string2[0])+1]
            x = string2.index(element)
            string2[0],string2[x] = string2[x],string2[0]
            string = string[:i-1] + ''.join(string2[0]) + ''.join(sorted(string2[1:]))
            return string    
    string = ''      
    return string

def BiggerGreater(data_big_greater):
    for i in range(len(data_big_greater)-1,0,-1):
        if data_big_greater[i] > data_big_greater[i-1]:
            data_temp = list(data_big_greater[i-1:])
            data_temp_max = sorted(data_temp)
            element_data_temp = data_temp_max[data_temp_max.index(data_temp[0])+1]
            position_element = data_temp.index(element_data_temp)
            data_temp[0],data_temp[position_element] = data_temp[position_element],data_temp[0]
            data_big_greater = data_big_greater[:i-1] + ''.join(data_temp[0]) + ''.join(sorted(data_temp[1:]))
            return data_big_greater    
    data_big_greater = ''      
    return data_big_greater
#2_________________________________________________________________________________________________
def BigMinus(s1,s2):
    if s1 == s2: return '0'
    if int(s1) < int(s2):
        s1,s2 = s2,s1 
    s2 = s2.rjust(len(s1),'0')
    per = 0
    s = ''
    for i in range(len(s1)-1,-1,-1):
        x = (10 + int(s1[i])- per - int(s2[i])) % 10
        if int(s1[i]) < int(s2[i]) : per = 1
        if int(s1[i]) > int(s2[i]) : per = 0 
        s = str(x) + s
    if s[0] == '0': s = s[1:]
    return s

def BigMinus(firs_input_string,last_input_string):
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

#3_________________________________________________________________________________________________
def shiftDoor(doors,n):
    for i in range(n-1,len(doors),n):
        if doors[i] == '0': doors[i] = '1'
        else: doors[i] = '0'
    return doors
def Keymaker(k,n=2):
    if k == 1: return '1' 
    doors = ['1'] * k
    while n < k:
        shiftDoor(doors,n)
        n +=1
    else:
        if doors[k-1] == '0': doors[k-1] = '1'
        else: doors[k-1] = '0'
    return ''.join(doors)

def shiftDoor(doors_status,closing_door_step):
    for i in range(closing_door_step-1,len(doors_status),closing_door_step):
        if doors_status[i] == '0': doors_status[i] = '1'
        else: doors_status[i] = '0'
    return doors_status
def Keymaker(num_doors,closing_door_step=2):
    if num_doors == 1: return '1' 
    doors_status = ['1'] * num_doors
    while closing_door_step < num_doors:
        shiftDoor(doors_status,num_doors)
        closing_door_step +=1
    else:
        if doors_status[num_doors-1] == '0': doors_status[num_doors-1] = '1'
        else: doors_status[num_doors-1] = '0'
    return ''.join(doors_status)
#4_________________________________________________________________________________________________
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

def LineAnalysis(character_string):
    is_Found = False
    reference_symbol = '*'
    if character_string == reference_symbol * len(character_string): 
        is_Found = True
        return is_Found
    if (character_string[0] != reference_symbol or 
        character_string[len(character_string)-1] != reference_symbol):
        return is_Found
    first_formated_str = character_string[1:len(character_string)-1]
    last_formated_str = (first_formated_str.replace('*',',')).split(',')
    for i in range(len(last_formated_str)-1):
        if last_formated_str[i] != last_formated_str[i+1]: return is_Found
    is_Found = True
    return is_Found

#5_________________________________________________________________________________________________
def MassVote(N,Votes):
    s1 = 'majority winner'
    s2 = 'minority winner'
    s3 = 'no winner'
    sortVotes = sorted(Votes, reverse = True)
    maxVotes = sortVotes[0] 
    if N > 1 and sortVotes[0] == sortVotes[1]: return s3
    resultVotes = round((sortVotes[0] * 100 / sum(Votes)),3) 
    for i in range(N):
        if Votes[i] == sortVotes[0]: position = ' ' + str(i+1)
    if resultVotes > 50: return s1 + position
    else: return s2 + position

def MassVote(num_candidates,candidates_votes):
    voting_result_string = ['majority winner','minority winner','no winner']
    votes_sorted = sorted(candidates_votes, reverse = True)
    if num_candidates > 1 and votes_sorted[0] == votes_sorted[1]: return voting_result_string[2]
    votes_resultat = round((votes_sorted[0] * 100 / sum(candidates_votes)),3) 
    for i in range(num_candidates):
        if candidates_votes[i] == votes_sorted[0]: position = ' ' + str(i+1)
    if votes_resultat > 50: return voting_result_string[0] + position
    else: return voting_result_string[1] + position

#6_________________________________________________________________________________________________
def MatrixTurn(Matrix,M,N,T):
    for j in range(T):
        matrix,counter,counter2 = Matrix[:],1,0
        for i in range(M):
            per = ''
            if i+1 < M: per = matrix[i+1][:counter]
            per +=matrix[i][counter2:N-counter]
            if i > 0:per += matrix[i-1][N-counter2:] 
            Matrix[i] = per
            if i >= M - N //2 and i+1 > M // 2:counter2 -= 1
            if counter2 < N // 2 and  i+1 <= M // 2: counter2 += 1
            if i+1 >= M - N //2 and i+1 >= M // 2:counter -= 1
            if counter < N // 2 and  i+1 < M // 2:counter += 1  

def MatrixTurn(matrix_data,number_of_rows,number_of_columns,T):
    for j in range(T):
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

#7_________________________________________________________________________________________________
def MaximumDiscount(N,price):
    priceMax = sorted(price, reverse = True)
    diskount = 0
    for i in range(N):
        if (i+1) % 3 == 0: diskount += priceMax[i]
    return diskount

def MaximumDiscount(discount_step,price_purchase_array):
    prices_purchase_sort = sorted(price_purchase_array, reverse = True)
    purchase_discount = 0
    for i in range(discount_step):
        if (i+1) % 3 == 0: purchase_discount += prices_purchase_sort[i]
    return purchase_discount

#8_________________________________________________________________________________________________
def PrintingCosts(Line):
    table = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',',
             '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\',
             ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
             'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
             'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
    data = [0,9,6,24,29,22,24,3,12,12,17,13,7,7,4,10,22,19,22,23,21,27,26,16,
            23,26,8,11,10,14,10,15,32,24,29,20,26,26,20,25,25,18,18,21,16,
            28,25,26,23,31,28,25,16,23,19,26,18,14,22,18,10,18,7,8,3,23,25,
            17,25,23,18,30,21,15,20,21,16,22,18,20,25,25,13,21,17,17,13,19,
            13,24,19,18,12,18,9]    
    
    summTonner = 0
    for i in range(len(Line)):
        if Line[i] in table:
            summTonner += data[table.index(Line[i])]
        else:
            summTonner += 23
    return summTonner

def PrintingCosts(text_data):
    text_symbol_print = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',',
                        '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8',
                        '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D',
                        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
                        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\',
                        ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                        'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
    cost_symbol_print = [0,9,6,24,29,22,24,3,12,12,17,13,7,7,4,10,22,19,22,23,21,27,26,16,
                        23,26,8,11,10,14,10,15,32,24,29,20,26,26,20,25,25,18,18,21,16,
                        28,25,26,23,31,28,25,16,23,19,26,18,14,22,18,10,18,7,8,3,23,25,
                        17,25,23,18,30,21,15,20,21,16,22,18,20,25,25,13,21,17,17,13,19,
                        13,24,19,18,12,18,9]    
    
    printing_costs = 0
    for i in range(len(text_data)):
        if text_data[i] in text_symbol_print:
            printing_costs += cost_symbol_print[text_symbol_print.index(text_data[i])]
        else:
            printing_costs += 23
    return printing_costs

#9_________________________________________________________________________________________________
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

def SherlockValidString(password_string):
    step_password_string = 0
    password_string_sort = sorted(password_string)
    num_first_element = password_string_sort.count(password_string_sort[0])
    num_last_element = password_string_sort.count(password_string_sort[num_first_element])
    if num_first_element > num_last_element and num_first_element-1 == num_last_element:
            num_first_element = num_last_element
    pos_first_elemen = num_first_element
    Found = True
    while pos_first_elemen < len(password_string_sort):
        quantity_elements = password_string_sort.count(password_string_sort[pos_first_elemen])
        if num_first_element != quantity_elements: 
            if (num_first_element + 1 == quantity_elements or quantity_elements == 1) and step_password_string == 0:
                step_password_string = 1
            else:
                Found = False
                return Found
        step_password_string +=quantity_elements
    return Found    

#10________________________________________________________________________________________________
def sort_key(j):
        return int(j[1])
def ShopOLAP(N,items):
    if N == 1: return items
    Items1 = []
    Items2 = []
    for j in items:
        Items1.append(j.split())
    Items1 = sorted(Items1)
    for i in range(len(Items1)-1):
        if Items1[i][0] == Items1[i+1][0]:
            Items1[i+1][1] = str(int(Items1[i][1]) + int(Items1[i+1][1]))
        else:
            Items2.append(Items1[i])
    Items2.append(Items1[i+1])
    sortItems = sorted(Items2, reverse = True, key=sort_key)
    resultat = []
    for y in range(len(sortItems)):
        per = sortItems[y][0] + ' ' + sortItems[y][1]
        resultat.append(per)
    return resultat

def sort_key(j):
        return int(j[1])
def ShopOLAP(quantity_items,items_shop_OLAP):
    if quantity_items == 1: return items_shop_OLAP
    first_items_shop = []
    last_items_shop = []
    for j in items_shop_OLAP:
        first_items_shop.append(j.split())
    first_items_shop = sorted(first_items_shop)
    for i in range(len(first_items_shop)-1):
        if first_items_shop[i][0] == first_items_shop[i+1][0]:
            first_items_shop[i+1][1] = str(int(first_items_shop[i][1]) + int(first_items_shop[i+1][1]))
        else:
            last_items_shop.append(first_items_shop[i])
    last_items_shop.append(first_items_shop[i+1])
    sortItems = sorted(last_items_shop, reverse = True, key=sort_key)
    resultat_items_shop = []
    for y in range(len(sortItems)):
        temp_items_shop = sortItems[y][0] + ' ' + sortItems[y][1]
        resultat_items_shop.append(temp_items_shop)
    return resultat_items_shop

#11________________________________________________________________________________________________
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


def TankRush(num_rows_map, num_column_map, data_map_array, 
             num_rows_tank, num_column_tank, data_tank_array):
    is_Done = False
    for i in range(len(data_map_array)-num_column_map):
        independent_counter = i
        is_Done = True
        for j in range(len(data_tank_array)):
            if data_tank_array[j] == ' ':
                independent_counter +=num_column_map - j + 1
                continue
            if data_map_array[independent_counter] == data_tank_array[j]:independent_counter += 1
            else:
                is_Done = False
                break            
        if is_Done: return is_Done
    return is_Done

#12________________________________________________________________________________________________

def codeEncripted(s):
    S = s.replace(' ','')
    squareRoot = pow(len(S),0.5) 
    if int(squareRoot //1) >= int(squareRoot % 1 * 10):
        string = int(squareRoot % 1 * 10) 
        column = int(squareRoot //1)
    else: 
        string = int(squareRoot //1) 
        column = int(squareRoot % 1 * 10) 
    
    while string * column < len(S):
        string += 1

    arr = []
    count = 0
    for i in range(column):
        arr2 = []
        for j in range(string):
            if count == len(S):break
            arr2.append(S[count])
            count += 1
        arr.append(arr2)

    result = ''
    for i in range(string):
        for j in range(column):
            if i < len(arr[j]):
                result += arr[j][i]
        result += ' '
    result =  result.strip()
    return result
    
def TheRabbitsFoot(s, encode):
    if encode == True:
        return codeEncripted(s)
    else:
        arr = s.split()
        result = ''
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i < len(arr[j]):
                    result += arr[j][i]
        return result

def codeEncripted(source_string):
    merged_string = source_string.replace(' ','')
    square_root_string = pow(len(merged_string),0.5) 
    if int(square_root_string //1) >= int(square_root_string % 1 * 10):
        number_of_rows_of_the_matrix = int(square_root_string % 1 * 10)
        number_of_matrix_columns = int(square_root_string // 1)
    else: 
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
    
def TheRabbitsFoot(source_string, encode):
    if encode == True:
        return codeEncripted(source_string)
    else:
        array_of_encrypted_data = source_string.split()
        decrypted_string = ''
        for i in range(len(array_of_encrypted_data)):
            for j in range(len(array_of_encrypted_data)):
                if i < len(array_of_encrypted_data[j]):
                    decrypted_string += array_of_encrypted_data[j][i]
        return decrypted_string
