all: evolve_10.png evolve_30.png evolve_100.png

evolve_10.png evolve_30.png evolve_100.png: evolve_10.dat evolve_30.dat evolve_100.dat plot.py
	python plot.py

evolve_100.dat : evolve.x
	./evolve.x 100 > evolve_100.dat

evolve_30.dat : evolve.x
	./evolve.x 30 > evolve_30.dat

evolve_10.dat : evolve.x
	./evolve.x 10 > evolve_10.dat

evolve.x : Ej31.cpp
	c++ Ej31.cpp -o evolve.x

clean:
	rm evolve.x *.dat