#include <Python.h>
int main(int argc, char *argv[]){
 Py_Initialize();
 PyRun_SimpleString("import prime");
 Py_Finalize();
 return 0;
}
