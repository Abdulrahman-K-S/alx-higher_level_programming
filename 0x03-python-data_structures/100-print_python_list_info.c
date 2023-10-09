#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include <stdio.h>

/**
 * printListInfo - A function that prints the python enviorment
 *
 * @p: The enviorment
*/
void printListInfo(PyObject* list) {
    if (PyList_Check(list)) {
        Py_ssize_t size = PyList_Size(list);
        printf("List Size: %zd\n", size);

        for (Py_ssize_t i = 0; i < size; i++) {
            PyObject* item = PyList_GetItem(list, i);
            PyObject* itemStr = PyObject_Str(item);
            char* itemChars = PyUnicode_AsUTF8(itemStr);
            printf("Item %zd: %s\n", i, itemChars);
            Py_XDECREF(itemStr);
        }
    } else {
        printf("The object is not a list.\n");
    }
}
