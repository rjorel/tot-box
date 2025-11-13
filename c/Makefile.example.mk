.PHONY: clean distclean

CC      = gcc
CFLAGS 	= -g -Wall -Wextra
LDFLAGS = -g -Wall -Wextra
EXEC 	= test 

SRCDIR 	= src
INCDIR 	= include
BLDDIR 	= build
BINDIR 	= bin

SRCS    = $(wildcard $(SRCDIR)/*.c)
OBJS	= $(SRCS:$(SRCDIR)/%.c=$(BLDDIR)/%.o)
DEPS	= $(wildcard $(INCDIR)/*.h)

$(BINDIR)/$(EXEC): $(OBJS)
	$(CC) $^ -o $@ $(LDFLAGS) $(LDLIBS)

$(BLDDIR)/%.o: $(SRCDIR)/%.c $(DEPS)
	$(CC) -c $< -o $@ $(CFLAGS) -I $(INCDIR)

clean:
	rm -f $(BLDDIR)/*.o

distclean: clean
	rm -f $(BINDIR)/$(EXEC)
