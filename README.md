# Vector_Manipulation_Homework
Create Vector Homework Problems for Students


Automate creating vector homework problems for students. In this repository, there are the key files you need to create as many problems as you would like for your students. (You will have to compile the output LaTeX file.) 

As described in main.py 
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

These list the types of problems that can be produced. To specify which problems to create, modify the inputStringList in main.py. It is a list of input strings that specify the number of problems (use leading zeros), the unit, the topic, and finally the type. For example, '05U01_T02_T01' would correspond to 5 problems of Unit 01 Topic 02 type 01, corresponding to 5 problems of two vector sums. The output will be placed in a folder called temp. So create that. Then compile the latex code for a document that has all the problems with answers. 

An example output is called temp.pdf that shows two examples of each type of problems.
