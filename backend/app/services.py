def string_to_json_array(string, max_len_of_array):
    array = string[1:-1].split(', ')
    clipped_array = array[0:max_len_of_array] if len(array) > max_len_of_array else array[0:len(array)]
    for i in range(len(clipped_array)):
        clipped_array[i] = clipped_array[i].replace("\"", "")
    return clipped_array
