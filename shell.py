from my_app.models import *
from django.utils import timezone


user1 = User.objects.create(email='nikname21@gmail.com', password='defender42')
client1 = Client.objects.create(name='Азат Соколов', card_number='4147 5657 9878 9009', user=user1)
user2 = User.objects.create(email='altywa1998@gmail.com', password='nono34')
worker1 = Worker.objects.create(name='Алтынай Алиева', position='Оператор кассы', user=user2)
food1 = Food.objects.create(name='Гамбургер', start_price=25)
food2 = Food.objects.create(name='Шаурма', start_price=50)
ingredient1 = Ingredient.objects.create(name='сыр', extra_price=10)
ingredient2 = Ingredient.objects.create(name='курица', extra_price=70)
ingredient3 = Ingredient.objects.create(name='говядина', extra_price=80)
ingredient4 = Ingredient.objects.create(name='салат', extra_price=15)
ingredient5 = Ingredient.objects.create(name='фри', extra_price=15)

food2.ingredients.set([ingredient3, ingredient1, ingredient4, ingredient5],
                      through_defaults={'client': client1, 'worker': worker1})

food1.ingredients.set([ingredient2, ingredient4],
                      through_defaults={'client': client1, 'worker': worker1})
sum_food2 = 0

for i in food2.ingredients.all():
    i = i.extra_price
    sum_ingredient2 = + i
    sum_food2 = sum_ingredient2 + food2.start_price
    print(sum_food2)

sum_food1 = 0


for i in food1.ingredients.all():
    i = i.extra_price
    sum_ingredient1 = + i
    sum_food1 = sum_ingredient1 + food2.start_price
    print(sum_food1)

print(sum_food2 + sum_food1)



