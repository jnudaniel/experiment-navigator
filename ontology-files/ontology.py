# BMI 210/CS 270 Final Project
# Team: Gaby Steiner, Akhila Monturu, Julia Daniel, Eric Cramer
# Ontology files for Python (UML style ontology)

# The following file contains:
# 	1. Class definition for an ontology
# 	2. Class definitions for the ontology
# 	3. Function to build the ontology to be traversed

""" 
To create an ontology using the classes below, run build_ontology(<name of ontology>). The name of the ontology is set in the constructor of the ontology and passed as an argument to build ontology. The ontology may have a root_class and a list of substances for which it contains experiment workflows. The root-class is an experiment object which itself has a list of experiment subtypes. To traverse the ontology, start at the 'Experiment' level and travers the subtype lists until the subtypes = None, at which point you have an experimental proceducre which can become part of a workflow.
"""

#######################################################################################################

""" Class definition for an ontology object """
class ontology():

	def __init__(self, name = "default"):
		self.name = name

	def add_objects(self, root_class):
		self.root_class = root_class

	def set_substances(self, substances):
		self.substances = substances

########################################################################################################
# Define the top level of the ontology 

""" A primary class from which all other classes are derived, similar to owl:thing in Protege """
class Experiment:

	def __init__(self, name="", experiment_type="", subtypes=[], description=""):
		self.subtypes = subtypes
		self.name = name
		self.experiment_type = experiment_type
		self.description = description
		self.attributes = {}

	# member variable to contain attributes
	attributes = {}

	def set_description(self, new_description):
		self.description = new_description

	def set_attributes(self, attributes):
		self.attributes = attributes

############################################################################################################
## Define 2nd level experiments ##

""" A 2nd level class to define a gene based experiment """
class GeneExperiment(Experiment):

	def __init__(self, name = "GeneExperiment"):
		self.name = name

""" A 2nd level class to define a protein based experiment """
class ProteinExperiment(Experiment):

	def __init__(self, name = "ProteinExperiment", subtypes = ["ProteinLocationExperiment", "ProteinStructureExperiment", "ProteinInteractionExperiment", "ProteinQuantificationExperiment", "ProteinDetectionExperiment"], description=""):
		self.name = name

""" A 2nd level class to define a DNA based experiment """
class DNAExperiment(Experiment):

	def __init__(self, name = "DNAExperiment"):
		self.name = name

""" A 2nd level class to define a RNA based experiment """
class RNAExperiment(Experiment):

	def __init__(self, name = "RNAExperiment"):
		self.name = name

####################################################################################################
### Define 3rd level experiments ###

