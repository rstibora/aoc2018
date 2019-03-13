#!/bin/bash

rm -rf build
mkdir build
cd build
# TODO: boost might be actually working without thiese hints.
cmake -DCMAKE_CXX_COMPILER=clang-8 -DCMAKE_CXX_FLAGS="-stdlib=libc++" -DCMAKE_SHARED_LINKER_FLAGS="-lc++ -lc++abi" ../day12
cd -