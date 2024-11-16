from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def arts(request):
    return render(request, 'arts.html')

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

def music(request):
    return render(request, 'music.html')

def outdoor_adventure(request):
    return render(request, 'outdoor_adventure.html')

def place(request):
    return render(request, 'place.html')

def place_alt(request):
    return render(request, 'place_alt.html')

def shopping_leisure(request):
    return render(request, 'shopping_leisure.html')

def tours(request):
    return render(request, 'tours.html')


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