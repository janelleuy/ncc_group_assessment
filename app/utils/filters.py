def string_filter(filter_key, filter_value, object_list):
    return list(filter(lambda x: x.get(filter_key) == filter_value, object_list))

def int_filter(filter_key, filter_value, object_list):
    return list(filter(lambda x: x.get(filter_key) == int(filter_value), object_list))