from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model  = Employee
        fields = ('fullname', 'emp_code', 'mobile', 'position') #It could also be be like this// fields = __all__ // fields = ('fullname', 'emp_code' etc.) basically listing the fiels you want in model
        labels = {
            'fullname': 'Full Name',
            'emp_code': 'EMP. CODE'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "SELECT"
        # currently all the fields are required so to change that the code below could be used
        # self.fields['emp.code'].required = False