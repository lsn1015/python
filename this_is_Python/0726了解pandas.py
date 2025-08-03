import pandas as pd
import numpy as np

lst= [6, 7, 1, 9, 2, 3]
ser = pd.Series(lst)
print(ser)

d = {'a': 1,'b': 2,'c': 3}
ser = pd.Series(d)
print(ser)

lst= [6, 7, 1, 9, 2, 3]
ser = pd.Series(lst, index = ['a','b','c','d','e','f'])
print(ser)

# np.nan  np.Nan   np.NAN

lst= [6, 7, 1, 9, 2, 3]
ser = pd.Series(lst, index = ['a','b','c',(),'e','f'])
print(ser)
print(ser['a'])
print(ser[()])

lst= [6, 7, 1, 9, 2, 3]
ser = pd.Series(lst, index = ['a','b','c','d','e','f'],name = 'first')
print(ser)
print(ser.dtype)
print(ser.shape)
print(ser.size)
print(ser.name)
print(ser.values)
print(type(ser.values))
print(ser.index)

lst= [6, 7, 1, 9, 2, 3]
ser = pd.Series(lst, index = ['a','b','c','d','e','f'],name = 'first')
ser.index =pd.RangeIndex(0,6,1)
ser.name = 'first-ser'
print(ser)

lst= [6, 7, 1, 9, 2, 3]
ser = pd.Series(lst, index = ['a','b','c','d','e','f'])

print(ser[3])
print(ser[-3])
print(ser['d'])
print(ser[1:4:2])
print(ser['b':'d':2])
print(ser[[1,3,-2]])
print(ser[['b','d','e']])
ser[1] = 777
print(ser)
ser['g'] = 8
print(ser)
del ser['c'], ser['a']
print(ser)


lst= [6, 7, 1, 9]
ser1 = pd.Series(lst, index = ['a','b','c','d'])
print(ser1)

lst= [3, 4, 6]
ser2 = pd.Series(lst, index = ['e','f','a'])
print(ser2)

print(ser1 + ser2)

lst = [6, 7, 1, 9]
df = pd.DataFrame(lst)
print(df)
print(df.shape)
print(df.values)

lst = [6, 7, 1, 9]
arr = np.array(lst)
df = pd.DataFrame(arr)
print(df)

lst = [['Tom', 18, 188, 75],
       ['Bob', 19, 179, 68],
       ['Linda', 19, 187, 78]]
df = pd.DataFrame(lst)
print(df)

d = {'name':['Tom', 'Bob', 'Linda'],
     'age':[18, 19, 17],
     'height':[188, 179, 177],
     'weight':[75, 68, 62]}
df = pd.DataFrame(d)
print(df)

index = ['name','age','height','weight']
lst = [pd.Series(['Tom', 18, 188, 75],index, name='Stu1'),
       pd.Series(['Bob', 19, 179, 68],index, name='Stu2'),
       pd.Series(['Linda', 19, 187, 78],index, name='Stu3')]
df = pd.DataFrame(lst)
print(df)

lst = [['Tom', 18, 188, 75],
       ['Bob', 19, 179, 68],
       ['Linda', 19, 187, 78]]
df = pd.DataFrame(lst, index=['stu1', 'stu2', 'stu3'],
                  columns=['name', 'age', 'height', 'weight'])

print(df)
print(df.dtypes)
print(df.shape)
print(df.size)
print(df.index)
print(df.columns)
print(df.values)
# df.index = [1,2,3]
# df.columns = list('abcd')
# print(df)
# print(df.loc[:,'age'])
# print(df.iloc[:,1])
# print(df.loc[:,'height':'age':-1])
# print(df.iloc[:,2:0:-1])



np.random.seed(3)
arr = np.random.randint(1,10,size=(3,4))
df1 = pd.DataFrame(arr, index=['f','a','g'],columns=list('TKMC'))
print(df1)
print()
print(df1 +100)

arr = np.random.randint(1,10,size=(4,3))
df2 = pd.DataFrame(arr, index=['a','d','g','l'],columns=list('shT'))
print(df2 + df1)


