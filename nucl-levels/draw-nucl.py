def draw_one_nucl( nucl_config, draw_config ):
    canv = ROOT.TCanvas( "canv", nucl_config.name,
        draw_config.x_size, draw_config.y_size )
    #
    min_E = nucl_config.levels[0][0]
    max_E = nucl_config.levels[-1][0]
    scale_factor = max_E - min_E
    #
    ll = []; tl = []; el = []; sp = []
    for ii in range(len(nucl_config.levels)):
        lE  = nucl_config.levels[ii][0]
        yy  = draw_config.low 
        yy += (draw_config.high-draw_config.low)*lE/scale_factor
        ll.append(ROOT.TLine(
            draw_config.left  , yy ,
            draw_config.right , yy ))
        tl.append( ROOT.TLatex( draw_config.right + draw_config.r_step, 
                                yy + draw_config.ry_corr, 
                                nucl_config.levels[ii][4]) )
        el.append( ROOT.TLatex( draw_config.left, 
                                yy + draw_config.e_corr, 
                                str(nucl_config.levels[ii][0]) ) )
        sp_str = str(nucl_config.levels[ii][1])
        if nucl_config.levels[ii][2]>=0:
            sp_str += "^{#plus}, "
        else:
            sp_str += "^{#minus}, "
        sp_str += ("T=" + str( nucl_config.levels[ii][3] ) )
        sp.append( ROOT.TLatex( draw_config.right + draw_config.sp_x_corr, 
                                yy + draw_config.e_corr, 
                                sp_str ) )
    #ll.append( ROOT.TLine(0.1,0.2,0.8,0.9) )
    ll[0].SetLineWidth(3)
    #
    for line in ll:
        line.Draw()
    for time_label in tl:
        time_label.Draw()
    for energy_label in el:
        energy_label.Draw()
    for sp_label in sp:
        sp_label.Draw()
    #
    nucl_label = ROOT.TLatex(draw_config.nucl_x, draw_config.nucl_y, nucl_config.nucl)
    nucl_label.SetTextSize(0.2)
    nucl_label.Draw()
    #
    fig_name  = draw_config.prefix + "_"
    fig_name += nucl_config.name   + "."
    fig_name += draw_config.format
    #
    canv.Print(fig_name)
    canv.Close()

draw_one_nucl(nucl_config,draw_config)