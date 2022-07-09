#讀檔
fs = open("color900.txt",'r')
data = fs.read()
arr = [[int(i) for i in j.split()]for j in data.split('\n')]
fs.close()

#找到程式最大國家代號
mm = 0
for i in arr:
    mm = max(mm,max(i))


#建構簡單圖  
adjli = [[] for i in range(mm+1)]
check = [[bool(i) for i in j]for j in arr]
ri,rj = len(arr),len(arr[0])
def build_graph(x,y):
    check[x][y] = False
    if x>0 and arr[x-1][y]:
        if arr[x][y] != arr[x-1][y] and arr[x-1][y] not in adjli[arr[x][y]]:
            adjli[arr[x][y]].append(arr[x-1][y])
        if check[x-1][y]:build_graph(x-1,y)
    if y>0 and arr[x][y-1]:
        if arr[x][y] != arr[x][y-1] and arr[x][y-1] not in adjli[arr[x][y]]:
            adjli[arr[x][y]].append(arr[x][y-1])
        if check[x][y-1]:build_graph(x,y-1)
    if x<ri-1 and arr[x+1][y]:
        if arr[x][y] != arr[x+1][y]  and arr[x+1][y] not in adjli[arr[x][y]]:
            adjli[arr[x][y]].append(arr[x+1][y])
        if check[x+1][y]:build_graph(x+1,y)
    if y<rj-1 and arr[x][y+1]:
        if arr[x][y] != arr[x][y+1] and arr[x][y+1] not in adjli[arr[x][y]]:
            adjli[arr[x][y]].append(arr[x][y+1])
        if check[x][y+1]:build_graph(x,y+1)
for i in range(ri):
    for j in range(rj):
        if check[i][j]:build_graph(i,j)

#著色
color = [-1 for i in range(mm+1)]
def valid(p,col):
    for i in adjli[p]:
        if color[i] == col:
            return False
    return True
fg = 0
def dfs_draw_color(p):
    global fg
    if p>mm:
        fg = 1
        return
    if not len(adjli[p]):
        dfs_draw_color(p+1)
        return
    for i in range(5):
        color[p] = i
        if valid(p,i):dfs_draw_color(p+1)
        if fg:return
        color[p] = -1
dfs_draw_color(1)

#輸出
fs = open("colorout_900.txt",'w')
for i in range(ri):
    for j in range(rj):
        fs.write(chr(color[arr[i][j]]+97))
        fs.write(" ")
    fs.write("\n")
fs.close()
print("Open \"op.txt\" to check the answer.")