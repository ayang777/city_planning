import pandas as pd
from sklearn import metrics
from sklearn import preprocessing
from sklearn.cluster import KMeans

# created a new CSV with no san francisco column or ID column
# only street address and neighborhood column
inputfilename = "SanFrancisco_UberData_noID.csv"
data = pd.read_csv(inputfilename, encoding='utf-8')

# have to normalize labels because data is not discrete
le = preprocessing.LabelEncoder()

encoded_data = data.apply(le.fit_transform)
encoded_data.to_csv("encoded_data.csv", sep='\t', encoding='utf-8')
featureNames = list(data)

features = [] # 75% of data
for row in range(0, 148):
	features.append(encoded_data.iloc[row])
labels = [] # 25% of data
for row in range(148, data.shape[0]):
	labels.append(encoded_data.iloc[row])

kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(features)
kmeans.predict(labels)

# printing out the cluster assignments
# these are the ENCODED cluster assignments
# I couldn't get it to work to transform it back to the string
# to get around this, I am printing the encoded data then manually
# finding what the values printed below map to in the encoded data CSV
for value in kmeans.cluster_centers_:
	print(value)
	#print(le.inverse_transform(value[0])) #not working
