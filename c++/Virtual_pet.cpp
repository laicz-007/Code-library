#include <iostream>
#include <windows.h>
using namespace std;

/*
Do n��t say I ��m bad. I ��m a fourth-grade elementary student. Some places may not do well. Besides, it ��s not that I do n��t define global variables,
 but global variables take too much memory. ��Ҫ˵�Ҳ���Ǹ����꼶Сѧ������Щ�ط��������Ĳ��ã����ⲻ���Ҳ��ᶨ��ȫ�ֱ���������ȫ�ֱ���̫���ڴ档
*/
int couting(int a,int b,int c,int d){

	cout<<"satiety:"<<a<<endl;
	cout<<"sleep:"<<b<<endl;
	cout<<"happiness:"<<c<<endl;
	cout<<"health:"<<d<<endl;	
}
int main(){
	int satiety,sleep,happiness,health,tick,state;
	bool bol;
	string order;
	satiety = 8;
	sleep = 8;
	happiness = 8;
	health = 8;
	bol = true;
	state = 0;
	while(bol){
		cin>>order;
		if(order == "exit"){
			return 0;	
		}else if(order == "play"){
			if(state == 0){
				state = 1;
				sleep -= 1;
				happiness += 4;
				satiety -= 1;
				if(happiness >= 10){
					happiness = 10;
				cout<<"play 25%"<<endl;
				Sleep(1000);
				cout<<"play 50%"<<endl;
				Sleep(1000);
				cout<<"play 75%"<<endl;
				Sleep(1000);
				cout<<"play 100%"<<endl;
				state = 0;
				}else{
					cout<<"Memory is occupied �ڴ汻ռ����"<<endl;
				}

			}
		}else if(order == "sleep"){
			if(state == 0){
				state = 1;
				sleep += 5;
				happiness += 1;
				satiety -= 1;
			}
				if(sleep >= 10){
					sleep = 10;
				cout<<"sleep 20%"<<endl;
				Sleep(1500);
				cout<<"sleep 40%"<<endl;
				Sleep(1500);
				cout<<"sleep 60%"<<endl;
				Sleep(1500);
				cout<<"sleep 80%"<<endl;
				Sleep(1500);
				cout<<"sleep 100%"<<endl;
				state = 0;
			}else{
				cout<<"Memory is occupied �ڴ汻ռ����"<<endl;
			}
			
			
		}else if(order == "eat"){
			if(state == 0){
				state = 1;
				sleep -= 1;
				happiness += 2;
				satiety += 3;
				if(happiness >= 10){
					happiness = 10;
				}
				if(satiety >= 10){
					satiety = 10;
				}
				cout<<"eat 25%"<<endl;
				Sleep(1500);
				cout<<"eat 50%"<<endl;
				Sleep(1500);
				cout<<"eat 75%"<<endl;
				if(rand() % 100 <= 5){
					cout<<"��ĳ������������ˣ�����ȥ��ҽ���ɣ� Your pet has a bad stomach! Take it to the doctor!"<<endl;
					health = 0;
				}
				Sleep(1500);
				cout<<"eat 100%"<<endl;
				state = 0;
			}else{
				cout<<"Memory is occupied �ڴ汻ռ����"<<endl; 
			}
		}else if(order == "doctor"){
			if(state == 0){
				state == 1;
				sleep -= 1;
				happiness -= 3;
				satiety -= 2;
				health = 10;
				cout<<"see a doctor 20%"<<endl;
				Sleep(1000);
				cout<<"see a doctor 40%"<<endl;
				Sleep(1000);
				cout<<"see a doctor 60%"<<endl;
				Sleep(1000);
				cout<<"see a doctor 80%"<<endl;
				if(rand() % 100 <= 10){
					cout<<"��ĳ�����ܾ������������ˣ�����Ҫ��10�����һ���ĳ��� Your pet ran away because he refused to see a doctor! You need to spend 10 seconds to retrieve your pet"<<endl;
					Sleep(1000); 
					cout<<"looking for pets 10 %"<<endl;
					Sleep(1000);
					cout<<"looking for pets 20 %"<<endl;
					Sleep(1000); 
					cout<<"looking for pets 30 %"<<endl;
					Sleep(1000); 
					cout<<"looking for pets 40 %"<<endl;
					Sleep(1000); 
					cout<<"looking for pets 50 %"<<endl;
					Sleep(1000); 
					cout<<"looking for pets 60 %"<<endl;
					Sleep(1000); 
					cout<<"looking for pets 70 %"<<endl;
					Sleep(1000); 
					cout<<"looking for pets 80 %"<<endl;
					Sleep(1000); 
					cout<<"looking for pets 90 %"<<endl;
					Sleep(1000); 
					cout<<"looking for pets 100 %"<<endl;
					state = 0;
				}
				Sleep(1000);
				cout<<"see a doctor 100%"<<endl;
				state = 0; 
			}
		}else{
			cout<<"����û�б�ָ�����Ŀ��ȫ��Դ�������޸� For the time being without this directive, this project is safe and open source and can be modified"<<endl; 
		} 
		couting(satiety,sleep,happiness,health);
        if(satiety <= 3){
            cout<<"��ʳ���½���3���£��������ιʳ Fullness drops below 3, please feed your pet"<<endl;
        }
        if(sleep <= 3){
            cout<<"˯�߶��½���3���£����ó���˯�� Sleep level drops below 3, please let your pet sleep"<<endl;
        }
        if(happiness <= 3){
            cout<<"���ֶ��½���3���£����������ˣ Happiness drops below 3, please play with pets"<<endl;
        }
        if(health <= 3){
            cout<<"�����½���3���£�������￴�� Health drops below 3, please bring your pet to the doctor"<<endl;
        }
	}
}


