# Create your views here.

from .models import *


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

    # return HttpResponse(pet.person)
#
# def pre(request):
#     if request.method == "GET":
