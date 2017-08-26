cmake_minimum_required(VERSION 2.8)
#needed in every CMakeLists.  
#include outside libraries, we’ll show you how to do that when we get into OpenCV
project(hw) #names the project

add_executable(hw main.cpp Parser.cpp) 

