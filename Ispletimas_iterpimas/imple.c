#include <Python.h>
int main(int argc, char *argv[]){
 Py_Initialize();
 PyRun_SimpleString("import prime\n" "x = int(input('Enter: '))\n"
		"prime.prime(x)");
 Py_Finalize();
 return 0;
}
