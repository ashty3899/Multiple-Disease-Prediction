import pickle
from re import L


filename = 'pickel_files/diabetes.pkl'
File = open(filename, 'rb')
diab_model = pickle.load(File)
# [[1,85,66,29,0,26.6,0.351,31]] sample for no
Catagory=["No... You don't have diabetes","Yes, you may have diabetes"]

def diabetes(data):
    arr=[]
    print(data)
    for i,x in data.items():
        if i!="csrfmiddlewaretoken":
            arr.append(float(x))
    arr=[arr]
    result=int(diab_model.predict(arr))
    return Catagory[result]



h_filename = 'pickel_files/heart.pkl'
h_File = open(h_filename, 'rb')
heart_model = pickle.load(h_File)
# [[63 ,1, 3,145,233,1,1,150,0,2.3,0,0,1]] yes
h_Catagory=["No.. You don't have any heart disease","Yes, you may have heart disease"]

def heart(data):
    arr=[]
    for i,x in data.items():
        if i!="csrfmiddlewaretoken":
            arr.append(float(x))
    arr=[arr]
    result=int(heart_model.predict(arr))
    return h_Catagory[result]



l_filename = 'pickel_files/liver.pkl'
l_File = open(l_filename, 'rb')
liver_model = pickle.load(l_File)
l_Catagory=["No.. You don't have any liver disease","Yes, you may have liver disease"]

def liver(data):
    arr=[]
    for i,x in data.items():
        if i!="csrfmiddlewaretoken":
            arr.append(float(x))
    arr=[arr]
    result=int(liver_model.predict(arr))
    return l_Catagory[result]
