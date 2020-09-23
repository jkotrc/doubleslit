#computation
cmake_minimum_required(VERSION 3.16.3)

add_library(cudadoubleslit doubleslit.h doubleslit.cpp)
set_target_properties(cudadoubleslit PROPERTIES LINKER_LANGUAGE CXX)
