#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Extractor
=========
After parsing, given a list of tuples of the format:
[(filename, filetxt, answer)]

output a list of tuples with
[(filename, filetxt, answer, feat1, feat2, feat3, ..)]

author = "Shreyas"
email = "shreyas@ischool.berkeley.edu"
python_version = "Python 2.7.5 :: Anaconda 1.6.1 (x86_64)"
"""
from __future__ import division
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords



def featureAggregator(inputdata):
    """
    Given a sentence, call the feature extractor and aggregate the
    returned features into the same dataset
    """
    outputdata = []
    for inputLine in inputdata:
        # aggregate those values into 1 tuple of features
        features = featureExtractor(inputLine[1])

        # append those features
        inputLineList = list(inputLine)
        inputLineList.append(features)
        outputLineTuple = tuple(inputLineList)
        outputdata.append(outputLineTuple)

    return outputdata



def featureExtractor(reportStr):
    """
    Extract Features
    """
    featList = {}

    featList['wordCount']       = getWordCount(reportStr)


    return featList




def getWordCount(rstr):
    words = [w.lower() for w in word_tokenize(rstr) if w not in stopwords.words('english')]

    return len(words)



def main():
    print "Extractor"



if __name__ == "__main__":
    main()
