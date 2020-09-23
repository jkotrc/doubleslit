#include "module.h"
#include "computation/doubleslit.h"

static PyObject* say_hello(PyObject* self, PyObject* args) {
    do_hello();
    Py_RETURN_NONE;
}

static PyMethodDef doubleslit_methods[] {
    {
        "say_hello", say_hello, METH_VARARGS, "a method that says hello"
    },
    {NULL,NULL,0,NULL}
};

static struct PyModuleDef doubleslit_definition = {
    PyModuleDef_HEAD_INIT,
    "doubleslit",
    "CUDA implementation of the project that taught me numpy",
    -1,
    doubleslit_methods
};

PyMODINIT_FUNC PyInit__doubleslit() {
    return PyModule_Create(&doubleslit_definition);
}
