# use this makefile to build shared libaray.
CC = g++
ifeq ($(CC),g++) 
	CPP = g++
	CFLAGS = -O2 
else 
	CPP=icpc
	CFLAGS = -O3 -xSSE4.2 
endif

OBJ= libkssolve.so
SOURCE = kssolve.o

$(OBJ): $(SOURCE)
	$(CPP) $(CFLAGS) -shared -lm -lfftw3   $^ -o $@ 

%.o: %.cc
	$(CPP) $(CFLAGS) -fpic -o $@ -c $^

clean:
	rm -f *.o 
