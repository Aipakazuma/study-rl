#include <boost/python.hpp>

int add_int(int a, int b) {
  return a + b;
}

boost::python::object add(int a, int b) {
  return boost::python::object(a + b);
}

char const* hello_char() {
  return "hello!";
}

boost::python::object hello() {
  return boost::python::object("hello!");
}

BOOST_PYTHON_MODULE(basic)
{
  boost::python::def("add_int", add_int);
  boost::python::def("add", add);
  boost::python::def("hello_char", hello_char);
  boost::python::def("hello", hello);
}
