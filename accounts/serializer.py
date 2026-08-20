from django.db import models
from rest_framework.serializers import ModelSerializer
from . models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  

class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class SchoolMembershipSerializer(ModelSerializer):
     class Meta:
         model = SchoolMembership
         fields = '__all__'               


class StudentProfileSerializer(ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'
                        

class ParentStudentLinkSerializer(ModelSerializer):
    class Meta:
        model = ParentStudentLink
        fields = '__all__'


class ConversationSerializer(ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'


class EnrollmentSerializer(ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'


class TeacherProfileSerializer(ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = '__all__'


class ParentProfileSerializer(ModelSerializer):
    class Meta:
        model = ParentProfile
        fields = '__all__'


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class ResourceSerializer(ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class ClassSerializer(ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class TeachingAssignmentSerializer(ModelSerializer):
    class Meta:
        model = TeachingAssignment
        fields = '__all__'
                                                                                                                                                                                            