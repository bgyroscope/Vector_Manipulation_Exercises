#!/bin/python
# 2021.10.16
# Defines everything I need for Unit 01

# Topics are as following... (see format_name) 
'''
Unit 01: Kinematics 
    Topic 01. Vector Components
        Type 1 - Generated Given A,theta find components
        Type 2 - Generated Given component, theta find A
        Type 3 - Generated Given components, find A, theta
    Topic 2. Vector Sums
        Type 1 - Generated two vector sums 
        Type 2 - Generated three vector sums
        Type 3 - Generated four vector sums 
'''
# based on the topics and problem types create an end of session
# homework packet for the studetn. 


# load in packages 
import sys

import symbolicManipulation as sm 
import vectorManipulation as vm 

import numpy as np 
import random

import os.path


#################### Repeated functions
compRng = [-10,10]    # random range for the components 
vecScale = 0.5 



# for general kinetic motion
timeRng = [1, 15 ] 
kinRng = [-10, 10 ] 

def formatKinSymbol(char): 
    helpdict = { 't':'t', 'x':'\\Delta x', 'y':'\\Delta y', 'u': 'v_0', 'v':'v',  
        'vy': 'v_y', 'th':'\\theta' , 'a':'a' } 
    return helpdict[char] 


# for 1D kinetic motion
def format1DKinVar( char,val ) : 
    if val == 0:
        direction = '' 
    elif val > 0 : 
        direction = 'right' 
    else:  direction = 'left'

    val = abs(val) 

    if char == 't': 
        return 'takes {:5.2f} $s$'.format(val) 
    elif char == 'x': 
        return 'travels {} {:5.2f} $m$'.format(direction, val) 
    elif char == 'u': 
        return 'initially moves {} at {:5.2f} $m/s$'.format(direction, val) 
    elif char == 'v': 
        return 'ends its motion moving {} at a speed of {:5.2f} $m/s$'.format(direction, val) 
    elif char == 'a': 
        return 'accelerates {} at {:5.2f} $m/s^2$'.format(direction, val) 

# for 2D kinematic motion
g = -9.81  # m/s^2

def format2DKinVar( char,val ) : 
    if val == 0:
        direction = '' 
    elif val > 0 : 
        direction = 'upwards' 
    else:  direction = 'downwards'

    val = abs(val) 

    if char == 't': 
        return 'takes {:5.2f} $s$'.format(val) 
    elif char == 'x': 
        return 'is displaced {:5.2f} $m$ to the right'.format( val) 
    elif char == 'u': 
        return 'initially moves at {:5.2f} $m/s$'.format( val) 
    elif char == 'th': 
        if val == 0: 
            angle_str = 'horizontally' 
        elif val > 0: 
            angle_str = 'at {:5.2f} degrees above the horizon'.format( val / np.pi * 180 ) 
        else: 
            angle_str = 'at {:5.2f} degrees below the horizon'.format( val / np.pi * 180 ) 
        return 'initially launched at {} '.format( angle_str ) 
    elif char == 'y': 
        return 'is displaced {:5.2f} $m$ {}'.format( val, direction) 
    elif char == 'vy': 
        return 'ends its motion with a y component of {:5.2f} $m/s$ {}'.format(val, direction ) 


# for relative motion 

# for 1D kinetic motion
def format1DRelMotion( char,val ) : 
    if val == 0:
        direction = '' 
    elif val > 0 : 
        direction = 'right' 
    else:  direction = 'left'

    return '{} moves {} at {} $m/s$ relative to {}'.format( char[1].upper(), direction, val, char[2].upper()  ) 








#################### U01_T01_T01----------  
def U01_T01_T01_getInfo(): 
    # Given the magnitude of the vector and direction, find the components 
    instruction = 'Find the x- and y-components given the magnitude and direction of the vector.' 
    explanation =  \
'''
Assuming standard convention for the angle $[0,2\\pi]$, the components of vector $\\vec{A}$ can be found by
\\begin{align}  
A_x &= A \\cos (\\theta)  \\nonumber \\\\  
A_y &= A \\sin (\\theta)  \\nonumber  
\\end{align}  
'''
    ncol = 2 
    return instruction, explanation, ncol 

def U01_T01_T01(): 

    vec = vm.vector( xcomp=random.randint( *compRng ), ycomp=random.randint( *compRng ) )  

    ### Statement 
    statement = \
