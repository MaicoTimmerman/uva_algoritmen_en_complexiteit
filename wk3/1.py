#!/usr/bin/python3

import random
import string
import copy

def create_shuffle(n):
    """ Creates a shuffled word z of two words, x and y, with length of z being n*2. """
    x =''.join(random.choice(string.ascii_lowercase) for _ in range(n))
    y =''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # Create copies to remember original x and y
    x_return = copy.copy(x)
    y_return = copy.copy(y)

    z = ''
    while not ((len(x) is 0) and (len(y) is 0)):
        # Generate a random point to split the word
        x_split =random.randint(0,5)
        y_split =random.randint(0,5)

        z += x[:x_split]
        z += y[:y_split]
        x = x[x_split:]
        y = y[y_split:]

    return x_return, y_return, z

def is_shuffle(x, y, z):
    """ Calculates if two words, x and y, are shuffles, meaning that word z can be
    created from word x and word y by taking a letter from either word at a time.
    """
    x_len = len(x)
    y_len = len(y)
    z_len = len(z)

    # If the lengths do not match, the words are definitely not a shuffle
    if (x_len + y_len is not z_len):
        return False

    # Generate a table without pointer replication
    table = []
    for i in range(x_len + 1):
        table.append([])
        for j in range(y_len+1):
            table[i].append(False)

    # If the word uses noletters from either word, the shuffle is true.
    table[0][0] = True

    # Walk through the table and determine if the next letter is part of the word
    for i in range(x_len + 1):
        for j in range(y_len + 1):
            if (i == 0) and (j == 0):
                continue
            elif (i == 0):
                table[i][j] = ((y[j-1] is z[i+j-1]) and table[i][j-1])
            elif (j == 0):
                table[i][j] = ((x[i-1] is z[i+j-1]) and table[i-1][j])
            else:
                table[i][j] = (((x[i-1] is z[i+j-1]) and table[i-1][j]) or ((y[j-1] is z[i+j-1]) and table[i][j-1]))

    # Print user friendly representation of the table
    for row in table:
        print(row)

    return table[x_len][y_len]


if __name__ == '__main__':

    # Generate 100 shuffles for testing
    # for i in range(100):
    #     a = create_shuffle(55)
    #     print('{}: {}'.format(a, is_shuffle(a[0],a[1],a[2])))

    print()
    x = "chill"
    y= "hips"
    z = "chipshill"
    print(x + ' + ' + y + ' = ' +z+'?')
    print(is_shuffle(x,y,z))
    x = "aabb"
    y = "baab"
    z = "aaabbabb"
    print(x + ' + ' + y + ' = ' +z+'?')
    print(is_shuffle(x,y,z))
    x = "pneumonoultramicroscopicsilicovolcanoconiosis"
    y = "supercalifragilisticexpialidocious"
    z = "pneusupercalmonoifrulagitramlisicroscticeopicsixpilaliicovolcanodocconioioussis"
    print(x + ' + ' + y + ' = ' +z+'?')
    print(is_shuffle(x,y,z))
