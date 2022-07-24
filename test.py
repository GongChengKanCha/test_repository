from keras.models import Sequential
from keras.layers import Dense


model = Sequential()
model.add(Dense(units=3,activation="sigmoid",input_dim=3))
model.add(Dense(units=1,activation="sigmoid"))

