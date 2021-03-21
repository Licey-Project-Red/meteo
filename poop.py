import json
def pechatay(x):

    with open('20_years_format\\'+x+'.json', 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    a = []
    s = 0.0
    for j in range (3):
        for i in range(j, j+4):
            a.append(data[i])
            s += data[i]
            print(i)
        s = s/5
        with open(x+'.txt', 'a', encoding='utf-8') as f:
            f.write(str(s)+'\n')
    for j in range (3, len(data)-2):
        for i in range(j-2, j+2):
            a.append(data[i])
            s += data[i]
            print(i)
        s = s/5
        with open(x+'.txt', 'a', encoding='utf-8') as f:
            f.write(str(s)+'\n')

    for j in range(len(data)-4, len(data)):
        for i in range(j-4, j):
            a.append(data[i])
            s += data[i]
            print(i)
        s = s/5
        with open(x+'.txt', 'a', encoding='utf-8') as f:
            f.write(str(s)+'\n')
pechatay("Южный")   