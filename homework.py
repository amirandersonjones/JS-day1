# *Write a fucntion that takes in an array and removes every even index with a splice,
# and replaces it with the string "even index" */
#need to find the even indexes, loop through them
#if the index is even i need to replace that variable with a string saying 'even index'
old_list = ["Max","Baseball","Reboot","Goku","Trucks","Rodger"]
def even_indexes(array):
    new_list = []
    for i in range(len(array)):
        if i % 2 == 0:
            new_list.append('even index')
        else: new_list.append(array[i])
    return new_list

print(even_indexes(old_list))
