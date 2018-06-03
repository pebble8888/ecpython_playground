#!/usr/bin/env python 

from ecpy import * # https://github.com/elliptic-shiho/ecpy/
import math

def bsgs(E, P, Q, ordP):
  # m = sqrt(#P) (round up)
  m = int(math.sqrt(ordP) + 0.5)
  # Calculate Baby-step table
  baby = []
  for i in range(m):
    baby += [(i, i * P)]
  h = -P * m
  t = Q
  # Main loop: Giant-step
  for j in range(m):
    b = list(filter(lambda x: x[1] == t, baby))
    if len(b) == 1:
      return b[0][0] + j * m
    t = t + h

def main():
  F = FiniteField(17)
  E = EllipticCurve(F, 3, 7)
  P = E(4, 10, 1)
  Q = E(10, 0, 1)
  ordP = 14
  x = bsgs(E, P, Q, ordP)
  assert x*P == Q
  print(x) # 7

if __name__ == "__main__":
  main()
