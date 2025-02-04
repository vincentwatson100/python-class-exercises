def chop(list):
    list = ['a', 'none', 'd']
    del list[0:4:2]
    print(list)
chop(['a', 'none', 'd'])

def middle(elements):
    elements = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    result = elements.pop(0)
    results = elements.pop(8)
    print(elements)
middle(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

