#include <stdio.h>
#include <math.h>
int coordinate[200][200] = {0};
int abso(float num){
    if (num<0){
        return -1*num;
    }
    return num;
}
void line(int x1,int y1,int x2,int y2){
    int temp;
    float slope,ac;

    if (x1 == x2){
        if (y2<y1){
            temp = y1;
            y1 = y2;
            y2 = temp;
        }
        for (int i=y1;i<=y2;i++){
            coordinate[x1][i] = 1;
        }
    }
    else if (y1 == y2){
        if (x2<x1){
            temp = x1;
            x1 = x2;
            x2 = temp;
        }
        for (int i=x1;i<=x2;i++){
            coordinate[i][y1] = 1;
        }
    }
    else{
        slope = (float)(y2-y1)/(float)(x2-x1);
        //tan < 45deg
        if (abso(slope)<=1){
            if (x2<x1){
                temp = x1;
                x1 = x2;
                x2 = temp;
                temp = y1;
                y1 = y2;
                y2 = temp;
            }
            ac = y1;
            for (int i=x1;i<=x2;i++){
                coordinate[i][(int)(ac+0.5)] = 1;
                ac += slope;
            }
        }
        //tan > 45deg 視y為自變數，x為應變數 y = m(x-x1)+y1 變成 x = 1/m(y-y1)+x1
        if (abso(slope)>1){
            if (y2<y1){
                temp = x1;
                x1 = x2;
                x2 = temp;
                temp = y1;
                y1 = y2;
                y2 = temp;
            }
            ac = x1;
            slope = 1/slope;
            for (int i=y1;i<=y2;i++){
                coordinate[(int)(ac+0.5)][i] = 1;
                ac += slope;
            }
        }
    }
    coordinate[x1][y1] = 2;
    coordinate[x2][y2] = 2;
    for (int i=0;i<200;i++){
        for (int j=0;j<200;j++){
            if (coordinate[i][j]==1){
                printf("*");
            }
            else if (coordinate[i][j]==2){
                printf("o");
            }
            else{
                printf(" ");
            }
        }
        printf("\n");
    }
}

int inside_circle(int x0,int y0,int r,int px,int py){
    float num = pow(px-x0,2)+pow(py-y0,2)-pow(r,2);
    if (num<=0){
        return 1;
    }else{
        return 0;
    }
}
void circle(int x0,int y0,int r){
    //分8瓣圓
    float xc,yc,rr;
    rr = (float)r/pow(2,0.5);
    //右上偏左
    yc = y0+r;
    for (int i=x0;i<x0+rr;i++){
        if (yc>=0 && yc<300)coordinate[i][(int)yc] = 1;
        if (!inside_circle(x0,y0,r,i+1,yc-0.5)){
            yc--;
        }
    }
    //右上偏右
    xc = x0+r;
    for (int i=y0;i<y0+rr;i++){
        if (xc>=0 && xc<300)coordinate[(int)xc][i] = 1;
        if (!inside_circle(x0,y0,r,xc-0.5,i+1)){
            xc--;
        }
    }
    //左上偏右
    yc = y0+r;
    for (int i=x0;i>x0-rr;i--){
        if (yc>=0 && yc<300)coordinate[i][(int)yc] = 1;
        if (!inside_circle(x0,y0,r,i-1,yc-0.5)){
            yc--;
        }
    }
    //左上偏左
    xc = x0-r;
    for (int i=y0;i<y0+rr;i++){
        if (xc>=0 && xc<300)coordinate[(int)xc][i] = 1;
        if (!inside_circle(x0,y0,r,xc+0.5,i+1)){
            xc++;
        }
    }

    //左下偏右
    yc = y0-r;
    for (int i=x0;i>x0-rr;i--){
        if (yc>=0 && yc<300)coordinate[i][(int)yc] = 1;
        if (!inside_circle(x0,y0,r,i-1,yc+0.5)){
            yc++;
        }
    }
    //左下偏左
    xc = x0-r;
    for (int i=y0;i>y0-rr;i--){
        if (xc>=0 && xc<300)coordinate[(int)xc][i] = 1;
        if (!inside_circle(x0,y0,r,xc+0.5,i-1)){
            xc++;
        }
    }
    //右下偏左
    yc = y0-r;
    for (int i=x0;i<x0+rr;i++){
        if (yc>=0 && yc<300)coordinate[i][(int)yc] = 1;
        if (!inside_circle(x0,y0,r,i+1,yc+0.5)){
            yc++;
        }
    }
    //右下偏右
    xc = x0+r;
    for (int i=y0;i>y0-rr;i--){
        if (xc>=0 && xc<300)coordinate[(int)xc][i] = 1;
        if (!inside_circle(x0,y0,r,xc-0.5,i-1)){
            xc--;
        }
    }
    coordinate[x0][y0]=2;

    for (int i=0;i<200;i++){
        for (int j=0;j<200;j++){
            if (coordinate[i][j]==1){
                printf("*");
            }
            else if (coordinate[i][j]==2){
                printf("o");
            }
            else{
                printf(" ");
            }
        }
        printf("\n");
    }
}

int main(void){
    char tp;
    printf("請輸入您想要繪製的圖形(直線L;圓形C):");
    scanf("%c",&tp);
    if (tp=='L'){
        int x1,y1,x2,y2;
        printf("請輸入第一點：");
        scanf("%d %d",&x1,&y1);
        printf("請輸入第二點：");
        scanf("%d %d",&x2,&y2);
        line(x1,y1,x2,y2);
    }
    else if (tp=='C'){
        int x0,y0,r;
        printf("請輸入圓心：");
        scanf("%d %d",&x0,&y0);
        printf("請輸入半徑：");
        scanf("%d",&r);
        circle(x0,y0,r);
    }
    return 0;
}

