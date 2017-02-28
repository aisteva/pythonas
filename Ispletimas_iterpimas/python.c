#include <Python.h>

static PyObject * spam_system(PyObject *self, PyObject *args){
	const char *command;
	int sts;
	if(!PyArg_ParseTuple(args, "s", &command))
		return NULL;
	sts = system(command);
	if(sts < o){
		return NULL;
	}
	return Py_BuildValue("i", sts);
}

static PyMethodDef spamMethods[] = {
	{"system", spam_system, METH_VARARGS, "Execute a shell command."},
	{NULL, NULL, o, NULL}
};
	