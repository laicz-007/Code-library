#include <iostream>
using namespace std;

int main(){
	int a,b,c,d,i;
	long long int key,before_num,after_num;
	cout<<"�������Ѽ������ֺ���Կ��4λ��:"; 
	cin>>before_num>>key;
	a = key / 1 % 10;
	b = key / 10 % 10;
	c = key / 100 % 10;
	d = key / 1000 % 10;
	after_num = before_num;
	for(i = 0;i <= a * b * c * d * a * b * c * d;i++){
		after_num -= b;
		after_num += c;
	}
	cout<<after_num<<endl; 
}
//������С����ԡ�������ע��һ�㣬��������Կʱ��ý���Կ��ʮλ���ڰ�λ��
/*Because the program has "features", please note that when entering the key, it is best to make the ten digits of the key greater
 than the hundred digits.
*/
