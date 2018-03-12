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

	def set_description(self, new_description):
		self.description = new_description

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

	def __init__(self, name = "ProteinExperiment", subtypes = ["StaticLocationExperiment", "DynamicLocatinExperiment"]):
		self.name = name
		self.subtypes = subtypes

"""" A 3rd level class to define finding the structure of a protein """
class ProteinStructureExperiment(ProteinExperiment):
	
	def __init__(self, name = "ProteinStructureExperiment", subtypes = ["XRayCrystalography"], experiment_type = "ProteinExperiment", description=""):
		self.name = name
		self.subtypes = subtypes

""" A 3rd level class to define protein interaction experiments """
class ProteinInteractionExperiment(ProteinExperiment):
	
	def __init__(self, name = "ProteinInteractionExperiment", subtypes = []):
		self.name = name
		self.subtypes = subtypes

""" A 3rd level class to define quantificaiton of protein """
class ProteinQuantificationExperiment(ProteinExperiment):
	
	def __init__(self, name = "ProteinQuantificationExperiment", subtypes = []):
		self.name = name
		self.subtypes = subtypes

""" A 3rd level class to define experiments to detect proteins """
class ProteinDetectionExperiment(ProteinExperiment):
	
	def __init__(self, name = "ProteinDetectionExperiment", subtypes = []):
		self.name = name
		self.subtypes = subtypes

#####################################################################################################
#### Define 4th level experiments ####

""" A 4th level class to define the type of protein location experiment """
class StaticProteinLocationExperiment(ProteinLocationExperiment):
	
	def __init__(self, name = "StaticProteinLocationExperiment", subtypes = []):
		self.name = name
		self.subtypes = subtypes

""" A 4th level class to define the type of protein location experiment """
class DynamicProteinLocatinExperiment(ProteinLocationExperiment):
	
	def __init__(self, name = "DynamicProteinLocatinExperiment", subtypes = []):
		self.name = name
		self.subtypes = subtypes

# defining kinds of detection experiments
class NonspecificProteinDetectionExperiment(ProteinDetectionExperiment):

	def __init__(self, name = "NonspecificProteinDetectionExperiment", subtypes = []):
		self.name = name
		self.subtypes

class SpecificProteinDetectionExperiment(ProteinDetectionExperiment):

	def __init__(self, name = "SpecificProteinDetectionExperiment", subtypes = []):
		self.name = name
		self.subtypes = subtypes

# defining protein interaction experiment sub-classes
class ProteinDNAInteractionExperiment(ProteinInteractionExperiment):

	def __init__(self, name = "ProteinDNAInteractionExperiment", subtypes = []):
		self.name = name
		self.subtypes = subtypes

class ProteinRNAInteractionExperiment(ProteinInteractionExperiment):

	def __init__(self, name = "ProteinInteractionExperiment", subtypes = []):
		self.name = name
		self.subtypes = subtypes

class ProteinProteinInteractionExperiment(ProteinInteractionExperiment):

	def __init__(self, name = "ProteinProteinInteractionExperiment", subtypes = []):
		self.name = name
		self.subtypes = subtypes

#####################################################################################################
##### Define 5th level experiments #####

