from sklearn import svm
import pickle

from sklearn.model_selection import GridSearchCV

param_grid={'C':[0.1,1,10,100],'gamma':[0.0001,0.001,0.1,1]}

svc=svm.SVC(probability=True)

model=GridSearchCV(svc,param_grid)

pickle.dump( model, open( 'Data/model.pickle', 'wb' ) )

