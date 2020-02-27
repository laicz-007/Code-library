#include <iostream>
using namespace std;

int main(){
	int a,b,c,d,i;
	long long int key,before_num,after_num;
	cout<<"请输入已加密数字和密钥（4位）:"; 
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
//因程序有“特性”所以请注意一点，在输入密钥时最好将密钥的十位大于百位。
/*Because the program has "features", please note that when entering the key, it is best to make the ten digits of the key greater
 than the hundred digits.
*/
