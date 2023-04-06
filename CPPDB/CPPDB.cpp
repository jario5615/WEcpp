#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int choice, price, id;
    string search, name;
    cout << "1: List all products" << endl;
    cout << "2: Search for product by name" << endl;
    cout << "3: Show products by maximum price" << endl;
    cout << "4: Add new product" << endl;
    cout << "5: Delete existing product" << endl;
    cout << "0: Exit" << endl;
    cout << "Enter number of choice: ";
    cin >> choice;
    while (choice != 0) {
        switch (choice) {
        case 1:
            // TODO - Enter function to get all entries from table
            cout << "Print all items from database" << endl;
            break;
        case 2:
            // TODO - Enter function to return entries based on search term
            cout << "Enter search term for name of product: ";
            cin >> search;
            cout << "Print results of " << search << endl;
            break;
        case 3:
            // TODO - Enter function to show products by max price based on entered number
            cout << "Enter max price of items to show: ";
            cin >> price;
            cout << "Print results of all products less than " << price << endl;
            break;
        case 4:
            // TODO - Enter function for adding new product
            cout << "Enter new product name: ";
            cin >> name;
            cout << "Enter new product price: ";
            cin >> price;
            cout << "Add new item to database";
            break;
        case 5:
            // TODO - Enter function for deleteing existing product
            cout << "Enter product id to be deleted: ";
            cin >> id;
            cout << "Deleting product " << id << endl;
            break;
        case 0:
            cout << "Exiting"<< endl;
            break;
        }
    }
}