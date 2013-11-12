#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Parser
========
Parse the txt files for outputting the reviews as a list of tuples
where each tuple is
(filename, linenumber, aggregatevote, sentence)

author = "Shreyas"
email = "shreyas@ischool.berkeley.edu"
python_version = "Python 2.7.5 :: Anaconda 1.6.1 (x86_64)"
"""

from __future__ import division
from optparse import OptionParser

import os
import re


def getReportDir():
    optionparser = OptionParser()

    optionparser.add_option('-d', '--dir', dest='dir')

    (option, args) = optionparser.parse_args()

    if not option.dir:
        return optionparser.error('directory not provided.\n Usage: --data="path.to.data"')

    return { 'dir' : option.dir }




def main():
    reportDir = getReportDir()

    print reportDir


if __name__ == "__main__":
    main()
