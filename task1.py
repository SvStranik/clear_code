# Изначальное решение

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

# Отредактированное решение 
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

