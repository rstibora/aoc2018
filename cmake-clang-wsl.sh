#!/bin/bash

rm -rf build
mkdir build
cd build
cmake -DCMAKE_CXX_COMPILER=clang-8 -DBOOST_INCLUDEDIR="/usr/include" -DBOOST_LIBRARYDIR="/usr/lib/x86_64-linux-gnu" ../day12
cd -