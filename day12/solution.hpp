#include <boost/python.hpp>

namespace aoc2018::day12 {
    using State = std::deque<char>;
    using RulePattern = std::array<char, 5>;
    using Rules = std::map<RulePattern, char>;

    boost::python::tuple solve_generations(boost::python::list state, boost::python::list rules, int no_of_generations);

namespace detail {

    std::pair<std::deque<char>, int> solve_generations(State state, const Rules& rules, const int no_of_generations);
    bool match_rule(const RulePattern& pattern, const State& state, const int index);

} // namespace detail
} // namespace aoc2018::day12

BOOST_PYTHON_MODULE(libday_12) {
    boost::python::def("solve_generations", aoc2018::day12::solve_generations);
}
