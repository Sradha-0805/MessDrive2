from django.shortcuts import render
from .forms import ExpenseForm

# Create your views here.
def expense(request):
    form = ExpenseForm
    return render(request, 'expense.html', {'form' : form})

def markPresent(request):
    absentees = request.POST.getlist('ddl-select')
    print (request.POST)
   # return render(request, 'expense.html')
    


