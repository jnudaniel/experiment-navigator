#! /usr/bin/env python
# Experiment Navigator user interaction script
# Julia Daniel, Akhila Moturu, Eric Cramer, and Gaby Steiner
# Final project for CS 270 / BMI 210, Winter 2018
# ----------------------------------------------------------

import ontology as o

if __name__ == "__main__":
    print("Welcome to the Experiment Navigator!")
    print("The Experiment Navigator is your tool to help find the right experiment for you, given a hypothesis you'd like to test.")
    print("Please enter your hypothesis here, in your own words:")
    hypothesis = input(" > ")
    print(hypothesis)
