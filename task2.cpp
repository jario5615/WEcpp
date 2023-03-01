#include <iostream>
#include <string>
#include "productlist.h"
using namespace std;

int main(){
    head = NULL;
    int ch, price, i;
    string name, category;
    Product temp;
	cnt =0;
    do
    {
        cout<<"\n1 Insert Product";
		cout<<"\n2 Pop Product";
		cout<<"\n3 Display Products";
        cout<<"\n4 Total Price of all products";
        cout<<"\n5 Exit" << endl;
        cin>>ch;
        switch(ch){
            case 1:
                cout << "\nInput product name: ";
                cin >> name;
                cout << "\nInput product price: ";
                cin >> price;
                cout << "\nInput product category: ";
                cin >> category;
                temp = createProduct(name,category,price);
                push_back(temp);
                break;
            case 2:
                pop_back().display();
                break;
            case 3:
                display_all();
                break;
            case 4:
                price_sum();
                break;
            case 5:
                break;
        }

    } while (ch!=5);
    
}