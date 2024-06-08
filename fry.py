#Uva online judge 12324

from sys import stdin
def phi( T, E, SE, n, e, mem ):
  if n == len(T): return 0
  if (n,e) in mem: return mem[(n,e)]
  else:
    if e == 0: result = T[n] + phi(T,E,SE,n+1, E[n],mem)
    elif e >= len(T)-n: result = (T[n]>>1) + phi(T,E,SE,n+1,e+E[n]-1, mem)
    else: result = min( T[n] + phi(T,E,SE,n+1,e+E[n],mem), (T[n]>>1) + phi(T,E,SE,n+1,e+E[n]-1, mem) )
  mem[(n,e)] = result
  return result
def main():
  trips = int( stdin.readline() )
  while trips != 0:
    t, e = [], []
    for _ in range( trips ):
      ti, bi = map( int, stdin.readline().strip().split() )
      t.append( ti )
      e.append( bi )
    mem = {}
    print( phi( t, e, sum(e), 0,0, mem ) )
    trips = int( stdin.readline() )
main()