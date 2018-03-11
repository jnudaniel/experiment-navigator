#! /usr/bin/env python
# Experiment Navigator user interaction script
# Julia Daniel, Akhila Moturu, Eric Cramer, and Gaby Steiner
# Final project for CS 270 / BMI 210, Winter 2018
# ----------------------------------------------------------

import ontology as o

if __name__ == "__main__":
	print("* ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ *")
	print("Welcome to the Experiment Navigator!")
	print("Loading our cutting-edge experiment ontology...")
	ont = o.build_ontology()
	print("...done!")
	print("The Experiment Navigator is your tool to help find the right experiment for you, given a hypothesis you'd like to test.")
	print("Please enter your hypothesis here, in your own words:")
	hypothesis = raw_input(" > ")
	print(hypothesis)
	print("Great! In order to determine which experiment(s) you should conduct to test this hypothesis, we need to know more about the substances and information involved.")

	print ont

	for substance in ont.substances:
		print substance
