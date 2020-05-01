from django.contrib import admin
from .models import ExpenseMaster,EarningMaster,BudgetMaster,ExpenseDetails,EarningDetails,BudgetDetails

# Register your models here.
admin.site.register(ExpenseMaster)
admin.site.register(EarningMaster)
admin.site.register(BudgetMaster)
admin.site.register(ExpenseDetails)
admin.site.register(EarningDetails)
admin.site.register(BudgetDetails)

