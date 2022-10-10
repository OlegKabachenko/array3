def get_root_list(list_data):
    new_list = []

    if len(list_data) > 0:

        i = 0
        while i < len(list_data):
            new_list += [float(list_data[i])  ** (0.5)]
            i += 1

        return new_list
    else:
        return 0
