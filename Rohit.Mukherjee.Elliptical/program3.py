#Name: Rohit Mukherjee
#Course: 5363 cryptography
#professor: Dr.Terry Griffin
#Program-3:Finding X3 and Y3 when given (X2,Y2) and (X1,Y1) and a,b values.


import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

# function used to find x3 using slope m 
def Finding_X3(x1,x2,m):
    M = m*m
    x3 = M-x1-x2
    return x3

# function to find y3 coordinate using m 
def Finding_Y3(x1,x3,y1,m):
     Mul = m*(x3-x1)
     y3 = y1+Mul
     return y3
     
# used to find if (x1,y1) and (x2,y2) are passing through the curve
def  x1_y1_valid(x1,y1,a,b):
    if((pow(y1, 2) - ( pow(x1, 3) - a*x1 + b )) == 0):
        return True
    else:
        return False
def  x2_y2_valid(x2,y2,a,b):
    if((pow(y2, 2) - ( pow(x2, 3) - a*x2 + b )) == 0):
        return True
    else:
        return False      
       

# used to display the curve and points(x1,y1) , (x2,y2)and (x3,y3)
def curve(x1,y1,x2,y2,a,b):
    m=0.0
    x3=0.0
    y3=0.0
    #Determines width and height of plot
    w = 10
    h = 12
    #To verify whether the two given points lies in the curve.    
    valid1 =x1_y1_valid(x1,y1,a,b)
    valid2 =x2_y2_valid(x2,y2,a,b)
    
    if((valid1 and valid2)==True):
        print("x and y passes through that curve")
    elif((valid1 or valid2)==False):
        print("x and y does not pass through that curve")
        exit()
    # Annotate the plot with your name using width (w) and height (h) as your reference points.
    an1 = plt.annotate("Rohit mukherjee", xy=(-w+2 , h-2), xycoords="data",
                  va="center", ha="center",
                  bbox=dict(boxstyle="round", fc="w"))
    
    # This creates a mesh grid with values determined by width and height (w,h)
    # of the plot with increments of .0001 (1000j = .0001 or 5j = .05)
    y, x = np.ogrid[-h:h:1000j, -w:w:1000j]
    
    # Plot the curve (using matplotlib's countour function)
    # This drawing function applies a "function" described in the
    # 3rd parameter:  pow(y, 2) - ( pow(x, 3) - x + 1 ) to all the
    # values in x and y.
    # The .ravel method turns the x and y grids into single dimensional arrays
    if(a!=0):    
        plt.contour(x.ravel(), y.ravel(), pow(y, 2) - ( pow(x, 3) - x + 1 ), [0])
    elif(a==0):
        plt.contour(x.ravel(), y.ravel(), pow(y, 2) - ( pow(x, 3) - a*x + b ), [0])
    
    if((x1!=x2)and(y1!=y2)):
      m = float(y2-y1)/(x2-x1)
    else:
      m = float(3*x1*x1+a)/(2*y1)
      print("slope is:",m)
    x3 = Finding_X3(x1,x2,m)
    y3 = Finding_Y3(x1,x3,y1,m)
    x3=round(x3,3)    
    y3=round(y3,3)    
    #x3=str(Fraction(x3).limit_denominator())
    #y3=str(Fraction(y3).limit_denominator())
    print(x3,y3)
    
    # Plot the points ('ro' = red, 'bo' = blue, 'yo'=yellow and so on)
    plt.plot(x1, y1,'ro')
    
    # Annotate point 1
    plt.annotate('x1,y1', xy=(x1, y1), xytext=(x1+1,y1+1),
            arrowprops=dict(arrowstyle="->",
            connectionstyle="arc3"),
            )
    
    plt.plot(x2, y2,'ro')
    
    # Annotate point 2
    plt.annotate('x2,y2', xy=(x2, y2), xytext=(x2+1,y2+1),
            arrowprops=dict(arrowstyle="->",
            connectionstyle="arc3"),
            )
    
    # Use a contour plot to draw the line (in pink) connecting our point.
    plt.contour(x.ravel(), y.ravel(), (y-y1)-m*(x-x1), [0],colors=('maroon'))
    
    
    
    # I hard coded the third point, YOU will use good ol mathematics to find
    # the third point
    print(x3,y3)    
    plt.plot(x3, y3,'yo')
    
    # Annotate point 3
    plt.annotate('x3,y3', xy=(x3, y3), xytext=(x3+1,y3+1),
            arrowprops=dict(arrowstyle="->",
            connectionstyle="arc3"),
            )
#    
    #plt.contour(x.ravel(), y.ravel(), (y-y1)-m*(x-x1), [0],colors=('blue'))
    
    # Show a grid background on our plot
    plt.grid()
    
    # Show the plot
    plt.show()

if __name__ == '__main__':
  pass