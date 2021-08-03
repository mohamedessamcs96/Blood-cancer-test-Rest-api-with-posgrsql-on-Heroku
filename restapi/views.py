from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



from .models import UserData
from .serializers import UserSerializers

import os
import joblib




#loaded_model=joblib.load(bloodmodel)
#loaded_model=joblib.load(open(r"C:\Users\Copy Center\Desktop\Cancer diagnos with blood analysis\Blood analysis rest api\localserver\cancerdiagnose\restapi\model\bloodmodel", 'rb'))

#loaded=os.path.join(os.path.dirname(os.path.dirname(__file__)),str('/model/bloodmodel'))

#loaded_model=joblib.load('Bloodmodel')

#loaded_model=joblib.load(open(r"restapi\bloodmodel", 'rb'))
import pandas as pd
from sklearn.preprocessing import StandardScaler
url='https://raw.githubusercontent.com/mohamedessamcs96/RestApi-for-cancer-diagnose-with-blood-analysis/master/cancerdiagnose/restapi/model/Blood%20Analysis.csv'


from sklearn.svm import SVC 
import joblib



def home(request):
    return HttpResponse('add users to your url')



class userList(APIView):
    def get(self,request):
        users=UserData.objects.all()
        serializer=UserSerializers(users,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        age=int(self.request.data['age'])
        bmi=float(self.request.data['bmi'])
        glucouse=float(self.request.data['glucouse'])
        insuline=float(self.request.data['insuline'])
        homa=float(self.request.data['homa'])
        leptin=float(self.request.data['leptin'])
        adiponcetin=float(self.request.data['adiponcetin'])
        resistiin=float(self.request.data['resistiin'])
        mcp=float(self.request.data['mcp'])
        #Machine Learning Model



        #cancer_diagnosis=pd.read_csv(url,delimiter=',',skipinitialspace=True)
        
        #X=cancer_diagnosis[['Age','BMI','Glucose','Insulin','HOMA','Leptin','Adiponectin','Resistin','MCP.1']]
        #y=cancer_diagnosis['Classification']
        #from sklearn.neighbors import KNeighborsClassifier
        #sc_X=StandardScaler()
        #X=sc_X.fit_transform(X)
        #knn = KNeighborsClassifier()
        #knn.fit(X,y)

        #svm = SVC(C=0.5,kernel='linear')
        #svm.fit(X, y)

        #joblib.dump(svm,"./train_mode.joblib",compress=True)
        clf=joblib.load("train_mode.joblib")
        #Machine Learning Model

        clf=clf.predict([[age,bmi,glucouse,insuline,homa,leptin,adiponcetin,resistiin,mcp]])
        
        for i in range(1):
            if(clf[i]==1):
                self.request.data['classification']="No Cancer" 

            elif(clf[i]==2):
                self.request.data['classification']="Cancer" 
        
        serializer=UserSerializers(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.data,status=404)

