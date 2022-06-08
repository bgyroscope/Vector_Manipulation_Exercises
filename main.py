#!/bin/python
# 2021.10.09 -- MAIN. 
# main program that makes calls to classes in common.  

# Topics are as following... (see format_name) 
'''
Unit 00 Prequisits 
    Topic 01 Similify Expressions
        Type 01 multiply by reciprocal 
    Topic 02 Solve 1D Equations 
        Type 01 cross multiply 
        Type 02 Linear Equation
Unit 01: Kinematics 
    Topic 01. Vector Components
        Type 1 - Given A,theta find components
        Type 2 - Given component, theta find A
        Type 3 - Given components, find A, theta
    Topic 2. Vector Sums
        Type 1 - two vector sums 
        Type 2 - three vector sums
        Type 3 - four vector sums 

'''
# based on the topics and problem types create an end of session
# homework packet for the studetn. 

import numpy as np
import random 
import os

from common import *   # common is in packages 


########## Initial Definitions--------------------------
inputStringList = [ '02U00_T01_T01', '02U00_T02_T01', '02U00_T02_T02', 
       '02U01_T01_T01', '02U01_T01_T02', '02U01_T01_T03', 
       '02U01_T02_T01', '02U01_T02_T02', '02U01_T02_T03' ]  



out_file = './temp/temp.tex' # latex file. 
out_directory = './temp/'   # output directory. 
headtex = 'header.txt' 

# ------------------------------------------------

os.system( 'cat {:s} > {:s}'.format( headtex , out_file )  ) 


with open( out_file, "a") as myfile: 
    
    # begin the document. 
    myfile.write( '\\begin{document} \n') 
    myfile.write( '\\begin{flushright} \\noindent\\today \\end{flushright} \n\n' ) 
    myfile.write( '\\noindent \n' )    

    ##### Get the problems.   
    prob_count = 0 
    sections = [] 

    # loop over the input code.. 
    for inputString in inputStringList: 
        inputString = inputString.strip() 
        # print( inputString) 
        sec = Section( inputString, prob_count) 
        print( inputString, sec.inputCode ) 
        prob_count += sec.nProb
        sections.append( sec) 

    ##### Write the problems.   
    myfile.write( '%------------------------------------\n' ) 
    myfile.write( '{ \\bf \\Large Problems } \\\\ \n' )  
    myfile.write( '%------------------------------------\n \n' ) 

    for sec in sections: 
        myfile.write( '\n\\noindent {{ \\bf {}: }} {}  \\\\ \n'.format(sec.inputCode, sec.info.instruction )  ) 
        if sec.info.ncol != 1 : 
            myfile.write( '\\begin{{multicols}}{{ {} }}\n'.format(sec.info.ncol) ) 
        for prob in sec.problems: 
            myfile.write('\\noindent {{ \\bf  Problem {:02d}: }}'.format(prob.number) )
            myfile.write( prob.statement )
            #  #myfile.write( '\\\\ \n' )  
        if sec.info.ncol != 1 : 
            myfile.write( '\\end{multicols}\n' ) 


    ##### Write the solutions.   
    myfile.write( '\n\n\\pagebreak \n' ) 
    myfile.write( '%------------------------------------\n' ) 
    myfile.write( '{ \\bf \\Large Solutions } \\\\ \n' )  
    myfile.write( '%------------------------------------\n \n' ) 

    for sec in sections: 
        myfile.write( '\n\\noindent {{ \\bf {}: }} {} \\\\ \n'.format( sec.inputCode, sec.info.explanation)  ) 
        if sec.info.ncol != 1 : 
            myfile.write( '\\begin{{multicols}}{{ {} }}\n'.format(sec.info.ncol) ) 
        for prob in sec.problems: 
            myfile.write('\\noindent {{ \\bf  Problem {:02d}: }} '.format(prob.number) )
            myfile.write( prob.solution )
            # myfile.write( '\\\\ \n' )  
        if sec.info.ncol != 1 : 
            myfile.write( '\\end{multicols}\n' ) 


    myfile.write ( '\\end{document}' ) 

