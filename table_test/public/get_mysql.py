#coding=utf-8
import pymysql
import datetime
from windlight.table_test.public.get_col import rep_list_last_n,rep_list_rep,rep_list_n_to_m,rep_list_n

def get_mysql_h(host,sql,n=2): #查询mysql数据库,传数据库地址，sql查询，保留小数位数
    conn = pymysql.connect(host=host,port=3306,user='eeep',passwd='eeep',db='ia',charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)  #设置查询参数
    col=cur.execute(sql) #获取总行数
    list_c=list(cur.fetchall())
    # print("sql初始查询值",list_c)
#     list_mc=[('0:23:22', 12.345, 3.232),(datetime.datetime(2017, 6, 13, 0, 4), 12.345, 3.232), (datetime.datetime(2017, 6, 13, 14, 4), 3.232, 4.3532),(datetime.datetime(2017, 6, 13, 14, 4), 4.262, 22.987), (datetime.datetime(2017, 6, 13, 14, 5), 0.0, 0.0)]
    listx=[]  #元组组成的列表变成列表组成的列表，并保留n位小数
    if col!=0:
        for i in list_c:
            listx.append(list(i))
        # print("sql转成列表组成的列表",listx)
        for i in listx:
            for k in i:
                try:
                    i[i.index(k)]=round(float(k+0.000001),n)
                except:
                    pass
    #     print(listx)
         
        for i in listx: #将datetime转成字符串型
            for k in i:
                try:
                    if isinstance(k,datetime.timedelta):
                        i[i.index(k)]=str(k)
                    if isinstance(k,datetime.date):
                        i[i.index(k)]=str(k)
                except:
                    pass
    #     print(listx)
        for i in listx: #将特殊时间转换
            for k in i:
                try:
                    if ':' in k[0:2]:
                        i[i.index(k)]='0'+k
                except:
                    pass
        # print("行组成列表",listx)
    else:
        print("查询结果为空")
        listx=[]
    cur.close()
    conn.close()
    return listx
def get_mysql_l(host,sql,n=2): #查询mysql数据库,传数据库地址，sql查询，保留小数位数
    conn = pymysql.connect(host=host,port=3306,user='rpps',passwd='rpps',db='rpps',charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)  #设置查询参数
    col=cur.execute(sql) #获取总行数
    list_c=list(cur.fetchall())
    print("初始查询值",list_c)
#     list_mc=[('0:23:22', 12.345, 3.232),(datetime.datetime(2017, 6, 13, 0, 4), 12.345, 3.232), (datetime.datetime(2017, 6, 13, 14, 4), 3.232, 4.3532),(datetime.datetime(2017, 6, 13, 14, 4), 4.262, 22.987), (datetime.datetime(2017, 6, 13, 14, 5), 0.0, 0.0)]
    listx=[]  #元组组成的列表变成列表组成的列表，并保留n位小数
    if col!=0:
        for i in list_c:
            listx.append(list(i))
#         print("转成列表组成的列表",listx)
        for i in listx:
            for k in i:
                try:
                    i[i.index(k)]=round(float(k),n)
                except:
                    pass
    #     print(listx)
         
        for i in listx: #将datetime转成字符串型
            for k in i:
                try:
                    if isinstance(k,datetime.timedelta):
                        i[i.index(k)]=str(k)
                    if isinstance(k,datetime.date):
                        i[i.index(k)]=str(k)
                except:
                    pass
    #     print(listx)
        for i in listx: #将特殊时间转换
            for k in i:
                try:
                    if ':' in k[0:2]:
                        i[i.index(k)]='0'+k
                except:
                    pass
        print("行组成列表",listx)
        list3=[] 
        list_q=[0]
        list_z=[]
        for i in range(len(listx[0])):  #生成转置无列表列表
            for k in range(len(listx)):
                list3.append(listx[k][i])
#         print("转置原始列表",list3)
            
        for i in range(1,len(listx[0])+1):#切片列表
            list_q.append(len(listx)*i)
#         print("切片 列表",list_q)
            
        for i in list_q:
            list_z.append(list3[i:i+len(listx)])#最终转置列表
        list_z.pop()
        print("竖向列表",list_z)
    else:
        print("查询结果为空")
        listx=col
    cur.close()
    conn.close()
    return listx

def get_mysql_one(host,sql,n):
    #     host=get_excelvale(host1,host2)
    conn = pymysql.connect(host=host,port=3306,user='rpps',passwd='rpps',db='rpps',charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)  #设置查询参数
    col=cur.execute(sql) #获取总行数
    list_c=list(cur.fetchall())
    print("初始查询值",list_c)
    listx=[]
    for i in list_c:
        for k in i:
            listx.append(k)
    print("列表的值",listx)
    for i in listx:
        try:
            listx[listx.index(i)]=round(float(i),n)
        except:
            pass
    print("单列小数列表",listx)
    for i in listx:
        try:
            if isinstance(i,datetime.timedelta):
                listx[listx.index(i)]=str(i)
            if isinstance(i,datetime.date):
                listx[listx.index(i)]=str(i)
        except:
            pass
    print("单列列表",listx)
    for i in listx: #处理0点时间
        try:
            if ':' in i[0:2]:
                listx[listx.index(i)]='0'+k
        except:
            pass