'''
\\begin{{align}}  
A = {:5.2f}, \\theta = {:5.2f} \\pi \\nonumber   
\\end{{align}}    
'''.format( vec.mag, vec.angle/np.pi, vecScale   )  
    
    ### Solution 
    solution = \
'''
\\begin{{align}}  
A_x &= A \\cos (\\theta) = {:5.2f} \\nonumber \\\\  
A_y &= A \\sin (\\theta) = {:5.2f} \\nonumber  
\\end{{align}}  
\\begin{{tikzpicture}}[scale={:3.1f}] 
{}
{} 
\\end{{tikzpicture}} \\\\
'''.format( vec.xcomp, vec.ycomp, vecScale, vec.draw_vector(), 
vec.draw_components(label_x='{:5.2f}'.format(vec.xcomp), label_y='{:5.2f}'.format(vec.ycomp)) )

    return statement, solution 


#################### U01_T01_T02----------  
def U01_T01_T02_getInfo(): 
    # Given the magnitude of the vector and direction, find the components 
    instruction = 'Find the magnitude and remaining component, given the angle and a component.' 
    explanation =  \
'''
Assuming standard convention for the angle $[0,2\\pi]$, the components of vector $\\vec{A}$ can be found by
\\begin{align}  
A_x &= A \\cos (\\theta)  \\nonumber \\\\  
A_y &= A \\sin (\\theta)  \\nonumber  
\\end{align}  
So this means that 
\\begin{align}
A &= \\frac{ A_x }{ \\cos \\theta } = \\frac{ A_y }{ \\sin \\theta } \\nonumber  \\\\
A_x &= \\sqrt{ A^2 - A_y^2 } \\nonumber \\\\
A_y &= \\sqrt{ A^2 - A_x^2 } \\nonumber 
\\end{align} 
as the case may be. 
'''
    ncol = 2 
    return instruction, explanation, ncol 

def U01_T01_T02(): 

    vec = vm.vector( xcomp=random.randint( *compRng ), ycomp=random.randint( *compRng ) )  

    if random.random() > 0.5: 
        comp = vec.xcomp
        comptext = 'A_x' 
        expline = ' A &= A_x /  \\cos (\\theta) '  
        expline2 =  'A_y &= \\sqrt{ A^2 - A_x^2 } ' 
        other = vec.ycomp
    else: 
        comp = vec.ycomp
        comptext = 'A_y' 
        expline = ' A &= A_y /  \\sin (\\theta) '  
        expline2 = ' A_x &= \\sqrt{ A^2 - A_y^2 } '
        other = vec.xcomp 

    # randomize how angle is presented. 
    if random.random() > 0.5: 
        angleStr = '{:5.2f} $\\pi$'.format(vec.angle/np.pi) 
    else: 
        angleStr = ' {} '.format( vec.get_theta_str(label_type='cardinal') ) 

    ### Statement 
    statement = \
'''
\\begin{{align}}  
{} &= {:5.2f} \\nonumber  
\\end{{align}}   
\\hspace{{3cm}} $ \\theta = $ {} 
'''.format( comptext, comp, angleStr   )  
    
    ### Solution 
    solution = \
'''
\\begin{{align}}  
{} = {:5.2f} \\nonumber \\\\  
{} = {:5.2f} \\nonumber
\\end{{align}}  
\\begin{{tikzpicture}}[scale={:3.1f}] 
{}
{} 
\\end{{tikzpicture}} \\\\
'''.format( expline, vec.mag, expline2, other, vecScale, 
        vec.draw_vector( label='{:5.3f}'.format(vec.mag)  ), 
vec.draw_components(label_x='{:5.2f}'.format(vec.xcomp), label_y='{:5.2f}'.format(vec.ycomp)) )

    return statement, solution 


#################### U01_T01_T03----------  
def U01_T01_T03_getInfo(): 
    # Given the components, find the vector magnitude and direction 
    instruction = 'Given the vector components, find the magnitude and direction. Specify angle in terms of cardinal directions, e.g. 30 degree north of east.' 
    explanation =  \
'''
Assuming standard convention for the angle $[0,2\\pi]$, the components of vector $\\vec{A}$ can be found by
\\begin{align}  
A_x &= A \\cos (\\theta)  \\nonumber \\\\  
A_y &= A \\sin (\\theta)  \\nonumber  
\\end{align}  
So this means that 
\\begin{align}
A &= \\sqrt{{ A_x^2 + A_y^2 }} \\nonumber  \\\\
\\tan \\theta = \\frac{{A_y}}{{A_x}} .  \\nonumber 
\\end{align} 
With the signs of the components you get the correct angle from $[0,2\\pi)$. Then convert that to cardinal directions.   
'''
    ncol = 2 
    return instruction, explanation, ncol 

