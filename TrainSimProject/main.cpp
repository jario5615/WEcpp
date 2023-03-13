#include <iostream>
#include <vector>
#include <string>
#include <chrono>
#include <thread>
#include "train.cpp"

using namespace std;

int main(){
    Station ast = Station("ast", "Alpha", 2);
    Station bst = Station("bst", "Bravo", 2);
    Station cst = Station("cst", "Charlie", 4);
    Station dst = Station("dst", "Delta", 2);
    Station est = Station("est", "Echo", 1);
    Station fst = Station("fst", "Foxtrot", 2);
    Station gst = Station("gst", "Golf", 2);
    Station hst = Station("hst", "Hotel", 1);

    vector<Station *> st00 = {&ast, &bst, &cst, &dst, &est, &dst, &cst, &bst};
    vector<int> jt00 = {10,7,11,6,6,11,7,10};
    vector<int> pl00 = {1,1,1,1,1,2,2,2};

    vector<Station *> st01 = {&ast, &bst, &cst, &fst, &gst, &hst, &gst, &fst, &cst, &bst};
    vector<int> jt01 = {10,7,3,5,4,4,5,3,7,10};
    vector<int> pl01 = {2,1,3,1,1,1,2,2,4,2};


    Train t00 = Train(10000, st00, jt00, pl00);
    Train t01 = Train(10001, st01, jt01, pl01);
    // ast.printPlatforms();
    // t00.move();
    // ast.printPlatforms();

    int count = 0;
    
    while(count < 120){
        cout << "T+" << count << endl;
        t00.move();
        t01.move();
        count++;
        this_thread::sleep_for(chrono::seconds(1));
    }
    
    return 0;
}