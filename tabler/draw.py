import ROOT
def draw2d( canvas, histo2d, name, opts, rng, fmt = "2.2f"):
    histo2d.GetZaxis().SetRangeUser(rng[0], rng[1])
    ROOT.gStyle.SetPaintTextFormat(fmt)
    histo2d.Draw(opts)
    canvas.Print(name)
