#Uva online judge 11552

from sys import stdin
def phi( i, k, s, chunks, used ):
    ans = float('inf')
    if i == len(s)//k: ans = chunks
    else:
        check, flag = [ False for _ in range(26) ], False
        for j in range(i*k,(i*k)+k ):
            if dp[i-1][ord(s[j])-97] != 0 and dp[i][ord(s[j])-97] != 0 and check[ord(s[j])-97] == False and used[i-1] != s[j] or (dp[i][ord(s[j])-97] == dp[i-1][ord(s[j])-97] and dp[i][ord(s[j])-97] == k and check[ord(s[j])-97] == False):
                check[ord(s[j])-97], flag = True, True
                used[i] = s[j]
                ans = min( ans, phi( i+1, k, s, chunks-1, used ) )
                used[i] = 'ñ'
        if j == ((i*k)+k)-1 and flag == False:
            ans = min( ans, phi( i+1, k, s, chunks, used ) )
    return ans
def main():
    cases = int( stdin.readline() )
    for _ in range(cases):
        global dp
        k, s = stdin.readline().split()
        dp, used, i, chunks = [ [ 0 for _ in range(26) ] for _ in range(len(s)//int(k)) ], [ 'ñ' for _ in range(len(s)//int(k)) ], 0, 0
        for j in range(len(s)//int(k)):
            while i < (j+1)*int(k):
                dp[j][ord(s[i])-97] += 1
                if dp[j][ord(s[i])-97] == 1:
                    chunks += 1
                i += 1
        print( phi( 1, int(k), s, chunks, used ) )

main()