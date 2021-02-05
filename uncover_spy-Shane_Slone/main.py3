def uncover_spy(n, trust):
    trustd = {i: [] for i in range(1, n + 1)}
    number_who_trust = {i: 0 for i in range(1, n + 1)}
    for i in range(len(trust)):
        p = trust[i][0]
        t = trust[i][1]
        trustd[p].append(t)
        number_who_trust[t] += 1
    for k in trustd:
        if trustd[k] == [] and number_who_trust[k] == n - 1:
            return k
    return -1
    

