from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    ethnicity_hispanic = models.BooleanField(default=False)
    gender = (
    ('M', 'Male'),
    ('F', 'Female'),
    )
    birth_date = models.DateField()
    race = (
    ('I', 'American Indian/Alaskan Native'),
    ('A', 'Asian'),
    ('B', 'Black'),
    ('H', 'Native Hawaiian/Other Pacific Islander'),
    ('W', 'White'),
    ('O', 'Other Multi racial'),
    )

class StudentIntakeForm(models.Model):
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    form_id = models.ForeignKey(IntakeForm, on_delete = models.CASCADE)

class IntakeForm(models.Model):
    form_id = models.AutoField(primary_key = True)
    form_date = models.DateField()
    student_age = models.IntegerField()
    current_grade = models.IntegerField()
    school = models.CharField(max_length=80)
    disabled = models.BooleanField(default=False)
    disabled_description = models.CharField(max_length=80)
    street_address_number = models.IntegerField()
    street_name = models.CharField(max_length = 80)
    zip_code = models.IntegerField()
    apartment_num = models.IntegerField()
    phone_number = models.IntegerField()
    homeless_youth = models.BooleanField(default=False)
    community_area =
    ward = models.IntegerField()
    family_type = (
    ('SF', 'Single Parent/Female'),
    ('SM', 'Single Parent/Male'),
    ('TP', 'Two-parent household'),
    ('IY', 'Independent Youth'),
    ('R', 'Relative'),
    ('G', 'Guardian'),
    )
    housing_status = (
    ('R', 'Rent'),
    ('O', 'Own'),
    ('H', 'Homeless/Shelter'),
    ('TH', 'In Temporary Housing'),
    )
    food_stampes = models.BooleanField(default=False)
    free_lunch = models.BooleanField(default=False)
    health_insurance = models.BooleanField(default=True)
    income_source = (
    ('Em', 'Employment'),
    ('P', 'Pension'),
    ('T', 'TANF'),
    ('Ea', 'Earnfare'),
    ('SS', 'Social Security'),
    ('UI', 'Unemployment Insurance'),
    ('O', 'Other - Including SSDI, Child Support and VA Benefits'),
    ('SSI', 'SSI'),
    )
    referral = models.CharField(max_length = 80)

class PickupPerson(models.Model):
    person_id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    relation = models.CharField(max_length = 45)
    phone_number = models.IntegerField()
    primary_language = models.CharField(max_length = 45)
    us_citizen = models.BooleanField(default=True)
    vote_registered = models.BooleanField(default=True)
    CMAA_interest = models.BooleanField(default=False)

class Permissions(models.Model):
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete = models.CASCADE)
    can_walk_home = models.BooleanField(default=False)
    can_be_picked_up = models.BooleanField(default=False)

class Grades(models.Model):
    grade_id = models.AutoField(primary_key = True)
    year = models.IntegerField()
    teacher_name = models.CharField(max_length = 45)
    notes = models.CharField(max_length = 80)
    course = models.CharField(max_length = 45)
    period = models.IntegerField()
    cycle_1 = models.CharField(max_length = 1)
    cycle_2 = models.CharField(max_length = 1)
    cycle_3 = models.CharField(max_length = 1)
    cycle_4 = models.CharField(max_length = 1)
    sem_1 = models.CharField(max_length = 1)
    sem_2 = models.CharField(max_length = 1)

class StudentGrades(model.Models):
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    grade_id = models.ForeignKey(Grades, on_delete = models.CASCADE)

class Worksheets(model.Models):
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    worksheets_completed = models.IntegerField()
    date = models.DateField()
