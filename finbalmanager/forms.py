from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from .models import ExpenseDetails,EarningDetails
class addExpenseForm(ModelForm):
    class Meta():
        model=ExpenseDetails
        fields=['budget_head','expense_head','expense_amount','expense_tax_amt','expense_date','expense_invoice_no','expense_order_ref_no','expense_trn_ref_no','expense_comments']


class addEarningForm(ModelForm):
    class Meta():
        model=EarningDetails
        fields=['budget_head','earning_head','earning_amount','earning_tax_amt','earning_date','earning_invoice_no','earning_order_ref_no','earning_trn_ref_no','earning_comments']