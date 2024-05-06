from django import forms
from .models import userAdd, adress, companyAdd

class addressForm(forms.ModelForm):  
    addr_zipcode = forms.CharField(label='CEP', widget=forms.TextInput(attrs={'placeholder':'Digite seu CEP', 'class':'cep'}))
    addr_street = forms.CharField(label='Rua', widget=forms.TextInput(attrs={'placeholder':'Digite sua rua'}))
    addr_number = forms.CharField(label='Número', widget=forms.TextInput(attrs={'placeholder':'Digite seu número'}))
    addr_complement = forms.CharField(label='Complemento', widget=forms.TextInput(attrs={'placeholder':'Digite seu complemento (opcional)'}), required=False)
    addr_district = forms.CharField(label='Bairro', widget=forms.TextInput(attrs={'placeholder':'Digite seu bairro'}))
    addr_city = forms.CharField(label='Cidade', widget=forms.TextInput(attrs={'placeholder':'Digite sua cidade'}))
    addr_state = forms.CharField(label='Estado', widget=forms.TextInput(attrs={'placeholder':'Digite seu estado'}))
    addr_country = forms.CharField(label='País', widget=forms.TextInput(attrs={'placeholder':'Digite seu país'})) 

    class Meta:
        model = adress;
        fields = (
            'addr_zipcode',
            'addr_street',
            'addr_number',
            'addr_complement',
            'addr_district',
            'addr_city',
            'addr_state',
            'addr_country',              
        )

class userForm(forms.ModelForm): 
    user_name = forms.CharField(label='Primeiro Nome:', widget=forms.TextInput(attrs={'placeholder':'Digite seu primeiro nome'}))
    user_lastname = forms.CharField(label='Sobrenome:', widget=forms.TextInput(attrs={'placeholder':'Digite seu sobrenome'}))
    user_document = forms.CharField(label='CPF:', widget=forms.TextInput(attrs={'placeholder':'Digite seu CPF', 'class':'cpf'}))
    user_phone = forms.CharField(label='Telefone:', widget=forms.TextInput(attrs={'placeholder':'Digite seu telefone', 'class':'phone'}))
    user_email = forms.CharField(label='Email:', widget=forms.EmailInput(attrs={'placeholder':'Digite seu email'}))
    address = addressForm()   
    
    class Meta:
        model = userAdd;
        fields = (
            'user_name',
            'user_lastname',
            'user_document',
            'user_phone',
            'user_email',                   
        )
class companyForm(forms.ModelForm):
        company_name = forms.CharField(label='Razão Social', widget=forms.TextInput(attrs={'placeholder':'Digite a Razão Social:'}))
        company_fantasy_name = forms.CharField(label='Nome Fantasia', widget=forms.TextInput(attrs={'placeholder':'Digite o Nome Fantasia:'}))
        company_document = forms.CharField(label='CNPJ:', widget=forms.TextInput(attrs={'placeholder':'Digite seu CNPJ:', 'class':'cnpj'}))
        company_phone = forms.CharField(label='telefone', widget=forms.TextInput(attrs={'placeholder':'Digite a Razão Social:', 'class':'phone'}))
        company_email = forms.CharField(label='email', widget=forms.EmailInput(attrs={'placeholder':'Digite a Razão Social:'}))
        
        class Meta:
            model = companyAdd
            fields = (
                'company_name',
                'company_fantasy_name',
                'company_document',
                'company_phone',
                'company_email'                
                
            )
    
