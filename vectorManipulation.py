# 2021.10.15
# Vector Manipulation Package 

#------------------------------
#  Defines class vector
#   -->  mag - magnitude
#   --> angle - 2D angle relative to x-axis (in radians) 
#   -->  xcomp - x component
#   -->  ycomp - y component
# Methods: 
#   init -- creates a series of terms added together based on coeList and varList
#       '' as var string is just a coefficient, e.g. 1, 2, 4.5  
#   repr -- print out mag, angle, xcomp and ycomp
#   copy -- copies expression
#   add -- adds expression together
#   scalarMultiply -- multiplies expressions (foils ) 
#
#------------------------------


import numpy as np 

class vector: 

    def __init__(self, mag=None, angle=None, xcomp=None, ycomp=None ) : 

        if (mag!=None) and (angle != None) : 
            self.mag = mag
            self.angle = angle 
            self.get_components() 

        elif (xcomp!=None) and (ycomp!=None): 
            self.xcomp = xcomp
            self.ycomp = ycomp 
            self.get_magAndAngle() 

        else: # default  
            self.mag = 0 
            self.angle =0
            self.xcomp =0
            self.ycomp =0


    def __repr__(self): 
        return 'vec: mag={:5.3f}, angle={:5.3f}, xcomp={:5.3f}, ycomp={:5.3f}'.format( 
            self.mag, self.angle, self.xcomp, self.ycomp ) 


    def copy(self): 
        return vector(mag=self.mag, angle=self.angle) 

    # for conversion -------------------
    def get_components(self): 
        self.xcomp = self.mag*np.cos( self.angle ) 
        self.ycomp = self.mag*np.sin( self.angle ) 

    def get_magAndAngle(self): 
        
        self.mag = np.sqrt( self.xcomp**2 + self.ycomp**2 ) 

        dir_tmp = np.arctan( self.ycomp / (self.xcomp+1.0E-10 )  ) 
        if abs(self.xcomp) < 1E-10 :
            angle = np.sign( self.ycomp) * np.pi / 2.
        elif self.xcomp < 0: 
            angle = np.pi + dir_tmp 
        else: # self.xcomp > 0  
            angle = dir_tmp

        self.angle = angle 


    #  methods-------------------- 
    def add(self, vec2): 
        return vector( xcomp=self.xcomp+vec2.xcomp, ycomp=self.ycomp+vec2.ycomp ) 

    def scalarMultiply(self, scalar): 
        return vector( xcomp=self.xcomp*scalar, ycomp=self.ycomp*scalar) 


    # nice LaTeX outputs ----------------

    def get_theta_str(self, label_type='math' ) : 
        theta = self.angle * 180 / np.pi 
        while theta<0: 
            theta = theta + 360 
        while theta>=360: # >= 360  
            theta = theta - 360  
        
        # based on cardinal direction. 
        if label_type == 'math': 
            return '{:6.2f} degrees'.format( theta ) 
        elif label_type == 'cardinal' : 
            if theta == 0: 
                theta_str = 'east' 
            elif theta < 90: 
                theta_str = '{:5.3f} degrees north of east'.format(theta)
            elif theta == 90: 
                theta_str = 'north' 
            elif theta<180: 
                theta_str = '{:5.3f} degrees north of west'.format(180-theta)
            elif theta == 180: 
                theta_str = 'west' 
            elif theta<270: 
                theta_str = '{:5.3f} degrees south of west'.format(theta-180)
            elif theta == 270: 
                theta_str = 'south' 
            elif theta<360: 
                theta_str = '{:5.3f} degrees south of east'.format(360-theta)
    
        elif label_type == 'horizon':
            if theta == 0: 
                theta_str = 'horizontally' 
            elif theta < 90: 
                theta_str = '{:5.3f} degrees above the horizon'.format(theta)
            elif theta == 90: 
                theta_str = 'up' 
            elif theta<180: 
                theta_str = '{:5.3f} degrees above the horizon'.format(180-theta)
            elif theta == 180: 
                theta_str = 'horizontally' 
            elif theta<270: 
                theta_str = '{:5.3f} degrees below the horizon'.format(theta-180)
            elif theta == 270: 
                theta_str = 'down' 
            elif theta<360: 
                theta_str = '{:5.3f} degrees below the horizon'.format(360-theta)
    
        return theta_str

    
    
    def draw_vector( self, x_start=0,y_start=0, color='black', label='' ):
        return "\\draw[->,{:s}, thick] ({:5.2f},{:5.2f}) -- ({:5.2f},{:5.2f}) node[midway,above,sloped]{{ {} }} ;".format(
            color,x_start,y_start,x_start+self.xcomp,y_start+self.ycomp, label) 

 

    def draw_components( self, x_start=0,y_start=0, color='red', label_x='', label_y='' ): 
        # input x and y component of a vector, color, starting coordinate
        # return a string that draws the main vector and the components. 
        out_str = ''  
        out_str += "\\draw[->,{:s},dashed] ({:5.2f},{:5.2f}) -- ({:5.2f},{:5.2f}) node[midway,below]{{ {} }};".format(color,x_start,y_start,x_start+self.xcomp, y_start, label_x ) 
        out_str += "\\draw[->,{:s},dashed] ({:5.2f},{:5.2f}) -- ({:5.2f},{:5.2f}) node[midway,right]{{ {} }};".format(color,x_start+self.xcomp,y_start,x_start+self.xcomp,y_start+self.ycomp, label_y ) 
    
        return out_str
 

    def draw_angle( self, x_start=0,y_start=0, rad=2., color='black', label=''  ): 
        return '\\draw[->,{}] ({:5.2f},{:5.2f}) arc (0:{:5.2f}:{:5.2f}) node[midway,anchor=west] {{ {} }} ;'.format( color, x_start+rad, y_start, self.angle*180/np.pi+1, rad, label ) 
 

