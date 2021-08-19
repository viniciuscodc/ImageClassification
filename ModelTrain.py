from sklearn.model_selection import train_test_split
import pandas as pd
import pickle
import time

x = pd.read_pickle("Data/x.pickle")
y = pd.read_pickle("Data/y.pickle")
model = pd.read_pickle("Data/model.pickle")

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=77,stratify=y)

print('Splitted Successfully')

print('Training...')

start_timer = time.time()
model.fit(x_train,y_train)
end_timer = time.time()

pickle.dump( model, open( 'Data/trainedModel.pickle', 'wb' ) )
pickle.dump( x_test, open( 'Data/x_test.pickle', 'wb' ) )
pickle.dump( y_test, open( 'Data/y_test.pickle', 'wb' ) )

print('The Model is trained')

hours, rem = divmod(end_timer-start_timer, 3600)
minutes, seconds = divmod(rem, 60)
print("--- {:0>2}:{:0>2}:{:0>2} ---".format(int(hours),int(minutes),int(seconds)))

