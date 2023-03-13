#include "station.cpp"
#include <iostream>

using namespace std;

class Node{

    Station *station;
    int journeyTime;
    int platformNo;
    Node *nextStop;

    public:
    Node(){
        this->journeyTime = 0;
        this->platformNo = 0;
        this->station = nullptr;
        this->nextStop = nullptr;
    }

    Node(int journey, Station *stop, int platform){
        journeyTime = journey;
        station = stop;
        platformNo = platform;
    }

    Node* addAfter(int journey, Station *stop, int platform){
        Node *curr = new Node(journey, stop, platform);
        //cout << "New node created" << endl;
        nextStop = curr;
        //cout << "New node attactched" << endl;
        return curr;
    }

    void setNext(Node *next){
        nextStop = next;
    }
    Node* getNext(){
        return this->nextStop;
    }

    Station* getStation(){
        return this->station;
    }

    int getPlatformNo(){
        return this->platformNo;
    }

    int getJourneyTime(){
        return this->journeyTime;
    }

    void PrintNode(){
        cout << this->station->getName() << ": Time to next station: " << this->journeyTime << endl;
    }

};

class Route{

    Node *startStop;
    Node *currentStop;
    bool reverse = false;
    
    public:
    Route(){
        startStop = new Node();
        currentStop = startStop;
    }

    Route(vector<Station *> stations, vector<int> journeys, vector<int> platforms){
        startStop = new Node(journeys[0], stations[0], platforms[0]);
        currentStop = startStop;
       //cout << "Initial Node set" << endl;
        for(int i = 1; i < stations.size(); i++){
            currentStop = currentStop->addAfter(journeys[i], stations[i], platforms[i]);
            //cout << "Node " << i << " set";
        }
        currentStop->setNext(startStop);
        //cout << "Route circularised" << endl;
        currentStop = startStop;
        //cout << "Route set" << endl;
    }

    void PrintRoute(){
        Node *temp = startStop;
        while(temp->getNext() != startStop){
            temp->PrintNode();
            temp = temp->getNext();
        }
    }

    Node* getNext(){
        return getCurrent()->getNext();
    }

    Node* getCurrent(){
        return currentStop;
    }

    Station* getStation(){
        return this->getCurrent()->getStation();
    }

    int getPlatform(){
        return this->getCurrent()->getPlatformNo();
    }

    int getJourneyTime(){
        return this->getCurrent()->getJourneyTime();
    }

    int getWaitTime(){
        return this->getCurrent()->getStation()->getWait();
    }

    void NextNode(){
        currentStop = getNext();
    }

};