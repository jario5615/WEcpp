#include "route.cpp"
#include <iostream>

using namespace std;

class Train{

    int id;
    int et2d;
    Route route;
    bool atStation;

    public:
    Train(int id, vector<Station *> stations, vector<int> journeys, vector<int> platforms){
        this->id = id;
        //cout << "ID Set" << endl;
        this->et2d = 0;
        //cout << "et2d Set" << endl;
        this->route = Route(stations, journeys, platforms);
        //cout << " Route set" << endl;
        this->route.getCurrent()->getStation()->arriveAtPlatform(this->id,this->route.getPlatform());
        this->atStation = true;
        //cout << "Train ready" << endl;
    }

    int getet2d(){
        return et2d;
    }

    int getid(){
        return id;
    }

    Route getRoute(){
        return route;
    }

    void toggleAtStation(){
        atStation ? atStation = false : atStation = true;
    }

    void move(){
        if(et2d > 0){
            et2d--;
            //cout << "m1" << endl;
        } else if (!atStation){
            //cout << "m2" << endl;
            if(route.getStation()->platformIsEmpty(route.getPlatform())){
                if(route.getStation()->arriveAtPlatform(id, route.getPlatform())){
                    toggleAtStation();
                    et2d = route.getWaitTime();
                    cout << "Train " << id << " arrived at " << route.getStation()->getName() << " at platform " << route.getPlatform() << endl;
                }
            } else {
                cout << "Train " << id << " is waiting outside " << route.getStation()->getName() << " for platform " << route.getPlatform() << endl;
            }
        } else {
            //cout << "m3" << endl;
            if(route.getStation()->leaveStation(route.getPlatform())){
                toggleAtStation();
                et2d = route.getJourneyTime();
                route.NextNode();
                cout << "Train " << id << " departing for " << route.getStation()->getName() << ". ETA " << et2d << " minutes" << endl;
            }
        }
    }

};