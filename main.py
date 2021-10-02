"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x;
    else:
        return foo(x-1) + foo(x - 2)
   
def longest_run(mylist, key):
    n = 0 
    v = []
    for x in range(len(mylist)):
        if mylist[x] == key:
            n +=1
        else: 
            n = 0
        v.append (n)
    return max(v)


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
def lrr(mylist, key):
    if len(mylist) > 1:
        left = lrr(mylist[:len(mylist)//2], key)
        right = lrr(mylist[len(mylist)//2:], key)
    if len(mylist) == 1:
        if mylist == [key]:
            return Result(1,1,1,1)
        else:
            return Result(0,0,0,0)
    x = Result(left.left_size,right.right_size,0,left.is_entire_range * right.is_entire_range)
    if x.is_entire_range == 1:
        x.longest_size = left.longest_size + right.longest_size
        x.left_size = x.longest_size
        x.right_size = x.longest_size
        return x
    if left.right_size >= 1 and right.left_size >= 1:
            x.longest_size = max(left.longest_size,right.longest_size,left.right_size + right.left_size)
    elif left.right_size == 0 or right.left_size == 0:
        x.longest_size = max(left.longest_size,right.longest_size)
    return (x) 

    
 

def longest_run_recursive(mylist, key):
    return lrr(mylist,key).longest_size
"""
def test_longest_run_recursive():
    assert longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run_recursive([12,12,12,8,12,12,12,0,12,1], 12) == 3  
    assert longest_run_recursive([12,12,12,8,12,12,12,0,12,1], 1) == 1
    assert longest_run_recursive([2,12,12,8,12,13,12,0,12,1], 12) == 2
    assert longest_run_recursive([7,7,7], 12) == 0
    assert longest_run_recursive([7,7,7], 7) == 3
    assert longest_run_recursive([2,12,12,8,12,12,12,0,12,1,12,12,12,12,12], 12) == 5
    print ("good")
"""
## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


