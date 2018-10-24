from keras.optimizers import adam,adamax
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

def network(x,y):
    
    rates = [0.01,0.001,0.0001]
    
    model = Sequential()
    model.add(Dense(units = 3, kernel_initalizer='uniform',activation = 'relu', input_dim=2))

    model.add(Dense(units=1, activation='linear'))
    
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,shuffle=True)
    
    for rate in rates:
        
        model.compile(optimizer = adam(lr=rate), loss='mean_squared_error', metrics=['accuracy'])
        model.fit(x_train,y_train,batch_size=250,epochs=100,verbose=0)
        
        scores = model.evaluate(x_test,y_test, verbose=0)[1]*100
        
        print('Learning rate {0} gave accuracy of {1} %'.format(rate,scores))
        
