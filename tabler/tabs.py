__doc__ = """Module to handle plain-text-tabels"""
#===============================================================================
from ostap.histos.histos import h1_axis, h2_axes
from   ostap.math.ve import VE
#===============================================================================
def dump(file_name):
    "Dump file to terminal"
    with open(file_name,"r") as f:
        for line in f:
            print(line[:-1])
#===============================================================================
def get_2d_bin(x, x_bins, y, y_bins):
    "Return bin-tuple for ROOT.TH2 conventions"
    i = x_bins.index( x ) + 1
    j = y_bins.index( y ) + 1
    return( (i,j) )
#===============================================================================
def header( file_name ):
    "Return table headers"
    with open(file_name,"r") as f:
        for line in f:
            if line[0]=="H":
                header = line[1:-1]
    return header
#===============================================================================
def find_vars( file_name, xvar, yvar, zvar ):
    "Return tuple with indexes for xvar, y var and zvar"
    xidx=-1; yidx=-1; zidx=-1;
    with open(file_name,"r") as f:
        for line in f:
            if line[0]=="v":
                wl = line[1:-1].split("|")
                for w in wl:
                    if w.strip()==xvar:
                        xidx = wl.index(w)
                    if w.strip()==yvar:
                        yidx = wl.index(w)
                    if w.strip()==zvar:
                        zidx = wl.index(w)
    return xidx, yidx, zidx
#===============================================================================
def h2( file_name, xvar, x_bins, yvar, y_bins, zvar):
    "Create 2d histo"
    h2 = h2_axes(x_bins, y_bins)
    print( "\nCreating 2D-histo:")
    print( "FILE   : " + file_name)
    print( "HEADER : " + header(file_name) )
    print( " x_var : " + xvar )
    print( " y_var : " + yvar )
    print( " z_var : " + zvar )
    xidx, yidx, zidx = find_vars(file_name, xvar, yvar, zvar)
    with open(file_name,"r") as f:
        for line in f:
            if line[0:2]==" |":
                wl = line[1:-1].split("|")
                for w in wl:
                    x_min = float( wl[xidx].split(",")[0]  )
                    y_min = float( wl[yidx].split(",")[0]  )
                    z_val = float( wl[zidx].split("+-")[0] )
                    z_err = float( wl[zidx].split("+-")[1] )
                    h2[ get_2d_bin(x_min,x_bins, y_min, y_bins) ] = VE( z_val, z_err**2 )
    return h2
#===============================================================================
#def parse(file_name):
#    """
#    Return a tuple with dictionaries
#
#    INPUT:
#    #---------------------
#    H Header
#    #---------------------
#    v| x |  bin |   ve   |
#    #---------------------
#     | 1 | 0, 1 | 2 +- 1 |
#     | 2 | 1, 2 | 4 +- 2 |
#    #---------------------
#
#    OUTPUT: tuple of dictionaries with fields as table variable
#
#    ({"x":1,"bin":(0,1),"ve":VE(2,1**2)},{"x":2,"bin":(1,2),"ve":VE(4,2**2)})
#
#    """
#    f = open(file_name,"r")
#    # print Header
#    for line in f:
#        if line[0]=="H":
#            print("LOADING : " + line[1:-1])
#    # load
#    for line in f:
#        if line[0]=="v":
#            w = line[1:-1].split("|")
#    f.close()