""" A 3rd level class to define a location experiment used to get the location of a protein """
class ProteinLocationExperiment(ProteinExperiment):

	def __init__(self, name = "ProteinExperiment", subtypes = ["StaticLocationExperiment", "DynamicLocatinExperiment"], experiment_type = "ProteinExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.experiment_type = experiment_type

	attributes = {"concept":["location"], "unit type":"distance"}

"""" A 3rd level class to define finding the structure of a protein """
class ProteinStructureExperiment(ProteinExperiment):
	
	def __init__(self, name = "ProteinStructureExperiment", subtypes = ["XRayCrystalography"], experiment_type = "ProteinExperiment", description=""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

	attributes = {"concept":["structure"], "unit type":"distance"}

""" A 3rd level class to define protein interaction experiments """
class ProteinInteractionExperiment(ProteinExperiment):
	
	def __init__(self, name = "ProteinInteractionExperiment", subtypes = [], experiment_type = "ProteinExperiment", description = ""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

		attributes = {"concept":["interaction"], "unit type":"distance"}

""" A 3rd level class to define quantificaiton of protein """
class ProteinQuantificationExperiment(ProteinExperiment):
	
	def __init__(self, name = "ProteinQuantificationExperiment", subtypes = [], experiment_type = "ProteinExperiment", description = ""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

	attributes = {"concept":["quantity"], "unit type":"concentration"}

""" A 3rd level class to define experiments to detect proteins """
class ProteinDetectionExperiment(ProteinExperiment):
	
	def __init__(self, name = "ProteinDetectionExperiment", subtypes = [], experiment_type = "ProteinExperiment", description = ""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

	attributes = {"concept":["detection"]}

#####################################################################################################
#### Define 4th level experiments ####

""" A 4th level class to define the type of protein location experiment """
class StaticProteinLocationExperiment(ProteinLocationExperiment):
	
	def __init__(self, name = "StaticProteinLocationExperiment", subtypes = [], experiment_type = "ProteinLocationExperiment", description = ""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

	attributes = {"tags":"nonspecific", "concept":["location"]}

""" A 4th level class to define the type of protein location experiment """
class DynamicProteinLocatinExperiment(ProteinLocationExperiment):
	
	def __init__(self, name = "DynamicProteinLocatinExperiment", subtypes = [], experiment_type = "ProteinLocationExperiment", description = ""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

	attributes = {"tags":"nonspecific", "concept":["location"]}

# defining kinds of detection experiments
class NonspecificProteinDetectionExperiment(ProteinDetectionExperiment):

	def __init__(self, name = "NonspecificProteinDetectionExperiment", subtypes = [], experiment_type = "ProteinDetectionExperiment", description = ""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

	attributes = {"tags":"nonspecific", "concept":["detection"]}

class SpecificProteinDetectionExperiment(ProteinDetectionExperiment):

	def __init__(self, name = "SpecificProteinDetectionExperiment", subtypes = [], experiment_type = "ProteinDetectionExperiment", description = ""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

	attributes = {"tags":"specific", "concept":"detection"}

# defining protein interaction experiment sub-classes
class ProteinDNAInteractionExperiment(ProteinInteractionExperiment):

	def __init__(self, name = "ProteinDNAInteractionExperiment", subtypes = [], experiment_type = "ProteinInteractionExperiment", description = ""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

	attributes = {"immunoprecipitation":True, "interaction points":"", "concept":["interaction"]}

class ProteinRNAInteractionExperiment(ProteinInteractionExperiment):

	def __init__(self, name = "ProteinInteractionExperiment", subtypes = [], experiment_type = "ProteinInteractionExperiment", description = ""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

	attributes = {"concept":["interaction"]}

class ProteinProteinInteractionExperiment(ProteinInteractionExperiment):

	def __init__(self, name = "ProteinProteinInteractionExperiment", subtypes = [], experiment_type = "ProteinInteractionExperiment", description = ""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

	attributes = {"concept":["interaction"]}

#####################################################################################################
##### Define 5th level experiments #####

# defining protein location terminal experiments
class FluorescenceResonanceEnergyTransfer(StaticProteinLocationExperiment):

	def __init__(self, name = "FluorescenceResonanceEnergyTransfer", subtypes = None, experiment_type = "StaticProteinLocationExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.experiment_type = experiment_type
		self.attributes["units"] = ["nm"] 
		self.attributes["tags"] = ["fluorescence", "dye"]
		self.attributes["unit type"] = ["distance", "luminence"]
		self.description = "https://en.wikipedia.org/wiki/Forster_resonance_energy_transfer"

class TimeLapse(DynamicProteinLocatinExperiment):

	def __init__(self, name = "TimeLapse", subtypes = None, experiment_type = "DynamicProteinLocatinExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.experiment_type = experiment_type
		self.attributes["units"] = ["seconds", "nm"]
		self.attributes["tags"] = ["imaging", "dye", "fluorescence"]
		self.description = "https://en.wikipedia.org/wiki/Time-lapse_microscopy"

""" A 5th level method to define experiment that identifies protein structure. This is a terminal node. """
class XRayCrystalography(ProteinStructureExperiment):
	
	def __init__(self, name="XRayCrystalography", subtypes = None, experiment_type="ProteinStructureExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.experiment_type = experiment_type
		self.attributes["units"] = ["nl", "kw", "angstroms"]
		self.description = "https://en.wikipedia.org/wiki/X-ray_crystallography"


# defining terminal nonspecific protein detection experiments
class Absorbance(NonspecificProteinDetectionExperiment):

	def __init__(self, name = "Absorbance", subtypes = None, experiment_type = "NonspecificProteinDetectionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = "https://www.thermofisher.com/us/en/home/life-science/protein-biology/protein-biology-learning-center/protein-biology-resource-library/pierce-protein-methods/overview-protein-assays.html"
		self.experiment_type = experiment_type
		self.attributes["units"] = ["nm"]

class AmidoBlack(NonspecificProteinDetectionExperiment):

	def __init__(self, name = "AmidoBlack", subtypes = None, experiment_type = "NonspecificProteinDetectionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.experiment_type = experiment_type
		self.description = "https://en.wikipedia.org/wiki/Amido_black_10B"
		self.attributes["tags"] = ["dye"]

class BCAAssay(NonspecificProteinDetectionExperiment, ProteinQuantificationExperiment):

	def __init__(self, name = "BCAAssay", subtypes = None, experiment_type = ["NonspecificProteinDetectionExperiment", "ProteinQuantificationExperiment"]):
		self.name = name
		self.subtypes = subtypes
		self.experiment_type = experiment_type
		self.attributes = {"units":["ug/ml", "mg/ml", "Molar", "nm"], "minimum concentration":"0.5 ug/ml", "maximum concentration":"1.5 mg/ml", "reagents":["bicinconinic acid", "naco3", "nahco3", "sodium tartrate"], "tags":["dye"]}
		self.attributes["units"] = ["ug/ml", "mg/ml", "Molar", "nm"]
		self.attributes["minimum concentration"] = 0.5
		self.attributes["maximum concentration"] = 1.5
		self.attributes["reagents"] = ["Bicinconinic acid", "NaCO3", "NaHCO3", "Sodium tartrate"]
		self.attributes["tags"] = ["dye"]
		self.attributes["relative uniformity"] = "high"
		self.attributes["variation coefficient"] = 14.7
		self.attributes["standard deviation"] = 0.15
		self.attributes["average ratio"] = 1.02
		self.description = "https://en.wikipedia.org/wiki/Bicinchoninic_acid_assay"

class BradfordAssay(NonspecificProteinDetectionExperiment, ProteinQuantificationExperiment):

	def __init__(self, name = "BradfordAssay", subtypes = None, experiment_type = ["NonspecificProteinDetectionExperiment", "ProteinQuantificationExperiment"]):
		self.name = name
		self.subtypes = subtypes
		self.experiment_type = experiment_type
		self.description = "https://en.wikipedia.org/wiki/Bradford_protein_assay"
		self.attributes["units"] = ["ug/ml", "Molar", "nm"]
		self.attributes["minimum concentration"] = 200
		self.attributes["maximum concentration"] = 1500
		self.attributes["reagents"] = ["NaCl"]
		self.attributes["tags"] = ["dye"]
		self.attributes["relative uniformity"] = "low"
		self.attributes["variation coefficient"] = 38.2
		self.attributes["standard deviation"] = 0.26
		self.attributes["average ratio"] = 0.68
		self.attributes["cost"] = 72

class LowryAssay(NonspecificProteinDetectionExperiment, ProteinQuantificationExperiment):

	def __init__(self, name = "LowryAssay", subtypes = None, description = "", experiment_type = ["NonspecificProteinDetectionExperiment", "ProteinQuantificationExperiment"]):
		self.name = name
		self.subtypes = subtypes
		self.experiment_type = experiment_type
		self.description = "https://en.wikipedia.org/wiki/Lowry_protein_assay"
		self.attributes = {"reagents":["folin-ciocalteu", "cu+", "al"], "units":["ug/ml", "Molar", "nm"]}
		self.attributes["reagents"] = ["folin-ciocalteu", "cu+", "al"]
		self.attributes["units"] = ["ug/ml", "Molar", "nm"]
		self.attributes["relative uniformity"] = "high"
		self.attributes["variation coefficient"] = 11.9
		self.attributes["standard deviation"] = 0.13
		self.attributes["average ratio"] = 1.09

# defining terminal specific detection experiments
class ELISA(SpecificProteinDetectionExperiment):

	def __init__(self, name = "ELISA", subtypes = None, experiment_type = "SpecificProteinDetectionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.experiment_type = experiment_type
		self.description = "https://www.thermofisher.com/us/en/home/life-science/protein-biology/protein-biology-learning-center/protein-biology-resource-library/pierce-protein-methods/overview-elisa.html"
		self.attributes["subtypes"] = ["direct", "indirect", "capture"]
		self.attributes["reagents"] = ["antibody"]
		self.attributes["sensitivity"] = 5
		self.attributes["units"] = ["pg/ml"]
		self.attributes["minimum"] = 7.8
		self.attributes["maximum"] = 500
		self.attributes["unit type"] = ["concentration"]

class HPLC(SpecificProteinDetectionExperiment):

	def __init__(self, name = "HPLC", subtypes = None, experiment_type = "SpecificProteinDetectionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = "https://www.chemguide.co.uk/analysis/chromatography/hplc.html"
		self.experiment_type = experiment_type
		self.attributes["units"] = ["mm"]
		self.attributes["unit_type"] = ["distance"]
		self.attributes["minimum"] = 0
		self.attributes["maximum"] = 250
		self.attributes["cost"] = 352

class LCMS(SpecificProteinDetectionExperiment):

	def __init__(self, name = "LCMS", subtypes = None, experiment_type = "SpecificProteinDetectionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = "https://en.wikipedia.org/wiki/Liquid_chromatography-mass_spectrometry"
		self.experiment_type = experiment_type
		self.attributes["units"] = ["mm", "nm"]
		self.attributes["unit type"] = ["distance","mass"]
		self.attributes["minimum distance"] = 0
		self.attributes["maximum distance"] = 250
		self.attributes["cost"] = 382

class WesternBlot(SpecificProteinDetectionExperiment):

	def __init__(self, name = "WesternBlot", subtypes = None, experiment_type = "SpecificProteinDetectionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3456489/"
		self.experiment_type = experiment_type
		self.attributes["unit type"] = ["concentration", "distance", "mass"]
		self.attributes["units"] = ["m","mm", "mg", "ug/ml"]
		self.attributes["reagents"] = ["antibody", "nacl", "kcl", "base", "acid", "h2o"]
		self.attributes["cost"] = 160

# defining terminal protein quantification experiments
class UVAbsorbance(ProteinQuantificationExperiment):

	def __init__(self, name = "UVAbsorbance", subtypes = None, description = "", experiment_type = "ProteinQuantificationExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type
		self.attributes["wavelength"] = 280
		self.attributes["units"] = ["nm"]
		self.attributes["unit type"] = ["luminence"]

# defining terminal protein interaction experiments
class ChIPonChip(ProteinDNAInteractionExperiment):

	def __init__(self, name = "ChIPonChip", subtypes = None, description = "", experiment_type = "ProteinDNAInteractionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type
		self.attributes["interaction points"] = "micro-array"

class ChipSequencing(ProteinDNAInteractionExperiment):

	def __init__(self, name = "ChipSequencing", subtypes = None, description = "", experiment_type = "ProteinDNAInteractionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type
		self.attributes["interaction points"] = "sequencing"

class FRET(ProteinRNAInteractionExperiment):

	def __init__(self, name = "FRET", subtypes = None, experiment_type = ["ProteinRNAInteractionExperiment", "ProteinProteinInteractionExperiment"]):
		self.name = name
		self.subtypes = subtypes
		self.description = "https://www.biotek.com/resources/white-papers/an-introduction-to-fluorescence-resonance-energy-transfer-fret-technology-and-its-application-in-bioscience/"
		self.experiment_type = experiment_type
		self.attributes["units"] = ["angstroms", "nm"]
		self.attributes["unit type"] = ["weight", "distance"]


class TCPseq(ProteinRNAInteractionExperiment):

	def __init__(self, name = "TCPseq", subtypes = None, description = "", experiment_type = "ProteinRNAInteractionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = "https://en.wikipedia.org/wiki/TCP-seq"
		self.experiment_type = experiment_type
		self.attributes["concept"] = ["sequencing"]
		self.attributes["sensitivity"] = "high"

class ToeprintingAssay(ProteinRNAInteractionExperiment):

	def __init__(self, name = "ToeprintingAssay", subtypes = None, experiment_type = "ProteinRNAInteractionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = "https://en.wikipedia.org/wiki/Toeprinting_assay"
		self.experiment_type = experiment_type
		self.attributes["unit type"] = ["concentration"]
		self.attributes["reagents"] = ["mrna", "ribosomes","dna primer","nucleotides","reverse transcriptase"]

class AffinitiyChromatography(ProteinProteinInteractionExperiment):

	def __init__(self, name = "AffinitiyChromatography", subtypes = None, experiment_type = "ProteinProteinInteractionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = "https://en.wikipedia.org/wiki/Affinity_chromatography"
		self.experiment_type = experiment_type
		self.attributes["reagents"] = ["antigen", "antibody", "enzyme", "substrate"]
		self.attributes["tags"] = ["purification", "separation"]
		self.attributes["unit type"] = ["distance"]
		self.attributes["concept"].append("affinity")

class AffinityElectrophoresis(ProteinProteinInteractionExperiment):

	def __init__(self, name = "AffinityElectrophoresis", subtypes = None, experiment_type = "ProteinInteractionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = "https://en.wikipedia.org/wiki/Affinity_electrophoresis"
		self.experiment_type = experiment_type
		self.attributes["unit type"] = "distance"
		self.attributes["tags"] = ["gel"]
		self.attributes["units"] = ["nm", "mm"]
		self.attributes["reagents"] = ["buffer"]
		self.attributes["concept"].append("affinity")

class ProteinFragmentComplementationAssay(ProteinProteinInteractionExperiment):

	def __init__(self, name = "ProteinFragmentComplementationAssay", subtypes = None, experiment_type = "ProteinProteinInteractionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = "https://en.wikipedia.org/wiki/Protein-fragment_complementation_assay"
		self.experiment_type = experiment_type
		self.attributes["unit type"] = ["luminence", "distance"]
		self.attributes["units"] = ["nm"]
		self.attributes["tags"] = ["bait", "prey", "reporter", "proteomics"]
		self.attributes["concept"].append("complementation")


######################################################################################################

""" Function to build a ontology object """
def build_ontology(onto_name = "default_ontology"):
	onto = ontology(onto_name)
	onto.set_substances(["protein", "gene", "dna", "rna", "guacamole"])

	# init classes in reverse order, starting from the leaves

	# adding protein structure objects
	XrayCrystal = XRayCrystalography()
	PSE = ProteinStructureExperiment(subtypes = [XrayCrystal])

	# adding protein detection objects
	absorbance = Absorbance()
	amido_black = AmidoBlack()
	bca_assay = BCAAssay()
	bradford_assay = BradfordAssay()
	lowry_assay = LowryAssay()
	NPDE = NonspecificProteinDetectionExperiment(subtypes = [absorbance, amido_black, bca_assay, bradford_assay, lowry_assay])
	elisa = ELISA()
	hplc = HPLC()
	lcms = LCMS()
	western_blot = WesternBlot()
	SPDE = SpecificProteinDetectionExperiment(subtypes = [elisa, hplc, lcms, western_blot])
	PDE = ProteinDetectionExperiment(subtypes = [NPDE, SPDE])

	# adding protein quantification objects
	uv_absorbance = UVAbsorbance()
	PQE = ProteinQuantificationExperiment(subtypes = [uv_absorbance, bca_assay, bradford_assay, lowry_assay])

	# adding protein interaction objects
	chip_on_chip = ChIPonChip()
	chip_sequencing = ChipSequencing()
	PDIE = ProteinDNAInteractionExperiment(subtypes = [chip_on_chip, chip_sequencing])
	affinity_chrom = AffinitiyChromatography()
	affinity_electro = AffinityElectrophoresis()
	pfca = ProteinFragmentComplementationAssay()
	fret = FRET()
	PPIE = ProteinProteinInteractionExperiment(subtypes = [affinity_chrom, affinity_electro, pfca, fret])
	tcp_seq = TCPseq()
	toeprinting_assay = ToeprintingAssay()
	PRIE = ProteinRNAInteractionExperiment(subtypes = [fret, tcp_seq, toeprinting_assay])
	PIE = ProteinInteractionExperiment(subtypes = [PDIE, PPIE, PRIE])

	# adding protein location experiment objects
	flourescence_resonance_energy_transfer = FluorescenceResonanceEnergyTransfer()
	time_lapse = TimeLapse()
	SPLE = StaticProteinLocationExperiment(subtypes = [flourescence_resonance_energy_transfer])
	DPLE = DynamicProteinLocatinExperiment(subtypes = [time_lapse])
	PLE = ProteinLocationExperiment(subtypes = [SPLE, DPLE])

	# declaring experiment sub-types
	GE = GeneExperiment()#subtypes = [])#, description = "Experiment that revolves around jeans")
	PE = ProteinExperiment(subtypes = [PSE, PDE, PQE, PIE, PLE])
	
	# adding experiment types to experiment

	E = Experiment(subtypes = [PE])
	onto.add_objects(E)
	return onto