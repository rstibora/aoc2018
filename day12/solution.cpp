#include <numeric>

#include "solution.hpp"

using namespace aoc2018::day12;

bool aoc2018::day12::detail::match_rule(const RulePattern& pattern, const State& state, const int state_idx_offset) {
    const int pattern_size = static_cast<int>(pattern.size());
    for (int pattern_idx = 0; pattern_idx < pattern_size; ++pattern_idx) {
        const int state_idx = pattern_idx + state_idx_offset - (pattern_size / 2);
        if (state_idx < 0 || state_idx >= static_cast<int>(state.size())) {
            if (pattern[pattern_idx] != '.') {
                return false;
            }
        } else {
            if (pattern[pattern_idx] != state[state_idx]) {
                return false;
            }
        }
    }
    return true;
}

// TODO: verify pass-by-value reasoning is correct.
std::pair<State, int> aoc2018::day12::detail::solve_generations(State state, const Rules& rules, const int no_of_generations) {
    auto new_state = state;
    int negative_pots = 0;
    for (int generation = 0; generation < no_of_generations; ++generation) {
        const auto state_size = static_cast<int>(state.size());
        const auto new_state_begin = std::begin(new_state);

        // State will be iterated in this fashion: [-1, -2, -3, 0, 1, 2, 3, ...] to make the code more lovely.
        auto state_indices = std::vector<int>(state_size + 6);
        std::iota(std::begin(state_indices) + 3, std::end(state_indices), 0);
        std::iota(std::rbegin(state_indices) + state_size - 7, std::rend(state_indices), -3);

        for (const auto& state_idx: state_indices) {
            for (const auto& rule: rules) {
                if (detail::match_rule(rule.first, state, state_idx)) {
                    if (state_idx < 0) {
                        new_state.push_front(rule.second);
                        ++negative_pots;
                    } else if (state_idx >= state_size) {
                        new_state.push_back(rule.second);
                    } else {
                        *(new_state_begin + state_idx) = rule.second;
                    }
                    // Assuming only a single rule matches for each state slice.
                    break;
                }
            }
        }
        std::swap(state, new_state);
        new_state.resize(state.size());
    }
    return std::make_pair(std::move(state), negative_pots);
}

boost::python::tuple aoc2018::day12::solve_generations(boost::python::list initial_state, boost::python::list rules, int no_of_generations) {
    auto state = State();
    for (int i = 0; i < boost::python::len(initial_state); ++i) {
        state.push_back(boost::python::extract<char>(initial_state[i]));
    }

    auto extracted_rules = Rules();
    for (int i = 0; i < boost::python::len(rules); ++i) {
        auto rule_pattern = RulePattern();
        for (int ii = 0; ii < boost::python::len(rules[i][0]); ++ii) {
            rule_pattern[ii] = boost::python::extract<char>(rules[i][0][ii]);
        }
        extracted_rules[std::move(rule_pattern)] = boost::python::extract<char>(rules[i][1]);
    }

    auto [new_state, negative_pots] = detail::solve_generations(std::move(state), extracted_rules, no_of_generations);

    auto final_state = boost::python::list();
    for (auto state_value: new_state) {
        final_state.append(state_value);
    }

    return boost::python::make_tuple(final_state, negative_pots);
}
