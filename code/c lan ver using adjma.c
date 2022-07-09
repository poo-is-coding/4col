#include <stdio.h>
#define bb 30
#define cc_up 900
int country_map[bb][bb];
int check[bb][bb]={0};
int adjma[cc_up][cc_up]={0};
int color[cc_up];
int flag = 0;
int cc_max = 0;
int minn(int a,int b){
    if (a<=b){
        return a;
    }
    return b;
}
void build_graph(int x,int y){
    check[x][y] = 0;
    if (x>0){
        if (country_map[x][y] != country_map[x-1][y])
            adjma[country_map[x][y]][country_map[x-1][y]] = 1;
        if (check[x-1][y])
            build_graph(x-1,y);
    }
    if (y>0){
        if (country_map[x][y] != country_map[x][y-1])
            adjma[country_map[x][y]][country_map[x][y-1]] = 1;
        if (check[x][y-1])
            build_graph(x,y-1);
    }
    if (x<bb-1){
        if (country_map[x][y] != country_map[x+1][y])
            adjma[country_map[x][y]][country_map[x+1][y]] = 1;
        if (check[x+1][y])
            build_graph(x+1,y);
    }
        if (y<bb-1){
        if (country_map[x][y] != country_map[x][y+1])
            adjma[country_map[x][y]][country_map[x][y+1]] = 1;
        if (check[x][y+1])
            build_graph(x,y+1);
    }
}
void reset(void){
    for (int i=0;i<cc_max+1;i++){
        color[i] = -1;
        flag = 0;
    }
}
int valid(int p,int col){
    for (int i=1;i<cc_max+1;i++){
        if (i == p)
            continue;
        if (adjma[p][i] && color[i] == color[p])
            return 0;
    }
    return 1;
}
void dfs_draw(p,col){
    if (p>cc_max){
        flag = 1;
        return;
    }
    int rrr = 0;
    for (int i=1;i<cc_max+1;i++){
        if (adjma[p][i]){
            rrr = 1;
            break;
        }
    }
    if (!rrr){
        dfs_draw(p+1,col);
        return;
    }
    for (int i=0;i<minn(p,col);i++){
        color[p] = i;
        if (valid(p,i))
            dfs_draw(p+1,col);
        if (flag)
            return;
        color[p] = -1;
    }
}
int main(void){
    int i,j;
    int col = 1;
    freopen(".\\K99.txt","r",stdin);

    for (i=0;i<bb;i++){
        for (j=0;j<bb;j++){
            scanf("%2d",&country_map[i][j]);
            if (country_map[i][j])
                check[i][j] = 1;
            if (country_map[i][j]>cc_max)
                cc_max = country_map[i][j];
        }
    }
    for (i=0;i<bb;i++){
        for(j=0;j<bb;j++){
            if (check[i][j])
                build_graph(i,j);
        }
    }
    while (!flag){
        printf("progress %d",col);
        reset();
        color[1] = 0;
        dfs_draw(2,col);
        col++;
    }
    freopen(".\\K99out.txt","w",stdout);
    for (i=0;i<bb;i++){
        for (j=0;j<bb;j++){
            printf("%c ",color[country_map[i][j]]+34);
        }
        printf("\n");
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
