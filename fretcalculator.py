#!/usr/bin/python
##################################
# Script to calculate fret distance
# algorithm lifted nearly wholesale from:
# http://www.buildyourguitar.com/resources/tips/fretdist.htm
# scale length (nut to bridge) explained: http://www.stewmac.com/How-To/Online_Resources/Fretting/Scale_Length_Explained.html 
##################################

##################################
# imports
##################################
import argparse


##################################
# Variables
##################################
parser = argparse.ArgumentParser(description="Calculate fret distance by inputing first distance from bridge to nut, then number of frets")
parser.add_argument("length", type=float, help="Scale length - distance between bridge and nut")
parser.add_argument("numFrets", type= int, help="Number of frets")

args = parser.parse_args()


##################################
# Functions
##################################

def main():
	#initialize variables first
	A = 0	# this represents the nut - start position for calculations
	B = 1	# this is fret number 1
	while (B <= args.numFrets): # loop through the function for each fret
		L = args.length - A 	# Length is set to (scale length - the last fret-distance value (A))
		X = (L / 17.817)		# X is set to (Length / 17.817)
		A = A + X				# A is set to (A + X)
		print "distance to fret ", B, ":", ("%.3f" % A) # print the distance with 3 decimal places
		B = B + 1				#move on to the next fret


##################################
# execute
##################################

main()
