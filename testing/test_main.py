import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_variables(self) :
        self.assertTrue( "cv_temperatures" in globals(), "there is no variable in your code called cv_temperatures" )
        self.assertTrue( "cv" in globals(), "there is no variable in your code called cv" )
        self.assertTrue( "cv_errors" in globals(), "there is no variable in your code called cv_errors" )
        
    def test_errorbars(self) :
        self.assertTrue( len(cv_errors)==10, "cv_errors has the wrong length" )
        filedata = np.loadtxt("md_results.txt")
        for i in range(len(cv_errors) ) :
            tmid = ( filedata[i,4] + 2*filedata[i,1]*filedata[i,2] ) / ( filedata[i,0]*filedata[i,0] )
            self.assertTrue( np.abs(tmid - cv_errors[i])<1E-6, "The error bars for your graph are incorrect" )
            
    def test_yvalues(self) :
        self.assertTrue( len(cv)==10, "cv has the wrong length" )
        filedata = np.loadtxt("md_results.txt")
        for i in range(len(cv) ) :
            cv_val = filedata[i,3] - filedata[i,1]*filedata[i,1]
            cv_val = cv_val / (filedata[i,0]*filedata[i,0] )
            self.assertTrue( np.abs(cv_val - cv[i])<1E-6, "the heat capacities have been computed wrongly"  )
            
    def test_xvalues(self) :
        self.assertTrue( len(cv_temperatures)==10, "cv_temperatures has the wrong length" )
        filedata = np.loadtxt("md_results.txt")
        for i in range(len(cv_temperatures) ) :
            self.assertTrue( np.abs(filedata[i,0] - cv_temperatures[i])<1E-6, "the temperatures at which you have plotted the heat capacities are incorrect" )
