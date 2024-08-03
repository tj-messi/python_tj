def chg_list(data_list):
    data_list.append(100)
    print(data_list)

def chg_list2(data_list):
    data_list=[]
    data_list.append(666)
    print(data_list)

if __name__ == '__main__':
    demo_list=['a',8,'x']
    chg_list(demo_list)
    print(demo_list)
    chg_list2(demo_list)
    print(demo_list)
