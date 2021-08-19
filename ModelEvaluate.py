from skimage.transform import resize
from skimage.io import imread
import matplotlib.pyplot as plt
import pandas as pd
import Lmp

Categories=['non-lung','normal','emphysema','ground-glass','fibrosis','micronodules','consolidation']

trained_model  = pd.read_pickle('Data/trainedModel.pickle')

url=input('Enter URL of Image :')
#url='ImagesConvertedLabeled/0/CT-9620-0011_2_192-130_88_0.png'
img=imread(url)

plt.imshow(img, cmap='gray')
plt.show()

l=[]
l.append(Lmp.describe(img,8,1)) 

probability=trained_model.predict_proba(l)

for ind,val in enumerate(Categories):    
    print(f'{val} = {probability[0][ind]*100}%')

print("The predicted image is : "+Categories[trained_model.predict(l)[0]])
