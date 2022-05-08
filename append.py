 b=[]
 name=["John","James"]
 names=["John","James"]
 for name in names:b.append(name)
 b
['John', 'James']
 print(f'{b} likes this')
['John', 'James'] likes this
       print(f'{b[0]} and {b[1]} likes this')
John and James likes this
 b
['John', 'James']
 b=[[],'John','James']
 b
[[], 'John', 'James']
 print(b[0])
[]
def likes(names):
    for name in names:
        b=[]
        b.append(name)
    return b
a=likes(['John','Amber'])
print(f'{a} likes this')
    # your code 

