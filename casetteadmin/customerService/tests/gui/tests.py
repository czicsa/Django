from customerService.data_access import customer_data_access as CustomerDataAccess
from customerService.models import Customer
from django.test import override_settings
from selenium.webdriver.support.wait import WebDriverWait
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import os

@override_settings(DEBUG=True)
class MySeleniumTests(StaticLiveServerTestCase):
    def setUp(self):
        Customer.objects.create(name="Egyes Egy", customer_identifier="egyegy01234", phone_number="01234", personal_identifier="0121212", address="addresstest" )
        Customer.objects.create(name="Kettes Kettő", customer_identifier="kettesketto01234", phone_number="43210", personal_identifier="112211", address="addresstest2" )
        Customer.objects.create(name="H-rmas Három", customer_identifier="harmasharom01234", phone_number="1212", personal_identifier="330011", address="addresstest3", is_deleted=True)

    @classmethod
    def setUpClass(cls):
        super(MySeleniumTests, cls).setUpClass()

        chromedriver = "C:/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        cls.selenium = webdriver.Chrome(chromedriver)
        #cls.selenium = webdriver.PhantomJS()
        #cls.selenium.implicitly_wait(0)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.refresh()
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def test_insert_customer_gui(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/customer/'))

        WebDriverWait(self.selenium, 10).until(lambda s: s.find_element_by_id("add_customer")).is_displayed()
        self.selenium.find_element_by_id("add_customer").click()

        WebDriverWait(self.selenium, 10).until(lambda s: s.find_element_by_id("name")).is_displayed()
        name = self.selenium.find_element_by_id("name")
        name.send_keys("Négyes Négy")

        phone = self.selenium.find_element_by_id("phone")
        phone.send_keys("11221111")

        pid = self.selenium.find_element_by_id("pid")
        pid.send_keys("334433")

        phone = self.selenium.find_element_by_id("address")
        phone.send_keys("addressTest4")

        self.selenium.find_element_by_id("save_customer").click()

        result = CustomerDataAccess.get_all_customer()
        self.assertEqual(result.count(), 3)

    def test_delete_customer_gui(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/customer/'))

        customer_id = Customer.objects.get(name="Egyes Egy").id
        WebDriverWait(self.selenium, 10).until(lambda s: s.find_element_by_id("delete_customer_" + str(customer_id))).is_displayed()
        self.selenium.find_element_by_id("delete_customer_" + str(customer_id)).click()


        result = CustomerDataAccess.get_all_customer()
        self.assertEqual(result.count(), 1)


