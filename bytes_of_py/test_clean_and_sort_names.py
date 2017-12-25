'''In this bite you will work with a list of names/surnames. First you will write a function to take out duplicates and title case the names. Then you will sort the list by surname and lastly determine what the shortest name is. With some Python handy builtins you can write this in a pretty concise way. Get it 'sorted' :)'''

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def clean_names(names):
    'dedup and title case names'
    # title() capitalize every word
    return [j.title() for j in set(names)]


def sort_by_surname_desc(names):
    names = clean_names(names)
    return sorted(names, key=lambda x:x.split()[1], reverse=True)


def shortest_name(names):
    'name not surname'
    names = clean_names(names)
    # return sorted(names, key=lambda x:len(x.split()[0]))[0].split()[0]
    names = [name.split()[0] for name in names]
    return min(names, key=len)



def test_clean_names():
    names = clean_names(NAMES)
    assert names.count('Bob Belderbos') == 1
    assert names.count('julian sequeira') == 0
    assert names.count('Brad Pitt') == 1
    assert len(names) == 10
    assert all(n.title() in names for n in NAMES)


def test_sort_by_surname_desc():
    names = sort_by_surname_desc(NAMES)
    assert names[0] == 'Julian Sequeira'
    assert names[-1] == 'Alec Baldwin'

def test_shortest_name():
    assert shortest_name(NAMES) == 'Al'
