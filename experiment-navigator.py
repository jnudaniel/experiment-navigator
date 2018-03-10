#! /usr/bin/env python
# Experiment Navigator user interaction script
# Julia Daniel, Akhila Moturu, Eric Cramer, and Gaby Steiner
# Final project for CS 270 / BMI 210, Winter 2018
# ----------------------------------------------------------

from owlready2 import *
onto = get_ontology("file://pizza.owl").load()

if __name__ == "__main__":
    print("hello")
    # acetaminophen   = ActivePrinciple("acetaminophen")
    my_pizza = onto.Pizza("pizza1")
    garlic = onto.GarlicTopping()
    mozz = onto.MozzarellaTopping()
    redon = onto.RedOnionTopping()

    my_pizza.hasTopping = [garlic, mozz, redon]
    print(my_pizza.hasTopping)

    sync_reasoner()

    print(my_pizza.__class__)
