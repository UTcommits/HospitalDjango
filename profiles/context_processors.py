from django.contrib.auth.models import Group

def hasGroup(user, groupName):
    try:
        group = Group.objects.get(name=groupName)
        return True if group in user.groups.all() else False
    except:
        return False

def navbar_menu(request):
    menu=[]
    user = request.user
    if hasGroup(user, 'doctor'):
        menu1= {'items':'Profile','url':'profile'}
        menu3= {'items':'Appointments','url':'appointments'}
        menu4= {'items':'Prescriptions','url':'prescription'}
        menu5= {'items':'Logout','url':'logout'}
        menu.append(menu1)
        menu.append(menu3)
        menu.append(menu4)
        menu.append(menu5)

    elif hasGroup(user, 'patient'):
        menu1= {'items':'Profile','url':'profile'}
        menu2= {'items':'Invoice & Payments','url':'invoice'}
        menu3= {'items':'Appointments','url':'appointments'}
        menu4= {'items':'Medical History','url':'prescription'}
        menu5= {'items':'Logout','url':'logout'}
        menu.append(menu1)
        menu.append(menu2)
        menu.append(menu3)
        menu.append(menu4)
        menu.append(menu5)
            
    elif hasGroup(user, 'receptionist'):
        menu1={'items':'Dashboard','url':'dashboard'}
        menu2= {'items':'Logout','url':'logout'}
        menu.append(menu1)
        menu.append(menu2)    
    elif hasGroup(user, 'hr'):
        menu1={'items':'Dashboard','url':'dashboard'}
        menu2={'items':'Accounting','url':'accounts'}
        menu3={'items':'Logout', 'url':'logout'}
        menu.append(menu1)
        menu.append(menu2)
        menu.append(menu3)
    else:
        menu1={'items':'Register','url':'register'}
        menu2={'items':'Login','url':'login'}
        menu.append(menu1)
        menu.append(menu2)

    return {'menu':menu}
