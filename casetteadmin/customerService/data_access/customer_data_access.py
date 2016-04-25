from customerService.models import Customer
import time

def get_all_customer():
    return Customer.objects.filter(is_deleted = False)

def get_customer_by_id(customer_id):
    return Customer.objects.get(id = customer_id)

def get_customer_by_name_and_customer_identifier_and_personal_identifier(name, customer_identifier, personal_identifier):
    result = Customer.objects.filter(is_deleted = False)
    if(name != ""):
        result = result.filter(name = name)
    if(customer_identifier != ""):
        result = result.filter(customer_identifier = customer_identifier)
    if(personal_identifier != ""):
        result = result.filter(personal_identifier = personal_identifier)
    return result

def insert_customer(customer):
    customer.customer_identifier = customer.name.lower().replace(" ", "") + '_' + time.strftime("%y%m%d%H%M%S")
    customer.save()

def update_customer(customer):
    customer.save()

def delete_customer(customer):
    customer.is_deleted = True
    customer.save()