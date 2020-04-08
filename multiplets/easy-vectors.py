#===============================================================================
title =    ROOT.TLatex( 0.55, 1.20,"J^{P}=1^{#minus}")
states = [ ROOT.TLatex(-0.90, 0.05, "#rho^{#minus}"),
           ROOT.TLatex( 0.10, 0.10, "#rho^{0}"     ),
           ROOT.TLatex( 0.85, 0.05, "#rho^{+}"     ),
           ROOT.TLatex(-0.70, 0.80, "K^{*0}"       ),
           ROOT.TLatex( 0.60, 0.80, "K^{*+}"       ),
           ROOT.TLatex(-0.70,-0.90, "K^{*#minus}"  ),
           ROOT.TLatex( 0.60,-0.90, "#bar{K}^{*0}" ),
           ROOT.TLatex(-0.20,-0.20, "#omega"       ),
           ROOT.TLatex( 0.10,-0.20, "#phi"         ) ]
#===============================================================================
# BEGIN
#===============================================================================
from math import sin, cos, pi
from ostap.histos.graphs import *
#===============================================================================
canv = ROOT.TCanvas("canv","my_canvas",800,800)
#===============================================================================
gr = makeGraph( [-1,1,-0.5,0.5,-0.5,0.5,-0.03,0.03,0], [0,0,1,1,-1,-1,-0.03,-0.03,0.03])
gr.SetMarkerStyle(20)
gr.SetMarkerSize(2)
gr.GetYaxis().SetRangeUser(-1.2,1.5)
gr.GetXaxis().SetTitle("Isospin projection")
gr.GetYaxis().SetTitle("Hypercharge")
gr.GetXaxis().SetTitleOffset( 1.4) ; gr.GetYaxis().SetTitleOffset( 1.1)
gr.GetXaxis().SetTitleSize(  0.04) ; gr.GetYaxis().SetTitleSize(  0.04)
gr.GetXaxis().CenterTitle()        ; gr.GetYaxis().CenterTitle()
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
