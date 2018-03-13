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
	# print(hypothesis)
	print("Great! In order to determine which experiment(s) you should conduct to test this hypothesis, we need to know more about the substances and information involved.")
	molecule = input("What type of molecule are you working with? ")
	if molecule.lower() == "protein":
		typeprotein = input("What do you want to learn about the protein? Please type one of the following: location, structure, interaction, quantification, detection. ")
		#DONE WITH LOCATION
		if typeprotein.lower() == "location":
			typelocation = input("Will you be determining location over time or at one point in time? ")
			if typelocation.lower() == "one point in time":
				print("The type of experiment that you want to perform is Fluorescence Resonance Energy Transfer!")
			elif typelocation.lower() == "over time":
				print("The type of experiment that you want to perform is Time Lapse!")
		#done with structure
		elif typeprotein.lower() == "structure":
			print("The type of experiment that you want to perform is XRay Crystalography!")
		elif typeprotein.lower() == "interaction":
			typeinteraction = input("What type of molecule is the protein interacting with? DNA, RNA, or another protein? ")
			#DONE WITH DNADNA INTERACTION
			if typeinteraction.lower() == "dna":
				typeproDNA = input("How will you determine interaction points? Micro-array or sequencing? ")
				if typeproDNA.lower() == o.ChIPonChip.attributes["interaction points"]:
					print("The type of experiment that you want to perform is Chip on Chip!")
				elif typeproDNA.lower() == o.ChIPonChip.attributes["interaction points"]:
					print("The type of experiment that you want to perform is Chip Sequencing!")
			#DONE WITH DNARNA INTERACTION
			elif typeinteraction.lower() == "rna":
				typereag = input("Do you know what reagants you will be using for the experiment? ")
				if typereag.lower() == "no":
					#we have narrowed it down to 
					sensi = input("Do you need high sensitivity? ")
					if sensi.lower() == "yes":
						print("The type of experiment that you want to perform is TCP sequencing!")
					else:
						print("The type of experiment that you want to perform is FRET!")
				if typereag.lower() == "yes":
					#we have narrowed down to toe printing
					istoe = input("Are any of the reagants mrna, ribosomes, dna primer, nucleotides, reverse transcriptase? ")
					if istoe.lower() == "yes":
						print("The type of experiment that you want to perform is Toe printing assay!")
			#~~~~~~NEED TO FINISH THIS~~~~~~~#
			elif typeinteraction.lower() == "protein":
				typedata = input("What type of unit are you looking for output?" )
				if typedata.lower() == "luminence":
					print("The type of experiment that you want to perform is Protein Fragment Complementation Assay!")
				elif typedata.lower() == "distance":
					#NEED TO ADD SOMETHING HERE
					pass
				else:
					print("Hmmmm, we don't seem to have a protein protein interaction experiment that measures %s"%typedata.lower())
				# typepropro = input("What type of protein protein experiment are you trying to do? Affinity chromatography, Affinity electrophoresis, PFCA, or Fret? ")
				# elif typepropro.lower() == "affinity chromatography":
				# 	print("The type of experiment that you want to perform is Affinity chromatography!")
				# elif typepropro.lower() == "affinity electrophoresis":
				# 	print("The type of experiment that you want to perform is Affinity electrophoresis!")
				# elif typepropro.lower() == "pfca":
				# 	print("The type of experiment that you want to perform is PFCA!")
		elif typeprotein.lower() == "quantification":
			lum = input("Are you looking to use luminence? ")
			if lum.lower() == "yes":
				print("The type of experiment that you want to perform is UV Absorbance!")
			else:
				uniform = input("Do you want high or low relative uniformity? ")
				if uniform.lower() == "high":
					reag = input("What reagants are you using? ")
					#NOT WORKING ~~ONCE THIS WORKS IT WILL BE DONE~~
					if reag.lower() in o.LowryAssay.attributes.get("reagents"):
						print("The type of experiment that you want to perform is Lowry assay!")
					if reag.lower() in o.BCAAssay.attributes.get("reagents"):
						print("The type of experiment that you want to perform is BCA assay!")
				elif uniform.lower() == "low":
					print("The type of experiment that you want to perform is Bradford assay!")
		elif typeprotein.lower() == "detection":
			typedet = input("What type of protein detection are you trying to do? Specific or nonspecific? ")
			if typedet.lower() == "specific":
				# typespec = input("What type of specific protein detection are you trying to do? ELISA, HPLC, LCMS, or Western Blot? ")
				#ELISA, HPLC, LCMS, or Western Blot
				typeunit = input("What type of unit are you looking for output? ")
				if typeunit.lower() == "concentration":
					#narrowed down to ELISA and WESTERNBLOT
				if typeunit.lower() == "mass":
					#narrowed down to LCMS and WesternBlot
				if typeunit.lower() == "distance":
					#narrowed down to WesternBlot and HPLC
				# if typespec.lower() == "elisa":
				# 	print("The type of experiment that you want to perform is ELISA!")
				# elif typespec.lower() == "hplc":
				# 	print("The type of experiment that you want to perform is HPLC!")
				# elif typespec.lower() == "lcms":
				# 	print("The type of experiment that you want to perform is LCMS!")
				# elif typespec.lower() == "western blot":
				# 	print("The type of experiment that you want to perform is Western Blot!")
			elif typedet.lower() == "nonspecific":
				# typenonspec = input("What type of nonspecific protein detection are you trying to do? Absorbance, Amido black, BCA assay, Bradford assay, Lowry assay? ")
				# #Absorbance, Amido black, BCA assay, Bradford assay, Lowry assay")
				# if typenonspec.lower() == "absorbance":
				# 	print("The type of experiment that you want to perform is Absorbance!")
				# elif typenonspec.lower() == "amido black":
				# 	print("The type of experiment that you want to perform is Amido Black!")
				# elif typenonspec.lower() == "bca assay":
				# 	print("The type of experiment that you want to perform is BCA assay!")
				# elif typenonspec.lower() == "bradford assay":
				# 	print("The type of experiment that you want to perform is Bradford assay!")
				# elif typenonspec.lower() == "lowry assay":
				# 	print("The type of experiment that you want to perform is Lowry assay!")
	elif molecule.lower() == "rna":
		print("We don't have much information on experiments of that molecule. We can only tell that the experiment is an RNA Experiment.")
	elif molecule.lower() == "dna":
		print("We don't have much information on experiments of that molecule. We can only tell that the experiment is a DNA Experiment.")
	elif molecule.lower() == "gene":
		print("We don't have much information on experiments of that molecule. We can only tell that the experiment is a Gene Experiment.")		
	else:
		print("Sorry! We don't have any information on experiments of that molecule.")
	# print ont

	# for substance in ont.substances:
	# 	print substance
