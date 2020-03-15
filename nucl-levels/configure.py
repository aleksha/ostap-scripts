class DrawConfig :
    """ Config class for drawing options.
    """
    def __init__(self):
        self.x_size  =  200 
        self.y_size  =  800
        self.low     =  0.1
        self.high    =  0.9
        self.left    =  0.1
        self.right   =  0.7
        self.r_step  =  0.05
        self.e_corr  =  0.01
        self.ry_corr = -0.005
        self.prefix = "Levels"
        self.format = "png"
        self.list_of_formats = ["png","pdf","eps","ps","gif","root","C","jpg"]

    def set_xy_sizes(self, x, y ):
        "Convert x and y into int and set"
        self.x_size = int(x)
        self.y_size = int(y)

    def set_prefix( self, prfx ):
        "Set prefix string"
        self.prefix = prfx

    def set_format( self, fmt ):
        "Check that format is valid and set"
        if fmt not in self.list_of_formats:
            print("ERROR: Format is not in list_of_formats" )
        else:
            self.format = fmt

dummy_levels = [
    (      0, 3, +1, 0, "stable"),
    ( 718.35, 1, +1, 0, "0.707 ns"),
    (1740.15, 0, +1, 1, "5 fs")
]

class NuclConfig :
    """ Config class for nucleous.
    """
    def __init__( self,  levels = dummy_levels ):
        self.name = "B-10"
        self.nucl = "^(10)_{5}B"
        self.levels = dummy_levels



draw_config = DrawConfig()
nucl_config = NuclConfig()

