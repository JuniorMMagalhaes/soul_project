from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import userForm, addressForm, companyForm
from .models import userAdd, companyAdd
# Create your views here.

#@Login_Required
def home(request): 
    return render(request, 'base.html')

#Cadastro PF
def createUser(request):
    if request.method == 'POST':
        user_form = userForm(request.POST)
        address_form = addressForm(request.POST)
        if user_form.is_valid() and address_form.is_valid():
            address = address_form.save()
            user = user_form.save(commit=False)
            user.address = address
            user.save()
            messages.success(request, "Cadastrado com sucesso.")
            return redirect('read_user')
        else:
            messages.error(request, "Erro ao cadastrar.")
    else:
        user_form = userForm()
        address_form = addressForm()
    return render(request, 'users/form_users.html', {'user_form': user_form, 'address_form': address_form})

def readUser(request):
        userRecod = userAdd.objects.all() 
        return render(request, 'users/read_users.html', {'userRecod': userRecod})
    
def updateUser(request, id):
    userUpdate = userAdd.objects.get(id=id)
    if request.method == 'POST':
        user_form = userForm(request.POST, instance=userUpdate)
        address_form = addressForm(request.POST, instance=userUpdate.address)
        if user_form.is_valid() and address_form.is_valid():
            user_form.save()
            address_form.save()
            messages.success(request, "Cadastro atualizado com sucesso.")
            return redirect('read_user')
    else:
        user_form = userForm(instance=userUpdate)
        address_form = addressForm(instance=userUpdate.address)
    
    return render(request, 'users/update_users.html', {'user_form': user_form, 'address_form': address_form})

def deleteUser(request,id):
    userDelete = get_object_or_404(userAdd, id=id)
    
    if request.method == 'POST':
        userDelete.delete()
        messages.success(request, 'Cadastrado deletado com sucesso')
        return redirect('read_user')
    else:
        return render(request, 'users/confirm_delete_user.html', {'userDelete' : userDelete})


#Cadastro PJ
def createCompany(request):
    if request.method == 'POST':
        company_form = companyForm(request.POST)
        address_form = addressForm(request.POST)
        if company_form.is_valid() and address_form.is_valid():
            address = address_form.save()
            company = company_form.save(commit=False)
            company.address = address
            company.save()
            messages.success(request, "Empresa cadastrada com sucesso.")
            return redirect('read_companies')
        else:
            messages.error(request, "Erro ao cadastrar empresa.")
    else:
        company_form = companyForm()
        address_form = addressForm()
    return render(request, 'companies/form_companies.html', {'company_form': company_form, 'address_form': address_form})

def readCompany(request):
        companyRecord = companyAdd.objects.all() 
        return render(request, 'companies/read_companies.html', {'companyRecord': companyRecord})
    
def updateCompany(request, id):
    companyUpdate = companyAdd.objects.get(id=id)
    if request.method == 'POST':
        company_form = companyForm(request.POST, instance=companyUpdate)
        address_form = addressForm(request.POST, instance=companyUpdate.address)
        if company_form.is_valid() and address_form.is_valid():
            company_form.save()
            address_form.save()
            messages.success(request, "Empresa atualizada com sucesso!")
            return redirect('read_companies')
    else:
        company_form = companyForm(instance=companyUpdate)
        address_form = addressForm(instance=companyUpdate.address)
    return render(request, 'companies/update_companies.html', {'company_form': company_form, 'address_form': address_form})

def deleteCompany(request, id):
    companyDelete = get_object_or_404(companyAdd, id=id)
    if request.method == 'POST':
        companyDelete.delete()
        messages.success(request, 'Empresa deletada com sucesso!')
        return redirect('read_companies')
    else:
        return render(request, 'companies/confirm_delete_company.html', {'companyDelete': companyDelete})
