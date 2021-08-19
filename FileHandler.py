import glob
import shutil
import os

Categories=['non-lung','normal','emphysema','ground-glass','fibrosis','micronodules','consolidation']

paths = glob.glob("Images/**/**", recursive=True)
#output = "Images/3\CT-7358-0002_0_196-275_96_0.dcm"

#ignore folders, pick files
def filterPath(list):   
    filteredPaths = []
    for path in list:
        if (path.endswith('dcm')):
            filteredPaths.append(path)
    return filteredPaths

paths = filterPath(paths)

def filterByCategory(n):
    filteredPaths = []
    for path in paths:
        split1 = path.split(".dcm") #output = "Images/3\CT-7358-0002_0_196-275_96_0"
        split2 = split1[0].split("_") #output = "0"
        label = split2[4]
        if (label == str(n)):
            filteredPaths.append(path)
    return filteredPaths

def createDirectories():

    dir = 'ImagesLabeled'

    if not os.path.isdir(dir):
        os.mkdir(dir)

        print('Creating directories...')
        for i, category in enumerate(Categories):
            category_dir=os.path.join(dir,str(i))
            os.mkdir(category_dir)

def copyFiles():
    
    print('Copying Files...')
    for i, category in enumerate(Categories):
        for img_file in filterByCategory(i):
            original = img_file
            dir = 'ImagesLabeled'
            category_dir=os.path.join(dir,str(i))
            target = category_dir
            shutil.copy(original, target)

createDirectories()
copyFiles()
print("Done")

