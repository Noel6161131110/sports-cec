from sportsbackend.models import Participate , PARTICIPATION_CHOICES , Position

reverse_choices = {}

for i in PARTICIPATION_CHOICES:
    reverse_choices[i[0]] = i[1]

for i in Participate.objects.all():
    if(Position.objects.filter(position = reverse_choices[i.position] ).count()  == 0 ):
        Position(position = reverse_choices[i.position]).save()
    pos_obj = Position.objects.get(position = reverse_choices[i.position])
    i.pos = pos_obj
    i.save()    
    print(i.pos)