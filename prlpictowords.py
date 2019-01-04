#
# Script for transforming figures to number of words in prl
#
# Pretty ad hoc at the moment as it assumes all images are either 1. single 
# images of one column width, or 2. forms pairs of two images to form two
# column image. At the moment the script does not know which images will
# combine to a two column image, so the final value will be an estimate
#
# Usage: 
# * put file where your images are at
# * put number of word in nwords variable
# * either put your image names in "lookfor" or uncomment "ifendswith()" to 
#   automatiacally append all images of some file type
#
# TODO 
#


from PIL import Image
import os

nwords = 2750

filenames = []
sizes = []
aspects = []

lookfor = ["model.png","minmaxplot.png","fstd.png","pstd.png","thermal.png","irregular.png","trajectory1.png","trajectory2.png","doubleslip.png","offset.png","veldep.png","veldeppot.png"]

for filename in os.listdir("./"):
#    if filename.endswith(".png"):
    if filename in lookfor:
        print filename
        filenames.append(filename)
        img = Image.open(filename)
        sizes.append(img.size)
    else:
        continue

for el in sizes:
    print [el[0],el[1]]
    aspect = float(el[0])/float(el[1])
    aspects.append(aspect)

#print (aspects)

total = 0;
for el in aspects:
    total += 300/(0.5*el) + 40
    
total /= 2
estimate = total + nwords
balance = 3750 - estimate

print "estimated word count from figures: {}".format(total)
print "estimated total word count: {}".format(estimate)
print "your estimated word count balance is: {}".format(balance)
