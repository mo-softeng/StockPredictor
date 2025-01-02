from prepareData import testing_data, trainig_data, scalar
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from fetchApi import company
model = load_model("keras_model.keras")
import numpy

df = trainig_data.tail(100)._append(testing_data, ignore_index=True) #add past 100 days to the testing data
input_test_data = scalar.fit_transform(df) 
x_test = []
y_test = []
for i in range(100, input_test_data.shape[0]):
    x_test.append(input_test_data[i-100:i])
    y_test.append(input_test_data[i, 0])
    
x_test, y_test = numpy.array(x_test), numpy.array(y_test) # y_test is orginal prices
y_predicted = model.predict(x_test) # predict values

y_predicted = y_predicted * (1/scalar.scale_)  # scaled up predicted values
y_test = y_test * (1/scalar.scale_) # scaled up acctual values

plt.plot(y_predicted, color="r")
plt.plot(y_test, color="b")
plt.xlabel("days")
plt.ylabel("prices")
plt.title(company.upper())
plt.show()

