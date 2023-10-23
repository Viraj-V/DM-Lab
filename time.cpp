#include<bits/stdc++.h>
using namespace std;
#include <bits/stdc++.h>
using namespace std;



int convertToMinute(string s){
    int hour, min;
    hour = stoi(s.substr(0,2));
    min = stoi(s.substr(3,2));
    
    string st = s.substr(5,2);
    if(st == "PM" && hour != 12){
        hour += 12;
    }
    if(st == "AM" && hour == 12){
        hour = 0;
    }
    
    return hour*60 + min;
}

string ArrayChallenge(vector<string> &strArr){
    int n = strArr.size();
    
    vector<pair<int,int>> event;
    
    for(auto a : strArr){
        string s1 = a.substr(0,7);
        string s2 = a.substr(8,7);
        
        int p1 = convertToMinute(s1);
        int p2 = convertToMinute(s2);
        event.push_back({p1, p2});
    }
    
    sort(event.begin(), event.end(), [&](pair<int,int> &p1, pair<int,int> &p2){
        return p1.second < p2.second;
  });
    
    int mx = 0;
    for(int i=1; i<n; i++){
        pair<int,int> prev = event[i-1];
        mx = max(mx, (event[i].first - prev.second));
    }
    
    int hour = mx/60;
    int min = mx%60;
    string res = "";
    if(hour < 10){
        res += "0" + to_string(hour);
    }
    else{
        res += to_string(hour);
    }
    res += ":";
    if(min < 10){
        res += "0" + to_string(min);
    }
    else{
        res += to_string(min);
    }
    cout << res << endl;
    return res;
}

int main(){
    vector<string> strArr = {"10:00AM-12:30PM", "02:00PM-02:45PM", "09:10AM-09:50AM"};
    
    ArrayChallenge(strArr);
    
     return 0;
}