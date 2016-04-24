from customerService.models import Customer
import time

def get_all_customer():
    return Customer.objects.filter(is_deleted = False)

def get_customer_by_id(customer_id):
    return Customer.objects.get(id = customer_id)

def insert_customer(customer):
    customer.customer_identifier = customer.name.lower().replace(" ", "") + '_' + time.strftime("%y%m%d%H%M%S")
    customer.save()

def delete_customer(customer):
    customer.is_deleted = True
    customer.save()