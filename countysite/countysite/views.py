from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def abbey(request):
    return render(request, 'abbey.html')

def arts(request):
    return render(request, 'arts.html')

def cameron_depot_museum(request):
    return render(request, 'cameron_depot.html')

def riley_carmack_museum(request):
    return render(request, 'riley_carmack.html')

def coming_soon(request):
    return render(request, 'coming_soon.html')

def culture(request):
    return render(request, 'culture.html')

def events(request):
    return render(request, 'events.html')

def family_fun(request):
    return render(request, 'family_fun.html')

def food_drink(request):
    context = {
        'businesses': temp_businesses
    }
    return render(request, 'food_drink.html', context)

def history_museums(request):
    return render(request, 'history_museums.html')

def lodging(request):
    context = {
        'businesses': temp_stay_businesses
    }
    return render(request, 'lodging.html', context)

def music(request):
    return render(request, 'music.html')

def outdoor_adventure(request):
    return render(request, 'outdoor_adventure.html')

def resources(request):
    context = {
        'resources': temp_resources
    }
    return render(request, 'resources.html', context)

def shatto_milk(request):
    return render(request, 'shatto_milk.html')

def shopping_leisure(request):
    context = {
        'businesses': temp_shop_businesses
    }
    return render(request, 'shopping_leisure.html', context)

def tours(request):
    return render(request, 'tours.html')

def golf(request):
    return render(request, 'golf.html')

def hartell_conservation_area(request):
    return render(request, 'hartell_conservation_area.html')

def mcgee_family_conservation(request):
    return render(request, 'mcgee_family_conservation.html')

def smithville_lake(request):
    return render(request, 'smithville_lake.html')

def trice_dedman(request):
    return render(request, 'trice_dedman.html')

def wallace_state_park(request):
    return render(request, 'wallace_state_park.html')


temp_businesses = [
    {
        'name': 'Business 1',
        'description': 'This is a description of business 1',
        'address': '123 Main St.',
        'city': 'city 1',
        'phone': '555-555-5555',
        'website': 'www.business1.com',
        'family_friendly': True,
        'dietary_restrictions': ['vegetarian', 'vegan'],
        'type': 'italian'
    },
    {
        'name': 'Business 2',
        'description': 'This is a description of business 2',
        'address': '456 Main St.',
        'city': 'city 2',
        'phone': '555-555-5555',
        'website': 'www.business2.com',
        'family_friendly': True,
        'dietary_restrictions': ['vegetarian'],
        'type': 'mexican'
    },
    {
        'name': 'Business 3',
        'description': 'This is a description of business 3',
        'address': '789 Main St.',
        'city': 'city 3',
        'phone': '555-555-5555',
        'website': 'www.business3.com',
        'family_friendly': True,
        'dietary_restrictions': ['gluten free'],
        'type': 'bbq'
    },
    {
        'name': 'Business 4',
        'description': 'This is a description of business 4',
        'address': '101 Main St.',
        'city': 'city 4',
        'phone': '555-555-5555',
        'website': 'www.business4.com',
        'family_friendly': False,
        'dietary_restrictions': ['vegetarian', 'vegan'],
        'type': 'bar'
    },
    {
        'name': 'Business 5',
        'description': 'This is a description of business 5',
        'address': '112 Main St.',
        'city': 'city 5',
        'phone': '555-555-5555',
        'website': 'www.business5.com',
        'family_friendly': True,
        'dietary_restrictions': ['vegetarian', 'vegan', 'gluten-free', 'dairy-free', 'kosher'],
        'type': 'greek'
    }
]

