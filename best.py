#Uva online judge 11658

from sys import stdin
def phi(n,x,X,A, mem):
  ans = float("inf")
  if n == len(A):
    if x > 5000:
      return x
    return float("inf")
  if (n,x) in mem: return mem[ (n,x) ]
  if n != X-1:
    ans = min( phi( n+1, x, X, A, mem ), phi(n+1, x+A[n], X, A, mem) )
  else:    
    ans = phi( n+1,x,X,A,mem )
  mem[ (n,x) ] = ans
  return ans
def main():
  N, X = map( int, stdin.readline().split() )
  cnt = 1
  while N != 0 and X != 0:
    A = []
    for i in range(N):
      tmp = stdin.readline().strip()
      tmp = tmp.replace(".","")
      A.append(int(tmp))
    if A[X-1] > 5000: print("{:.2f}".format(100))
    else:
      tmp = phi( 0, A[X-1], X, A, {} )
      tmp = (1.0 * A[X-1] * 100 ) / tmp
      print("{:.2f}".format(tmp))
    N, X = map( int, stdin.readline().split() ) 
    cnt += 1
main()