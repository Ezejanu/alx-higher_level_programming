#include "lists.h"
#include <stdio.h>
#include <python.h>

/**
 * print_python_list_info - a function that prints
 * some basic info about Python lists
 * @p: pointer to the python list whose info is to be printed
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i = 0;
	PyObject *element;
	const char *element_type;
	Py_ssize_t list_size = PyList_Size(p);
	Py_ssize_t list_allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %d\n", list_allocated);

	for (; i < list_size; i++)
	{
		element = PyList_GetItem(p, i);
		element_type = Py_TYPE(element)->tp_name;

		printf("Element %d: %s\n", i, element_type);
	}
}
