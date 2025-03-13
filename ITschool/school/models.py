from django.shortcuts import reverse
from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()




class Course(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length = 1000 , blank = True) #velky text area
    image = models.ImageField(blank = True, null = True, upload_to='course/')

    # blank = volitelne na urovni UI
    # null = volene na urovni DB

    #vazba 1:N User - Course.user_id -> User.id
    #_ on delete_ co se ma stat se zaznamy Course, pokud vymazeme User
    # v tomto pripade se nastavi null  pokud uzivatele vymazeme

    lector = models.ForeignKey(User, blank= True, null = True, on_delete=models.SET_NULL, related_name= 'lector_courses')

    # vazba M:N na User, blank - neni povinne aby tam mel studenty
    students = models.ManyToManyField(User, blank=True, related_name='student_courses')


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('school:course_detail', kwargs={"pk": self.pk})


