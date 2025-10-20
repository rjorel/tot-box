.PHONY: clean, mrproper

CC = ocamlopt

all: snake draw

snake: snake.ml 
	$(CC) graphics.cmxa unix.cmxa $^ -o $@
	
draw: draw.ml
	$(CC) graphics.cmxa $< -o $@ 

clean:
	rm -f *.cmi *.cmo *.cmx *.o

mrproper: clean
	rm -f snake draw
