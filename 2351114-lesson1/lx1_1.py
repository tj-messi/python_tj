#2351114-朱俊泽-大数据科学与技术
'''
编写一个 diamond(n,m)函数，输入n,m，则print出n个字符*组成的菱形，菱形最长为m个*
当n=2,m=3时，输出示例
   *
  ***
 *****
  ***
   *
   *
  ***
 *****
  ***
   *
'''
def diamond(n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(" "*(m-j),end='')
            print("*"*(2*j-1))
        for j in range(1,m):
            print(" "*(j),end='')
            print("*"*(2*(m-j)-1))

if __name__ == '__main__':
    n=input('n=')
    m=input('m=')
    diamond(int(n),int(m))