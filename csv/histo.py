
from ostap.histos.histos import h1_axis 
from   ostap.math.ve import VE

csv_file = open("325.csv","r")

pt_bins = [1,2,3,4,5,6,7,8]

hR_5tev = h1_axis(pt_bins)
hR_7tev = h1_axis(pt_bins)
hR_13tev = h1_axis(pt_bins)

hR_5tev.blue()
hR_13tev.red()

bin=0
for line in csv_file:
    bin+=1
    w = line[:-1].split(",")
    hR_5tev [bin] = VE(float(w[ 3]),float(w[ 6])**2)
    hR_7tev [bin] = VE(float(w[ 7]),float(w[10])**2)
    hR_13tev[bin] = VE(float(w[11]),float(w[14])**2)
    print(w)


hR_5tev.GetYaxis().SetRangeUser(0,4)
hR_5tev.GetXaxis().SetTitleSize(0.05)
hR_5tev.GetXaxis().SetTitle("p_{T}, GeV/c")
hR_5tev.GetYaxis().SetTitle("( d#sigma(D*)/dp_{T} ) / ( d#sigma(D^{0})/dp_{T} )")

hR_5tev.Draw("e1")
hR_7tev.Draw("same e1")
hR_13tev.Draw("same e1")

canvas >> "Fig_325"

def is_consistent( h1, h2, title =  " ", p_min = 0.003 ):
    """Chack that two histo sith same binning are consistent"""
    print("\n\n"+title)
    hd = h1 - h2
    r = hd.Fit("pol0","S")
    print(r)

is_consistent( hR_5tev,  hR_7tev, " 5 and  7 TeV")
is_consistent( hR_5tev, hR_13tev, " 5 and 13 TeV")
is_consistent( hR_7tev, hR_13tev, " 7 and 13 TeV")
