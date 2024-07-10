from apps.expense_manager.models import Supplier
from faker import Faker

fake = Faker()

class SupplierFactory:
    
    def supplier_json(self):
        return {
            'ruc':str(fake.random_number(digits=11)),
            'business_name': fake.company(),
            'address': fake.address(),
            'phone':str(fake.phone_number()),
            'email':fake.email()                   
        }
        
    def create_supplier(self):
        return Supplier.objects.create(**self.supplier_json())