
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
}

def dish (request):
    url = request.path.strip('/')
    if url in DATA.keys():
        context ={}
        context['recipe'] = DATA[f'{url}']
        servings=request.GET.get('servings')
        if servings != None:
            composition_dish = {}
            for x in DATA[f'{url}'].items():
                y=(x[1])*int(servings)
                composition_dish[x[0]]=y
            context['recipe'] = composition_dish
        return render(request, 'calculator/index.html', context)
