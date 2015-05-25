#include <iostream>
#include <cstdint> /* defines fixed sizes */
#include <array> /* array wrapper */

int main()
{
	/* INT
	 * signed
	 * plataform specific
	 * default value unknown
	 * 0xCCCCCCCC in Visual Studio debug mode
	 */
	 std::cout << sizeof(int) << std::endl;
	 std::cout << sizeof(int32_t) << std::endl;
	 std::cout << sizeof(uint64_t) << std::endl;
	/* float
	 * typically single precision (32 bit)
	 * double
	 * typically double precision (64 bit)
	 */
	 float f;
	 double d;
	 std::cout << "Size of float: " << sizeof(f) << " bytes" << std::endl;
	 std::cout << "Size of double: " << sizeof(d) << " bytes" << std::endl;
	 /* logical 
	  * zero = false, non-zero = true
	  */
	 bool b = true;
	 bool b1 = false;
	 /* pointers
	  * store the address
	  * no default (as always)
	  * int *x, y (only x is a pointer, y is an int)
	  */
	 float *n; // pointer to float
	 float fp = 4.2f;
	 n = &fp;
	 std::cout << "address of fp: " << n << std::endl; 
	 std::cout << "value of fp: " << *n << std::endl; 
	 float **p = &n; // pointer to pointer
	 std::cout << "value of p: " << **p << std::endl;
	 /* references 
	  * initialization uses &
	  * no concept of null reference
	  * can have reference-to-reference
	  */
	  int y = 42;
	  int &x = y; // x is a reference to i
	  std::cout << "value of x: " << x << std::endl;
	  // reference from pointer
	  // pointer to reference is illegal
	  // affects storing references in containers std::reference_wrapper
	  int *i;
	  int &j = *i;
	 /* arrays
	  * c-style arrays, pointers to the first element
	  * we cannot tell how long the array is
	  * when passing an array to a function, you need to pass its length
	  * separately
      */
       int numbers[] {1, 2, 3};
       std::cout << (*numbers) << std::endl;
       int zeros[10] { 0 }; // size of the array is 10
       int ident[2][2] { {1, 0}, {0, 1} };
       // std::array - wrapper for an array of known size
       std::array<int, 3> ex { {1, 2, 3} }; // header <array>
       std::cout << "the size of the array is " << ex.size() << std::endl;
       // std::vector - resizable array

      /* character types 
       * ascii character stored in a char (1 byte)
       * wide character wchar_t, compiler specfic, not recomended by unicode standard
       * char16_t, char32_t
       * char/wchar duality propagates everywhere (string/wstring, main/wmain, cout/wcout)
       */
        char c = 'z';
        wchar_t cc = 'a';
        std::cout << "size of char: " << sizeof(c) << " bytes" << std::endl;
	 	std::cout << "size of wchar: " << sizeof(cc) << " bytes" << std::endl;

	  /* strings
	   * c-style strings - arrays of characters terminated by a zero
	   */
	 	char *text = "Hello";
	 	wchar_t *text2 = L"Hello";
	 	std::string s {"hello"};
	 return 0;
}