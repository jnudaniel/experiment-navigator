#! /usr/bin/env python
# Experiment Navigator user interaction script
# Julia Daniel, Akhila Moturu, Eric Cramer, and Gaby Steiner
# Final project for CS 270 / BMI 210, Winter 2018
# ----------------------------------------------------------

import ontology as o
import sys

if __name__ == "__main__":
	print("* ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ *")
	print("Welcome to the Experiment Navigator!")
	print("Loading our cutting-edge experiment ontology...")
	ont = o.build_ontology()
	print("...done!")
	print("The Experiment Navigator is your tool to help find the right experiment for you, given a hypothesis you'd like to test.")
	print("Please enter your hypothesis here, in your own words:")
	hypothesis = input(" > ")
	print(hypothesis)
	print("Great! In order to determine which experiment(s) you should conduct to test this hypothesis, we need to know more about the substances and information involved.")
	molecule = input("What type of molecule are you working with? ")
	if molecule.lower() == "protein":
		typeprotein = input("What do you want to learn about the protein? Please type one of the following: location, structure, interaction, quantification, detection. ")
		if typeprotein.lower() == "location":
			typelocation = input("What type of location are you trying to learn? Static or dynamic? ")
			if typelocation.lower() == "static":
				print("The type of experiment that you want to perform is Fluorescence Resonance Energy Transfer!")
			elif typelocation.lower() == "dynamic":
				print("The type of experiment that you want to perform is Time Lapse!")
		elif typeprotein.lower() == "structure":
			print("The type of experiment that you want to perform is XRay Crystalography!")
		elif typeprotein.lower() == "interaction":
			typeinteraction = input("What type of molecule is the protein interacting with? DNA, RNA, or another protein? ")
			if typeinteraction.lower() == "dna":
				typeproDNA = input("How will you determine interaction points? Micro-array or sequencing? ")
				if typeproDNA.lower() == o.chip_on_chip.attributes["interaction points"]:
					print("The type of experiment that you want to perform is ChIPonChip!")
				elif typeproDNA.lower() == o.chip_sequencing.attributes["interaction points"]:
					print("The type of experiment that you want to perform is Chip Sequencing!")
			elif typeinteraction.lower() == "rna":
				typeproRNA = input("What type of protein RNA sequencing are you trying to do? Fret, TCP Sequencing, or Toe printing assay? ")
				if typeproRNA.lower() == "fret":
					print("The type of experiment that you want to perform is Fret!")
				elif typeproRNA.lower() == "tcp sequencing":
					print("The type of experiment that you want to perform is TCP sequencing!")
				elif typeproRNA.lower() == "toe printing assay":
					print("The type of experiment that you want to perform is Toe printing assay!")
			elif typeinteraction.lower() == "protein":
				typepropro = input("What type of protein protein experiment are you trying to do? Affinity chromatography, Affinity electrophoresis, PFCA, or Fret? ")
				if typepropro.lower() == "fret":
					print("The type of experiment that you want to perform is Fret!")
				elif typepropro.lower() == "affinity chromatography":
					print("The type of experiment that you want to perform is Affinity chromatography!")
				elif typepropro.lower() == "affinity electrophoresis":
					print("The type of experiment that you want to perform is Affinity electrophoresis!")
				elif typepropro.lower() == "pfca":
					print("The type of experiment that you want to perform is PFCA!")
		elif typeprotein.lower() == "quantification":
			typequant = input("What type of quantification are you trying to do? UV Absorbance, BCA assay, Bradford assay, Lowry assay? ")
			if typequant.lower() == "uv absorbance":
				print("The type of experiment that you want to perform is UV Absorbance!")
			elif typequant.lower() == "bca assay":
				print("The type of experiment that you want to perform is BCA assay!")
			elif typequant.lower() == "bradford assay":
				print("The type of experiment that you want to perform is Bradford assay!")
			elif typequant.lower() == "lowry assay":
				print("The type of experiment that you want to perform is Lowry assay!")
		elif typeprotein.lower() == "detection":
			typedet = input("What type of protein detection are you trying to do? Specific or nonspecific? ")
			if typedet.lower() == "specific":
				typespec = input("What type of specific protein detection are you trying to do? ELISA, HPLC, LCMS, or Western Blot? ")
				#ELISA, HPLC, LCMS, or Western Blot
				if typespec.lower() == "elisa":
					print("The type of experiment that you want to perform is ELISA!")
				elif typespec.lower() == "hplc":
					print("The type of experiment that you want to perform is HPLC!")
				elif typespec.lower() == "lcms":
					print("The type of experiment that you want to perform is LCMS!")
				elif typespec.lower() == "western blot":
					print("The type of experiment that you want to perform is Western Blot!")
			elif typedet.lower() == "nonspecific":
				typenonspec = input("What type of nonspecific protein detection are you trying to do? Absorbance, Amido black, BCA assay, Bradford assay, Lowry assay? ")
				#Absorbance, Amido black, BCA assay, Bradford assay, Lowry assay")
				if typenonspec.lower() == "absorbance":
					print("The type of experiment that you want to perform is Absorbance!")
				elif typenonspec.lower() == "amido black":
					print("The type of experiment that you want to perform is Amido Black!")
				elif typenonspec.lower() == "bca assay":
					print("The type of experiment that you want to perform is BCA assay!")
				elif typenonspec.lower() == "bradford assay":
					print("The type of experiment that you want to perform is Bradford assay!")
				elif typenonspec.lower() == "lowry assay":
					print("The type of experiment that you want to perform is Lowry assay!")
	else:
		print("Sorry! We don't have much information on experiments of that molecule.")
	# print ont

	# for substance in ont.substances:
	# 	print substance
