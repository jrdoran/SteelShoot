'''
To add another column, you would have to loop over each row. An easy way to do this is with a list comprehension.

L = [x + [0] for x in L]
giving

L = [[1,2,3,0],
     [4,5,6,0]]  
     
 '''    
print ('jd starting')

import operator

def sort_table(table, cols):
    """ sort a table by multiple columns
        table: a list of lists (or tuple of tuples) where each inner list 
               represents a row
        cols:  a list (or tuple) specifying the column numbers to sort by
               e.g. (1,0) would sort by column 1, then by column 0
    """
    for col in reversed(cols):
        table = sorted(table, key=operator.itemgetter(col) )

    return table


if __name__ == '__main__':
    mytable = [
        ['Joe', 'Clark', '1989'],
        ['Charlie', 'Babbitt', '1988'],
        ['Alan', 'Clark', '1804'],
        ]
        
mytable.append(['aJim','apontiac','1111'])
mytable.append(['bJim','Bpontiac','2222'])
    
for row in sort_table(mytable, (1,0)):    
    print (row)
       
        
print ('jd ending')

'''
Results:
('Frank', 'Abagnale', '2002')
('Charlie', 'Babbitt', '1988')
('Alan', 'Clark', '1804')
('Bill', 'Clark', '2009')
('Joe', 'Clark', '1989')

list.append(x)
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is x. It is an error if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.clear()
Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])
Return zero-based index in the list of the first item whose value is x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)
Return the number of times x appears in the list.

list.sort(key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Equivalent to a[:].



'''