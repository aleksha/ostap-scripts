class DrawConfig :
    """ Config class for drawing options.
    """
    def __init__():
        self.x_size = 200 
        self.y_size = 800
        self.prefix = "Levels"
        self.format = "png"
        self.list_of_formats = ["png","pdf","eps","ps","gif","root","C","jpg"]

    def set_xy_sizes( x, y ):
        "Convert x and y into int and set"
        self.x_size = int(x)
        self.y_size = int(y)

    def set_prefix( prfx ):
        "Set prefix string"
        self.prefix = prfx

    def set_format( fmt ):
        "Check that format is valid and set"
        if fmt not in self.list_of_formats:
            print("ERROR: Format is not in list_of_formats" )
            break
        self.format = fmt




