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
        # selected_related는 1 : 1 관계 또는 1 : N에서 N이 사용가능하다.
        # Pet의 입장에서는 주인은 한명만 있을 수 있으므로 selected_related를 사용한다
        pet = Pet.objects.select_related('person__country').get(id=1)
        person = pet.person
        country = person.country

    return HttpResponse(pet.person)


def pre(request):
    if request.method == "GET":
        # prefetch_related는 M : N 또는 1 : N 관계에서 1이 사용가능 하다

        # 쿼리 7번
        # 아래는 person마다 language_set을 가져와야 한다
        # people = Person.objects.all()
        # for person in people:
        #     print(f'{person.name} : ', end="")
        # person.language_set 캐시에 데이터가 없으므로 DB에 접근하여 가져온다
        #     for language in person.language_set.all():
        #         print(f'{language.name}', end="")
        #     print("")

        # 쿼리 4번
        # 아래는 people을 가져올때 self.language_set을 별도로 실행해 받아온 data를 캐시에 넣어둔다
        # Person은 language를 여러개 사용 가능하므로 prefetch_related를 사용한다.
        people = Person.objects.prefetch_related('language_set').all()
        for person in people:
            print(f'{person.name} : ', end="")
            # person.language_set을 할때 캐시에 넣어둔 data를 이용한다.
            for language in person.language_set.all():
                print(f'{language.name}', end="")
            print("")

        # return HttpResponse('asdf')
