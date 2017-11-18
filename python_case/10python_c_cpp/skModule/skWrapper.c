
//#include "Python.h"
#include "/usr/include/python2.7/Python.h"
#include <stdlib.h>
#include <string.h>
#include "sk.h"

static PyObject* sk_fac(PyObject* self, PyObject* args)
{
   int num;
   if (!PyArg_ParseTuple(args,"i",&num))
      return NULL;

   return (PyObject*)Py_BuildValue("i",fac(num));
}

static PyObject* sk_reverse(PyObject* self, PyObject* args)
{
   char* src;
   char* mstr;
   PyObject* retval;

   if(!PyArg_ParseTuple(args,"s",&src))
   	return NULL;
   
   mstr = malloc(strlen(src)+1);
   strcpy(mstr,src);
   reverse(mstr);
   retval = (PyObject*)Py_BuildValue("ss",src,mstr);
   free(mstr);

   return retval;
}

static PyObject* sk_test(PyObject* self, PyObject* args)
{
   test();
   return (PyObject*)Py_BuildValue("");
}


static PyMethodDef skMethods[] = {
  	{"fac", sk_fac, METH_VARARGS},
  	{"reverse", sk_reverse, METH_VARARGS},
  	{"test", sk_test, METH_VARARGS},
  	{NULL, NULL},
 };

void initsk(void)
{
    Py_InitModule("sk",skMethods);
}






