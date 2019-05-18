import pandas as pd 
import quandl 
import numpy
import math
from sklearn import preprocessing,svm, model_selection
from sklearn.linear_model import LinearRegression



quandl.ApiConfig.api_key = "f1XKZXDBqeXGTDc797UY"
df = quandl.get('BATS/EDGA_XLTY')
# mydata = quandl.get("FRED/GDP")
# print df
# print mydata

# for item in mydata:
#     # print item
# print mydata['Value']
df=df[['Total Volume','Short Volume']]

df['diff']=(df['Total Volume'] + df['Short Volume'])/ len(df['Total Volume'] )

forcast_col='diff'

df.fillna(-99999, inplace=True)

forcast_out=int(math.ceil(0.1*len(df)))



df['label'] = df[forcast_col].shift(-forcast_out)

df.dropna(inplace=True)


X= numpy.array(df.drop(['label'],1))
y = numpy.array(df['label'])

X = preprocessing.scale(X)

df.dropna(inplace=True)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.1)


clf= LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
accuracy=clf.score(X_test,y_test)


print accuracy

