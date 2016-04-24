from customerService.models import Customer

def get_all_customer():
    return Customer.objects.all()

def insert_customer(customer):
    customer.save()