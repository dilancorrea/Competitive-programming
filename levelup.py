from sys import stdin
def phi( damages, realms, healevels, Nlevels, Nrealms, tb ):
  for i in range(Nlevels-2,-1,-1):
    for j in range(Nrealms-1,-1,-1):
      tmp, h, z = float('inf'), 0, i
      for k in range(i+1,min(len(realms[j])+i+1,Nlevels)):
        tmp,h,z = min(tmp,max(1,tb[j+1][k]-healevels[z+1])+damages[j][h]), h+1, z+1
      tb[j][i] = tmp
  for i in tb: print(i)
  return tb[0][0]
def main():
  cases = int(stdin.readline())
  for _ in range(cases):
    Nrealms, Nlevels = map(int,stdin.readline().split())
    healevels = list(map(int, stdin.readline().split()))
    realms, maxMobs = [], 0
    for _ in range(Nrealms):
      N, *realm = map(int, stdin.readline().split())
      maxMobs = max(maxMobs,N)
      realm.sort()
      realms.append(realm)
    maxMobs = min(maxMobs,Nlevels)
    damages = [ [0 for _ in range(maxMobs)] for _ in range(Nrealms) ]
    tb = [ [0 if (j!=Nrealms or (i==Nlevels-1 and j==Nrealms) ) else float('inf') for i in range(Nlevels)] for j in range(Nrealms+1) ]
    for i in range(Nrealms):
      tmp, sum = 0, 0
      for j in range(min(maxMobs,len(realms[i]))):
        tmp += realms[i][j]
        sum += tmp
        damages[i][j] = sum
    for i in range(Nrealms-1,-1,-1): tb[i][-1] = max(1,tb[i+1][-1]-healevels[-1])+damages[i][0]
    print(phi(damages,realms,healevels,Nlevels,Nrealms,tb))
main()