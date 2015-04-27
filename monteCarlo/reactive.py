#Feras Aldahlawi
#Nov. 26
#Monte calro simulation
from __future__ import division
from time import time
import random
import sys

#get user input on number of iterations from command line
numOfIterations = int(sys.argv[1])

start = time()

#initialize bag (44 green, 20 blue, 15 yellow,  11 red, 2 white, 1 black
#a counter
#and question counter
bag = 44*'g'+ 20*'b' + 15*'y' + 11*'r' + 2*'w' + 'k'
counter = {'g':0, 'b':0,'y':0 ,'r':0,'w':0,'k':0}
question = [0,0,0,0,0]


for i in xrange(0,numOfIterations):
  for j in xrange(0,19):
    draw = random.choice(bag)
    if draw == 'g' and counter['g'] < 4:
      bag = bag[1::]
    counter[draw]+=1
  if counter['w'] >0 and counter['k'] > 0: question[0]+=1
  if counter['b'] > counter['r']: question[1]+=1
  if counter['b'] > counter['y']: question[2]+=1
  if counter['y'] > counter['r']: question[3]+=1
  if counter['g'] < (counter['b']+counter['y']+counter['r']+counter['w']+counter['k']): question[4]+=1
  for k in counter: counter[k] = 0
  bag = 44*'g'+ 20*'b' + 15*'y' + 11*'r' + 2*'w' + 'k'

p = [100*question[0]/numOfIterations,
    100*question[1]/numOfIterations,
    100*question[2]/numOfIterations,
    100*question[3]/numOfIterations,
    100*question[4]/numOfIterations]

print ' Q1   Q2   Q3   Q4   Q5'
print p

end = time()

print 'it took ' +str(end-start)+ ' seconds'
