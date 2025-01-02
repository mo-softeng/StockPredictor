import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from fetchApi import company
import numpy


#convert json file to pandas data fram
df = pd.read_json(F"stock_data.json")

#remove unwanted columns
df = df.drop(["date", "adjLow", "adjOpen", "adjVolume", "divCash", "splitFactor", "volume", "adjClose", "adjHigh"], axis=1)

#split data into test and training 
trainig_data = pd.DataFrame(df['close'][0:int(len(df)*0.70)]) # 70% of data 
testing_data = pd.DataFrame(df['close'][int(len(df)*0.70):])  # 30% of data

#scale down training data between 0, 1
scalar = MinMaxScaler(feature_range=(0,1))
scaled_array_training_data = scalar.fit_transform(trainig_data)

x_train = []
y_train = []

for i in range(100, scaled_array_training_data.shape[0]):
    x_train.append(scaled_array_training_data[i-100:i])
    y_train.append(scaled_array_training_data[i, 0])

x_train, y_train = numpy.array(x_train), numpy.array(y_train)
print("Data prepared")




