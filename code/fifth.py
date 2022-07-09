import time,sys,gc
sys.setrecursionlimit(100000)
#處理輸入(讀檔)

st = time.time()
fs = open(".\\testcase\\color900.txt",'r')
rd = fs.readline
country_map = []
trans = {}
strr,counter = rd(),1
while strr != "":
    if strr != '\n':
        data = list(map(int,strr.split()))
        for i in range(len(data)):
            if data[i] and data[i] in trans:data[i] = trans[data[i]]
            elif data[i]:
                trans[data[i]] = counter
                data[i] = counter
                counter += 1
        country_map.append(data)
    strr = rd()
fs.close()
del trans
gc.collect()
ed = time.time()
first_part = ed-st

#---------------------------------------------------------------------------#
#建構國家的關係圖(以adjacency list形式)

st = time.time()
adjli = [[] for i in range(counter)]#adjacency list
#print(country_map,mm)

ri = len(country_map)#原地圖總列數
rj = len(country_map[0])#原地圖總行數
check = [[bool(i) for i in j]for j in country_map]#dfs 建圖時的確認變數
#國家關係圖建構函式(採dfs進行)
def build_graph(x,y):
    check[x][y] = False
    if x>0:
        if country_map[x][y] != country_map[x-1][y] and country_map[x-1][y] not in adjli[country_map[x][y]]:adjli[country_map[x][y]].append(country_map[x-1][y])
        if check[x-1][y]:build_graph(x-1,y)
    if y>0:
        if country_map[x][y] != country_map[x][y-1] and country_map[x][y-1] not in adjli[country_map[x][y]]:adjli[country_map[x][y]].append(country_map[x][y-1])
        if check[x][y-1]:build_graph(x,y-1)
    if x<ri-1:
        if country_map[x][y] != country_map[x+1][y]  and country_map[x+1][y] not in adjli[country_map[x][y]]:adjli[country_map[x][y]].append(country_map[x+1][y])
        if check[x+1][y]:build_graph(x+1,y)
    if y<rj-1:
        if country_map[x][y] != country_map[x][y+1] and country_map[x][y+1] not in adjli[country_map[x][y]]:adjli[country_map[x][y]].append(country_map[x][y+1])
        if check[x][y+1]:build_graph(x,y+1)

#建構(為確保為連通的國家也能被建構，採迴圈進行)
for i in range(ri):
    for j in range(rj):
        if check[i][j]:build_graph(i,j)
del check
gc.collect()
ed = time.time()
second_part = ed-st

#---------------------------------------------------------------------------#
#實際上色

st = time.time()
color = [-1 for i in range(counter)]#上色結果

#判斷上色是否合理的函式
def valid(p,col):
    for i in adjli[p]:
        if color[i] == col:
            return False
    return True
fg = 0#是否找到解

#上色函式(採dfs進行)
def dfs_draw_color(p,col):
    #print(p,end="->")
    global fg
    #print("point",p,"max",counter)
    if p>=counter:
        fg = 1
        return
    if not len(adjli[p]):
        dfs_draw_color(p+1,col)
        return
    for i in range(col):
        color[p] = i
        if valid(p,i):dfs_draw_color(p+1,col)
        if fg:return
        color[p] = -1

#上色
col = 1
while not fg:
    print("progress",col)
    color = [-1 for i in range(counter)]
    color[1] = 0
    ffff = time.time()
    dfs_draw_color(2,col)
    ssss = time.time()
    print(ssss-ffff)
    col+=1
#print("\n",col)
#print(color)
ed = time.time()
third_part = ed-st

#---------------------------------------------------------------------------#
#匯出答案

st = time.time()
fs = open(".\\op\\op.txt",'w',encoding="utf-8")
for i in range(ri):
    for j in range(rj):
        fs.write(chr(color[country_map[i][j]]+97))
        fs.write(" ")
    fs.write("\n")
ed = time.time()
fourth_part = ed-st
fs.write("使用顏色數： "+str(col-1)+" 讀入測資耗時： "+str(first_part)+" 生成關係圖耗時： "+str(second_part)+" 上色耗時： "+str(third_part)+" 匯出耗時： "+str(fourth_part))
fs.close()
print("Open \"op_fifth_ver.txt\" to check the answer.")