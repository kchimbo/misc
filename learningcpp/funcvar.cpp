#include <iostream>
#include <string>

namespace life {int meaning = 42;
				auto* p = &meaning;
				auto& rm = meaning;}

inline int add(int a, int b) { return a + b;}

auto add2(int a, int b) -> int { return a + b;}

void inc(int& a) { a++; }


int main(int argc, char* argv[])
{
	std::cout << "Hello, world!" << std::endl;
	// using namespace life;
	using life::meaning;
	std::cout << meaning << " takes up " << sizeof(meaning) << " bytes " << std::endl;
	*life::p = 43;
	std::cout << meaning << std::endl;
	life::rm = 42;
	std::cout << meaning << std::endl;

	std::string s ("hello"); // allocated in the stack
	std::string *t = new std::string("world"); // allocated in the heap

	delete t; // deallocate

	int* values = new int[128];

	delete[] values;

	std::cout << argv[0] << std::endl;

	int n = 10;
	std::cout << n << std::endl;
	inc(n);
	std::cout<< n << std::endl;

	int x = 4;

	auto doubleValue = [](int z) { return z * 2; };

	std::cout << x << " * 2 = " << doubleValue(x) << std::endl;

	/* lambda 
	 * [] - lambda does not access enclosing scope
	 * [=] - capture everything by value;
	 * [&] - capture everything reference
	 * [x, &y] - capture x by value and y by reference
	 * [&, z] - capture everything by reference, but z by value
	 */

	int y = 5;

	auto increaseByY = [&y](int z) {return y + z; }; // try with &

	y = 100;

	std::cout << "the result of 4 + y = " << increaseByY(x) << std::endl;

	/* enums */

	enum Color
	{
		RED, GREEN, BLUE
	};

	enum class GameState 
	{
		WIN, LOSE
	};

	Color color = RED;
	int i = color;

	GameState gs = GameState::WIN;
 	//int j = gs;	// does work with enum class

	/* different types of data over the same memory */
 	union Data
 	{
 		int integer;
 		float fp;
 		char* text;
 	};

 	struct Data2
 	{
 		int size;
 		float volume;
 		char* text;
 	};

 	Data2 data{15, 10.5f, "Hello"};

 	std::cout << "size of data (union): " << sizeof(Data) << std::endl;

 	std::cout << "size of data2 (struct): " << sizeof(Data2) << std::endl;

	return 0;	
}



