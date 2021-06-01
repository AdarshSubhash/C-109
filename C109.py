import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
count=[]
diceresult=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceresult.append(dice1+dice2)
mean=sum(diceresult)/len(diceresult)
sd=statistics.stdev(diceresult)
median=statistics.median(diceresult)
mode=statistics.mode(diceresult)   
firstsdstart,firstsdend=mean-sd,mean+sd
secondsdstart,secondsdend=mean-(2*sd),mean+(2*sd)
thirdsdstart,thirdsdend=mean-(3*sd),mean+(3*sd)
print('Mean is{}'.format(mean))
print('Standard Deviation is{}'.format(sd))
print('Median is{}'.format(median))
print('Mode is{}'.format(mode))
fig=ff.create_distplot([diceresult],['result'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[firstsdstart,firstsdstart],y=[0,0.17],mode="lines",name="SD1"))
fig.add_trace(go.Scatter(x=[firstsdend,firstsdend],y=[0,0.17],mode="lines",name="SD1"))
fig.add_trace(go.Scatter(x=[secondsdstart,secondsdstart],y=[0,0.17],mode="lines",name="SD2"))
fig.add_trace(go.Scatter(x=[secondsdend,secondsdend],y=[0,0.17],mode="lines",name="SD2"))
fig.show()
listofdatawithinfirstsd=[result for result in diceresult if result>firstsdstart and result<firstsdend]
listofdatawithinsecondsd=[result for result in diceresult if result>secondsdstart and result<secondsdend]
listofdatawithinthirdsd=[result for result in diceresult if result>thirdsdstart and result<thirdsdend]
print("{}% of datalieswithin firstsd".format(len(listofdatawithinfirstsd)*100.0/len(diceresult)))
print("{}% of datalieswithin secondsd".format(len(listofdatawithinsecondsd)*100.0/len(diceresult)))
print("{}% of datalieswithin thirdsd".format(len(listofdatawithinthirdsd)*100.0/len(diceresult)))