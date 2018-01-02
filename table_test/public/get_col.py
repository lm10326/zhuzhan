#coding=utf-8
# list=[['2017-06-24', '00:00:00', '1', ' ', '3'], ['2017-06-24', '00:15:00', '4', '2', '6'],['2017-08-08', '00:45:00', ' ']]
# list=[['2017-08-08', '00:15:00', ' '], ['2017-08-08', '00:45:00', ' '], ['2017-08-08', '01:15:00', ' '], ['2017-08-08', '01:45:00', ' '], ['2017-08-08', '02:15:00', ' '], ['2017-08-08', '02:45:00', ' '], ['2017-08-08', '03:15:00', ' '], ['2017-08-08', '03:45:00', ' '], ['2017-08-08', '04:15:00', ' '], ['2017-08-08', '04:45:00', ' '], ['2017-08-08', '05:15:00', ' '], ['2017-08-08', '05:45:00', ' '], ['2017-08-08', '06:15:00', ' '], ['2017-08-08', '06:45:00', ' '], ['2017-08-08', '07:15:00', ' '], ['2017-08-08', '07:45:00', ' '], ['2017-08-08', '08:15:00', ' '], ['2017-08-08', '08:45:00', ' '], ['2017-08-08', '09:15:00', ' '], ['2017-08-08', '09:45:00', ' '], ['2017-08-08', '10:15:00', ' '], ['2017-08-08', '10:45:00', ' '], ['2017-08-08', '11:15:00', ' '], ['2017-08-08', '11:45:00', ' '], ['2017-08-08', '12:15:00', ' '], ['2017-08-08', '12:45:00', ' '], ['2017-08-08', '13:15:00', ' '], ['2017-08-08', '13:45:00', ' '], ['2017-08-08', '14:15:00', ' '], ['2017-08-08', '14:45:00', ' '], ['2017-08-08', '15:15:00', ' '], ['2017-08-08', '15:45:00', ' '], ['2017-08-08', '16:15:00', ' '], ['2017-08-08', '16:45:00', ' '], ['2017-08-08', '17:15:00', ' '], ['2017-08-08', '17:45:00', ' '], ['2017-08-08', '18:15:00', ' '], ['2017-08-08', '18:45:00', ' '], ['2017-08-08', '19:15:00', ' '], ['2017-08-08', '19:45:00', ' '], ['2017-08-08', '20:15:00', ' '], ['2017-08-08', '20:45:00', ' '], ['2017-08-08', '21:15:00', ' '], ['2017-08-08', '21:45:00', ' '], ['2017-08-08', '22:15:00', ' '], ['2017-08-08', '22:45:00', ' '], ['2017-08-08', '23:15:00', ' '], ['2017-08-08', '23:45:00', ' ']]
# list=[['0034bbc66f3c021b175fdb18896cd8c6', -99, 'JIANGSU', 'EEE2718', 32],['0101', 1.0, 4.0, -99.0, 0.9745, 0.868, -99.0] ,[-99.0,-99.0,-99.0, -99.0, -99.0, -99.0, -99.0]]
list=[['山东地区', 'EEE1001', '（华润电力）威海东兴风电场', 1.0, '无', 18.0, '-99', '-99', '-99', '-99', '71.66', '-99', '-99', '-99', '-99', '-99', '-99', '-99', '-99', '-99', '--', '--', '--'], ['山东地区', 'EEE1017', '（大唐）长岛联凯驼矶风电场', 1.0, '无', 9.0, '-99', '-99', '-99', '80.09', '78.08', '-99', '-99', '-99', '-99', '-99', '-99', '-99', '-99', '-99', '--', '--', '--']]

def get_col(list,n):#得到第1,2列和第n列值列表组成的列表
    list_zong=[]
    for i in list:
        get_yuan=[]
        get_yuan.append(i[0])
        get_yuan.append(i[1])
        get_yuan.append(i[n-1])
        list_zong.append(get_yuan)
    return list_zong

def get_col_two(list,n):#得到第1列和第n列值列表组成的列表
    list_zong=[]
    for i in list:
        get_yuan=[]
        get_yuan.append(i[0])
        get_yuan.append(i[n-1])
        list_zong.append(get_yuan)
    return list_zong

def get_col_n(list,n):#得到某一列表组成的列表
    list_zong=[]
    for i in list:
        get_yuan=[]
        get_yuan.append(i[n-1])
        list_zong.append(get_yuan)
    return list_zong


def deltup(list,a): #删除列表中的某一特定元素
    lista=[]
    for i in list:
        listb=[]
        for k in i:
            if k!=a:
                listb.append(k)
        lista.append(listb)
    return lista
def del_list_tup(list,a): #删除列表中含某一元素的列表
    lista=list.copy()
    listb=[]
    for i in lista:
        if a not in i:
            listb.append(i)
    return listb

def del_list_n(list,n): #删除第n列表
    lista=list.copy()
    for i in lista:
        i.pop(n-1)
    return lista

def rep_list_n(list,n,m):#将第n列替换成m
    lista = list.copy()
    for i in lista:
        i[n-1]=m
    return lista

def rep_list_n_to_m(list,n,m):
    lista = list.copy()
    qq=''
    for i in lista:
        qq=i[n-1]
        i[n-1]=i[m-1]
        i[m-1]=qq
    return lista




def rep_list_last_n(list,n,m):#修改后n行为m
    lista = list.copy()
    for i in lista:
        for k in range(n):
            i[-(k+1)]=m
    return lista

def get_col_t(list,n):#修改后n列类型
    lista=list.copy()
    for i in lista:
        for k in range(n):
            i[-(k+1)]=str(i[-(k+1)])
    return lista


def rep_list_rep(list,a,b,n): #将值替换成某一值，并扩大n倍
    lista=list.copy()
    for i in lista:
        for m in i:
            if m==a:
                i[i.index(m)]=b
    for i in lista:
        for m in i:
            try:
                if m>0 and m<1:
                    i[i.index(m)]=i[i.index(m)]*n
            except:
                pass
    return lista

def set_str(list):#将列表中的数值全部转成str
    listb=[]
    for i in list:
        lista = []
        for k in i:
            try:
                lista.append(str(k))
            except:
                lista.append(k)
        listb.append(lista)
    return listb

def set_float(list,n):#将列表中的数值全部转成float
    listb=[]
    for i in list:
        lista = []
        for k in i:
            try:
                m=round((float(k)+0.000001),n)
                lista.append(m)
            except:
                lista.append(k)
        listb.append(lista)
    return listb


if __name__ == '__main__':
    # print(list)
    # print(get_col(list,5))
    # print(list)
    # print(deltup(list,' '))
    # print(list)
    # print(del_list_tup(list,' '))
    # print(list)
    # print(rep_list_rep(list,'-99','--',1))
    # print(rep_list_n_to_m(list,1,23))
    # print(del_list_n(list,1))
    # print(rep_list_n(list,2,222))
    # print(type(get_col_t(list,1)[-1][-1]))
    list1=[[3.05, 3.05, 4.6, '--', '','',],[33, '', '', '', '', '']]
    print(set_float(list1,1))
