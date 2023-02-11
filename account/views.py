from django.http import HttpResponse

def Signup(req):
    return HttpResponse("i guess you want to signup")


def Login(req):
    return HttpResponse("i guess you want to login")

def Update(req):
    return HttpResponse("i guess you want to update")


def Delete(req):
    return HttpResponse("i guess you want to delete")

def getUser(req):
    return HttpResponse("here is particular info about user")

def getAllUser(req):
    return HttpResponse("All user info")










