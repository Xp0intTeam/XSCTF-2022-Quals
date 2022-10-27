// 扫雷程序   源自https://github.com/Tachone/TinyGames
#include <iostream>  
#include <cstdlib>  
#include <string>  
#include <queue>  
#include <cstring>  
#include <ctime>  


using namespace std;  

//flag{h4pp4-M1n3-G4m3}

int grid[10][10];  
int randMark[100][100];  
char showUs[100][100];  
int vis[100][100];  
int dir[8][2]={{-1,0},{1,0},{0,1},{0,-1},{-1,-1},{-1,1},{1,-1},{1,1}};//方向数组   
int res,mine_sum=25;   
string ans = "*ur)O}t@r{u!c&|}d\\9m>M4NtsrjL";
struct node  
{  
    int x;  
    int y;  
};  
void bfs(int nx,int ny) //处理点击空白   
{  
    queue <node> q;  
    node temp;  
    node t;  
    t.x=nx,t.y=ny;  
    q.push(t);  
    vis[nx][ny]=1;  
    while(!q.empty())  
    {  
        res++;  
        temp=q.front();  
        showUs[temp.x][temp.y]=grid[temp.x][temp.y]+'0';  
        q.pop();  
        for(int i=0;i<8;i++)  
        {  
            int xx=temp.x+dir[i][0];  
            int yy=temp.y+dir[i][1];  
            if(xx>=0&&xx<10&&yy>=0&&yy<10)  
            {  
                if(!vis[xx][yy]&&grid[xx][yy]==0)  
                {  
                   t.x=xx,t.y=yy;  
                   vis[xx][yy]=1;  
                   showUs[xx][yy]=grid[xx][yy]+'0';  
                   q.push(t);         
                }  
                if(!vis[xx][yy]&&grid[xx][yy]>0&&grid[temp.x][temp.y]==0)  
                {  
                   t.x=xx,t.y=yy;  
                   vis[xx][yy]=1;  
                   showUs[xx][yy]=grid[xx][yy]+'0';  
                   q.push(t);         
                }  
            }  
        }  
    }  
}  
int main()  
{  
    memset(grid,0,sizeof(grid));  
    memset(randMark,0,sizeof(randMark));  
    memset(vis,0,sizeof(vis));  
    for(int i=0;i<10;i++)  
    for(int j=0;j<10;j++)  
    showUs[i][j]='*';  
    srand(unsigned(time(NULL)));  
    int sum=0;  
    while(1)  
    {  
        int x=rand()%10;  
        int y=rand()%10;  
        if(randMark[x][y]!=1)  
        {  
            randMark[x][y]=1;//有雷  
            sum++;    
        }  
        if(sum==mine_sum)  
        break;  
           
    }  
    res=0;  
    for(int i=0;i<10;i++)  
    for(int j=0;j<10;j++)  
    {  
        if(randMark[i][j])  
        grid[i][j]=-1;  
    }   
    for(int i=0;i<10;i++)  
    for(int j=0;j<10;j++)  
    {  
        if(grid[i][j]!=-1)  
        {  
            for(int k=0;k<8;k++)  
            {  
                int x=i+dir[k][0];  
                int y=j+dir[k][1];  
                if(x>=0&&x<10&&y>=0&&y<10&&grid[x][y]==-1)  
                {  
                   grid[i][j]++;      
                }  
            }  
        }  
    }  
    for(int i=0;i<10;i++)  
    {  
        for(int j=0;j<10;j++)  
        cout<<showUs[i][j]<<" ";  
        cout<<endl;  
    }  
      
    cout<<"请输入要翻开的位置的坐标："<<endl;  
    int x,y;  
    while(1)  
    {  
        if(res==100-mine_sum){
        	int ans_len = ans.length();
        	for (int xxx=0;xxx<ans_len;xxx++)
        		cout<<char(ans[xxx]^(ans_len-xxx));
        	cout<<endl;
        	break;
		}
        cin>>x>>y;  
        if(grid[x][y]==-1)  
        {  
            cout<<"您中雷啦！"<<endl;  
            break;  
        }  
        else if(!vis[x][y]&&grid[x][y]>0)  
        {  
            res++;  
            vis[x][y]=1;  
            showUs[x][y]=grid[x][y]+'0';  
            system("cls");  
            for(int i=0;i<10;i++)  
            {  
                for(int j=0;j<10;j++)  
                cout<<showUs[i][j]<<" ";  
                cout<<endl;  
            }  
            cout<<"请输入要翻开的位置的坐标："<<endl;  
        }  
        else if(!vis[x][y]&&grid[x][y]==0)  
        {  
            bfs(x,y);  
            system("cls");  
            for(int i=0;i<10;i++)  
            {  
                for(int j=0;j<10;j++)  
                cout<<showUs[i][j]<<" ";  
                cout<<endl;  
            }  
            cout<<"请输入要翻开的位置的坐标："<<endl;  
        }  
    }  
    system("pause");
    return 0;  
}
