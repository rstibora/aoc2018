cmake_minimum_required(VERSION 3.10.2)
project(day_12 LANGUAGES CXX)
set(CMAKE_CXX_FLAGS "-std=c++17 -Wextra -O3")

find_package(Boost REQUIRED python3)
find_package(PythonLibs 3.6 REQUIRED)

add_library(day_12 SHARED solution.cpp)
target_include_directories(day_12 PUBLIC "${PYTHON_INCLUDE_DIRS}" "${Boost_INCLUDE_DIR}")
target_link_libraries(day_12 "${Boost_PYTHON3_LIBRARY_RELEASE}")
install(TARGETS day_12 DESTINATION "${CMAKE_SOURCE_DIR}")