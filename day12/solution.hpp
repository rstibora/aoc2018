#include <boost/python.hpp>

namespace aoc2018::day12 {

    boost::python::list solve_generations(boost::python::list state, boost::python::dict rules, int no_of_generations);

namespace detail {

    std::vector<char> solve_generations(std::vector<char> state, const std::map<std::string, char>& rules, const int no_of_generations);

} // namespace detail
} // namespace aoc2018::day12
