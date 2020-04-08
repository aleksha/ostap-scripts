#===============================================================================
title =    ROOT.TLatex( 1.05,-2.00,"J^{P}=#frac{3}{2}^{#plus}")
#
states = [ ROOT.TLatex(-1.60, 1.10, "#Delta^{#minus}"  ),
           ROOT.TLatex(-0.60, 1.10, "#Delta^{0}"       ),
           ROOT.TLatex( 0.40, 1.10, "#Delta^{+}"       ),
           ROOT.TLatex( 1.40, 1.10, "#Delta^{++}"      ),
           ROOT.TLatex(-1.10, 0.10, "#Sigma^{*#minus}" ),
           ROOT.TLatex(-0.10, 0.10, "#Sigma^{*0}"      ),
           ROOT.TLatex( 0.90, 0.10, "#Sigma^{*#plus}"  ),
           ROOT.TLatex(-0.60,-0.90, "#Xi^{*#minus}"    ),
           ROOT.TLatex( 0.40,-0.90, "#Xi^{*0}"         ),
           ROOT.TLatex(-0.10,-1.90, "#Omega^{#minus}"  )]
#===============================================================================
# BEGIN
#===============================================================================
from math import sin, cos, pi
from ostap.histos.graphs import *
#===============================================================================
canv = ROOT.TCanvas("canv","my_canvas",800,800)
#===============================================================================
gr = makeGraph( [-1.5,-0.5,0.5,1.5,-1,0,1, -0.5,0.5, 0 ], [1,1,1,1, 0,0,0, -1,-1, -2])
gr.SetMarkerStyle(20)
gr.SetMarkerSize(2)
gr.GetYaxis().SetRangeUser(-2.2,1.5)
gr.GetXaxis().SetTitle("Isospin projection")
gr.GetYaxis().SetTitle("Hypercharge")
gr.GetXaxis().SetTitleOffset( 1.4) ; gr.GetYaxis().SetTitleOffset( 1.1)
gr.GetXaxis().SetTitleSize(  0.04) ; gr.GetYaxis().SetTitleSize(  0.04)
#gr.GetXaxis().CenterTitle()        ; gr.GetYaxis().CenterTitle()
gr.Draw("AP");
#===============================================================================
#print("X axis")
#print( gr.GetXaxis().GetTitleColor()  )
#print( gr.GetXaxis().GetTitleFont()   )
#print( gr.GetXaxis().GetTitleOffset() )
#print( gr.GetXaxis().GetTitleSize()   )
#print("Y axis")
#print( gr.GetYaxis().GetTitleColor()  )
#print( gr.GetYaxis().GetTitleFont()   )
#print( gr.GetYaxis().GetTitleOffset() )
#print( gr.GetYaxis().GetTitleSize()   )
#===============================================================================
ROOT.gPad.SetGridx()
ROOT.gPad.SetGridy()
for tl in states:
    tl.SetTextSize(0.05)
    tl.Draw()
title.Draw()
canv.Print( "EasyMultiplet.png" )
canv.Close()
#===============================================================================
# END
#===============================================================================
