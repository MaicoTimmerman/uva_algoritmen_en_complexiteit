from copy import copy

# Generate a list of posible values for permutation
def getlist(n):
    return list(range(1,n+1))

# Swap two elements and return the new set
def swap(i,j):
    temp = i
    i = j
    j = temp
    return i,j

# Recursive function that fixes the index_start
# and requests the permutations from index_start+1
def calc_permutations(current_list, index_start, index_stop):
    if index_start == index_stop:
        global permutations
        permutations.append(copy(current_list))
    else:
        for i in range(index_start, index_stop):
            current_list[index_start], current_list[i] = \
                    swap(current_list[index_start], current_list[i])
            calc_permutations(current_list, index_start+1, index_stop)
            current_list[index_start], current_list[i] = \
                swap(current_list[index_start], current_list[i])

n = int(input("Give a positieve integer: "))
permutations = []
start_list = getlist(n)
calc_permutations(start_list, 0, len(start_list))
print(permutations)
