#pragma once
#include <python3.8/Python.h>

static PyObject* say_hello(PyObject* self, PyObject* args);
PyMODINIT_FUNC PyInit__doubleslit();
