# 예제 [[3.564	136.5]]
# input() return str() -> float() 형식을 바꿔야함. 랩핑해주기 
perimeter_se = float(input('perimeter_se : '))
perimeter_worst = float(input('perimeter_worst : '))

import pickle 

# 설명변수는 이런 서비스를 줄거다라는 것을 예측할 수 있도록 함. 
# ex)현재상황을 입력시 예측할 수 있는 머신러닝을 만들 예정. 
with open('datasets/BreastCancerWisconsinDataSet.pkl', 'rb') as regression_file :
    loaded_model = pickle.load(regression_file)
    input_labels = [[perimeter_se, perimeter_worst]] #학습했던 설명변수 형식에 맞게 적용 
    result_predict = loaded_model.predict(input_labels)
    print('Predict diagnosis Result : {}'.format(result_predict))
    pass 

# Predict diagnosis Result : [0] 예측값이 0이 /실제값도 0