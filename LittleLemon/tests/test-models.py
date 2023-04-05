from django.test import TestCase
from restaurant.models import Menu

from django.core import serializers


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(item, "IceCream: 80")





class MenuViewTest(TestCase):
    
    def setUp(self):
        # create some test instances of the Menu model
        Menu.objects.create(Title='Prawn', Price=23.30, Inventory=2)
        Menu.objects.create(Title='Lobster', Price=30.30, Inventory=2)
        Menu.objects.create(Title='Lamb', Price=50, Inventory=5)
    
    def test_getall(self):
        self.maxDiff = None
        
        menus = Menu.objects.all()
        serialized_data = serializers.serialize('json', menus)
       
        expected_response = '[{"model": "restaurant.menu", "pk": 2, "fields": {"Title": "Prawn", "Price": "23.30", "Inventory": 2}},' \
                            '{"model": "restaurant.menu", "pk": 3, "fields": {"Title": "Lobster", "Price": "30.30", "Inventory": 2}},' \
                            '{"model": "restaurant.menu", "pk": 4, "fields": {"Title": "Lamb", "Price": "50", "Inventory": 5}}]'      
        self.assertEqual(serialized_data, expected_response)