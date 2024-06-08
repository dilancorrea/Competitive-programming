#Uva online judge 11987

from sys import stdin

def findParent( x ):
   global parent
   if parent[ x ] != x:
      parent[ x ] = findParent( parent[ x ] )
   return parent[ x ]

def values( case, line ):
   global parent
   if parent[ int( case[0] ) + int( line[1] )  ] != int( case[0] ) + int( line[1] ):
      parent_x = findParent( int( case[0] ) + int( line[1] ) )
   else:
      parent_x = findParent( int(line[1]) )
   if len(line) > 2:
      if parent[ int( case[0] ) + int( line[2] )  ] != int( case[0] ) + int( line[2] ):
         parent_y = findParent( int( case[0] ) + int( line[2] ) )
      else:
         parent_y = findParent( int(line[2]) )
   else:
      parent_y = None
   return parent_x, parent_y

def main():
   case = stdin.readline().split()
   while len(case) != 0:
      global parent
      parent, rank, size, sum = [], [], [], []
      for i in range( ( 2*int( case[ 0 ] ) ) + 1 ):
         if i <= int(case[ 0 ]):
            rank.append(0)
            size.append(1)
            sum.append(i)
         parent.append(i)
      for _ in range( int(case[1]) ):
         line = stdin.readline().split()
         if int( line[0] ) == 1:
            parent_x, parent_y = values( case, line )
            if parent_x != parent_y:
               if rank[ parent_x ] > rank[ parent_y ]:
                  sum[ parent_x ] += sum[ parent_y ]
                  size[ parent_x ] += size[ parent_y ]
                  parent[parent_y] = parent_x
               else:
                  if rank[ parent_x ] == rank[ parent_y ]:
                     rank[ parent_y ] += 1
                  sum[ parent_y ] += sum[ parent_x ]
                  size[ parent_y ] += size[ parent_x ]
                  parent[parent_x] = parent_y
         elif int( line[0] ) == 2:
            parent_x, parent_y = values( case, line )
            if parent_x != parent_y:
               sum[parent_x] -= int( line[1] )
               size[parent_x] -= 1
               sum[parent_y] += int( line[1] )
               size[parent_y] += 1
               if rank[parent_x] > 0:
                  parent[int(line[1])+int(case[0])] = parent_y
               else:
                  parent[int(line[1])] = parent_y 
            if rank[parent_y] == 0: rank[parent_y] += 1
         else:
            parent_x, parent_y = values( case, line )
            print( size[parent_x], sum[parent_x])
      case = stdin.readline().split()
      
if __name__ == '__main__':
   main()