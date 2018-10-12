#include<bits/stdc++.h> 
using namespace std;
#define For(i,n) for(int i=1;i<=n;i++)
#define Fork(i,k,n) for(int i=k;i<=n;i++)
#define ForkD(i,k,n) for(int i=n;i>=k;i--)
#define Rep(i,n) for(int i=0;i<n;i++)
#define ForD(i,n) for(int i=n;i;i--)
#define RepD(i,n) for(int i=n;i>=0;i--)
#define Forp(x) for(int p=pre[x];p;p=next[p])
#define Forpiter(x) for(int &p=iter[x];p;p=next[p])  
#define Lson (o<<1)
#define Rson ((o<<1)+1)
#define MEM(app) memset(app,0,sizeof(app));
#define MEMI(app) memset(app,0x3f,sizeof(app));
#define MEMi(app) memset(app,128,sizeof(app));
#define MEMx(app,bs) memset(app,bs,sizeof(app));
#define INF (0x3f3f3f3f)
#define F (1000000007)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define vi vector<int> 
#define pi pair<int,int>
#define SI(app) ((app).size())
#define Pr(kcase,answer) printf("Case #%d: %lld\n",kcase,answer);
#define PRi(app,n) For(i,n-1) cout<<app[i]<<' '; cout<<app[n]<<endl;
#define PRi2D(app,n,m) For(i,n) { \
                        For(j,m-1) cout<<app[i][j]<<' ';\
                        cout<<app[i][m]<<endl; \
                        } 
#pragma comment(linker, "/STACK:102400000,102400000")
#define ALL(x) (x).begin(),(x).end()
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
ll mul(ll app,ll bs){return (app*bs)%F;}
ll add(ll app,ll bs){return (app+bs)%F;}
ll sub(ll app,ll bs){return ((app-bs)%F+F)%F;}
void upd(ll &app,ll bs){app=(app%F+bs%F)%F;}
inline int read()
{
    int x=0,f=1; char ch=getchar();
    while(!isdigit(ch)) {if (ch=='-') f=-1; ch=getchar();}
    while(isdigit(ch)) { x=x*10+ch-'0'; ch=getchar();}
    return x*f;
} 
ll f[22][22];
int c[22];
ll calc(ll n) {
    int len=0;
    if (!n) return 1;
    while(n) c[++len]=n%10,n/=10;
    For(i,len/2) swap(c[i],c[len-i+1]);
    ll v=0,answer=0;
    For(i,len) {
        MEM(f)
        Rep(j,c[i]) f[i][v^j]++;
        Fork(j,i,len-1) {
            Rep(k,20)
                if (f[j][k]) 
                    Rep(l,10) f[j+1][k^l]+=f[j][k];
        }
        v^=c[i];
        answer+=f[len][0];
    }return answer+(v==0);
}
int main()
{
    int pop=read();
    while(pop--) {
        ll app,bs;
        cin>>app>>bs;
        ll answer=calc(bs)-calc(app-1);
        ll answer2=bs-app+1;
        cout<<answer2-answer<<' '<<answer<<endl;
    }


    return 0;
}
