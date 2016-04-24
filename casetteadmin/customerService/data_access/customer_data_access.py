from customerService.models import Customer

def get_all_customer():
    return Customer.objects.filter(is_deleted = False)

def get_customer_by_id(customer_id):
    return Customer.objects.get(id = customer_id)

def insert_customer(customer):
    customer.save()

def delete_customer(customer):
    customer.is_deleted = True
    customer.save()