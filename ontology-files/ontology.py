# BMI 210/CS 270 Final Project
# Team: Gaby Steiner, Akhila Monturu, Julia Daniel, Eric Cramer
# Ontology files for Python (UML style ontology)

# The following file contains:
# 	1. Class definition for an ontology
# 	2. Class definitions for the ontology
# 	3. Function to build the ontology to be traversed

#######################################################################################################

""" Class definition for an ontology object """
class ontology():

	def __init__(self):
		pass

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

#####################################################################################################
##### Define 5th level experiments #####

""" A 5th level method to define experiment that identifies protein structure. This is a terminal node. """
class XRayCrystalography(ProteinStructureExperiment):
	
	def __init__(self, name="XRayCrystalography", subtypes = None, description="", experiment_type="ProteinStructureExperiment"):
		self.name = name
		self.subtypes = subtypes
		self.description = description
		self.experiment_type = experiment_type

######################################################################################################

""" Function to build a ontology object """
def build_ontology():
	onto = ontology()
	onto.set_substances(["protein", "gene", "dna", "rna", "guacamole"])

	# init classes in reverse order, starting from the leaves

	# adding protein structure objects
	XrayCrystal = XRayCrystalography("https://en.wikibooks.org/wiki/Structural_Biochemistry/Proteins/X-ray_Crystallography")
	PSE = ProteinStructureExperiment(subtypes = [XrayCrystal], description = "Experiment to determine a protein's structure.")

	# declaring experiment sub-types
	GE = GeneExperiment()#subtypes = [])#, description = "Experiment that revolves around jeans")
	PE = ProteinExperiment(subtypes = [PSE], description = "Experiment that revolves around proteins.")
	
	# adding experiment types to experiment

	E = Experiment(subtypes = [PE], description = "Science! http://i0.kym-cdn.com/photos/images/facebook/000/752/867/644.jpg")
	onto.add_objects(E)
	return onto