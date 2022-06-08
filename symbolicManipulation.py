# 2021.10.02 
# Symbolic Manipulation Package 

#------------------------------
#  Defines class expression, which is a series of terms. 
#  --> self.termDict is dictionary of terms (xxy = x^2, etc) where value is coefficient. 
# Methods: 
#   init -- creates a series of terms added together based on coeList and varList
#       '' as var string is just a coefficient, e.g. 1, 2, 4.5  
#   copy -- copies expression
#   get_random_term -- get random linear term. 
#   add -- adds expression together
#   subtract -- subtracts expressions (uses negate) 
#   multiply -- multiplies expressions (foils ) 
#   evaluate -- numerically evaluate an expression  
#   formatExpression -- formats for LaTeX output 
#   simplifyRatio -- removes common factors from numerator and denominator
#
#------------------------------

import numpy as np 

import math 

from string import ascii_lowercase 
import random



class expression: 
    # List of added term stored as a dictionary of string of variables. 
    # for example 4 x y - 2 x^2  = {'xy': 4, 'xx': -2 } (stored alphabetically sorted) 
    def __init__(self, coeList=[0], varList=[''] ): 

        # properties. 
        self.termDict = {}

        # create term based on input
        minLen = min( len(coeList) , len(varList) )
        if len(coeList) != len(varList): 
            print( 'WARNING: mismatch in term creation. Some terms will be dropped.' ) 

        for j in range(minLen) : 
            if coeList[j] == 0 :  # empty termDict means 0 
                continue
            varStr = ''.join(sorted(varList[j]) ) 

            if not( varStr in self.termDict ): 
                self.termDict[varStr] = coeList[j]  

            else: 
                self.termDict[varStr] += coeList[j] 
                if self.termDict[varStr] == 0 : 
                    del self.termDict[varStr] 


    def __repr__(self): 
        return self.formatExpression()

    def copy(self): 
        new = expression() 
        new.termDict = self.termDict.copy() 
        return new 


    def findGCF(self): 
        if len( self.termDict) <= 1: 
            return self.copy()
       
        gcfvar = list( self.termDict.keys() ) [0] 
        for key in self.termDict.keys() :
            temp = key 
            gcfvar_temp = ''
            for char in gcfvar: 
                if char in temp: 
                    gcfvar_temp += char 
                    idx = temp.index(char); temp = temp[:idx] + temp[idx+1:]   
                    

        gcfcoe = list( self.termDict.values() ) [0] 
        for val in self.termDict.values(): 
            sign = 1; 
            if gcfcoe<0 and val<0: sign = -1 
            gcfcoe = sign* math.gcd( gcfcoe, val )  

        return expression( [gcfcoe], [gcfvar_temp] ) 

    ##########  operations 
    def removeZero(self):  
        delkeys = [ k for k, v in self.termDict.items() if v == 0  ] 
        # print( 'delkeys ', delkeys ) 
        for k in delkeys: 
            del self.termDict[ k ] 
        
    def add( self, term2) : 
        newTerm = expression()  
        # newTerm.termDict = self.termDict.copy() 
        # for key in term2.termDict.keys() : 
        #     if key in newTerm.termDict: 
        #         newTerm.termDict[key] += term2.termDict[key] 
        #     else: 
        #         newTerm.termDict[key] =  term2.termDict[key]  

        newTerm.termDict = { **self.termDict, **term2.termDict, \
            **{k:v+v2 for k,v in self.termDict.items() for k2,v2 in term2.termDict.items() \
            if k == k2 }   } 
        newTerm.removeZero() 
        return newTerm 

    def negate( self ) : 
        for key in self.termDict.keys() : 
            self.termDict[key] = -1 * self.termDict[key] 

    def subtract(self, term2): 
        temp = term2.copy() 
        temp.negate()
        return self.add(temp ) 

    def multiply( self, term2 ) : 
        newTerm = expression()  
        for key in self.termDict.keys(): 
            for key2 in term2.termDict.keys(): 
                tempCoe = self.termDict[key] * term2.termDict[key2] 
                tempStr = key+key2
                # print( 'key={}, key2={}, tempCoe={}, tempStr={}'.format(key, key2, tempCoe, tempStr ) ) 
                newTerm = newTerm.add( expression([tempCoe],[tempStr])  )
                # print( newTerm.termDict ) 

        return newTerm 

    #### Evaluate expression. 
    def evaluate(self, subs ) : 
        # get subs 
        # subs is a dictionary of substitute { 'x':1 , 'y':4 } would be x=1, y=4 
        # for now just numerical values
        totsum = expression() 
        for key in self.termDict.keys(): 
            temp = expression( [self.termDict[key] ] , [''] )    # change this line if not numer
            for char in key: 
                if char in subs: 
                    new = expression( [subs[char] ], [''] ) # number 
                else: 
                    new = expression( [1] , [char] ) 
                temp = temp.multiply( new  ) 
            totsum = totsum.add( temp ) 
        return totsum  # expression  



    ########## format 
    def formatExpression(self): 
        if not self.termDict: 
            # return '' 
            return '0' 
       
        outStr = ''
        for key in self.termDict.keys():  
            
            tempDict = {} 
            for s in key: 
                tempDict.setdefault( s, 0 )   
                tempDict[s] += 1 

            termStr = '' 
            for k in tempDict.keys(): 
                termStr += '{}^{}'.format( k , tempDict[k] ) 
                if termStr[-1] == '1': 
                    termStr = termStr[:-2] 

            addStr = ' {:+}'.format( self.termDict[key] );  
            if abs( self.termDict[key] ) ==1 and key != '' : 
                addStr = addStr[:-1]

            outStr = outStr + addStr  +  termStr 

        if outStr[0:2] == ' +':  # remove space and initial + sign
            outStr = outStr[2:] 

        
        return outStr 