# defining protein location terminal experiments
class FluorescenceResonanceEnergyTransfer(StaticProteinLocationExperiment):

	def __init__(self, name = "FluorescenceResonanceEnergyTransfer", subtypes = None, description = "", experiment_type = "StaticProteinLocationExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

class TimeLapse(DynamicProteinLocatinExperiment):

	def __init__(self, name = "DynamicProteinLocatinExperiment", subtypes = None, description = "", experiment_type = "DynamicProteinLocatinExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

""" A 5th level method to define experiment that identifies protein structure. This is a terminal node. """
class XRayCrystalography(ProteinStructureExperiment):
	
	def __init__(self, name="XRayCrystalography", subtypes = None, description="", experiment_type="ProteinStructureExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

# defining terminal nonspecific protein detection experiments
class Absorbance(NonspecificProteinDetectionExperiment):

	def __init__(self, name = "Absorbance", subtypes = None, description = "", experiment_type = "NonspecificProteinDetectionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

class AmidoBlack(NonspecificProteinDetectionExperiment):

	def __init__(self, name = "AmidoBlack", subtypes = None, description = "", experiment_type = "NonspecificProteinDetectionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

class BCAAssay(NonspecificProteinDetectionExperiment, ProteinQuantificationExperiment):

	def __init__(self, name = "BCAAssay", subtypes = None, description = "", experiment_type = ["NonspecificProteinDetectionExperiment", "ProteinQuantificationExperiment"]):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

class BradfordAssay(NonspecificProteinDetectionExperiment, ProteinQuantificationExperiment):

	def __init__(self, name = "BradfordAssay", subtypes = None, description = "", experiment_type = ["NonspecificProteinDetectionExperiment", "ProteinQuantificationExperiment"]):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

class LowryAssay(NonspecificProteinDetectionExperiment, ProteinQuantificationExperiment):

	def __init__(self, name = "LowryAssay", subtypes = None, description = "", experiment_type = ["NonspecificProteinDetectionExperiment", "ProteinQuantificationExperiment"]):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

# defining terminal specific detection experiments
class ELISA(SpecificProteinDetectionExperiment):

	def __init__(self, name = "ELISA", subtypes = None, description = "", experiment_type = "SpecificProteinDetectionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

class HPLC(SpecificProteinDetectionExperiment):

	def __init__(self, name = "HPLC", subtypes = None, description = "", experiment_type = "SpecificProteinDetectionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

class LCMS(SpecificProteinDetectionExperiment):

	def __init__(self, name = "LCMS", subtypes = None, description = "", experiment_type = "SpecificProteinDetectionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

class WesternBlot(SpecificProteinDetectionExperiment):

	def __init__(self, name = "WesternBlot", subtypes = None, description = "", experiment_type = "SpecificProteinDetectionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

# defining terminal protein quantification experiments
class UVAbsorbance(ProteinQuantificationExperiment):

	def __init__(self, name = "UVAbsorbance", subtypes = None, description = "", experiment_type = "ProteinQuantificationExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

# defining terminal protein interaction experiments
class ChIPonChip(ProteinDNAInteractionExperiment):

	def __init__(self, name = "ChIPonChip", subtypes = None, description = "", experiment_type = "ProteinDNAInteractionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

class ChipSequencing(ProteinDNAInteractionExperiment):

	def __init__(self, name = "ChipSequencing", subtypes = None, description = "", experiment_type = "ProteinDNAInteractionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

class FRET(ProteinRNAInteractionExperiment):

	def __init__(self, name = "FRET", subtypes = None, description = "", experiment_type = ["ProteinRNAInteractionExperiment", "ProteinProteinInteractionExperiment"]):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

class TCPseq(ProteinRNAInteractionExperiment):

	def __init__(self, name = "TCPseq", subtypes = None, description = "", experiment_type = "ProteinRNAInteractionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

class ToeprintingAssay(ProteinRNAInteractionExperiment):

	def __init__(self, name = "ToeprintingAssay", subtypes = None, description = "", experiment_type = "ProteinRNAInteractionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

class AffinitiyChromatography(ProteinProteinInteractionExperiment):

	def __init__(self, name = "AffinitiyChromatography", subtypes = None, description = "", experiment_type = "ProteinProteinInteractionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

class AffinityElectrophoresis(ProteinProteinInteractionExperiment):

	def __init__(self, name = "AffinityElectrophoresis", subtypes = None, description = "", experiment_type = "ProteinInteractionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

class ProteinFragmentComplementationAssay(ProteinProteinInteractionExperiment):

	def __init__(self, name = "ProteinFragmentComplementationAssay", subtypes = None, description = "", experiment_type = "ProteinProteinInteractionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

######################################################################################################

""" Function to build a ontology object """
def build_ontology(onto_name = "default_ontology"):
	onto = ontology(onto_name)
	onto.set_substances(["protein", "gene", "dna", "rna", "guacamole"])

	# init classes in reverse order, starting from the leaves

	# adding protein structure objects
	XrayCrystal = XRayCrystalography("https://en.wikibooks.org/wiki/Structural_Biochemistry/Proteins/X-ray_Crystallography")
	PSE = ProteinStructureExperiment(subtypes = [XrayCrystal], description = "Experiment to determine a protein's structure.")

	# adding protein detection objects
	absorbance = Absorbance()
	amido_black = AmidoBlack()
	bca_assay = BCAAssay()
	bradford_assay = BradfordAssay()
	lowry_assay = LowryAssay()
	NPDE = NonspecificProteinDetectionExperiment(subtypes = [absorbance, amido_black, bca_assay, bradford_assay, lowry_assay], description = "Nonspecific ways of detecting a protein.")
	elisa = ELISA()
	hplc = HPLC()
	lcms = LCMS()
	western_blot = WesternBlot()
	SPDE = SpecificProteinDetectionExperiment(subtypes = [elisa, hplc, lcms, western_blot], description = "Specific protein assays and detection.")
	PDE = ProteinDetectionExperiment(subtypes = [NPDE, SPDE], description = "experiemnts to detect proteins")

	# adding protein quantification objects
	uv_absorbance = UVAbsorbance()
	PQE = ProteinQuantificationExperiment(subtypes = [uv_absorbance, bca_assay, bradford_assay, lowry_assay], description = "Experiments to quantify protein amounts.")

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
	PIE = ProteinInteractionExperiment(subtypes[PDIE, PPIE, PRIE])

	# adding protein location experiment objects
	flourescence_resonance_energy_transfer = FluorescenceResonanceEnergyTransfer()
	time_lapse = TimeLapse()
	SPLE = StaticProteinLocationExperiment(subtypes = [flourescence_resonance_energy_transfer])
	DPLE = DynamicProteinLocatinExperiment(subtypes = [time_lapse])
	PLE = ProteinLocationExperiment(subtypes = [SPLE, DPLE])

	# declaring experiment sub-types
	GE = GeneExperiment()#subtypes = [])#, description = "Experiment that revolves around jeans")
	PE = ProteinExperiment(subtypes = [PSE, PDE, PQE, PIE, PLE], description = "Experiment that revolves around proteins.")
	
	# adding experiment types to experiment

	E = Experiment(subtypes = [PE], description = "Science! http://i0.kym-cdn.com/photos/images/facebook/000/752/867/644.jpg")
	onto.add_objects(E)
	return onto