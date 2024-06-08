#Uva online judge 11402

from sys import stdin

def build( arr, n ):
    tree = [ 0 ] * ( 2*n )
    for i in range( n ):
        tree[ n+i ] = int( arr[ i ] )
    for i in range( n-1, 0, -1 ):
        tree[ i ] = tree[ i<<1 ] + tree[ i<<1|1 ]
    return tree

def query( l, r, n, tree ):
    res = 0
    l += n
    r += n
    while l < r:
        if( l & 1 ):
            res += tree[ l ]
            l += 1
        if( r & 1 ):
            r -= 1
            res += tree[ r ]
        l >>= 1
        r >>= 1
    return res

def updateTreeNode( p, q, value, n, tree, land ):
    if value != -1:
        for i in range( p + n, q + n + 1 ):
            tree[ i ] = value
    else:
        for i in range( p + n, q + n + 1 ):
            tree[ i ] = int( not( int( tree[ i ] ) ) )
    for i in range( n-1, 0, -1 ):
        tree[i] = tree[i << 1] + tree[i << 1 | 1]
    return land, tree

def main():
    T = int( stdin.readline() )
    for i in range( 1,T+1 ):
        print(f'Case {i}:')
        M = int( stdin.readline() )
        land, j = '', 1
        for _ in range( M ):
            rep = int( stdin.readline() )
            tmp = str( stdin.readline().strip() )
            land += tmp * rep
        Q = int( stdin.readline() )
        tree = build( land, len(land) )
        for _ in range( Q ):
            op = list( stdin.readline().split() )
            if op[ 0 ] == 'F':
                land, tree = updateTreeNode( int( op[ 1 ] ), int( op[ 2 ] ), 1, len(land), tree, land )
            elif op[ 0 ] == 'E':
                land, tree = updateTreeNode( int( op[ 1 ] ), int( op[ 2 ] ), 0, len(land), tree, land )
            elif op[ 0 ] == 'I':
                land, tree = updateTreeNode( int( op[ 1 ] ), int( op[ 2 ] ), -1, len(land), tree, land )
            else:
                print(f'Q{j}: {query( int( op[ 1 ] ), int( op[ 2 ] )+1, len(land), tree )}')
                j += 1
main()