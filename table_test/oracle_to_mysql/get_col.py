#coding=utf-8
list=[['2017-06-24', '00:00:00', '1 ', ' ', ' 3'], ['2017-06-24', '00:15:00', ' 4', ' ', '6 ']]
def get_col(list,n):#得到第1,2列和第n列值列表组成的列表
    list_zong=[]
    for i in list:
        get_yuan=[]
        get_yuan.append(i[0])
        get_yuan.append(i[1])
        get_yuan.append(i[n-1])
        list_zong.append(get_yuan)
    return list_zong
def deltup(list,a): #删除列表中的某一特定元素
    try:
        for i in list:
            for k in i:
                if k==a:
                    i.remove(k)
    except:
        pass
    return list

if __name__ == '__main__':
    print(get_col(list,5))
    print(deltup(list,' '))

