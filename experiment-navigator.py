#! /usr/bin/env python
# Experiment Navigator user interaction script
# Julia Daniel, Akhila Moturu, Eric Cramer, and Gaby Steiner
# Final project for CS 270 / BMI 210, Winter 2018
# ----------------------------------------------------------

from owlready2 import *
onto = get_ontology("file://pizza.owl").load()

if __name__ == "__main__":
    print("hello")
    my_pizza = onto.NamedPizza()
    mozz = onto.MozzarellaTopping()

    #my_pizza.hasTopping = [mozz, onto.TomatoTopping()]
    my_pizza.hasTopping.only([mozz, onto.TomatoTopping()])
    print("should print:")
    print(my_pizza)
    print(my_pizza.hasTopping)
    print("Should have printed")

    list(onto.classes())

    #close_world(my_pizza)

    sync_reasoner()

    print("done. class is:")
    print(my_pizza.__class__)
