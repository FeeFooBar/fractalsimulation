#!/bin/bash
let i=0
while [ $i -lt 1 ]
do
  ./fractal $1 $2 $3 > positions.pos
  cat positions.pos
  python3 regex.py mstm.inp $3
  ./mstm.out mstm.inp
  echo 'Result :'
  cat test.dat > run1/$i.txt
  let i=$i+1
done
