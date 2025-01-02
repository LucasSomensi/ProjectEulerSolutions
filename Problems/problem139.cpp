#include <iostream>
using namespace std;

int gcd(int a, int b){
    int temp;
    while (b!=0){
        temp=a%b;
        a=b;
        b=temp;        
    }
    return a;
}

int a(int m,int n,int d=1){return (m*m-n*n)*d;}
int b(int m,int n,int d=1){return 2*m*n*d;}
int c(int m,int n,int d=1){return (m*m+n*n)*d;}
int p(int m,int n,int d=1){return 2*m*(m+n)*d;}
int abs(int n){return ((n>=0)?n:-n);}

int main(){
    int limit;
    int count=0;
    cout << "limit: ";
    cin >> limit;
    for (int m=2; p(m,1)<limit; m++){
        cout << m << endl;
        for (int n=(m%2==0)?1:2; p(m,n)<limit; n+=2){
            if (gcd(m,n)==1){
                if (c(m,n)%abs(a(m,n)-b(m,n))==0) count+=limit/p(m,n);
            }
        }
    }
    cout << count << endl;
}
