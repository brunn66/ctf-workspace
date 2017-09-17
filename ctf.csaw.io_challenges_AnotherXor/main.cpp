/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: Brunn
 *
 * Created on den 17 september 2017, 22:58
 */

#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>


using namespace std;

/*
 * 
 */

string xor_crypt(const string &key, string data)
{
    for (size_t i = 0; i != data.size(); i++)
        data[i] ^= key[ i % key.size() ];
    return data;
}



int main(int argc, char** argv) {

    
    
    string hex2 = "0a0b170e0f00015d025a0a58580f5f095908560a550b0d580259590c560a5957535f5957570f0b";

    string res;
    res.reserve(hex2.size() / 2);
    for (int i = 0; i < hex2.size(); i += 2)
    {
    istringstream iss(hex2.substr(i, 2));
    int temp;
    iss >> hex >> temp;
    res += static_cast<char>(temp);
    }
    res;
    
    string myKey = "anno"; //hex2.substr(hex2.size()-32, 32);
    string mySecret = res;
    string publicSecret = xor_crypt(myKey, mySecret);
    cout << "Decoded: " << publicSecret << endl;
    string st = publicSecret.substr(0, publicSecret.size()-32);
    string hash = publicSecret.substr(publicSecret.size()-32, 32);
    cout << "Decoded: " << st << endl;
    cout << "Hash: " << hash << endl;
    return 0;
}

