#include <iostream>
#include <ctime>
#include <random>
#include <string>
#include <fstream>
#include <queue>
#include <vector>
#include <unordered_set>

using namespace std;

void success()
{
	system("cat flag");
	exit(0);
}

typedef struct
{
	bool operator()(const pair<char, int> x, const pair<char, int> y)
	{
		return x.second > y.second;
	}
} comp;

int main()
{
	time_t t = time(0);
	srand(t);
	int cnt = 6;
	priority_queue<pair<char, int>, vector<pair<char, int> >, comp> pq;
	unordered_set<char> us;
	string check;

	ifstream ifs("param", ios::in);
	string s1, s2;
	ifs >> s1 >> s2;
	ifs.close();

	string uuid1, uuid2;
	for (auto i = s1.rbegin(); i != s1.rend(); i++)
	{
		if (*i == '-')
			continue;
		else
			uuid1 += *i;
	}
	for (auto i = s2.begin(); i != s2.end(); i++)
	{
		if (*i == '-')
			continue;
		else
			uuid2 += *i;
	}

	while (pq.size() < 16)
	{
		if (rand() % 2 == 1)
		{
			auto temp = rand() % uuid2.size();
			if (us.find(uuid2[temp]) == us.end())
			{
				us.insert(uuid2[temp]);
				pq.push(make_pair(uuid2[temp], rand() % 0xc0ffee));
			}
		}
		else
		{
			auto temp = rand() % uuid1.size();
			if (us.find(uuid1[temp]) == us.end())
			{
				us.insert(uuid1[temp]);
				pq.push(make_pair(uuid1[temp], rand() % 0xc0ffee));
			}
		}
	}

	string passwd;
	while (!pq.empty())
	{
		auto temp = pq.top();
		pq.pop();
		int c = temp.first;
		int add = temp.second;
		while ((c + add) >= 127)
			add /= 2;
		passwd += char(c + add);
	}



	while (cnt--)
	{
		// system("clear");
		printf("\033c");
		// cout << passwd << endl;
		printf("You have %d/%ld times.\n", cnt, t);
		if (cnt == 0)
		{
			printf("You cannot try anymore.\nBye!\n");
			exit(-1);
		}
		else
		{
			printf("Welcome to %s Lab\nusername: %s\npassword: ", s1.c_str(), s2.c_str());
			cin >> check;
			if (check == passwd)
				success();
		}
	}
	return 0;
}