#################### Other functions 

def get_random_term( notThese=[], coeRng=[-10,10] ): 
    # returns random expression 
    # notThese, don't choice from notThese for variable
    # rtype: expression 
    notThese = notThese + ['d','e','i','o']
    lett_string = ascii_lowercase
    for j in notThese: 
        lett_string = lett_string.replace( j, '' )

    coe = 0
    while coe == 0:  # demand it isn't zero!! 
        coe = random.randint( coeRng[0], coeRng[1]) 

    return expression( [coe], random.choice(lett_string) ) 

def get_random_linear( var='x', coeRngs=[ [-10,10], [-10,10] ] ): 

    coes = [0,0] 
    for j in range(len(coes) ): 
        while coes[j] == 0: 
            coes[j] = random.randint( coeRngs[j][0], coeRngs[j][1] ) 

    return expression( coes, [ var, '' ] ) 

def simplifyRatio( top, bot) : 
    # input of the top and bottom of a ratio
    # find common factors and return simplified versions
    topgcf = top.findGCF()
    botgcf = bot.findGCF()

    # to avoid issue of -1 + -2 = -3, use random characters to add terms
    topgcf = topgcf.multiply( expression( [1],['#'] )   ) 
    botgcf = botgcf.multiply( expression( [1],['@'] )   ) 

    com = (topgcf.add(botgcf) ).findGCF()

    if len(com.termDict) == 0: 
        return top, bot

    var = list( com.termDict.keys() )[0] 
    coe = list( com.termDict.values() )[0] 

    # edit top 
    res = [] 
    for expr in [ top, bot]: 
        keyList = list( expr.termDict.keys()  ) 
        coeList= list(  expr.termDict.values() )         
        for j in range(len(coeList) ) : 
            coeList[j] = coeList[j] // coe  # only com factors --> no fraction
        for j in range(len(keyList) ) : 
            for char in var: 
                key = keyList[j]; idx = key.index( char ) 
                keyList[j] = key[:idx] + key[idx+1: ] 
        res.append( expression( coeList, keyList )   ) 

    return res[0], res[1] 





