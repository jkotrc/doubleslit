cmake_minimum_required(VERSION 3.16.3)
if(SKBUILD)
  message(STATUS "The project is built using scikit-build")

project(cudadoubleslit)
find_package(PythonExtensions REQUIRED)

add_definitions("-fPIC")

add_library(_doubleslit MODULE module.h module.cpp)
add_subdirectory(computation)#comment this out if it fucks with the build
target_link_libraries(_doubleslit cudadoubleslit)

python_extension_module(_doubleslit)

install(TARGETS _doubleslit LIBRARY DESTINATION doubleslit)
else()

message(STATUS "doing test build!")
project(cudadoubleslit)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/out)
add_subdirectory(computation)
add_subdirectory(test)

endif()