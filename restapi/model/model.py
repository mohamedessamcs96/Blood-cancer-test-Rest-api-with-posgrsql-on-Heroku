import pandas as pd
from sklearn.svm import SVC 
import joblib
cancer_diagnosis=pd.read_csv('Blood Analysis.csv', delimiter=',')
X=cancer_diagnosis[['Age','BMI','Glucose','Insulin','HOMA','Leptin','Adiponectin','Resistin','MCP.1']]
y=cancer_diagnosis['Classification']
svm = SVC()
svm.fit(X, y)
joblib.dump(svm,'bloodmodel.pkl')
clf=joblib.load('bloodmodel.pkl')
clf=clf.predict([[10000,5000,40,50,2000,16,9,2,1]])
print(clf)
