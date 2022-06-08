#!/bin/python
# 2021.10.09
# Defines everything I need for Unit 00 

# Topics are as following... (see format_name) 
'''
Unit 00 Prequisits 
    Topic 01 Similify Expressions
        Type 01 multiply by reciprocal 
    Topic 02 Solve 1D Equations 
        Type 01 cross multiply 
        Type 02 Linear Equation
'''
# based on the topics and problem types create an end of session
# homework packet for the studetn. 



# load in packages 
import sys
import symbolicManipulation as sm 

import random 

# get info returns info about the problem
# UxxTxxTxx returns the problem itself

#### repeated functions 
def get_random_terms( n, notThese = [] , coeRng=[-10,10]) : 
    exprs = [ ]
    for j in range(n): 
       exprs.append( sm.get_random_term( notThese, coeRng ) )  
    return exprs 



#################### U00_T01_T01----------  
def U00_T01_T01_getInfo(): 
    # simplify a/b / c/d = a d / (b c ) 
    instruction = 'Simplify the fractions. ' 
    explanation =  \
'''
Multiple the top fraction by the reciprocal, i.e. 
\\begin{align}
\\frac{ a / b } { c / d } &= \\left( \\frac{a}{b}  \\right)  \\left( \\frac{d}{c} \\right)  = \\frac{ a d } { b c }  \\nonumber 
\\end{align} 
'''
    ncol = 3 
    return instruction, explanation, ncol 

def U00_T01_T01(): 
    exprs = get_random_terms( 4 ) 

    top = exprs[0].multiply( exprs[3] ) 
    bot = exprs[1].multiply( exprs[2] ) 

    ### Statement 
    statement = \
'''
\\begin{{align}} 
\\frac{{ {} / {}  }} {{ {} / {}  }}  \\nonumber 
\\end{{align}} 
'''.format( *[ obj.formatExpression() for obj in exprs ] ) 
    
    ### Solution 
    solution = \
'''
\\begin{{align}} 
\\frac{{ {}  }} {{ {}  }}  \\nonumber 
\\end{{align}} 
'''.format( *[ obj.formatExpression() for obj in sm.simplifyRatio(top,bot) ] ) 
 
    return statement, solution 

#################### U00_T01_T02----------  
def U00_T02_T01_getInfo(): 
    instruction = 'Solve for $x$.' 
    explanation = 'Cross multiply and then simplify.' 
    ncol = 3 
    return instruction, explanation, ncol 

def U00_T02_T01(): 
    exprs = get_random_terms(4, notThese=['x']  ) 
    # randomly choose one to solve for. 
    switch = random.randint(0,3) 
    exprs[switch] = sm.expression( [1], ['x'] ) 

    # simplify   a/b = c/d  depending on x location
    if switch == 0 :  # x d = b c \\implies x = b c / d  
        order = [ 1, 2, 3 ] 
    elif switch == 1:  # x c = a d \implies a * d / c 
        order = [ 0, 3, 2 ] 
    elif switch == 2:  # x b = a d \implies a * d / b  
        order = [ 0, 3, 1 ] 
    elif switch == 3:  # x a = b c \implies b * c / a  
        order = [ 1, 2, 0 ] 
    
    line = '{} &= {} \\implies x = \\frac{{ {} }} {{ {} }} '.format( 
            *[ obj.formatExpression() for obj in [   
            exprs[0].multiply( exprs[3] ) , exprs[1].multiply( exprs[2] ), 
            *sm.simplifyRatio( exprs[order[0]].multiply( exprs[order[1]] ), exprs[order[2]] ) ]] )

    statement = \
'''
\\begin{{align}} 
\\frac{{ {} }}{{  {}  }} = \\frac {{ {} }}{{ {}  }}  \\nonumber 
\\end{{align}} 
'''.format( *[ obj.formatExpression() for obj in exprs ] ) 
 
    solution = \
'''
\\begin{{align}} 
{}  \\nonumber  
\\end{{align}} 
'''.format(line) 
    return statement, solution 

#################### U00_T02_T02----------  
def U00_T02_T02_getInfo(): 
    instruction = 'Solve for $x$' 
    explanation = 'Isolate $x$ by first subtracting and then dividing by coefficient of $x$.' 
    ncol = 2 
    return instruction, explanation, ncol 

def U00_T02_T02(): 
    exprs = get_random_terms(3, notThese=['x'], coeRng=[-20,20]  ) 

    withx = exprs[0].multiply( sm.expression([1],['x'] )  ) 
    lhs = withx.add( exprs[1] ) 

    top = exprs[2].subtract( exprs[1] ) 
    bot = exprs[0] 
    stop , sbot = sm.simplifyRatio( top, bot )  

    statement = \
'''
\\begin{{align}} 
{} &= {} \\nonumber 
\\end{{align}} 
'''.format( lhs.formatExpression(), exprs[2].formatExpression() ) 

    solution = \
'''
\\begin{{align}} 
{} &= {} \\implies x = \\frac{{ {} }} {{ {} }}   \\nonumber  
\\end{{align}} 
'''.format( *[ obj.formatExpression() for obj in [withx, top, stop, sbot] ] ) 
 
    return statement, solution 











