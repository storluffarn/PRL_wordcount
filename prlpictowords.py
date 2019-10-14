#
# Script for transforming figures to number of words in prl
#
# written by: David Andersson
#
# Limitations:
# Pretty ad hoc, but it does the trick mostly. The program only handles either single
# or two side by side images at the moment. However, more complex figures can be 
# estimated by the offset parameter. Side by side images are assumed to have the same
# aspect ratio. The automated word counting from tex source only works on UNIX sytems
# with texcount installed (tested for version 3.1). Probably doesn't work for obscure
# image formats, see Python PIL package
#
# Usage: 
# * put the file where your images are at
# * put your tex source file in "texfile" or put your current number of word in 
#   "nwords" and comment out the lines before that
# * either put your file names in "lookfor" or uncomment "ifendswith(*.type)" to 
#   automatiacally append all images of some file type
# * for side by side images: only add only *one* of the images to "lookfor", 
#   and add those files' filenames to the "sidebyside" list. e.g. if you have two
#   images img1.x and img2.x that you wand side by side, only add img1 to "lookfor",
#   but also add it to "sidebyside". for multi column images, only add the first of
#   each column
# * word "balance" holds the remaining PRL word count, it is printed in the end, 
#   you want it be > 0 in order not to be in trouble
#
# Changelog:
# 
# TODO 
#
# * more image layouts than only side by side with two columns
# * possibly read in from pdf instead of tex
# * update to python 3
#


from PIL import Image
import os
import subprocess

texfile = "paper.tex"
child = subprocess.Popen('texcount {} | grep "Words in text"'.format(texfile),stdout=subprocess.PIPE,shell=True)
wordsstring = child.communicate()[0]
words = wordsstring.split()[-1]

nwords = int(words)

print "number of words in source text {}".format(words)

filenames = []
sizes = []
aspects = []

lookfor = ["file1.png","file2.png"]

sidebyside = ["file1.png"]

print "processing image:"
for filename in os.listdir("./"):        # read in all files in lookfor
#    if filename.endswith(".png"):      # read in all files of *.type
    if filename in lookfor:
        print filename
        filenames.append(filename)
        img = Image.open(filename)

        x,y = img.size
        if filename in sidebyside:
            x = x*2

        size = [x,y]

        sizes.append(size)
    else:
        continue

print "fetching image sizes"
for el in sizes:                        # claculate all aspects
    print [el[0],el[1]]
    aspect = float(el[0])/float(el[1])
    aspects.append(aspect)

print "the calculated the aspects"
print (aspects)

total = 0;
for el in aspects:
    total += 300/(0.5*el) + 40
    
# offset = 2                            # used for estimating non-standard image configurations
# total /= offset
estimate = total + nwords
balance = 3750 - estimate

print "estimated word count from figures: {}".format(total)
print "estimated total word count: {}".format(estimate)
print "your estimated word count balance is: {}".format(balance)

