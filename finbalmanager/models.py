from django.db import models
# from .models import ExpenseDetails,EarningDetails
# from .models import BudgetDetails
# Create your models here.

class BudgetMaster(models.Model):
    budget_head=models.CharField(max_length=100)
    budget_desc=models.TextField(max_length=1000)

    def __str__(self):
        name=str(self.budget_head)
        # +'_'+str(self.budget_desc)
        return (str(name))

class ExpenseMaster(models.Model):
    expense_head=models.CharField(max_length=100)
    expense_desc=models.TextField(max_length=1000)
    def __str__(self):
        name=str(self.expense_head)
        # +'_'+str(self.expense_desc)
        return (str(name))
class EarningMaster(models.Model):
    earning_head=models.CharField(max_length=100)
    expense_desc=models.TextField(max_length=1000)
    def __str__(self):
        name=str(self.earning_head)
        # +'_'+str(self.expense_desc)
        return (str(name))
class BudgetDetails(models.Model):
    budget_head=models.ForeignKey(BudgetMaster,on_delete=models.CASCADE,default=1)
    amount_allocated=models.FloatField()
    budget_fy_startDate=models.DateField()
    amount_used=models.FloatField()
    amount_surplus=models.FloatField()
#    expenses=models.ManyToManyField(ExpenseDetails)
#    earnings=models.ManyToManyField(EarningDetails)
    comments=models.TextField(max_length=500)
    def __str__(self):
        name=str(self.budget_head)+'_FY_'+str(self.budget_fy_startDate)
        return (str(name))

class ExpenseDetails(models.Model):
    budget_head=models.ForeignKey(BudgetDetails,on_delete=models.CASCADE,default=1)
    expense_head=models.ForeignKey(ExpenseMaster,on_delete=models.CASCADE,default=1)
    expense_amount=models.FloatField(default=0.00)
    expense_tax_amt=models.FloatField(default=0.00)
    expense_date=models.DateField()
    expense_invoice_no=models.CharField(max_length=50,blank=True)
    expense_order_ref_no=models.CharField(max_length=50,blank=True)
    expense_trn_ref_no=models.CharField(max_length=50,blank=True)
    expense_comments=models.CharField(max_length=500)

    def __str__(self):
        name=str(self.budget_head)+'_'+str(self.expense_head)
        return (str(name))

class EarningDetails(models.Model):
    budget_head=models.ForeignKey(BudgetDetails,on_delete=models.CASCADE,default=1)
    earning_head=models.ForeignKey(EarningMaster,on_delete=models.CASCADE,default=1)
    earning_amount=models.FloatField(default=0.00)
    earning_tax_amt=models.FloatField(default=0.00)
    earning_date=models.DateField()
    earning_invoice_no=models.CharField(max_length=50,blank=True)
    earning_order_ref_no=models.CharField(max_length=50,blank=True)
    earning_trn_ref_no=models.CharField(max_length=50,blank=True)
    earning_comments=models.CharField(max_length=500)

    def __str__(self):
        name=str(self.budget_head)+'_'+str(self.earning_head)
        return (str(name))


