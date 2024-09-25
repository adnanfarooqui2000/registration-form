from django.shortcuts import render
 # Create your views here.
# # def home(request):
#     # data1={'name':'Arun','age':24,'city':'Bhopal'}
#     # data2={'name':'Rahul','age':20,'city':'Betul'}
#     # data3={'name':'Sonam','age':21,'city':'Jabalpur'}
#     # data4={'name':'Mukesh','age':29,'city':'Jaipur'}
#     # data1={'name':'Mukesh','age':29,'city':'Jaipur'}
#     # data2={}
#     # data3={}
#     # data4={}
#     # return render(request,'index.html',{'key1':data1,'key2':data2,'key3':data3,'key4':data4})
def home(request):
    return render(request,'home.html')
# # def collection(request):
# #     data=[{'name':'Arun','age':24,'city':'Bhopal'},
# #           {'name':'Aman','age':20,'city':'Indore'},
# #           {'name':'Aman','age':20,'city':'Indore'},
# #           {'name':'Aman','age':20,'city':'Indore'},
# #           {'name':'Aman','age':20,'city':'Indore'},
# #           {'name':'Aman','age':20,'city':'Indore'},
# #           {'name':'Arun','age':24,'city':'Bhopal'},
# #           {'name':'Aman','age':20,'city':'Indore'},
# #           {'name':'Aman','age':20,'city':'Indore'},
# #           {'name':'Aman','age':20,'city':'Indore'},
# #           {'name':'Aman','age':20,'city':'Indore'},
# #           {'name':'Aman','age':20,'city':'Indore'}
# #           ]
# #     return render(request,'collection.html',{'data':data})
# def register(request):
#     return render(request,'register.html')
   
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        data1=request.session.get('data')
        print(data1)
        print(data1["name"],data1["email"],data1["contact"],data1["password"])
        if data1['email']==email:
            if data1['password']==password:
                My_Data={
                    'nm':data1['name'],
                    'em':data1['email'],
                    'con':data1['contact'],
                    'pass':data1['password']
                }
                return render(request,'dashboard.html',My_Data)
            else:
                msg='Invalid Password'
                return render(request,'login.html',{'msg':msg}) 
        else:
            msg='Email is not Valid'
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')        
#     if request.method=='POST':
#         email1=request.POST.get('email')
#         password1=request.POST.get('password')
#         # print(email,password)
#         name=request.COOKIES['name']
#         email=request.COOKIES['email']
#         contact=request.COOKIES['contact']
#         password=request.COOKIES['password']
#         if email1==email:
#             if password1==password:
#                 data={'name':name,
#                       'email':email,
#                       'contact':contact,
#                       'password':password
#                       }
#                 return render(request,'dashboard.html',data)
#             else:
#                 msg='email id and password not matched'
#                 return render(request,'login.html',{'msg':msg})
                

#         else:
#             msg='email id not register'
#             return render(request,'login.html',{'msg':msg})
#     else:
#         return render(request,'login.html')
# def logout(request):
#     response =render(request,'home.html')
#     response.delete_cookie('name')
#     response.delete_cookie('email')
#     response.delete_cookie('contact')
#     response.delete_cookie('password')    
#     return response

# def register_Data(request):
#     # print(request.method)
#     # print(request.POST)
#     cstoken=request.POST.get('csrfmiddlewaretoken')
#     name=request.POST.get('nm')
#     email=request.POST.get('em')
#     contact=request.POST.get('con')
#     password=request.POST.get('pass')

#     # print(cstoken)
#     # print(name)
#     # print(email)
#     # print(contact)
#     # print(password)
#     response=render(request,'login.html')
#     response.set_cookie('name',name)
#     response.set_cookie('email',email)
#     response.set_cookie('contact',contact)
#     response.set_cookie('password',password)
#     return response

# def userlogin(request):
#     if request.method=='POST':
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         print(email,password)


def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        password=request.POST.get('password')
        data={
            'name':name,
            'email':email,
            'contact':contact,
            'password':password
        }
        request.session['data']=data
        return render(request,'login.html')
    else:
        return render(request,'register.html')
         