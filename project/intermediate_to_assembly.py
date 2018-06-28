
from project import intermedCode
from project import  semanticAnalysis

class IntermediateToAssembly:

    def __init__(self, semantic: semanticAnalysis.SemanticAnalysisTableG, intermediate: intermedCode.IntermedCode):
        self.assembly = []
        self.semantic_table = semantic.table
        self.intermediate = intermediate
        self.stack_register = []
        self.temp_to_register = {}
        self.convertToAssembly()

    def convertToAssembly(self):
        print()
