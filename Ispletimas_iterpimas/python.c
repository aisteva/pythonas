#include <Python.h>

static PyObject *spam_system(PyObject *self, PyObject *args)
{
    int number;
    int sts;

    if (!PyArg_ParseTuple(args, "i", &number)) //atlieka vertima
        return NULL;
    sts = prime(number);
	printf("%d REZULTATAS \n",sts);
	if (sts == 1 )
        printf("%d is prime number\n",number);
    else
        printf("%d is not prime number\n", number);
    return PyLong_FromLong(sts); //returns integer object
}

//metodu lentele
static PyMethodDef spamMethods[] = {
	{"prime", /* name */
	spam_system, /* function API name */
	METH_VARARGS, /* flag */
	"Execute a function."},

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
    return PyModule_Create(&python); /* python - module structure */
}


int prime(int a)
{
   int i;

   for ( i = 2 ; i <= a - 1 ; i++ )
   {
      if ( a%i == 0 )
	 return 0;
   }
   if ( i == a )
      return 1;
}
