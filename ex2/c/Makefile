CC := gcc
CFLAGS := -g -Wall -Wextra

all : ex2-1 ex2-2

ex2-1: ex2-1.c utils.h
	$(CC) ex2-1.c utils.h $(CFLAGS) -o ex2-1.o

ex2-2: ex2-2.c utils.h
	$(CC) ex2-2.c utils.h $(CFLAGS) -o ex2-2.o


clean: 
	$(RM) ex2-1.o ex2-2.o
