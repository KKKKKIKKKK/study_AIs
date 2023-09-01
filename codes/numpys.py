# 기존방식으로 하면 array 인지 모름 . 
py_list = [[1,2]
           ,[3,4]
           ,[5,6]] # list 3차원 

import numpy as np 
np_array = np.array([[7,8]
                    ,[9,10]
                    ,[11,12]]) # array = 행렬 
#병합
np_array02 = np.array(py_list)
np.concatenate((np_array, np_array02), axis=0 ) # 열기준
np.concatenate((np_array, np_array02), axis=1 ) # 행기준
pass 

# np.mean(np_array)
# 9.5

# np.mean(np_array, axis=0) //0 열단위 (밑으로)
# array([ 9., 10.])

#np.mean(np_array, axis=1) //행단위 (옆으로)
#array([ 7.5,  9.5, 11.5])
