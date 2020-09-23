cmake_minimum_required(VERSION 3.16.3)


add_executable(testing main.cpp)
set_target_properties(testing PROPERTIES LINKER_LANGUAGE CXX)
target_link_libraries(testing cudadoubleslit)
