from django.db import models as md

# Create your md here.
class Company(md.Model):
    company_id = md.AutoField(primary_key=True)
    name = md.CharField(max_length=255)
    license_no = md.CharField(max_length=255)
    address = md.CharField(max_length=255)
    contact_no = md.CharField(max_length=255)
    email = md.CharField(max_length=255)
    description = md.CharField(max_length=255)
    added_on = md.DateTimeField(auto_now_add=True)
    objects = md.Manager()


class Medicine(md.Model):
    id = md.AutoField(primary_key=True)
    name = md.CharField(max_length=255)
    medical_type = md.CharField(max_length=255)
    buy_price = md.CharField(max_length=255)
    sell_price = md.CharField(max_length=255)
    c_gst = md.CharField(max_length=255)
    s_gst = md.CharField(max_length=255)
    batch_no = md.CharField(max_length=255)
    shelf_no = md.CharField(max_length=255)
    expiry_date = md.DateField()
    mfg_date = md.DateField()
    company_id = md.ForeignKey(Company, on_delete=md.CASCADE)
    descriptions = md.CharField(max_length=255)
    in_stock_total = md.IntegerField()
    qty_in_strip = md.IntegerField()
    added_on = md.DateTimeField(auto_now_add=True)
    objects = md.Manager()


class MedicalDetails(md.Model):
    id = md.AutoField(primary_key=True)
    medicine_id = md.ForeignKey(Medicine, on_delete=md.CASCADE)
    salt_name = md.CharField(max_length=255)
    salt_qty = md.CharField(max_length=255)
    salt_qty_type = md.CharField(max_length=255)
    description = md.CharField(max_length=255)
    added_on = md.DateTimeField(auto_now_add=True)
    objects = md.Manager()


class Employee(md.Model):
    id = md.AutoField(primary_key=True)
    name = md.CharField(max_length=255)
    employee = md.CharField(max_length=255)
    joining_date = md.DateField()
    phone = md.CharField(max_length=255)
    address = md.CharField(max_length=255)
    added_on = md.DateTimeField(auto_now_add=True)
    objects = md.Manager()



class Customer(md.Model):
    id = md.AutoField(primary_key=True)
    name = md.CharField(max_length=255)
    address = md.CharField(max_length=255)
    contact = md.CharField(max_length=255)
    added_on = md.DateTimeField(auto_now_add=True)
    objects = md.Manager()


class Bill(md.Model):
    id = md.AutoField(primary_key=True)
    customer_id = md.ForeignKey(Customer, on_delete=md.CASCADE)
    added_on = md.DateTimeField(auto_now_add=True)
    objects = md.Manager()


class EmployeeSalary(md.Model):
    id = md.AutoField(primary_key=True)
    employee_id = md.ForeignKey(Employee, on_delete=md.CASCADE)
    salary_date = md.DateField()
    salary_amt = md.IntegerField()
    added_on = md.DateTimeField(auto_now_add=True)
    objects = md.Manager()

