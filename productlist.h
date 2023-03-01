#include <iostream>
#include <string>
using namespace std;

struct Product
{
    int PID;
    string PNAME;
    int PRICE;
    string CATEGORY;

    void display(){
        cout << PID <<": Name: " << PNAME << " Price: " << PRICE << " Category: " << CATEGORY << endl;
    }
};
int id = 1;
struct Node
{
    Product info;
    struct Node *next;
};
Node *head;
int cnt;
Node* createNode(Product p)
{
    Node *temp = new Node();
    temp->info = p;
    temp->next = NULL;
    return temp;
}
void push_back(Product p){
    Node *temp = createNode(p);
     if(head == NULL)
        head = temp;
    else
    {
        Node *a;
        for(a=head ; a->next!=NULL;a=a->next);       
        a->next = temp;              
    }   
    cnt++;  
}
Product pop_back(){
    if(head == NULL)
        cout<<"\n no ele in list \n";
    else
    {
        Node *cp = head,*pp=head;
        for(;cp->next!=NULL;pp=cp,cp=cp->next);
        if(pp==cp)
            head = NULL;
        else
            pp->next=NULL;
        
        Product p = cp->info;
        cp = NULL;
        delete cp;
        cnt--;
        return p;
    }
}
void display_all(){
    Node *p = head;
    for(int i = 0; i < cnt; i++){
        p->info.display();
        p=p->next;
    }
}
Product createProduct(string name, string category, int price){
    Product *temp = new Product();
    temp->PID = id;
    temp->PNAME = name;
    temp->PRICE = price;
    temp->CATEGORY = category;
    return *temp;
}
void price_sum(){
    Node *temp = head;
    int total = 0;
    for (int i = 0; i < cnt; i++){
        total += temp->info.PRICE;
        cout << total << endl;;
        temp = temp->next;
    }
    cout << "\nTotal Price: " << total;
}
