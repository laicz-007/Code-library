#include <iostream>
using namespace std;

int main(){
	int a,b,c,d,i;
	long long int key,num;
	cout<<"��������������ֺ���Կ��4λ��:"; 
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

