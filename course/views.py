from django.core.serializers import serialize
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from course.models import Course
from course.serializers import CourseSerializer


# Create your views here.
@api_view(['GET'])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_course(request):
    serializer = CourseSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data,
            status = status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status = status.HTTP_400_BAD_REQUEST
    )

@api_view(['GET'])
def get_course_by_id(request, id):
    try:
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    except Course.DoesNotExist:
        return Response(
            {'error': 'Course does not exist'},
            status=status.HTTP_404_NOT_FOUND
        )

@api_view(['DELETE'])
def delete_course(request, id):
    try:
        course = Course.objects.get(id=id)
        course.delete()
        return Response(
            {'success': 'Delete thành công'},
            status=status.HTTP_200_OK
        )
    except Course.DoesNotExist:
        return Response(
            {'error': 'Course does not exist'},
            status=status.HTTP_404_NOT_FOUND
        )

@api_view(['PUT'])
def update_course(request, id):
    try:
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    except Course.DoesNotExist:
        return Response(
            {'error': 'Course does not exist'},
            status=status.HTTP_404_NOT_FOUND
        )