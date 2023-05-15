#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Print some basic info about Python lists
 * @p: A pointer to a PyObject list
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyListObject *list;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %zd\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %zd\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %zd: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
