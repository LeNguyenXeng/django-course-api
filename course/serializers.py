from rest_framework import serializers
from course.models import Course

class CourseSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S",
        read_only=True
    )

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'description',
            'price',
            'is_free',
            'created_at',
        ]
