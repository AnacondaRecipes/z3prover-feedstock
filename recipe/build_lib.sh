#!/usr/bin/env bash

set -xe

mkdir -p build_lib && cd build_lib

cmake -G "Ninja" \
    ${CMAKE_ARGS} \
    -DPython3_EXECUTABLE=${BUILD_PREFIX}/bin/python \
    -DZ3_BUILD_DOCUMENTATION=FALSE \
    -DZ3_BUILD_LIBZ3_CORE=ON \
    -DZ3_BUILD_LIBZ3_SHARED=TRUE \
    -DZ3_BUILD_PYTHON_BINDINGS=FALSE \
    -DZ3_INCLUDE_GIT_DESCRIBE=FALSE \
    -DZ3_INCLUDE_GIT_HASH=FALSE \
    ..
ninja install
