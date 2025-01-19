# Largest Polyhedra

## Problem Statement
The aim of this project is to find numerically the n-vertex polyhedra with the largest volume, as well as the one with the most area. Both of these geometrical bodies are within the unit sphere.
The problem of n = 8 is specially considered as the motivation is the paper Search For Largest Polyhedra from 1962 by Donald W. Grace.

## Results
The known value for the volume of the largest 8-vertex polyhedra (V = 1.81570) is succesfully reached to at least 3 decimal places.
The result for the area problem with n = 8 was a value around 8.12, a bit far from a theoretical result (as seen by Donahue et al. in https://arxiv.org/pdf/2005.13660)
Trials for grater values of n also appear relatively close to other results (for example for n = 10, the code yields as maximum area 8.96, whereas the paper by Danahue lists it as 9.02)

## Further doings
Some improvements that can be done are:
 - Fixing one point so the search becomes faster (only n-1 points will be being perturbated)

## Credits
This project was done in collaboration with Jimena Campos and Hancel Borrego, at the time, students from the Universidad de Colima.
