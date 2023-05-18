#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Print some basic info about Python bytes
 * @p: A pointer to a PyObject list
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size = PyBytes_Size(p);
	Py_ssize_t i;
	char *str;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first %ld bytes: ", (size > 10) ? 10 : size);
	str = (char *)bytes->ob_sval;
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i < size - 1 && i < 9)
			printf(" ");
	}
	printf("\n");
}
/**
 * print_python_list - Print some basic info about Python lists
 * @p: A pointer to a PyObject list
 * Return: void
 */

void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;
	PyObject *item;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		type = item->ob_type->tp_name;

		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(item);
	}
}
