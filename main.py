from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print

#parse_file( 'script', edges, transform, screen, color )

screen = new_screen()
color = [ 0, 255, 255 ]
edges = []
transform = new_matrix()

parse_file( 'myscript', edges, transform, screen, color )
