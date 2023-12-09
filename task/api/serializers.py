from task.models import Task, Image
from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(default=serializers.CurrentUserDefault(),read_only=True)
    images = ImageSerializer(many=True,read_only=True)
    upload_images = serializers.ListField(child=serializers.ImageField(allow_empty_file=False, use_url=False),write_only=True)
    class Meta:
        model = Task
        fields = ['id','user','title','description','start_date','end_date','priority','complete','images','upload_images']

    def create(self, validated_data):
        upload_images = validated_data.pop('upload_images')

        task = Task.objects.create(**validated_data)

        for image in upload_images:
            Image.objects.create(task=task,image=image)
        
        return task


