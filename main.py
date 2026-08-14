import re

def console_input(tip: str) -> str:
#     return '''def f1():
#     print(67)
#     printf(1)
#     return -0.3
# def f2():
#     print(67)
#     printf(2)
#     return -0.6
# def f3():
#     print(67)
#     printf(3)
#     return -0.9
# '''
    input_list = []
    print(tip)
    try:
        while True:
            input_list.append(input())
    except EOFError:
        print()
    except KeyboardInterrupt:
        print()
    input_string = '\n'.join(input_list) 
    return input_string
def linear(y0,y1,x) -> float:
    return float(y0) + float(x) * (float(y1) - float(y0))
def the_xth_cycle(x:int, cycle:list, numbers:list) -> str:
    out = cycle[0]
    nums_per_cycle = len(cycle) - 1
    for i in range(len(cycle)-1):
        out += str( linear( numbers[i], numbers[i+nums_per_cycle], x ) )
        out += cycle[i+1]
    return out
def nexter(input_string:str,times:int) -> str:
    input_no_space = ''.join(input_string.split())
    find_number_re = r'-?\d+(?:\.\d+)?'
    raw_letters = re.split(find_number_re, input_string)
    letters = re.split(find_number_re, input_no_space)
    numbers = re.findall(find_number_re, input_no_space)
    spliter = letters[-1] + letters[0]
    cycle = []
    for i in range(len(letters)-1,-1,-1):
        if spliter == letters[i]:
            cycle = [raw_letters[0]] + raw_letters[i+1:]
            break
    if cycle:
        output = ''
        for i in range(times):
            output += the_xth_cycle(i,cycle,numbers)
        return output
    else:
        raise RuntimeError('在'+input_no_space+'中未找到循环节')
# print(cycle)
if __name__ == '__main__':
    # input_string = 
    output = ''
    try:
        input_string = console_input('请输入要找规律的内容，按Ctrl+C或Ctrl+D结束输入：')
        times = int(input('请输入续写项数：'))
        output = nexter(input_string,times)
    except Exception as e:
        output = '错误：' + str(e)
    finally:
        if output:
            print(output)
        else:
            print('错误：返回值为空')