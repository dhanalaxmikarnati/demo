
from django.shortcuts import render

from travs.models import Destination
#from .models import person_collection

# Create your views here.

def index(request):
 #   dest1=Destination()
  #  dest1.name= "dhana"
  #  dest1.img="dhana.jpg"
  #  dest1.price= 900
  #  dest1.offer=False
  #  dest1.dscrp="dhana doesnt have sense"
    
   # dest2=Destination()
   # dest2.name= "varun"
   # dest2.img="varun.jpg"
   # dest2.price= 9000
   # dest2.offer=True
   # dest2.dscrp="varun world famous lazy fellow"
    
  #  dest3=Destination()
  #  dest3.name= "aadhyavish"
  #  dest3.img="aadhyavish.jpg"
  #  dest3.offer=True
  #  dest3.price= 90000
  #  dest3.dscrp="aadhyavish kids of dhanavarun"
    
    
   # dests=[dest1,dest2,dest3]
   dests = Destination.objects.all()
   return render(request, 'index.html',{'dests':dests})