# get_mysql_h('192.168.60.35','SELECT ctime,speed ,direction FROM rpps_data_calstation ORDER BY ctime asc limit 2',2)
# get_mysql_l('192.168.60.35','SELECT ctime,speed ,direction FROM rpps_data_calstation ORDER BY ctime asc limit 2',2)
# get_mysql_one('192.168.60.35','SELECT ctime FROM rpps_data_calstation ORDER BY ctime asc limit 2',2)
if __name__ == '__main__':

    # sqldate="\"2017-08-04\""
    # sql_old="SELECT a.PRE_DATE,a.PRE_TIME,a.ARI_TEM,a.WIND_SPEED,a.HUMIDITY,a.PRESSURE,a.TOTAL_IRRAD,a.DIRECT_IRRAD,a.DIFFUSE_IRRAD,a.GROUP_ID \
    # FROM GF_SPPS_NWP_DEAL a WHERE a.PRE_DATE=sqldate ORDER BY a.PRE_TIME"
    # sql=sql_old.replace("sqldate",sqldate)
    # get_mysql_h('192.168.60.167',sql)
    sql = "SELECT IF(ISNULL(( SELECT kname FROM dr_cmt_farminfo WHERE kid = b.pid AND ktype = '1' ))," \
          " '无', ( SELECT kname FROM dr_cmt_farminfo WHERE kid = b.pid AND ktype = '1' )) " \
          "AS province , farm_id, farm_name, project_type , IF(ISNULL(( SELECT deptname FROM tf_rbac_department WHERE deptid = b.fromcompany ))," \
          " '无', ( SELECT deptname FROM tf_rbac_department WHERE deptid = b.fromcompany )) AS owned_company , send_abnormal_days ," \
          " IF(mse_accuracy_rate_m >= 0, FORMAT(mse_accuracy_rate_m * 100, 2), -99) AS mse_accuracy_rate_m , IF(mse_accuracy_rate_nowcast_1 >= 0, " \
          "FORMAT(mse_accuracy_rate_nowcast_1 * 100, 2), -99) AS mse_accuracy_rate_nowcast_1 , IF(mse_accuracy_rate_nowcast_16 >= 0, FORMAT" \
          "(mse_accuracy_rate_nowcast_16 * 100, 2), -99) AS mse_accuracy_rate_nowcast_16 , IF(mse_accuracy_rate_a3_00 >= 0, FORMAT(mse_accuracy_rate_a3_00 * 100, 2), -99) " \
          "AS mse_accuracy_rate_a3_00 , IF(mse_accuracy_rate_a3_05 >= 0, FORMAT(mse_accuracy_rate_a3_05 * 100, 2), -99) AS mse_accuracy_rate_a3_05 ," \
          " IF(mse_accuracy_rate_a3_06 >= 0, FORMAT(mse_accuracy_rate_a3_06 * 100, 2), -99) AS mse_accuracy_rate_a3_06 , IF(mse_accuracy_rate_a3_e1 >= 0, " \
          "FORMAT(mse_accuracy_rate_a3_e1 * 100, 2), -99) AS mse_accuracy_rate_a3_e1 , IF(mse_accuracy_rate_a3_e2 >= 0, FORMAT(mse_accuracy_rate_a3_e2 * 100, 2), -99) " \
          "AS mse_accuracy_rate_a3_e2 , IF(mse_accuracy_rate_m_00 >= 0, FORMAT(mse_accuracy_rate_m_00 * 100, 2), -99) AS mse_accuracy_rate_m_00 , IF(mse_accuracy_rate_m_05 >= 0, " \
          "FORMAT(mse_accuracy_rate_m_05 * 100, 2), -99) AS mse_accuracy_rate_m_05 , IF(mse_accuracy_rate_m_06 >= 0, FORMAT(mse_accuracy_rate_m_06 * 100, 2), -99) " \
          "AS mse_accuracy_rate_m_06 , IF(mse_accuracy_rate_m_e1 >= 0, FORMAT(mse_accuracy_rate_m_e1 * 100, 2), -99) AS mse_accuracy_rate_m_e1 , IF(mse_accuracy_rate_m_e2 >= 0, " \
          "FORMAT(mse_accuracy_rate_m_e2 * 100, 2), -99) AS mse_accuracy_rate_m_e2 , IF(mse_accuracy_rate_05 >= 0, FORMAT(mse_accuracy_rate_05 * 100, 2), -99) AS mse_accuracy_rate_05 ," \
          " mse_assessment_score, mse_assessment_price, mse_assessment_memo FROM ia_forecast_deviation_analysis_month a INNER JOIN dr_cmt_farminfo b ON a.farm_id = b.farmorcordid WHERE 1 " \
          "= 1 AND province_key = 'SHANDONG' AND data_month = '2017-11' ORDER BY data_month, farm_id LIMIT 0,20"
    get_mysql_h('192.168.150.92',sql,4)

    list_sql_yuejun = get_mysql_h('192.168.150.92', sql, 4)
    list_set_nine_web = rep_list_rep(list_sql_yuejun, '-99', '--', 1)
    list_zong_none = rep_list_last_n(list_set_nine_web, 3, '--')
    list_zong_feng=rep_list_n(list_zong_none,4,"风测")
    print(list_zong_feng)
    # if str(listss[0][-1])=='None':
    #     print("ok")
