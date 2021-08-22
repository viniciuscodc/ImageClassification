## ImageClassification

Image classification utilizing some machine learning libraries from python. The algorithm classify lung diseases patterns and features from 
images are extracted using Local Binary Pattern (LBP). It might take a while to train the model.

## Execution order

- InputData
- GenerateModel
- ModelTrain
- ModelTest
- ModelEvaluate

## Classes

- 0 - non-lung
- 1 - normal
- 2 - emphysema
- 3 - ground-glass
- 4 - fibrosis
- 5 - micronodules
- 6 - consolidation


## Filename Convention

{img_name}_{roi_number}_{coord_x}-{coord_y}_{percent}_{label}.dcm <br />
img_name = original image name <br />
roi_number = number of the roi found in the mask <br />
coord_x = x coordinate where starts the ROI rectangle <br />
coord_y = y coordinate where starts the ROI rectangle <br />
percent = percentage of pixels falling inside the roi <br />
label = label of the roi
