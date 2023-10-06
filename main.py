# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#数字
print(74)
print(98.5)
#字符串
print('helloworld')
print("helloworld")
#含有运算符的表达式
print(3+1)
fp=open('D:/text.text','a+')
print('helloworld',file=fp)
fp.close()

print('hello','world','Python')

var1 = 'Hello World!'
var2 = "Python Runoob"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])
stu = {"name":"zhufeiyu","age":19}
stu["age"] =20
print(stu)
del stu["age"]
print(stu)
stu = {"name":"zhufeiyu","age":19}
stu["sex"] = "m"
print(stu)
for i in range(10):  #0 ~ 9
    print(i)