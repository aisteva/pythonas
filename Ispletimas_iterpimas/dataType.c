#include <Python.h>
#include "structmember.h"

typedef struct {
    PyObject_HEAD
    PyObject *guess; /* guess name */
    PyObject *type;  /* type name */
    int number;
} DataType;

static void
DataType_dealloc(DataType* self)
{
    Py_XDECREF(self->guess);
    Py_XDECREF(self->type);
    Py_TYPE(self)->tp_free((PyObject*)self);
}

//2
static PyObject *
DataType_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{

    DataType *self;

    self = (DataType *)type->tp_alloc(type, 0);
    if (self != NULL) {
        self->guess = PyUnicode_FromString("");
        if (self->guess == NULL) {
            Py_DECREF(self);
            return NULL;
        }

        self->type = PyUnicode_FromString("");
        if (self->type == NULL) {
            Py_DECREF(self);
            return NULL;
        }

        self->number = 0;
    }

    return (PyObject *)self;
}

//3
static int
DataType_init(DataType *self, PyObject *args, PyObject *kwds)
{

    PyObject *guess=NULL, *type=NULL, *tmp;

    static char *kwlist[] = {"guess", "type", "number", NULL};

    if (! PyArg_ParseTupleAndKeywords(args, kwds, "|OOi", kwlist,
                                      &guess, &type,
                                      &self->number))
        return -1;

    if (guess) {
        tmp = self->guess;
        Py_INCREF(guess);
        self->guess = guess;
        Py_XDECREF(tmp);
    }

    if (type) {
        tmp = self->type;
        Py_INCREF(type);
        self->type = type;
        Py_XDECREF(tmp);
    }

    return 0;
}


static PyMemberDef DataType_members[] = {
    {"guess", T_OBJECT_EX, offsetof(DataType, guess), 0,
     "guess name"},
    {"type", T_OBJECT_EX, offsetof(DataType, type), 0,
     "type name"},
    {"number", T_INT, offsetof(DataType, number), 0,
     "dataType number"},
    {NULL}  /* Sentinel */
};

static PyObject *
DataType_name(DataType* self)
{


    if (self->guess == NULL) {
        PyErr_SetString(PyExc_AttributeError, "guess");
        return NULL;
    }

    if (self->type == NULL) {
        PyErr_SetString(PyExc_AttributeError, "type");
        return NULL;
    }

    printf("THE GUESS WAS: \n");
    return PyUnicode_FromFormat("%S %S", self->guess, self->type);
}

static PyMethodDef DataType_methods[] = {
    {"name", (PyCFunction)DataType_name, METH_NOARGS,
     "Return the name, combining the guess and type name"
    },
    {NULL}  /* Sentinel */
};

static PyTypeObject DataTypeType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "noddy.DataType",             /* tp_name */
    sizeof(DataType),             /* tp_basicsize */
    0,                         /* tp_itemsize */
    (destructor)DataType_dealloc, /* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_reserved */
    0,                         /* tp_repr */
    0,                         /* tp_as_number */
    0,                         /* tp_as_sequence */
    0,                         /* tp_as_mapping */
    0,                         /* tp_hash  */
    0,                         /* tp_call */
    0,                         /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT |
        Py_TPFLAGS_BASETYPE,   /* tp_flags */
    "DataType objects",           /* tp_doc */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    DataType_methods,             /* tp_methods */
    DataType_members,             /* tp_members */
    0,                         /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc)DataType_init,      /* tp_init */
    0,                         /* tp_alloc */
    DataType_new,                 /* tp_new */
};

static PyModuleDef dataTypemodule = {
    PyModuleDef_HEAD_INIT,
    "dataType",
    "Example module that creates an extension type.",
    -1,
    NULL, NULL, NULL, NULL, NULL
};


//1
PyMODINIT_FUNC
PyInit_dataType(void)
{

 Py_Initialize();

 //Py_Finalize();


    PyObject* m;

    if (PyType_Ready(&DataTypeType) < 0)
        return NULL;

    m = PyModule_Create(&dataTypemodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&DataTypeType);
    PyModule_AddObject(m, "DataType", (PyObject *)&DataTypeType);
    PyRun_SimpleString("import prime");
    return m;
}




