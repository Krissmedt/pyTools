#### Kris' Data Managing Methods####
import pyTools as pt
import os
import numpy as np
from math import sin, cos

def mkDataDir(*args):
    foldername = ""
    for a in range(0,len(args)):
        try:
            foldername = foldername + args[a]
        except TypeError:
            foldername = foldername + str(args[a])
        except:
            print(
                  "Unexptected error, did you enter a string or otherwise" +
                  " parsable value? Code:", sys_exc_info()[0])
    
    k = 1
    error = True
    append = ""
    while error == True:
        try:
            os.mkdir("./" + foldername + append)
            error = False
        except FileExistsError:
            append = "(" + str(k) + ")"
            error = True
            k = k+1
            
    foldername = foldername + append
    
    return foldername


def writePData(pos,tstep,tsteps,**kwargs):
    if "foldername" in kwargs:
        filename = "./" + kwargs[
                          "foldername"] + "/" + str(
                                                tstep) + ".vtu"
    else:
        filename = str(tstep) + ".vtu"
        
    if "vtk_writer" in kwargs:
        vtk_writer = kwargs["vtk_writer"]
    else:
        vtk_writer = pt.VTK_XML_Serial_Unstructured()
    
    vtk_writer.snapshot(filename,pos[:,0],pos[:,1],pos[:,2])
    
    if tstep == (tsteps-1) and "foldername" in kwargs:
        vtk_writer.writePVD("./" 
                             + kwargs["foldername"] 
                             + "/" + "run" + ".pvd")
    elif tstep == (tsteps-1): 
        vtk_writer.writePVD("run" + ".pvd")
