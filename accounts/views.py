# Create your views here.
from django.http import HttpResponse

from .models import *

# selected_related와 prefetch_related의 차이점
# selected는 하나의 쿼리로 related objects를 모두 다 가져온다
# prefetch는 main query가 실행된 뒤 별도의 쿼리를 따로 실행한다.

def sel(request):
    if request.method == "GET":
        # 쿼리가 5번
        # pet = Pet.objects.get(id=1)
        # person = pet.person
        # country = person.country

        # 쿼리 3번
        # pet 을 가져올때 person과 country를 같이 가져옴
        # selected_related는 Foreign_Key와 One To One과 같은 1 : N 관계에서 1이 사용 가능하다
        pet = Pet.objects.select_related('person__country').get(id=1)
        person = pet.person
        country = person.country

    return HttpResponse(pet.person)

def pre(request):
    if request.method == "GET":
        # 쿼리 7번
        # people = Person.objects.all()
        # for person in people:
        #     print(f'{person.name} : ', end="")
        #     for language in person.language_set.all():
        #         print(f'{language.name}', end="")
        #     print("")

        people = Person.objects.prefetch_related('language_set').all()
        for person in people:
            print(f'{person.name} : ', end="")
            for language in person.language_set.all():
                print(f'{language.name}', end="")
            print("")

        # return HttpResponse('asdf')