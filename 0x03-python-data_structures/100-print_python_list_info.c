#include <Python.h>
#include <listobject.h>
#include <object.h>
/*
 * print_python_list_info - python in c
 * @p: arg
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *listObj = (PyListObject *)p;
	Py_ssize_t size = PyList_GET_SIZE(p);
	Py_ssize_t allocated = listObj->allocated;
	
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GET_ITEM(p, i);
		const char *typeName = Py_TYPE(item)->tp_name;
		printf("Element %zd: %s\n", i, typeName);
	}
}

