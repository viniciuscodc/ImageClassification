import pandas as pd
import os
from skimage.transform import resize
from skimage.io import imread
from skimage import feature
import numpy as np
import Lmp

Categories=['non-lung','normal','emphysema','ground-glass','fibrosis','micronodules','consolidation']

flat_data_arr=[] #input 
target_arr=[] #output array

datadir = 'ImagesConvertedLabeled'

for i, category in enumerate(Categories):

    print(f'loading... category : {category}')

    path=os.path.join(datadir,str(i))

    for img in os.listdir(path):

        img_array=imread(os.path.join(path,img))  

        flat_data_arr.append(Lmp.describe(img_array,8,1))

        target_arr.append(i)
        
        print(f'loaded category:{category} successfully')
        

flat_data=np.array(flat_data_arr)
target=np.array(target_arr)

df=pd.DataFrame(flat_data) #dataframe
df['Target']=target

x=df.iloc[:,:-1] #input data 
y=df.iloc[:,-1] #output data

x.to_pickle('Data/x.pickle')
y.to_pickle('Data/y.pickle')

