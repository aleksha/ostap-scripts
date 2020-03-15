def draw_one_nucl( nucl_config, draw_config ):
    canv = ROOT.TCanvas( "canv", nucl_config.name,
        draw_config.x_size, draw_config.y_size )
    #
    min_E = nucl_config.levels[0][0]
    max_E = nucl_config.levels[-1][0]
    print(min_E)
    print(max_E)
    #for ii in range(len(nucl_config.levels)):
    #
    fig_name  = draw_config.prefix + "_"
    fig_name += nucl_config.name   + "."
    fig_name += draw_config.format
    #
    canv.Print(fig_name)
    canv.Close()

draw_one_nucl(nucl_config,draw_config)