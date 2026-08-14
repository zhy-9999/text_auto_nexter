import this
from main import *
test = [
'''def f1():
    print(67)
    printf(1)
    return -0.3
def f2():
    print(67)
    printf(2)
    return -0.6
def f3():
    print(67)
    printf(3)
    return -0.9
''',
'',
'789113',
'q1.5w1.5e1.5r1.5t1.5q-2w-2e-2r-2t-2',
'x1aa2xx3bb4xx5cc6x'
]
for i in test:
    try:
        print(nexter(i,5))
    except Exception as e:
        print(str(e))