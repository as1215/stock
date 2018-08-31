import pandas as pd
from sqlalchemy import create_engine
import getopt
import sys
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
pd.options.mode.chained_assignment = None 
#test
engine = create_engine('oracle+cx_oracle://dwhuaxing:QF#wJpjLh@sensor3')

#把sql语句粘贴到下面                       
create_table_sql = '''
create table abc (
xxx
xxx
xx
)
'''

truncate_table_sql = '''
truncate table dwhuaxing.lte_cell_geohash_20180829
'''
                       

#创建一张表
def create_table():
    engine.connect().execute(create_table_sql)
    print('创表完成')

#入库
def input_data():
    df = pd.read_csv('~/python_test/xxxx.csv',engine,if_exists='append', index=False)
    df.to_sql('lte_cell_geohash_20180829',engine)
    
    print('success input_data')
    
#清空一张表  
def truncate_table():
    engine.connect().execute(truncate_table_sql)


#添加数据
def add_data():
    df = pd.read_csv('~/python_test/xxxx.csv',engine,if_exists='append', index=False)
    df.to_sql('lte_cell_geohash_20180829',engine)
    
    print('success add_data')
    pass


if __name__ == '__main__':
    
    opts, args = getopt.getopt(sys.argv[1:], 'acit')
    
    add = 0
    create= 0
    input_base = 0
    truncate = 0
    
    for opt, value in opts:
        if opt == '-c':  # 创建一张表
            create= 1
        elif opt == '-i':  # 入库
            input_base = 1
        elif opt == '-t':  # 清空一张表
            truncate = 1
        elif opt == 'a':
            add ==1  #添加数据
    
    if create == 1 :
        pass
    
    if input_base ==1 :
        input_data()
        
    if truncate == 1 :
        truncate_table()
        
    if add == 1 :
        add_data()
        