def U01_T01_T03(): 
    vec = vm.vector( xcomp=random.randint( *compRng ), ycomp=random.randint( *compRng ) )  
    ### Statement 
    statement = \
'''
\\begin{{align}}  
A_x = {:5.2f} \\nonumber \\\\  
A_y = {:5.2f} \\nonumber
\\end{{align}}   
'''.format( vec.xcomp, vec.ycomp )  
    
    ### Solution 
    solution = \
'''
\\begin{{align}}  
A = {:5.2f} \\nonumber 
\\end{{align}}  
\\hspace{{3cm}} The direction is {} . \\\\
\\begin{{tikzpicture}}[scale={:3.1f}] 
{}
{} 
{}
\\end{{tikzpicture}} \\\\
'''.format( vec.mag, vec.get_theta_str(label_type='cardinal') , vecScale, 
        vec.draw_vector( label='{:5.3f}'.format(vec.mag)  ), vec.draw_components(), \
        vec.draw_angle( label=vec.get_theta_str() ) ) 

    return statement, solution 

#################### U01_T02_T01----------  
def U01_T02_T01_getInfo(): 
    return U01_T02_general_getInfo(2) 
def U01_T02_T01(): 
    return U01_T02_general(2)

def U01_T02_T02_getInfo(): 
    return U01_T02_general_getInfo(3) 
def U01_T02_T02(): 
    return U01_T02_general(3)

def U01_T02_T03_getInfo(): 
    return  U01_T02_general_getInfo(4) 
def U01_T02_T03(): 
    return U01_T02_general(4)




def U01_T02_general_getInfo(nvec): 
    # Sum the two vectors. 
    instruction = 'Add the {} vectors.'.format( {2:'two',3:'three', 4:'four'}[nvec] )  
    explanation =  \
'''
Assuming standard convention for the angle $[0,2\\pi]$, the components of vector $\\vec{A}$ can be found by
\\begin{align}  
A_x &= A \\cos (\\theta)  \\nonumber \\\\  
A_y &= A \\sin (\\theta)  \\nonumber  
\\end{align}  
We get the sum of a vector by adding together the components as 
\\begin{align}
\\vec{A} + \\vec{B} &= \\begin{pmatrix}
A_x + B_x \\\\ A_y + B_y   
\\end{pmatrix} , \\nonumber  
\\end{align} 
for the number of vectors we have. 
'''
    ncol = {2:2, 3:2, 4:1}[nvec] 
    return instruction, explanation, ncol 


def U01_T02_general(nvec): 
    vecs = [] 
    for j in range(nvec): 
        vecs.append( vm.vector( xcomp=random.randint( *compRng ), ycomp=random.randint( *compRng ) )  ) 

    vec = vecs[0] 

    res = vm.get_resultant( vecs) 

    # sometimes give the mag and angle, sometimes the components. 

    ### Statement 
    statement = '\\begin{align}\n'; vecNames = [ 'A', 'B', 'C', 'D', 'E' ] 
    for j in range(nvec):  
        if random.random() > 0.5: 
            statement += \
'''{} &= {:5.2f} \\nonumber \\\\
\\theta_{} &= {:5.2f} \\pi \\nonumber \\\\
'''.format( vecNames[j], vec.mag, vecNames[j], vec.angle/np.pi   )  
        else:
            statement += \
'''{0}_x &= {1:5.2f} \\nonumber \\\\  
{0}_y &= {2:5.2f} \\nonumber \\\\
'''.format( vecNames[j], vec.xcomp, vec.ycomp )  
    statement += '\\nonumber \\end{align}' 


    ### Solution 
    solution = \
'''
\\begin{{align}}  
R_x &= {:5.2f} \\nonumber \\\\  
R_y &= {:5.2f} \\nonumber  
\\end{{align}}  
\\begin{{tikzpicture}}[scale={:3.1f}] 
{}
{}
{} 
\\end{{tikzpicture}} \\\\
'''.format( res.xcomp, res.ycomp, vecScale, \
vm.draw_head_to_tail( vecs, labels=vecNames[:nvec] ), \
res.draw_vector(color='red'),  \
res.draw_components(label_x='{:5.2f}'.format(res.xcomp), label_y='{:5.2f}'.format(res.ycomp)) )

    return statement, solution 




