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
				if typeproDNA.lower() == "micro-array":
					print("The type of experiment that you want to perform is Chip on Chip!")
				elif typeproDNA.lower() == "sequencing":
					print("The type of experiment that you want to perform is Chip Sequencing!")
			#DONE WITH DNARNA INTERACTION
			elif typeinteraction.lower() == "rna":
				typereag = input("Do you know what reagants you will be using for the experiment? ")
				if typereag.lower() == "no":
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
			#DONE WITH PROTEINPROTEIN INTERACTION#
			elif typeinteraction.lower() == "protein":
				typedata = input("What type of unit are you looking for output? luminescence or distance")
				if typedata.lower() == "luminescence":
					print("The type of experiment that you want to perform is Protein Fragment Complementation Assay!")
				elif typedata.lower() == "distance":
					reag = input("Which of the following reagents will you be using? antigen, antibody, enzyme, substrate, buffer, bait, prey, reporter? ")
					# if reag.lower() in o.AffinitiyChromatography.attributes["reagents"]:
					if reag.lower() == "antigen" or reag.lower() == "antibody" or reag.lower() == "enzyme" or reag.lower() == "substrate":
						print("The type of experiment that you want to perform is Affinity Chromatography!")
					# elif reag.lower() in o.AffinityElectrophoresis.attributes["reagents"]:
					elif reag.lower() == "buffer":
						print("The type of experiment that you want to perform is Affinity Electrophoresis!")
					# elif reag.lower() in o.ProteinFragmentComplementationAssay.attributes["reagents"]:
					elif reag.lower() == "bait" or reag.lower() == "prey" or reag.lower() == "reporter":
						print("The type of experiment that you want to perform is Protein Fragment Complementation Assay!")
				else:
					print("Hmmmm, we don't seem to have a protein protein interaction experiment that measures %s"%typedata.lower())
		elif typeprotein.lower() == "quantification":
			lum = input("Are you looking to use luminence? ")
			if lum.lower() == "yes":
				print("The type of experiment that you want to perform is UV Absorbance!")
			else:
				uniform = input("Do you want high or low relative uniformity? ")
				if uniform.lower() == "high":
					reag = input("Which of the following reagents will you be using? folin-ciocalteu, cu+, al, bicinconinic acid, naco3, nahco3, sodium tartrate? ")
					#NOT WORKING ~~ONCE THIS WORKS IT WILL BE DONE~~
					# print(o.LowryAssay.attributes["reagents"])
					# if reag.lower() in o.LowryAssay.attributes.get("reagents"):
					if reag.lower() == "folin-ciocalteu" or reag.lower() == "cu+" or reag.lower() == "al":
						print("The type of experiment that you want to perform is Lowry assay!")
					# elif reag.lower() in o.BCAAssay.attributes.get("reagents"):
					elif reag.lower() == "bicinconinic acid" or reag.lower() == "naco3" or reag.lower() == "nahco3" or reag.lower() == "sodium tartrate":
						print("The type of experiment that you want to perform is BCA assay!")
					else:
						print("We don't have an experiment type in our ontology that fits your constraints. Sorry!")
				elif uniform.lower() == "low":
					print("The type of experiment that you want to perform is Bradford assay!")
		elif typeprotein.lower() == "detection":
			typedet = input("What type of protein detection are you trying to do? Specific or nonspecific? ")
			#DONE WITH SPECIFIC DETECTION
			if typedet.lower() == "specific":
				# typespec = input("What type of specific protein detection are you trying to do? ELISA, HPLC, LCMS, or Western Blot? ")
				#ELISA, HPLC, LCMS, or Western Blot
				typeunit = input("What type of unit are you looking for output? concentration, mass, or distance? ")
				if typeunit.lower() == "concentration":
					#narrowed down to ELISA and WESTERNBLOT
					print(o.ELISA.attributes["units"])

					unit = input("What units would you like to measure the concentration in? pg/ml or ug/ml? ")
					# print(o.WesternBlot.attributes["units"])
					# if unit.lower() in o.ELISA.attributes["units"]:
					if unit.lower() == "pg/ml":
						print("The type of experiment that you want to perform is ELISA!")
					# elif unit.lower() in o.WesternBlot.attributes["units"]:
					elif unit.lower() == "ug/ml":
						print("The type of experiment that you want to perform is Western Blot!")
					else:
						print("We don't have an experiment type in our ontology that fits your constraints. Sorry!")
				if typeunit.lower() == "mass":
					#narrowed down to LCMS and WesternBlot
					cost = input("What cost are you trying to stay under? ")
					if int(cost)>382:
						print("The type of experiment that you want to perform is LCMS!")
					elif int(cost)>160:
						print("The type of experiment that you want to perform is Western Blot!")
					else:
						print("We don't have an experiment type in our ontology that fits your constraints. Sorry!")
				if typeunit.lower() == "distance":
					#narrowed down to WesternBlot and HPLC
					cost = input("What cost are you trying to stay under? ")
					if int(cost)>352:
						print("The type of experiment that you want to perform is HPLC!")
					elif int(cost)>160:
						print("The type of experiment that you want to perform is Western Blot!")
					else:
						print("We don't have an experiment type in our ontology that fits your constraints. Sorry!")
			#DONE WITH NONSPECIFIC DETECTION
			elif typedet.lower() == "nonspecific":
				# pass
				cost = input("What cost range are you operating in? ")
				if cost.lower() == "low":
					#narrowed down to Lowry and Absorbance
					dye = input("Are you using dye? ")
					if dye.lower() == "yes":
						print("The type of experiment that you want to perform is Absorbance!")
					elif dye.lower() == "no":
						print("The type of experiment that you want to perform is Lowry assay!")
				elif cost.lower() == "med":
					#then narrowed to BCA and Bradford
					uniform = input("Do you want high or low relative uniformity? ")
					if uniform.lower() == "high":
						print("The type of experiment that you want to perform is BCA assay!")
					elif uniform.lower() == "low":
						print("The type of experiment that you want to perform is Bradford assay!")
				elif cost.lower() == "high":
					print("The type of experiment that you want to perform is Amido Black!")
	elif molecule.lower() == "rna":
		print("We don't have much information on experiments of that molecule. We can only tell that the experiment is an RNA Experiment.")
	elif molecule.lower() == "dna":
		print("We don't have much information on experiments of that molecule. We can only tell that the experiment is a DNA Experiment.")
	elif molecule.lower() == "gene":
		print("We don't have much information on experiments of that molecule. We can only tell that the experiment is a Gene Experiment.")		
	else:
		print("Sorry! We don't have any information on experiments of that molecule.")
