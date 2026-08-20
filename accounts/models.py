from django.db import models

# apps/schools/models.py
class User (models.Model):
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Admin', 'Admin'),
    ]
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    ]
    name = models.CharField(max_length=255,default=None, null=True, blank=True)
    email = models.EmailField(unique=True,default=None, null=True, blank=True)
    password_hash = models.CharField(max_length=255,default=None, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Inactive')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Student')
    created_at = models.DateTimeField(default=None, null=True, blank=True)  
    def __str__(self):
        return f"{self.role}"  


class School(models.Model):
    ROLE_CHOICES=[
        ('Pending','Pending'),
        ('Active','Active'),
        ('Rejected','Rejected')
    ]
    SCHOOL_CHOICES = [
        ('Primary', 'Primary'),
        ('Secondary', 'Secondary')
       
    ]
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100, choices=SCHOOL_CHOICES, default='Primary')
    registration_number = models.CharField(max_length=50, unique=True)
    region = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    contact_email = models.EmailField()
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=ROLE_CHOICES,default='Pending') 

    def __str__(self):
        return self.name


class SchoolMembership(models.Model):
    choice=[
        ('Pending','Pending'),
        ('Approved','Approved'),
        ('Rejected','Rejected')
    ]
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Admin', 'Admin'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES,default='Student')  # redundant but quick
    status = models.CharField(max_length=10, choices=choice, default='Pending')

    def __str__(self):
        return f"{self.user} - {self.school.name} - {self.role}"





   # apps/teachers/models.py
class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    qualifications = models.CharField(max_length=255, blank=True)
    profile_data = models.JSONField(default=dict, blank=True)  # For additional fields like subjects taught, experience, etc.
    # additional fields

    def __str__(self):
        return f"{self.user.name}"

class Class(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classes')
    name = models.CharField(max_length=50)  # "Form 1A"
    level = models.CharField(max_length=20, blank=True)
    stream = models.CharField(max_length=20, blank=True)
    academic_year = models.CharField(max_length=20)  # "2026-2027"
    status = models.BooleanField(default=True)

# apps/students/models.py
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    school_id = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students',default=None, null=True, blank=True)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students',default=None, null=True, blank=True)
    profile_data = models.JSONField(default=dict, blank=True)  # For additional fields like guardian info, etc.

# apps/parents/models.py
class ParentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='parent_profile')
    profile_data = models.JSONField(default=dict, blank=True)  # For additional fields like occupation, etc.

class ParentStudentLink(models.Model):
    choices=[
        ('invited','Invited'), 
        ('accepted','Accepted')
    ]
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='linked_students')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='linked_parents')
    status = models.CharField(max_length=20, choices=choices,default='invited')
    invited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='sent_invites')
    accepted_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.parent.name} - {self.student.name} - {self.status}"   

 


class Subject(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

class TeachingAssignment(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role':'teacher'})
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"({self.subject_id})"
    # unique_together = ('teacher', 'subject', 'class_obj')

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role':'student'})
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='active')

    def __str__(self):
        return f"{self.student.name} - {self.class_id.name} - {self.status}"


    #message
# apps/messaging/models.py
class Conversation(models.Model):
    TYPE_CHOICES = [
        ('private', 'Private'),
        ('group', 'Group')
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES,default='private')
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True)  # for group
    participants = models.ManyToManyField(User, through='ConversationParticipant')

    def __str__(self):
        return f"Conversation {self.id} - {self.type}"


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message {self.id} from {self.sender.name} in Conversation {self.conversation.id}"
    # read_by many-to-many? For simplicity, keep a boolean per message, or track read receipts separately.    



    # apps/resources/models.py
class Resource(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role':'teacher'})
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='resources/%Y/%m/%d/')
    metadata = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.school.name} - {self.class_id.name}"
    # metadata: file_type, size, etc. can be derived


# apps/notifications/models.py
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    type = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    body = models.TextField()
    read_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification {self.id} for {self.user.name} - {self.type}" 
    # optional: link to object (e.g., message, resource) via GenericForeignKey 

class ConversationParticipant(models.Model):
    conversation = models.ForeignKey(Conversation,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.user.name} in Conversation {self.conversation.id}"  