# # # # # # # # # # Testing # # # # # # # # # #
# # # Test cases for initialization and print expression --------------------------
# testCases = [
# (expression( [-1,0,1,2,-3], ['xyxy', 'a','b',  'y' , 'z' ] ) , ' -x^2y^2 +b +2y -3z'), 
# (expression( [1, 2], ['a','a' ] ) , '3a'), 
# (expression( [-2, 2], ['a','a' ] ) , '0'), 
# (expression( [-2, 2, 1], ['a','a', 'a' ] ) , 'a'), 
# (expression( [-2, 2, -3], ['a','a', 'a' ] ) , ' -3a'), 
# (expression( [1,2,3], ['a','aa', 'aaa' ] ) , 'a +2a^2 +3a^3'), 
# (expression([6], ['']  ) , '6' ) , 
# (expression([-1], ['']  ) , ' -1' ) , 
# (expression( ) , '0') 
# ]
# 
# count = 0 
# for test in testCases: 
#     if not( test[0].formatExpression() == test[1] ) : 
#         print( 'Failed case {}'.format(count) )
#         print( test[0].formatExpression() ) 
#         print( test[1] ) 
#         quit()
#     count += 1 
# print( 'Success in all {} cases'.format(count)  ) 

# for j in range(10): 
#     # expr = get_random_term(notThese= ['a','b','c','d','e'] )  
#     expr = get_random_term()  
#     print( expr.formatExpression()  ) 
# quit() 


# # # Testing add and subtract 
# print( '------- ' ) 
# expr = expression( [1,-1,2,-2]  , ['a', 'b', 'c', 'd' ]  ) 
# print( expr.formatExpression() ) 
# expr2= expression( [-1,1,-2,2]  , ['aa', 'b', 'c', 'd' ]  ) 
# print( expr2.formatExpression() ) 
# 
# print( 'add' ) 
# res = expr.add( expr2 ) 
# print( res.formatExpression() )  
# 
# print( 'subtract' ) 
# res = expr.subtract( expr2 ) 
# print( res.formatExpression() )  
# 
# print( '--------' ) 
# expr3 = expression() 
# res = expr.add(expr3) 
# res2 = expr3.add(expr) 
# print( res.formatExpression(), res2.formatExpression() , res.formatExpression() == res2.formatExpression() ) 
# 
# expr = expression( [-10], [''] ) 
# expr2= expression( [3] , ['' ] ) 
# expr3= expression( [3] , ['' ] ) 
# 
# # res = expr.add(expr2) 
# res = expr3.subtract(expr2)
# print( res.termDict ) 
# print( res.formatExpression() ) 




# # Test cases for multiply 
# print( '---------------- ' ) 
# testCases = [
# (expression( ), expression( ) , ''), 
# (expression([1], ['x']  ), expression([4], ['x']  ) , '4x^2'), 
# (expression([-3], ['y']  ), expression([-4], ['x']  ) , '12xy'), 
# (expression([1,1], ['x', '' ]  ), expression([1,1], ['x', '']  ) , 'x^2 +2x +1'), 
# (expression([1,1], ['x', 'y' ]  ), expression([1,1], ['x', '']  ) , 'x^2 +x +xy +y'), 
# (expression([2,3], ['w', 'x' ]  ), expression([-1,1], ['y', 'z']  ) , ' -2wy +2wz -3xy +3xz'), 
# (expression([1,-1], ['w', 'x' ]  ), expression([1,1], ['w', 'x']  ) , 'w^2 -x^2'), 
# (expression([-1],['']  ), expression([1,2,-1], ['a','b','c']  ) , ' -a -2b +c'), 
# (expression( ), expression( ) , '') 
# ]
# 
# count = 0 
# for test in testCases: 
#     newTerm = test[0].multiply( test[1] ) 
#     out = newTerm.formatExpression() 
#     if not( out  == test[2] ) : 
#         print( 'Failed case {}'.format(count) )
#         print( test[0].formatExpression() ) 
#         print( test[1].formatExpression() ) 
#         print( test[2] , 'vs' )
#         print( out ) 
#         quit()
#     count += 1 
# print( 'Success in all {} cases'.format(count)  ) 


