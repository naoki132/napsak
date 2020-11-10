import random as r

with open('p01_c.txt', mode='r') as f:
    c = f.read()

with open('p01_w.txt', mode='r') as f:
    w = [s.strip() for s in f.readlines()]

with open('p01_p.txt', mode='r') as f:
    p = [s.strip() for s in f.readlines()]

print("<各荷物の重さと評価値>")
print(w)
print(p)

c_limit = int(c)
item = len(w)

x = 9

e = [[0] * item for _ in range(x)]

for i in range(x):
    for j in range(item):
        e[i][j] = r.randint(0,1)

w_sum = [0] * x
p_sum = [0] * x

for i in range(x):
    w_sum[i] = 0
    p_sum[i] = 0

    for j in range(item):
        if(e[i][j] == 1):
            w_sum[i] += int(w[j])
            p_sum[i] += int(p[j])
        
        if(w_sum[i] > c_limit):
            p_sum[i] = 0


print("\n<1回目の重さの合計と評価値>")
print(w_sum)
print(p_sum)

top2 = [0] * 2
n_top2 = [0] * 2

if(p_sum[0] > p_sum[1]):
    top2[0] = p_sum[0]
    top2[1] = p_sum[1]
    n_top2[0] = 0
    n_top2[1] = 1
else:
    top2[0] = p_sum[1]
    top2[1] = p_sum[0]
    n_top2[0] = 1
    n_top2[1] = 0

for i in range(2,x):
    if(p_sum[i] > top2[0]):
        top2[1] = top2[0]
        top2[0] = p_sum[i]
        n_top2[0] = i
        n_top2[1] = 0
    elif(p_sum[i] > top2[1]):
        top2[1] = p_sum[i]
        n_top2[1] = i

print("\n<上位2つを表示>")
print(top2)

elite = [[0] * item for i in range(2)]

for i in range(2):
    for j in range(item):
        elite[i][j] = e[n_top2[i]][j]

print(elite)

nexte = [[0] * item for i in range(x)]

total = 0
for i in range(x):
    total += p_sum[i]

for i in range(x):
    arrow = r.randint(0,total)
    sum = 0
    for j in range(x):
        sum += p_sum[j]
        if(sum >= arrow):
            for k in range(item):
                nexte[i][k] = e[j][k]
            break
print("\n<成績が良い個体を9個作る>")
print(nexte)

for i in range(0,x,2):
    if((x%2 == 1 and i < x-1) or (x%2 == 0 and i < x)):
        break
    crossrate = r.randint(0,99)
    if(crossrate < 95):
        r1 = r.randint(0,item-1)
        r2 = r1 + r.randint(0,item-r1-1)
        child = [[0] * item for i in range(2)]

        for j in range(item):
            if(r1 <= j and j <= r2):
                child[0][j] = nexte[i+1][j]
                child[1][j] = nexte[i][j]
            else:
                child[0][j] = nexte[i][j]
                child[1][j] = nexte[i+1][j]
        
        for j in range(item):
            nexte[i][j] = child[0][j]
            nexte[i+1][j] = child[1][j]
    else:
        print("\n入れ替えなし")

#突然変異
for i in range(x):
    mutantrate = r.randint(0,99)
    if(mutantrate < 3):
        m = r.randint(0,item-1)
        nexte[i][m] = (nexte[i][m] + 1) % 2

for i in range(x):
    for j in range(item):
        if(i == 0 or i == 1):
            e[i][j] = elite[i][j]
        else:
            e[i][j] = nexte[i][j]

print("\n＜結果＞")
print(e)