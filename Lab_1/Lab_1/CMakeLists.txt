cmake_minimum_required(VERSION 3.10)
project(MyTests)

set(CMAKE_TOOLCHAIN_FILE "C:/path/to/vcpkg/scripts/buildsystems/vcpkg.cmake" CACHE STRING "Vcpkg toolchain file")

find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})

add_executable(test_program test_LogCon.cpp)
target_link_libraries(test_program GTest::GTest GTest::Main)
