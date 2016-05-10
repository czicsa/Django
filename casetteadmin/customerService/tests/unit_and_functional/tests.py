from customerService.models import Customer
from django.test import TestCase, Client
from customerService.data_access import customer_data_access as CustomerDataAccess
from selenium import webdriver

class CustomerServiceTests(TestCase):
    def setUp(self):
        #unit
        Customer.objects.create(name="Egyes Egy", customer_identifier="egyegy01234", phone_number="01234", personal_identifier="0121212", address="addresstest" )
        Customer.objects.create(name="Kettes Kettő", customer_identifier="kettesketto01234", phone_number="43210", personal_identifier="112211", address="addresstest2" )
        Customer.objects.create(name="H-rmas Három", customer_identifier="harmasharom01234", phone_number="1212", personal_identifier="330011", address="addresstest3", is_deleted=True)

        #funkcionális
        self.client = Client(enforce_csrf_checks=False)

#unit teszt
    def test_get_all_customer(self):
        result = CustomerDataAccess.get_all_customer()
        self.assertEqual(result.count(), 2)
        first = result.get(name="Egyes Egy")
        self.assertEqual(first.customer_identifier, "egyegy01234")

        second = result.get(name="Kettes Kettő")
        self.assertEqual(second.customer_identifier, "kettesketto01234")

    def test_get_customer_by_id(self):
        customer_id = Customer.objects.get(name="Egyes Egy").id
        result = CustomerDataAccess.get_customer_by_id(customer_id)
        self.assertEqual(result.customer_identifier, "egyegy01234")

#funkcionális teszt
    def test_insert_customer(self):
        response = self.client.post("/customer/insertcustomer", {"name": "Négyes Négy", "phone": "112211", "pid": "11221100", "address": "addresstest4"})
        self.assertEqual(response.status_code, 302)

        result = CustomerDataAccess.get_all_customer()
        self.assertEqual(result.count(), 3)


    def test_delete_customer(self):
        customer_id = Customer.objects.get(name="Egyes Egy").id
        response = self.client.post("/customer/deletecustomer/" + str(customer_id) + "/")
        self.assertEqual(response.status_code, 302)

        result = CustomerDataAccess.get_all_customer()
        self.assertEqual(result.count(), 1)

