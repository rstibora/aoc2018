#include "solution.hpp"

std::vector<char> aoc2018::day12::detail::solve_generations(std::vector<char> state, const std::map<std::string, char>& rules, const int no_of_generations) {
    return state;
}

boost::python::list aoc2018::day12::solve_generations(boost::python::list state, boost::python::dict rules, int no_of_generations) {
    auto extracted_state = std::vector<char>(boost::python::len(state));
    for (int i = 0; i < boost::python::len(state); ++i) {
        extracted_state[i] = boost::python::extract<char>(state[i]);
    }

    std::map<std::string, char> extracted_rules;

    extracted_state = detail::solve_generations(std::move(extracted_state), extracted_rules, no_of_generations);

    return state;
}

BOOST_PYTHON_MODULE(libday_12) {
    boost::python::def("solve_generations", aoc2018::day12::solve_generations);
}
