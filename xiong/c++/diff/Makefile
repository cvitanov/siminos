CC=gcc
#CC=icc

#MARCH=core2
MARCH=corei7
SSE=SSE4.2
#SSE=SSE3
ifeq ($(CC),gcc) 
	CPP = g++
	COPTFLAGS = -O3 -W -march=$(MARCH) -lm -std=c99  -fopenmp 
else 
	CPP=icpc
	COPTFLAGS = -O3 -x$(SSE) -lm -std=c99 -openmp 
endif

OBJ= slice
SOURCE= diffvec.c

$(OBJ): $(SOURCE)
	$(CC)  $^ -o $@ $(COPTFLAGS)
clean:
	rm -f $(OBJ)
