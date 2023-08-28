# 예제 [[16.34, 87.21]]
# input() return str() -> float() 형식을 바꿔야함. 랩핑해주기 
texture_mean = float(input('texture_mean : '))
perimeter_mean = float(input('perimeter_mean : '))

# 값 예측하려면 pickle이용해서 import 해야함 

import pickle 

# 설명변수는 이런 서비스를 줄거다라는 것을 예측할 수 있도록 함. 
# ex)현재상황을 입력시 예측할 수 있는 머신러닝을 만들 예정. 
with open('datasets/BreastCanceerWisconsin_Regression.pkl', 'rb') as regression_file :
    loaded_model = pickle.load(regression_file)
    input_labels = [[texture_mean, perimeter_mean]] #학습했던 설명변수 형식에 맞게 적용 
    result_predict = loaded_model.predict(input_labels)
    print('Predict radius_mean Result : {}'.format(result_predict))
    pass 


