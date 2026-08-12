import re
first = []
print('请输入要找规律的内容，按Ctrl+C或Ctrl+D结束输入：')
# aa1bb bb1ccaa4bb bb1cc
try:
    while True:
        first.append(input())
except EOFError:
    print()
except KeyboardInterrupt:
    print()
second = ''.join(first)
third = ''.join(second.split())
raw_letters = re.split(r'-?\d+(?:\.\d+)?', second)
letters = re.split(r'-?\d+(?:\.\d+)?', third)
numbers = re.findall(r'-?\d+(?:\.\d+)?', third)
# print(letters)
# print(numbers)
fenge = letters[-1] + letters[0]
# print(fenge)
for i in range(len(letters)-1,-1,-1):
    if fenge == letters[i]:
        xvnhuan = [raw_letters[0]] + raw_letters[i+1:]
        break
# print(xvnhuan)
def zhixian(y0,y1,x):
    return str(float(y0) + float(x) * (float(y1) - float(y0)))
def xiang(x):
    out = xvnhuan[0]
    nums_per_xvnhuan = len(xvnhuan) - 1
    for i in range(len(xvnhuan)-1):
        out += zhixian(numbers[i],numbers[i+nums_per_xvnhuan],x)
        out += xvnhuan[i+1]
    return out
for i in range(0,int(input('请输入续写项数：'))):
    print(xiang(i))