# # Testing findGCF
# print( '---------------- ' ) 
# testCases = [
# (expression( ),  ''), 
# (expression([1],['x'] ),  'x'), 
# (expression([1,3],['x','x'] ),  '4x'), 
# (expression([1,3],['xx','xxx'] ),  'x^2'), 
# (expression([-3,-1],['xx','xxx'] ),  '-x^2'), 
# (expression([-6,-2],['xxyyy','xxxyy'] ),  '-2x^2y^2'), 
# (expression([-6,10],['xxyyyzzzz','xxxyyzz'] ),  '2x^2y^2z^2'), 
# # (expression( ), expression( ) , '') 
# ]
# 
# count = 0 
# for test in testCases: 
#     gcf = test[0].findGCF() 
#     out = gcf.formatExpression().strip()  
#     if not( out  == test[1] ) : 
#         print( 'Failed case {}'.format(count) )
#         print( test[0].formatExpression() ) 
#         print( test[1] , 'vs' )
#         print( out ) 
#         quit()
#     count += 1 
# print( 'Success in all {} cases'.format(count)  ) 



# # Test cases for simplifyRatio
# print( '---------------- ' ) 
# testCases = [
# (expression( ), expression( ) , '0', '0' ), 
# (expression([2],['xx']  ), expression( [1], ['x'] ) , '2x', '1' ), 
# (expression([2],['x']  ), expression( [1], ['xx'] ) , '2', 'x' ), 
# (expression([2,3],['x', 'xy']  ), expression( [2], ['xx'] ) , '2 +3y', '2x' ), 
# (expression([8,4],['xzzz', 'xyzz']  ), expression( [2,2], ['xxzz', 'yzzz'  ] ) , '4xz +2xy', 'x^2 +yz' ), 
# (expression([8,4],['xxxzzzz', 'xyzz']  ), expression( [2,2], ['xxzz', 'yzzz'  ] ) , '4x^3z^2 +2xy', 'x^2 +yz' ), 
# (expression([-17,-5],['u', 'n']  ), expression( [-14,-2], ['w', 'n'] ) , '17u +5n', '14w +2n' ), 
# ]
# 
# count = 0 
# for test in testCases: 
#     top, bot = simplifyRatio(test[0], test[1]) 
#     if not( ( top.formatExpression()  ==  test[2] ) and ( bot.formatExpression()==test[3] ) ) : 
#         print( 'Failed case {}'.format(count) )
#         print( top.formatExpression() ) 
#         print( bot.formatExpression() ) 
#         print( 'vs' )
#         print( test[2] ) 
#         print( test[3] ) 
#         quit()
#     count += 1 
# print( 'Success in all {} cases'.format(count)  ) 



# # Test cases for evaluate 
# print( '---------------- ' ) 
# testCases = [
# (expression([1], ['x']  ), {'x':4} ,  '4' ), 
# (expression([1], ['xx']  ), {'x':4} ,  '16' ), 
# (expression([1,2], ['xx', 'xy' ]  ), {'x':4} ,  '16 +8y' ), 
# (expression([1,2], ['xx', 'xy' ]  ), {'x':0} ,  '0' ), 
# (expression([1,-1], ['xx', 'xy' ]  ), {'y':0} ,  'x^2' ), 
# (expression([1,-1], ['xx', 'xy' ]  ), {'x':2, 'y':2} ,  '0' ), 
# (expression([4,-1], ['xxz', 'xy' ]  ), {'z':2, 'y':2} ,  '8x^2 -2x' ), 
# ]
# 
# count = 0 
# for test in testCases: 
#     out= test[0].evaluate( test[1] ) 
#     if not( out.formatExpression() == test[2]   ) : 
#         print( 'Failed case {}'.format(count) )
#         print( test[0].formatExpression() ) 
#         print( test[1] ) 
#         print( 'gives me: ', out.formatExpression() ) 
#         print( 'vs' )
#         print( test[2] ) 
#         quit()
#     count += 1 
# print( 'Success in all {} cases'.format(count)  ) 




