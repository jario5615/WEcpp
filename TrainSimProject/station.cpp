#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Station{
    
    string id;
    string name;
    int size;
    int wait = 2;
    vector<int> platforms;

    public:
    Station(string id, string name, int size){
        this->id = id;
        this->name = name;
        this->size = size;
        for(int i = 0; i < size; i++){platforms.push_back(0);}
    }

    string getName(){return name;}

    bool platformIsEmpty(int platform){
        return platforms[platform-1] == 0 ? true : false;
    }

    bool arriveAtPlatform(int id, int platform){
        if(platform <= size && platform >= 1){
            this->platforms[platform-1] = id;
            return true;
        } else {
            cout << "Invalid platform Number" << endl;
            return false;
        }
    }

    bool leaveStation(int platform){
        if(platform <= size && platform > 0){
            platforms[platform-1] = 0;
            return true;
        } else {
            cout << "Invalid platform Number" << endl;
            return false;
        }
    }

    void printPlatforms(){
        for(int i = 0; i < size; i++){
            cout << "Platform " << i+1 << " has train " << platforms[i] << endl;
        }
    }

    int getWait(){
        return wait;
    }

};