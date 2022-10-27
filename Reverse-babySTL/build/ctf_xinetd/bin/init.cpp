#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <unistd.h>
#include <ctime>

using namespace std;

int main()
{

	system("(cat /proc/sys/kernel/random/uuid && cat /proc/sys/kernel/random/uuid) > param");
	ofstream flag("./flag", ios::out);
	flag << "flag{cp1usplu5_stl_is_f@ntastic}" << endl;

	exit(0);
}