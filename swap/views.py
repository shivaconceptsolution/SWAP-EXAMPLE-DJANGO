from django.shortcuts import render

def index(request):
	return render(request,"swap/index.html")


def swaplogic(request):
	a = request.POST["txtnum1"]
	b = request.POST["txtnum2"]
	a,b = b,a
	return render(request,"swap/index.html",{'key1':a,'key2':b})