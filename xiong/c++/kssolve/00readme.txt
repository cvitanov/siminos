$Tue Jul  8 14:13:19 EDT 2014$
$Author: Xiong Ding$

C++ codes: 
    KS integrator with/without calculating Jacobian matirx.
    This code is ~10x faster than the corresponding matlab code
    tested on Phys32125. It depends on FFTW3 library, so 
    make sure the fftw3 library is available in your computer.
--------------------------------
File description:

"kssolve.hpp" and "kssolve.cc" are the main codes for the integrator.

"Makefile" generates the shared library for the integrator.

"driver.cc" is a simple example driver file to use the integrator.

"ksfjaco.cpp" is the correpsonding MEX file to generate callable
matlab library. (NOT WORKING at this moment!)

--------------------------------
exmpale usage:

>> make && make clean
>> g++ driver.cc -I. -L. -lkssolve -o execu
>> ./execu