##############################
# end of class ----------------
def draw_head_to_tail( vectors, x_start=0, y_start=0, color='black', labels=[]) : 
    out_str = ''
    x_prev = x_start
    y_prev = y_start
    for j,vec in enumerate(vectors):
        if not labels: templabel = ''
        else: templabel = labels[j] 
        out_str += vec.draw_vector( x_start=x_prev, y_start=y_prev, color=color, label=templabel) 
        x_prev = x_prev + vec.xcomp  
        y_prev = y_prev + vec.ycomp  

    return out_str 


def get_resultant( vecs ) : 
    outVec = vector( ) 
    for vec in vecs: 
        outVec = outVec.add(vec)      
    return outVec


########## Testing 
# # Test cases for init
# print( '----------------  Testing __init__ ' ) 
# testCases = [
# ( vector(), 0, 0, 0, 0    ) , 
# ( vector(mag=1,angle=0.), 1, 0, 1, 0    ) , 
# ( vector(xcomp=1,ycomp=0 ) 1, 0, 1, 0     ) , 
# ( vector(xcomp=1,ycomp=np.sqrt(3) ), 2, np.pi/3, 1, np.sqrt(3)     ) , 
# ( vector(xcomp=-1,ycomp=np.sqrt(3) ), 2, 2*np.pi/3, -1, np.sqrt(3)     ) , 
# ( vector(xcomp=-1,ycomp=-np.sqrt(3) ), 2, np.pi+np.pi/3, -1, -np.sqrt(3)     ) , 
# ( vector(mag=2, angle=4*np.pi/3 ), 2, np.pi+np.pi/3, -1, -np.sqrt(3)     ) , 
# ( vector(mag=2, angle=np.pi/4 ), 2, np.pi/4, 2/np.sqrt(2), 2/np.sqrt(2)      ) , 
# ( vector(mag=2, angle=3*np.pi/4 ), 2, 3*np.pi/4, -2/np.sqrt(2), 2/np.sqrt(2)      ) , 
# ( vector(xcomp=-np.sqrt(2),ycomp=np.sqrt(2) ), 2, 3*np.pi/4, -2/np.sqrt(2), 2/np.sqrt(2) ) , 
# ]
# 
# 
# count = 0 
# for test in testCases: 
#     if not(  abs( test[0].mag - test[1]   ) < 0.1 ) or \
#         not( abs( test[0].angle -  test[2]) < 0.1 ) or  \
#         not( abs( test[0].xcomp -  test[3]) < 0.1 ) or  \
#         not( abs( test[0].ycomp -  test[4]) < 0.1 )  : 
#         print( 'Failed case {}'.format(count) )
#         print( test[0] ) 
#         print( test[1] , test[2], test[3], test[4] ) 
#         quit()
#     count += 1 
# print( 'Success in all {} cases'.format(count)  ) 


# print( '----------------  Testing vector add ' ) 
# testCases = [
# ( vector(xcomp=2,ycomp=0), vector(xcomp=1,ycomp=0), 3, 0   ) , 
# ( vector(xcomp=0,ycomp=2), vector(xcomp=1,ycomp=0), 1, 2   ) , 
# ( vector(xcomp=0,ycomp=10), vector(xcomp=1,ycomp=10), 1, 20   ) , 
# ( vector(xcomp=0,ycomp=-3), vector(xcomp=1,ycomp=10), 1, 7   ) , 
# ]
# 
# 
# count = 0 
# for test in testCases: 
#     out = test[0].add(test[1]) 
#     if  not( abs( out.xcomp -  test[2]) < 0.1 ) or  \
#         not( abs( out.ycomp -  test[3]) < 0.1 )  : 
#         print( 'Failed case {}'.format(count) )
#         print( test[0] ) 
#         print( test[1] )
#         print( 'add: ' , out) 
#         print( test[2], test[3]  ) 
#         quit()
#     count += 1 
# print( 'Success in all {} cases'.format(count)  ) 



#print( '----------------  Testing vector multiply ' ) 
#testCases = [
#( vector(xcomp=2,ycomp=0), 5, 10, 0   ) , 
#( vector(xcomp=2,ycomp=0), 0, 0, 0   ) , 
#( vector(xcomp=2,ycomp=0), -1, -2, 0   ) , 
#]
#
#
#count = 0 
#for test in testCases: 
#    out = test[0].scalarMultiply(test[1]) 
#    if  not( abs( out.xcomp -  test[2]) < 0.1 ) or  \
#        not( abs( out.ycomp -  test[3]) < 0.1 )  : 
#        print( 'Failed case {}'.format(count) )
#        print( test[0] ) 
#        print( test[1] )
#        print( 'add: ' , out) 
#        print( test[2], test[3]  ) 
#        quit()
#    count += 1 
#print( 'Success in all {} cases'.format(count)  ) 


# print( '--------------  simple test of draw functions ---------- ' ) 
# vec  =  vector( xcomp=3, ycomp=2 ) 
# print( vec.draw_vector( 0,0, "blue" )  ) 
# vectors = [ vector( xcomp=1,ycomp=1 ) , vector( xcomp=2, ycomp=2) , vector(xcomp=1,ycomp=1) ] 
# print( draw_head_to_tail( vectors,0,0, "blue" )  ) 








