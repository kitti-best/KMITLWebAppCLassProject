# Generated by Django 4.1.7 on 2023-09-23 03:31

from django.conf import settings
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LearningCenter',
            fields=[
                ('_uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=150, unique=True, validators=[django.core.validators.MinLengthValidator(4)])),
                ('description', models.TextField()),
                ('latitude', models.FloatField(default=0, max_length=15)),
                ('longtitude', models.FloatField(default=0, max_length=15)),
                ('house_number', models.CharField(default='', max_length=15)),
                ('section', models.CharField(default='', max_length=10)),
                ('street', models.CharField(default='', max_length=15)),
                ('sub_district', models.CharField(default='', max_length=30)),
                ('district', models.CharField(default='', max_length=30)),
                ('province', models.CharField(default='', max_length=30)),
                ('country', models.CharField(default='Thailand', max_length=30)),
                ('website', models.URLField(blank=True, null=True)),
                ('phone', models.CharField(default='', max_length=30, validators=[django.core.validators.RegexValidator(regex='((\\+66|0)(\\d{1,2}\\-?\\d{3}\\-?\\d{3,4}))|((\\+๖๖|๐)([๐-๙]{1,2}\\-?[๐-๙]{3}\\-?[๐-๙]{3,4}))')])),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('levels', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('subjects_taught', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('popularity', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('waiting', 'waiting'), ('approve', 'approve'), ('reject', 'reject')], default='waiting', editable=False, max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [('learning_center_admin', 'can approve or reject the learning center, can view the waiting and reject learning center')],
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('tutor_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=150, unique=True, validators=[django.core.validators.MinLengthValidator(4)])),
                ('description', models.TextField()),
                ('profile', models.ImageField(upload_to='pictures')),
                ('learning_center', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LearningCenter.learningcenter')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=150, unique=True, validators=[django.core.validators.MinLengthValidator(4)])),
                ('description', models.TextField()),
                ('learning_center', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LearningCenter.learningcenter')),
            ],
        ),
    ]