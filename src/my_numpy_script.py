import numpy as np

def add_two_things(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    list_A = [1, 2, 3]
    list_B = [4, 5, 6]

    array_A = np.array(list_A)
    array_B = np.array(list_B)

    print 'Summing lists\n{}'.format(add_two_things(list_A, list_B))

    print 'Summing arrays\n{}'.format(add_two_things(array_A, array_B))
