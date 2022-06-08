# 2021.10.08
# Common
# Contains all the classes needed for main
# 

from getUnitModule import getUnitModule

class Section: 
    def __init__(self, inputString, prob_offset = 0 ) : 
        # input string 
        self.inputString = inputString
        # formated input string UxxTxxTxx 
        self.inputCode = ''.join( inputString[2:].split('_' )  ) 
        # input string of the form xxUxxTxxTxx, i.e. nprobs, unit num, topic, type
        self.nProb, self.unit, self.topic, self.type = self.interpretInput( self.inputString) 
        # Problem Info object that gives instructions and general explanations+ other formatting
        self.info = SectionInfo( self.unit, self.topic, self.type  ) 
        # Problems is a list of problems. 
        self.problems = self.getProblems( prob_offset )

    def interpretInput( self, inputString): 
        nProb = int( inputString[:2] )
        parts = inputString[2:].split( '_' ) 
        unit = int( parts[0][1:] ) 
        topic= int( parts[1][1:] ) 
        ptype = int( parts[2][1:] ) 

        return nProb, unit, topic, ptype

    def getProblems(self, prob_offset):  
        helpList = [] 
        for j in range( self.nProb): 
            helpList.append( Problem(self.unit, self.topic, self.type, j+1+prob_offset)  ) 

        return helpList 

class SectionInfo: 
    def __init__(self, unit, topic, ptype ): 
        self.instruction = "Do this." 
        self.explanation = "This is how."
        self.ncol = 2

        info = self.get_info( unit, topic, ptype ) 
        if info: 
            self.instruction, self.explanation, self.ncol = info 
        else: 
            print( 'Warning: no U{:02d}_T{:02d}_T{:02d}_getInfo found.'.format( unit, topic, ptype) )

    def get_info(self,  unit, topic, ptype ): 
        unitModule =  getUnitModule(unit) 
        func_name = 'U{:02d}_T{:02d}_T{:02d}_getInfo'.format( unit, topic, ptype) 
        if hasattr( unitModule, func_name) and callable( func:= getattr(unitModule, func_name) ):
            return  func()  


class Problem: 
    def __init__(self, unit, topic, ptype, num=0) : 
        self.number = num 
        self.statement = "Solve this." 
        self.solution = "By doing this." 

        probText = self.get_problem( unit, topic, ptype )
        if probText: 
            self.statement, self.solution = probText 
        else: 
            print( 'Warning: no U{:02d}_T{:02d}_T{:02d} found.'.format( unit, topic, ptype) )


    def get_problem(self,  unit, topic, ptype ): 
        unitModule =  getUnitModule(unit) 
        func_name = 'U{:02d}_T{:02d}_T{:02d}'.format( unit, topic, ptype) 
        if hasattr( unitModule, func_name) and callable( func:= getattr(unitModule, func_name) ):
            return  func()  





# # testing 
# newSec = Section( '05U00_T00_T00' , 10 ) 
# print( newSec.nProb, newSec.unit, newSec.topic, newSec.type  ) 
# print( newSec.Info.instruction ) 
# for prob in newSec.Problems : 
#     print( prob.number, prob.statement ) 
# 


# class ProblemSet: 
#     def __init__ (self, inputString): 
#         self.inputString = inputString 
#         self.instructions = ''
#         self.numOfProb = numOfProb
#         self.problems= [] 
#         self.explanation = '' 
#         self.solutions = []
# 
# instructions
# problems
# explanation
# solutions


