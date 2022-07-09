import time,sys,gc
sys.setrecursionlimit(5000)
#處理輸入(讀檔)

st = time.time()
fs = open(".\\testcase\\testcase_adv.txt",'r')
rd = fs.readline
country_map = []
strr,mm = rd(),0
while strr != "":
    if strr != '\n':
        data = list(map(int,strr.split()))
        mm = max(mm,max(data))
        country_map.append(data)
    strr = rd()
fs.close()
ed = time.time()
first_part = ed-st

#---------------------------------------------------------------------------#
#建構國家的關係圖(以adjacency list形式)

st = time.time()
adjli = [[] for i in range(mm+1)]#adjacency list
#print(country_map,mm)
check = [[bool(i) for i in j]for j in country_map]#dfs 建圖時的確認變數
ri = len(country_map)#原地圖總列數
rj = len(country_map[0])#原地圖總行數

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
for i in range(len(adjli)):
    print("與"+str(i)+"國家相鄰的國家：",end=" ")
    for j in adjli[i]:
        if j:
            print(j,end=" ")
    print()
ed = time.time()
second_part = ed-st

#---------------------------------------------------------------------------#
#實際上色

st = time.time()
color = [-1 for i in range(mm+1)]#上色結果

#判斷上色是否合理的函式
def valid(p,col):
    for i in adjli[p]:
        if color[i] == col:
            return False
    return True
fg = 0#是否找到解

#上色
def dfs_draw_color(p,col):
    global fg
    if p>mm:
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
col = 1
while not fg:
    dfs_draw_color(1,col)
    col+=1

ed = time.time()
third_part = ed-st

#---------------------------------------------------------------------------#
#匯出答案

st = time.time()
fs = open("op_fourth_ver.txt.txt",'w',encoding="utf-8")
for i in range(ri):
    for j in range(rj):
        fs.write(chr(color[country_map[i][j]]+97))
        fs.write(" ")
    fs.write("\n")
ed = time.time()
fourth_part = ed-st
fs.write("使用顏色數： "+str(col-1)+" 讀入測資耗時： "+str(first_part)+" 生成關係圖耗時： "+str(second_part)+" 上色耗時： "+str(third_part)+" 匯出耗時： "+str(fourth_part))
fs.close()
print("Open \"op_fourth_ver.txt\" to check the answer.")