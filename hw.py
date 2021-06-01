import pandas as pd
import csv
import statistics
import plotly.graph_objects as go
df=pd.read_csv("height-weight.csv")
heightlist=df["Height"].to_list()
weightlist=df["Weight"].to_list()
#mean1
heightmean=statistics.mean(heightlist)
weightmean=statistics.mean(weightlist)
#median1
heightmedian=statistics.median(heightlist)
weightmedian=statistics.median(weightlist)
#mode1
heightmode=statistics.mode(heightlist)
weightmode=statistics.mode(weightlist)
#sd1
heightsd=statistics.stdev(heightlist)
weightsd=statistics.stdev(weightlist)
print("mean,median and mode of height is {},{} and {}".format(heightmean,heightmedian,heightmode))
print("mean,median and mode of weight is {},{} and {}".format(weightmean,weightmedian,weightmode))
print("sd of height is {}".format(heightsd))
print("sd of weight is {}".format(weightsd))
#Height
Hfirstsdstart,Hfirstsdend=heightmean-heightsd,heightmean+heightsd
Hsecondsdstart,Hsecondsdend=heightmean-(2*heightsd),heightmean+(2*heightsd)
Hthirdsdstart,Hthirdsdend=heightmean-(3*heightsd),heightmean+(3*heightsd)
#Weight
Wfirstsdstart,Wfirstsdend=weightmean-weightsd,weightmean+weightsd
Wsecondsdstart,Wsecondsdend=weightmean-(2*weightsd),weightmean+(2*weightsd)
Wthirdsdstart,Wthirdsdend=weightmean-(3*weightsd),weightmean+(3*weightsd)

heightlistofdatawithinfirstsd=[result for result in heightlist if result>Hfirstsdstart and result<Hfirstsdend]
heightlistofdatawithinsecondsd=[result for result in heightlist if result>Hsecondsdstart and result<Hsecondsdend]
heightlistofdatawithinthirdsd=[result for result in heightlist if result>Hthirdsdstart and result<Hthirdsdend]

weightlistofdatawithinfirstsd=[result for result in weightlist if result>Wfirstsdstart and result<Wfirstsdend]
weightlistofdatawithinsecondsd=[result for result in weightlist if result>Wsecondsdstart and result<Wsecondsdend]
weightlistofdatawithinthirdsd=[result for result in weightlist if result>Wthirdsdstart and result<Wthirdsdend]

print("{}% of data for height lies within 1sd ".format(len(heightlistofdatawithinfirstsd)*100.0/len(heightlist)))
print("{}% of data for height lies within 2sd ".format(len(heightlistofdatawithinsecondsd)*100.0/len(heightlist)))
print("{}% of data for height lies within 3sd ".format(len(heightlistofdatawithinthirdsd)*100.0/len(heightlist)))

print("{}% of data for weight lies within 1sd ".format(len(weightlistofdatawithinfirstsd)*100.0/len(weightlist)))
print("{}% of data for weight lies within 2sd ".format(len(weightlistofdatawithinsecondsd)*100.0/len(weightlist)))
print("{}% of data for weight lies within 3sd ".format(len(weightlistofdatawithinthirdsd)*100.0/len(weightlist)))