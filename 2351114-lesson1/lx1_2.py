#2351114-朱俊泽-大数据科学与技术
'''
编写一个tablem(n)函数，输出n阶乘法表
当 n=6 输出示例
1
2 4
3 6   9
4 8   12  16
5 10 15  20  25
6 12 18  24  30 36
'''
def tablem(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j*i,end='')
            print(' ',end='')
        print()

if __name__ == '__main__':
    n=input('n=')
    tablem(int(n))