temp_shop_businesses = [
    {
        'name': 'Shop Business 1',
        'description': 'This is a description of shop business 1',
        'address': '123 Main St.',
        'city': 'city 1',
        'phone': '555-555-5555',
        'website': 'www.shopbusiness1.com',
        'family_friendly': True,
        'type': 'clothing'
    },
    {
        'name': 'Shop Business 2',
        'description': 'This is a description of shop business 2',
        'address': '456 Main St.',
        'city': 'city 2',
        'phone': '555-555-5555',
        'website': 'www.shopbusiness2.com',
        'family_friendly': True,
        'type': 'electronics'
    },
    {
        'name': 'Shop Business 3',
        'description': 'This is a description of shop business 3',
        'address': '789 Main St.',
        'city': 'city 3',
        'phone': '555-555-5555',
        'website': 'www.shopbusiness3.com',
        'family_friendly': True,
        'type': 'toys'
    },
    {
        'name': 'Shop Business 4',
        'description': 'This is a description of shop business 4',
        'address': '101 Main St.',
        'city': 'city 4',
        'phone': '555-555-5555',
        'website': 'www.shopbusiness4.com',
        'family_friendly': False,
        'type': 'tools'
    },
    {
        'name': 'Shop Business 5',
        'description': 'This is a description of shop business 5',
        'address': '112 Main St.',
        'city': 'city 5',
        'phone': '555-555-5555',
        'website': 'www.shopbusiness5.com',
        'family_friendly': True,
        'type': 'books'
    }
]

temp_stay_businesses = [
    {
        'name': 'Stay Business 1',
        'description': 'This is a description of stay business 1',
        'address': '123 Main St.',
        'city': 'city 1',
        'phone': '555-555-5555',
        'website': 'www.staybusiness1.com',
        'family_friendly': True,
        'type': 'hotel_motel'
    },
    {
        'name': 'Stay Business 2',
        'description': 'This is a description of stay business 2',
        'address': '456 Main St.',
        'city': 'city 2',
        'phone': '555-555-5555',
        'website': 'www.staybusiness2.com',
        'family_friendly': True,
        'type': 'airbnb_bnb'
    },
    {
        'name': 'Stay Business 3',
        'description': 'This is a description of stay business 3',
        'address': '789 Main St.',
        'city': 'city 3',
        'phone': '555-555-5555',
        'website': 'www.staybusiness3.com',
        'family_friendly': True,
        'type': 'hotel_motel'
    },
    {
        'name': 'Stay Business 4',
        'description': 'This is a description of stay business 4',
        'address': '101 Main St.',
        'city': 'city 4',
        'phone': '555-555-5555',
        'website': 'www.staybusiness4.com',
        'family_friendly': False,
        'type': 'campground'
    },
    {
        'name': 'Stay Business 5',
        'description': 'This is a description of stay business 5',
        'address': '112 Main St.',
        'city': 'city 5',
        'phone': '555-555-5555',
        'website': 'www.staybusiness5.com',
        'family_friendly': True,
        'type': 'airbnb_bnb'
    }
]

temp_resources = [
    {
        'name': 'Resource 1',
        'description': 'This is a description of resource 1',
        'address': '123 Main St.',
        'city': 'city 1',
        'phone': '555-555-5555',
        'website': 'www.resource1.com',
        'type': 'type_1'
    },
    {
        'name': 'Resource 2',
        'description': 'This is a description of resource 2',
        'address': '456 Main St.',
        'city': 'city 2',
        'phone': '555-555-5555',
        'website': 'www.resource2.com',
        'type': 'type_2'
    },
    {
        'name': 'Resource 3',
        'description': 'This is a description of resource 3',
        'address': '789 Main St.',
        'city': 'city 3',
        'phone': '555-555-5555',
        'website': 'www.resource3.com',
        'type': 'type_2'
    },
    {
        'name': 'Resource 4',
        'description': 'This is a description of resource 4',
        'address': '101 Main St.',
        'city': 'city 4',
        'phone': '555-555-5555',
        'website': 'www.resource4.com',
        'type': 'type_1'
    },
    {
        'name': 'Resource 5',
        'description': 'This is a description of resource 5',
        'address': '112 Main St.',
        'city': 'city 5',
        'phone': '555-555-5555',
        'website': 'www.resource5.com',
        'type': 'type_1'
    }
]