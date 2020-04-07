#===============================================================================
# BEGIN
#===============================================================================
from math import sin, cos, pi
#===============================================================================
canv = ROOT.TCanvas(canv_name, canv_title, canv_size_x, canv_size_y)
#===============================================================================
max_X = 0 ; max_Y = 0
for state in states:
    if abs(state[0])>max_X:
        max_X = abs( state[0] )
    if abs(state[1])>max_Y:
        max_Y = abs( state[1] )
max_XY = (max_X, max_Y)
#===============================================================================
def convert_coordinate( state , max_XY ):
    xnew = state[0]*(0.5-state_map_offset)/max_XY[0] + 0.5
    ynew = state[1]*(0.5-state_map_offset)/max_XY[1] + 0.5
    lx = xnew + state_label_dist*cos(state[4]*pi/180.)
    ly = ynew + state_label_dist*sin(state[4]*pi/180.)
    return( (xnew, ynew, lx, ly) )
#===============================================================================
tl_ss = []; m_ss = []
def add_state( state , max_XY ):
    pos = convert_coordinate( state , max_XY )
    m_s =  ROOT.TArc(pos[0], pos[1], 0.01*state[3])
    if state[3]!=1:
        m_s.SetFillStyle(0)
    m_ss .append( m_s )
    tls = ROOT.TLatex(pos[2], pos[3], state[2])
    tls.SetTextSize( state_label_size )
    tl_ss.append( tls )
# c0 = ROOT.TArc(0,0,r0); c0.SetLineWidth(3); c0.SetFillStyle(0)
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
for state in states:
    add_state( state , max_XY )
#===============================================================================
for mr in m_ss:
    mr.Draw()
for tl in tl_ss:
    tl.Draw()
#===============================================================================
canv.Print( out_file_name )
canv.Close()
#===============================================================================
# END
#===============================================================================
