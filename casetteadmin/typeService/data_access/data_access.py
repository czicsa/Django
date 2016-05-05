from typeService.models import Category, Type

def get_category_by_resource_key(category_resource_key):
    return Category.objects.get(resource_key = category_resource_key)

def get_types_by_category_resource_key(category_resource_key):
    category = get_category_by_resource_key(category_resource_key)
    return Type.objects.filter(category = category.id)

def get_type_by_id(type_id):
    return Type.objects.get(id = type_id)

def get_type_by_resource_key(resource_key):
    return Type.objects.get(resource_key = resource_key)