Created on 18/07/2019 by Shawn Park.

#This directory "SVD" is a directory for recommendation system using SVD.

SVD
  |-- svd.py : python program for SVD.
  |-- randomMatrixGenerator.py: python program for randomly generated matrix.
  |-- input.csv : input file for svd.py
  |-- output.csv : output file from svd.py
  |-- random.csv : result csv file of randomMatrixGenerator.py
  |-- README.md



## BASIC INFO:

INPUT FORMAT : n x m matrix. row : users / column : words / entry : information about familiar or not or unknown.

OUTPUT FORMAT : n x m matrix with no unknown entries.

Entries : represents familiar words as value 1, unfamiliar words as value -1, unknowns as value 0.



##USAGES:

1. randomMatrixGenerator.py : python3 randomMatrixGenerator.py n m (ex, python3 randomMatrixGenerator.py 10 10)


2. svd.py : python3 svd.py <filename.csv> (ex. python3 svd.py input.csv)