#===============================================================================
sx = 5.
sy = 7.
N  = 1000000
#===============================================================================
from math import sqrt
#
rand_x = ROOT.TRandom3()
rand_y = ROOT.TRandom2()
#===============================================================================

def quadrant(x,y):
    if x>=0:
        if y>=0:
            return(1)
        return(4)
    if y>=0:
        return(2)
    return(3)
#
#class Anode:
#    def __init__(self,)
#
#===============================================================================
#  Generate sample
msxy = max(sx,sy)
h2 = ROOT.TH2F("h2"," ",100,-6.*msxy,6.*msxy,
                       100,-6.*msxy,6.*msxy)
#
#h2.GetXaxis().SetTitle("x, mm")
#h2.GetYaxis().SetTitle("y, mm")
#
smpl = []
for i in range(N):
    x = rand_x.Gaus(0.,sx)
    y = rand_y.Gaus(0.,sy)
    h2.Fill(x,y)
    smpl.append(  sqrt(x**2+y**2) )
#===============================================================================
import numpy as np
sample = np.array( smpl )
#===============================================================================
#print("Median         : " + str( np.median  ( sample        ) ) )
r0 = np.quantile( sample, 0.5   )
r1 = np.quantile( sample, 0.9   )
r2 = np.quantile( sample, 0.999 )
print("50% quantile   : " + str( r0 ) )
print("90% quantile   : " + str( r1 ) )
print("99.9% quantile : " + str( r2 ) )
#
c0 = ROOT.TArc(0,0,r0); c0.SetLineWidth(3); c0.SetFillStyle(0)
c1 = ROOT.TArc(0,0,r1); c1.SetLineWidth(3); c1.SetFillStyle(0)
c2 = ROOT.TArc(0,0,r2); c2.SetLineWidth(3); c2.SetFillStyle(0)
#
l1 = ROOT.TLine( r0, 0., r2, 0.); l1.SetLineWidth(3)
l2 = ROOT.TLine( 0., r0, 0., r2); l2.SetLineWidth(3)
l3 = ROOT.TLine(-r0, 0.,-r2, 0.); l3.SetLineWidth(3)
l4 = ROOT.TLine( 0.,-r0, 0.,-r2); l4.SetLineWidth(3)
#
tx = ROOT.TLatex( -5.*msxy, 5.*msxy, "#sigma_{x} = " + str(sx) + " mm" )
ty = ROOT.TLatex( -5.*msxy, 4.*msxy, "#sigma_{y} = " + str(sy) + " mm" )
tx.SetTextSize(0.03)
ty.SetTextSize(0.03)
#
t0 = ROOT.TLatex( 3.5*msxy, 5.*msxy, "r_{0} = " + "{0:4.1f}".format(r0) + " mm" )
t1 = ROOT.TLatex( 3.5*msxy, 4.*msxy, "r_{1} = " + "{0:4.1f}".format(r1) + " mm" )
t2 = ROOT.TLatex( 3.5*msxy, 3.*msxy, "r_{2} = " + "{0:4.1f}".format(r2) + " mm" )
t0.SetTextSize(0.03)
t1.SetTextSize(0.03)
t2.SetTextSize(0.03)
#===============================================================================
canv = ROOT.TCanvas("canv","canv",700,700)
h2.Draw("col")
c0.Draw(); t0.Draw()
c1.Draw(); t1.Draw()
c2.Draw(); t2.Draw()
l1.Draw()
l2.Draw()
l3.Draw()
l4.Draw()
tx.Draw()
ty.Draw()
canv.Print("RESULT.png")
canv.Close()
