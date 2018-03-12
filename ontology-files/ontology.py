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

	def __init__(self, name = "ProteinExperiment", subtypes = ["StaticLocationExperiment", "DynamicLocatinExperiment"]):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

"""" A 3rd level class to define finding the structure of a protein """
class ProteinStructureExperiment(ProteinExperiment):
	
	def __init__(self, name = "ProteinStructureExperiment", subtypes = ["XRayCrystalography"], experiment_type = "ProteinExperiment", description=""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

""" A 3rd level class to define protein interaction experiments """
class ProteinInteractionExperiment(ProteinExperiment):
	
	def __init__(self, name = "ProteinInteractionExperiment", subtypes = [], experiment_type = "ProteinExperiment", description = ""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

""" A 3rd level class to define quantificaiton of protein """
class ProteinQuantificationExperiment(ProteinExperiment):
	
	def __init__(self, name = "ProteinQuantificationExperiment", subtypes = [], experiment_type = "ProteinExperiment", description = ""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

""" A 3rd level class to define experiments to detect proteins """
class ProteinDetectionExperiment(ProteinExperiment):
	
	def __init__(self, name = "ProteinDetectionExperiment", subtypes = [], experiment_type = "ProteinExperiment", description = ""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

#####################################################################################################
#### Define 4th level experiments ####

""" A 4th level class to define the type of protein location experiment """
class StaticProteinLocationExperiment(ProteinLocationExperiment):
	
	def __init__(self, name = "StaticProteinLocationExperiment", subtypes = [], experiment_type = "ProteinLocationExperiment", description = ""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

""" A 4th level class to define the type of protein location experiment """
class DynamicProteinLocatinExperiment(ProteinLocationExperiment):
	
	def __init__(self, name = "DynamicProteinLocatinExperiment", subtypes = [], experiment_type = "ProteinLocationExperiment", description = ""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

# defining kinds of detection experiments
class NonspecificProteinDetectionExperiment(ProteinDetectionExperiment):

	def __init__(self, name = "NonspecificProteinDetectionExperiment", subtypes = [], experiment_type = "ProteinDetectionExperiment", description = ""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

class SpecificProteinDetectionExperiment(ProteinDetectionExperiment):

	def __init__(self, name = "SpecificProteinDetectionExperiment", subtypes = [], experiment_type = "ProteinDetectionExperiment", description = ""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

# defining protein interaction experiment sub-classes
class ProteinDNAInteractionExperiment(ProteinInteractionExperiment):

	def __init__(self, name = "ProteinDNAInteractionExperiment", subtypes = [], experiment_type = "ProteinInteractionExperiment", description = ""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

class ProteinRNAInteractionExperiment(ProteinInteractionExperiment):

	def __init__(self, name = "ProteinInteractionExperiment", subtypes = [], experiment_type = "ProteinInteractionExperiment", description = ""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

class ProteinProteinInteractionExperiment(ProteinInteractionExperiment):

	def __init__(self, name = "ProteinProteinInteractionExperiment", subtypes = [], experiment_type = "ProteinInteractionExperiment", description = ""):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

#####################################################################################################
##### Define 5th level experiments #####

# defining protein location terminal experiments
class FluorescenceResonanceEnergyTransfer(StaticProteinLocationExperiment):

	def __init__(self, name = "FluorescenceResonanceEnergyTransfer", subtypes = None, experiment_type = "StaticProteinLocationExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type
		self.attributes = {"units":"nm", "tags":["fluorescence", "dye"]}
		self.description = "FRET has been used to measure distance and detect molecular interactions in a number of systems and has applications in biology and chemistry. FRET can be used to measure distances between domains in a single protein and therefore to provide information about protein conformation. FRET can also detect interaction between proteins. Applied in vivo, FRET has been used to detect the location and interactions of genes and cellular structures including intergrins and membrane proteins. FRET can be used to obtain information about metabolic or signaling pathways. FRET is also used to study lipid rafts in cell membranes. FRET and BRET are also the common tools in the study of biochemical reaction kinetics and molecular motors. The applications of fluorescence resonance energy transfer (FRET) have expanded tremendously in the last 25 years, and the technique has become a staple technique in many biological and biophysical fields. FRET can be used as spectroscopic ruler in various areas such as structural elucidation of biological molecules and their interactions in vitro assays, in vivo monitoring in cellular research, nucleic acid analysis, signal transduction, light harvesting and metallic nanomaterial etc. Based on the mechanism of FRET a variety of novel chemical sensors and biosensors have been developed. <https://en.wikipedia.org/wiki/Forster_resonance_energy_transfer#Methods_to_measure_FRET_efficiency>"

class TimeLapse(DynamicProteinLocatinExperiment):

	def __init__(self, name = "TimeLapse", subtypes = None, experiment_type = "DynamicProteinLocatinExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type
		self.attributes = {"units":["seconds", "nm"], "tags":["imaging", "dye", "fluorescence"]}
		self.description = "https://en.wikipedia.org/wiki/Time-lapse_microscopy"

""" A 5th level method to define experiment that identifies protein structure. This is a terminal node. """
class XRayCrystalography(ProteinStructureExperiment):
	
	def __init__(self, name="XRayCrystalography", subtypes = None, experiment_type="ProteinStructureExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type
		self.attributes = {"units":["nl", "kW", "angstroms"]}
		self.description = "https://en.wikipedia.org/wiki/X-ray_crystallography"


# defining terminal nonspecific protein detection experiments
class Absorbance(NonspecificProteinDetectionExperiment):

	def __init__(self, name = "Absorbance", subtypes = None, description = "", experiment_type = "NonspecificProteinDetectionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

class AmidoBlack(NonspecificProteinDetectionExperiment):

	def __init__(self, name = "AmidoBlack", subtypes = None, experiment_type = "NonspecificProteinDetectionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type
		self.description = "https://en.wikipedia.org/wiki/Amido_black_10B"
		self.attributes = {"tags":["dye"]}

class BCAAssay(NonspecificProteinDetectionExperiment, ProteinQuantificationExperiment):

	def __init__(self, name = "BCAAssay", subtypes = None, experiment_type = ["NonspecificProteinDetectionExperiment", "ProteinQuantificationExperiment"]):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type
		self.attributes = {"units":["ug/ml", "mg/ml", "Molar", "nm"], "minimum concentration":"0.5 ug/ml", "maximum concentration":"1.5 mg/ml", "reagents":["Bicinconinic acid", "NaCO3", "NaHCO3", "Sodium tartrate"], "tags":["dye"]}
		self.description = "https://en.wikipedia.org/wiki/Bicinchoninic_acid_assay"

class BradfordAssay(NonspecificProteinDetectionExperiment, ProteinQuantificationExperiment):

	def __init__(self, name = "BradfordAssay", subtypes = None, experiment_type = ["NonspecificProteinDetectionExperiment", "ProteinQuantificationExperiment"]):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type
		self.description = "https://en.wikipedia.org/wiki/Bradford_protein_assay"
		self.attributes = {"units":["ug/ml", "Molar", "nm"], "minimum concentration":"200 ug/ml", "maximum concentration":"1500 ug/ml", "reagent":"NaCl" ,"tags":["dye"]}

class LowryAssay(NonspecificProteinDetectionExperiment, ProteinQuantificationExperiment):

	def __init__(self, name = "LowryAssay", subtypes = None, description = "", experiment_type = ["NonspecificProteinDetectionExperiment", "ProteinQuantificationExperiment"]):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type
		self.description = "https://en.wikipedia.org/wiki/Lowry_protein_assay"
		self.attributes = {"reagents":["Folin–Ciocalteu", "Cu+", "Al"], "units":["ug/ml", "Molar", "nm"]}

# defining terminal specific detection experiments
class ELISA(SpecificProteinDetectionExperiment):

	def __init__(self, name = "ELISA", subtypes = None, experiment_type = "SpecificProteinDetectionExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type
		self.description = "https://en.wikipedia.org/wiki/ELISA"

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