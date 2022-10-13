import random

def make_randlist(n,sm,lrg):
    """
    Generates List of 'n' random numbers between or equal
    smallest and largest value.
    
    Parameters:
        n (int) : Number of values in list.
        sm (int): smallest possible number.
        lrg(int): largest possible number.

    Returns:
        l (list): Generated list.
    """
    l = []
    for i in range(0,n):
        l.append(random.randint(sm,lrg))
    return l

def complete(org,sort):
    if len(org) != len(sort):
        return False
    else:
        l = [False]*len(org)
        for e in org:
            i = 0
            while i<len(sort):
                if l[i]==False and e==sort[i]:
                    l[i]=True
                i = i+1
        return not False in l

def test_sort(func, ntests, nelems,min=0,max=1000):
    """
    Generates n Tests for testing sorting function on numbered lists.
    Prints passed tests and list that failed to be sorted.

    Parameters:
        func (function): Sorting function to be tested.
        ntests (int)   : Number of tests.
        nelems (int)   : Number of elements in numbered lists.

    Returns:
        boolean        : True if all test passed and False if not.
    """
    for n in range(1,ntests + 1):
        l = make_randlist(nelems,min,max)
        m = l.copy()
        func(l)
        if not sorted(l) and not complete(m,l):
            print('FAILED: COULD NOT SORT ' + str(m))
            return False
    
    print('Passed all Tests.')
    return True
