#include <Python.h>
#include <stdio.h>


/**
 * print_python_list - Display basic information about a list.
 * @p: List.
 *
 */

void print_python_list(PyObject *p)
{
	int i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %d: %s\n", i, PyList_GET_ITEM(p, i)->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - Display basic information about a bytes.
 * @p: bytes.
 *
 */

void print_python_bytes(PyObject *p)
{
	int i;
	char *str;

	printf("[.] bytes object info\n");
	if (!(PyBytes_Check(p)))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));
	str = PyBytes_AsString(p);
	printf("  first elements: ");
	for (i = 0; i < PyBytes_Size(p) && i < 10; i++)
	{
		if (i != PyBytes_Size(p) - 1)
			printf("%hhx ", str[i]);
		else
			printf("%hhx", str[i]);
	}
	putchar('\n');
}

