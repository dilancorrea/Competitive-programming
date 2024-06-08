#Uva online judge 222
from sys import stdin

def solve(capacity, act_gas, miles, cost, gas_station, i):
    global min_cost
    if i == len(gas_station)-1 and cost < min_cost:
        min_cost = cost
    elif cost < min_cost:
        gas_next = (gas_station[i+1][0] - gas_station[i][0]) / miles
        if gas_next > act_gas:
            solve(capacity, capacity-gas_next, miles, cost + 200 + ((capacity-act_gas)*gas_station[i][1]), gas_station, i+1)
        elif act_gas <= capacity/2:
            solve(capacity, capacity-gas_next, miles, cost + 200 + ((capacity-act_gas)*gas_station[i][1]), gas_station, i+1)
            solve(capacity, act_gas-gas_next, miles, cost, gas_station, i+1)
        else:
            solve(capacity, act_gas-gas_next, miles, cost, gas_station, i+1)

def main():
    global min_cost
    N = float(stdin.readline())
    cnt = 1
    while N != -1:
        min_cost = 999999
        capacity, miles, fill_oc, cnt_gs = map(float, stdin.readline().split())
        gas_stations = []
        for _ in range(int(cnt_gs)):
            x, y = map(float, stdin.readline().split())
            gas_stations.append((x, y))
        gas_stations.append([N])
        solve(capacity, capacity-(gas_stations[0][0]/miles), miles, fill_oc*100, gas_stations, 0)
        print(f'Data Set #{cnt}')
        print(f'minimum cost = ${round((min_cost/100),2):.2f}')
        N = float(stdin.readline())
        cnt += 1
if __name__ == '__main__': main()