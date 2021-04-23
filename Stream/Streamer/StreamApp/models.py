from django.db import models

# Create your models here.
class StreamerName(models.Model):
    name=models.CharField(max_length=120)
    quality=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Video(models.Model):
    #Foreign key is used to provide relation such that if linker model changes then corresponding changes should be reflected in model to which it is linked. 
    vid=models.ForeignKey(StreamerName,related_name='v_obj',on_delete=models.CASCADE)
    vtype=models.CharField(default=None,max_length=200)
    # class Meta:
    #     unique_together=['vid','vtype']
    #     ordering=['vtype']
    #Whenever the object is called it directly throw its representation but to throw in string format we are using string representation
    def __str__(self):
        return self.vtype
    #When we are using related_name attribute reverse feature activates that means with the help of related name we can directly access the attributes of that class
    #to access just add class_name.{related_name}.all() instead of class_name.{anotclassname}_set.all()