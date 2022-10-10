def get_multiplication_list(list_data):
    new_list = []
    average = float(sum(list_data)) / len(list_data)

    if len(list_data) > 0:

        i = 0
        while i < len(list_data):
            new_list += [float(list_data[i]) * float(average)]
            i += 1

        return new_list
    else:
        return 0
