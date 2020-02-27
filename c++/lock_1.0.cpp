#include <iostream>
using namespace std;

int main(){
	int a,b,c,d,i;
	long long int key,num;
	cout<<"请输入待加密数字和密钥（4位）:"; 
	cin>>num>>key;
	a = key / 1 % 10;
	b = key / 10 % 10;
	c = key / 100 % 10;
	d = key / 1000 % 10;
	for(i = 0;i <= a * b * c * d * a * b * c * d;i++){
		num += b;
		num -= c;
	}
	cout<<num<<endl;
}

