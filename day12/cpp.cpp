#include <boost/python.hpp>

const char* greet() {
    return "Hellow world!";
}

BOOST_PYTHON_MODULE(libday_12) {
    boost::python::def("greet", greet);
}

