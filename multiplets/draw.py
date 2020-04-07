#===============================================================================
# BEGIN
#===============================================================================
canv = ROOT.TCanvas(canv_name, canv_title, canv_size_x, canv_size_y)
#===============================================================================
ll_ax = ROOT.TArrow(axis_x_params["offset"],0.5, (1.0-axis_x_params["offset"]), 0.5, 0.02,"|>")
ll_ax.SetLineWidth(axis_x_params["width"])
ll_ax.SetLineStyle(axis_x_params["style"])
#
tl_ax = ROOT.TLatex( (1.0-axis_x_params["offset"]),
                     (0.5-axis_y_params["offset"]),
                     axis_x_params["title"] )
tl_ax.SetTextSize(axis_x_params["size"])
tl_ax.SetTextFont(axis_x_params["font"])
#
ll_ay = ROOT.TArrow(0.5, axis_y_params["offset"],0.5,(1.0-axis_y_params["offset"]), 0.02,"|>")
ll_ay.SetLineWidth(axis_y_params["width"])
ll_ay.SetLineStyle(axis_y_params["style"])
#
tl_ay = ROOT.TLatex( (0.5+axis_x_params["offset"]),
                     (1.0-axis_y_params["offset"]),
                     axis_y_params["title"] )

tl_ay.SetTextSize(axis_y_params["size"])
tl_ay.SetTextFont(axis_y_params["font"])
#
tl_ti = ROOT.TLatex( (1.0-4.*axis_x_params["offset"]),
                     (1.0-2.*axis_y_params["offset"]),
                     fig_title )
tl_ti.SetTextSize(0.07)
tl_ti.SetTextFont(22)
#tl_dd = ROOT.TLatex(0.5,0.3,"Xyz"); tl_dd.Draw()
tl_ax.Draw(); tl_ay.Draw(); tl_ti.Draw()
#
ll_ax.Draw(); ll_ay.Draw()
#
#print( axis_x_params["title"] )
#print( axis_y_params["title"] )
#print( canv.GetWindowWidth() *(1.0-axis_x_params["offset"]) )
#print( canv.GetWindowHeight()*(0.5+axis_y_params["offset"]) )
#===============================================================================
canv.Print( out_file_name )
canv.Close()
#===============================================================================
# END
#===============================================================================
