from django.contrib import admin
from django.urls import path
from . models import *
from .serializer import *
from . views import generic_api


urlpatterns = [
    path('schools/',generic_api(School, SchoolSerializer),name='schools'),
    path('schools/<int:id>/',generic_api(School, SchoolSerializer),name='school-detail'),

    path('users/',generic_api(User, UserSerializer),name='users'),
    path('users/<int:pk>/',generic_api(User, UserSerializer),name='user-detail'),

    path('school-memberships/',generic_api(SchoolMembership, SchoolMembershipSerializer),name='school-memberships'),
    path('school-memberships/<int:pk>/', generic_api(SchoolMembership, SchoolMembershipSerializer), name='school-membership-detail'),

    path('teacher-profiles/', generic_api(TeacherProfile, TeacherProfileSerializer), name='teacher-profile'),
    path('teacher-profiles/<int:pk>/', generic_api(TeacherProfile, TeacherProfileSerializer), name='teacher-profile-detail'),

    path('student-profiles/', generic_api(StudentProfile, StudentProfileSerializer), name='student-profile'),
    path('student-profiles/<int:pk>/', generic_api(StudentProfile, StudentProfileSerializer), name='student-profile-detail'),

    path('parent-profiles/', generic_api(ParentProfile, ParentProfileSerializer), name='parent-profile'),
    path('parent-profiles/<int:pk>/', generic_api(ParentProfile, ParentProfileSerializer), name='parent-profile-detail'),

    path('parent-student-links/', generic_api(ParentStudentLink, ParentStudentLinkSerializer), name='parent-student-link'),
    path('parent-student-links/<int:pk>/', generic_api(ParentStudentLink, ParentStudentLinkSerializer), name='parent-student-link-detail'),

    path('notifications/', generic_api(Notification, NotificationSerializer), name='notification-list'),
    path('notifications/<int:pk>/', generic_api(Notification, NotificationSerializer), name='notification-detail'),

    path('conversations/', generic_api(Conversation, ConversationSerializer), name='conversation'),
    path('conversations/<int:pk>/', generic_api(Conversation, ConversationSerializer), name='conversation-detail'),

    path('messages/', generic_api(Message, MessageSerializer), name='message'),
    path('messages/<int:pk>/', generic_api(Message, MessageSerializer), name='message-detail'),

    path('resources/', generic_api(Resource, ResourceSerializer), name='resource'),
    path('resources/<int:pk>/', generic_api(Resource, ResourceSerializer), name='resource-detail'),

    path('api/classes/', generic_api(Class, ClassSerializer), name='class'),
    path('api/classes/<int:pk>/', generic_api(Class, ClassSerializer), name='class-detail'),

    path('api/subjects/', generic_api(Subject, SubjectSerializer), name='subject'),
    path('api/subjects/<int:pk>/', generic_api(Subject, SubjectSerializer), name='subject-detail'),

    path('api/teaching-assignments/', generic_api(TeachingAssignment, TeachingAssignmentSerializer), name='teaching-assignment'),
    path('api/teaching-assignments/<int:pk>/', generic_api(TeachingAssignment, TeachingAssignmentSerializer), name='teaching-assignment-detail'),

    path('api/enrollments/', generic_api(Enrollment, EnrollmentSerializer), name='enrollment'),
    path('api/enrollments/<int:pk>/', generic_api(Enrollment, EnrollmentSerializer), name='enrollment-detail'),

]