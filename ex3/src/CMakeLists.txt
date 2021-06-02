cmake_minimum_required(VERSION 2.8)
project(dispersion-curve)

find_package(CUDA REQUIRED)

CUDA_ADD_LIBRARY(CUDA_LIB STATIC
    dichotomy.cu
    dichotomy.h
)

include_directories(
    /usr/include
)

add_executable(${PROJECT_NAME}
    main.cpp
    dichotomy.h
)

target_link_libraries(${PROJECT_NAME} CUDA_LIB)
