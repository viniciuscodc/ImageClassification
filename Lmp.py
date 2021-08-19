import numpy as np
from skimage import feature

def describe(image,points,radius, eps=1e-7):
	# compute the Local Binary Pattern representation
	# of the image, and then use the LBP representation
	# to build the histogram of patterns
	lbp = feature.local_binary_pattern(image, points,
		radius, method="uniform")
	(hist, _) = np.histogram(lbp.ravel(),
		bins=np.arange(0, points + 3),
		range=(0, points + 2))
	# normalize the histogram
	hist = hist.astype("float")
	hist /= (hist.sum() + eps)
	# return the histogram of Local Binary Patterns
	return hist