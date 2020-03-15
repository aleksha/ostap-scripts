def draw_one_nucl( nucl_config, draw_config ):
    canv = ROOT.TCanvas( "canv", nucl_config.name,
        draw_config.x_size, draw_config.y_size )
    #
    fig_name  = draw_config.prefix + "_"
    fig_name += nucl_config.name   + "."
    fig_name += draw_config.format
    #
    canv.Draw(fig_name)
    canv.Close()