from django.shortcuts import render,redirect
from django.views.generic import View
from Myapp.models import Film

#FilmCreate

#FilmList

#FilmDelete

#FilmDetail

#url : localhost:8000/employees/all/

class FilmListView(View):
    def get(self,request,*args,**kwargs):

        qs=Film.objects.all()

        return render(request,"film_list.html",{"films":qs})

#film create

#url:localhost:8000/employees/add
#method:get,post

class FilmCreateView(View):
    def get(self,request,*args,**kwargs):

        return render(request,"film_create.html")
    
    def post(self,request,*args,**kwargs):

        title_box_val=request.POST.get("titlebox")
        year_box_val=request.POST.get("yearbox")
        director_box_val=request.POST.get("directorbox")
        producer_box_val=request.POST.get("producerbox")

        #ORM qury to create obj
        #modelname.objects.create
        Film.objects.create(
           title=title_box_val,
           year=year_box_val,
           director=director_box_val,
           producer=producer_box_val,

        )
        #django shortcuts fn => function redirect(name)
        
        # return render(request,"film_create.html")
        
        return redirect("film-list")
    

        #use RENDER to create an html page/template
        #use REDIRECT to redirect to another view

#FILM DETAIL
#url:localhost:8000/films/{pk}/
#method:get

class FilmDetailView(View):
     def get(self,request,*args,**kwargs):
         
         print(kwargs)#kwargs recieved url parameter as dictionarykwargs={'pk':3}
         
         id=kwargs.get("pk")
         
         #orm query for fetching employee with id
         
         qs=Film.objects.get(id=id)

         return render(request,"film_detail.html",{"films":qs})

class FilmDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Film.objects.get(id=id).delete()

        return redirect("film-list")

class FilmUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Film.objects.get(id=id)

        return render(request,"film_update.html",{"films":qs})

    def post(self,request,*args,**kwargs):
    
        data=request.POST

        id=kwargs.get("pk")

        Film.objects.filter(id=id).update(
            title=request.POST.get("title"),
            year=int(request.POST.get("year")),
            director=request.POST.get("director"),
            producer=request.POST.get("producer"),
            
        )

        return redirect("film-list")

 
