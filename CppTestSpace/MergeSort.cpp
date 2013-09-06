/*
 * MergeSort.cpp
 *
 *  Created on: Aug 17, 2013
 *      Author: phcostello
 */

#include <vector>;
#include <stdlib.h>;
#include <iostream>;

using namespace std;

vector<double> merge( vector<double> left, vector<double> right)
{
	vector<double> result;

	while(left.size() > 0 && right.size() >0 ){

			if(left[0] <= right[0])
			{
				result.push_back( *left.begin() );
				left.erase(left.begin());
			}
			if(left[0] > right[0])
			{
				result.push_back( *right.begin() );
				right.erase(right.begin());
			}
	}
	if( left.size() > 0)
	{
		for( double it: left)
		{
			result.push_back(it);
		}
	}
	else if( right.size() > 0)
	{
		for( double it: right)
		{
			result.push_back(it);
		}
	}


	return result;

}

vector<double> mergesort( vector<double> input )
{

	vector<double> output;

	if( input.size() <= 1){

		output = input;
		return output;
	}


	int mid = input.size()/2;

	vector<double> leftt(input.begin(),input.begin()+mid);
	vector<double> rightt(input.begin()+mid, input.end());

	if(input.size() == 2){
		leftt = vector<double> {input[0]};
		rightt = vector<double> {input[1]};

	}

	leftt = mergesort(leftt);
	rightt = mergesort(rightt);


	output = merge(leftt,rightt);

	return output;



}

int main(){

	vector<double> vec;
	int myarr[] = {1,2,3,4,5,6,7,8,9};
	int this_rand;
	vector<double> ll = {1,2,5};
	vector<double> rr = {3,4,7};

	for(int i = 0; i<10000; i++)
	{
		this_rand = rand()% 10000;
		vec.push_back(this_rand);
		cout<< this_rand << " ";

	}

	cout << endl;
	vector<double> res;
//	res = merge(rr,ll);
	res = mergesort(vec);
	cout << "merged" << endl;

	for(double it: res)
	{
		cout<< it << " ";
	}




//	for( i rand_r()



	//Define mergesort


	//Define merge

	return 0;

}



