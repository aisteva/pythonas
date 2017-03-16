#include <Python.h>

static PyObject *spam_system(PyObject *self, PyObject *args)
{
    const int *command;
    int sts;
    //int result;

    //result = check_prime(command);





    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    return PyLong_FromLong(sts);

    if ( command == 1 )
      printf("is prime.\n");
   else
      printf("is not prime.\n");
}

//metodu lentele
static PyMethodDef spamMethods[] = {
	{"system", spam_system, METH_VARARGS,
	"Execute a shell command."},

	{NULL, NULL, 0, NULL}/* Sentinel */
};

//iniciavimas
static struct PyModuleDef python = {
   PyModuleDef_HEAD_INIT,
   "spam",   /* name of module */
   NULL, /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   spamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    return PyModule_Create(&python);
}


int system(int a)
{
   int c;

   for ( c = 2 ; c <= a - 1 ; c++ )
   {
      if ( a%c == 0 )
	 return 0;
   }
   if ( c == a )
      return 1;
}
