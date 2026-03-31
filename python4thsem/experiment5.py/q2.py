#wap that loops over a sequence of elements of list,tuple,dictionary and set in python
# Function to loop over different sequence types
def loop_sequences():
    my_list = [1, 2, 3, 4]
    my_tuple = ('a', 'b', 'c', 'd')
    my_dict = {'x': 10, 'y': 20, 'z': 30}
    my_set = {100, 200, 300, 400}

    for item in my_list:
        print(f"List item: {item}")

    for item in my_tuple:
        print(f"Tuple item: {item}")

    for key, value in my_dict.items():
        print(f"Dictionary item: {key}: {value}")

    for item in my_set:
        print(f"Set item: {item}")

loop_sequences()
