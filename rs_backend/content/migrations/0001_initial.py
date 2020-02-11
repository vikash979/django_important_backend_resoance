# Generated by Django 2.2.9 on 2020-02-11 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0003_auto_20200211_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('object_status', models.SmallIntegerField(choices=[(1, 'Deleted'), (0, 'Active')], default=0)),
                ('type', models.SmallIntegerField(choices=[(1, 'Exercise'), (2, 'Daily Practice Problems'), (3, 'Solved Examples')], default=0)),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('timed_type', models.SmallIntegerField(choices=[(0, 'Timed on Total'), (1, 'Timed on Questions')], default=0)),
                ('timed_duration_mins', models.IntegerField(default=0)),
                ('total_marks', models.IntegerField(default=0)),
                ('attempts_allowed', models.IntegerField(default=0)),
                ('is_graded', models.BooleanField(default=False)),
                ('difficulty', models.SmallIntegerField(choices=[(0, 'Easy'), (1, 'Medium'), (2, 'Hard'), (3, 'Very Hard')], default=0)),
                ('result_after', models.SmallIntegerField(choices=[(0, 'Every Question'), (1, 'All Questions')], default=0)),
                ('allowed_after_duedate', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssessmentSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('object_status', models.SmallIntegerField(choices=[(1, 'Deleted'), (0, 'Active')], default=0)),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('negative_marking_per_q', models.IntegerField(default=0)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Assessment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('object_status', models.SmallIntegerField(choices=[(1, 'Deleted'), (0, 'Active')], default=0)),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('object_status', models.SmallIntegerField(choices=[(1, 'Deleted'), (0, 'Active')], default=0)),
                ('start_date_time', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('duration_hours', models.IntegerField(default=0)),
                ('phase_id', models.IntegerField()),
                ('batch_id', models.IntegerField()),
                ('faculty', models.IntegerField(default=0)),
                ('room', models.CharField(blank=True, help_text='The class where lecture is happening', max_length=120, null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.HasSubjects')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('object_status', models.SmallIntegerField(choices=[(1, 'Deleted'), (0, 'Active')], default=0)),
                ('uid', models.CharField(blank=True, help_text='The unique identifier of question', max_length=120, null=True)),
                ('question_type', models.SmallIntegerField(choices=[(1, 'Multiple Choice Questions'), (2, 'Single Integer Questions'), (3, 'Multiple Response Questions'), (4, 'Fill in the Blanks'), (5, 'True False')], default=0)),
                ('duration_seconds', models.IntegerField(default=0)),
                ('marks', models.FloatField(default=0)),
                ('negative_marking', models.IntegerField(default=0)),
                ('source', models.SmallIntegerField(choices=[(1, 'Exercise'), (2, 'Daily Practice Problems'), (3, 'Solved Examples')], default=0)),
                ('difficulty', models.SmallIntegerField(choices=[(0, 'Easy'), (1, 'Medium'), (2, 'Hard'), (3, 'Very Hard')], default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('object_status', models.SmallIntegerField(choices=[(1, 'Deleted'), (0, 'Active')], default=0)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.Question')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionTOCMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('object_status', models.SmallIntegerField(choices=[(1, 'Deleted'), (0, 'Active')], default=0)),
                ('level', models.SmallIntegerField(choices=[(0, 'Unit'), (1, 'Chapter'), (2, 'Topic'), (3, 'Subtopic')])),
                ('toc_id', models.IntegerField()),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.Question')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('object_status', models.SmallIntegerField(choices=[(1, 'Deleted'), (0, 'Active')], default=0)),
                ('statement', models.TextField()),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.Language')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.Question')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionOptionsStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('object_status', models.SmallIntegerField(choices=[(1, 'Deleted'), (0, 'Active')], default=0)),
                ('statement', models.TextField()),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.Language')),
                ('question_option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.QuestionOptions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionOptionsExplanation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('object_status', models.SmallIntegerField(choices=[(1, 'Deleted'), (0, 'Active')], default=0)),
                ('explanation', models.TextField()),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.Language')),
                ('question_option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.QuestionOptions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LectureTOCMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('object_status', models.SmallIntegerField(choices=[(1, 'Deleted'), (0, 'Active')], default=0)),
                ('level', models.SmallIntegerField(choices=[(0, 'Unit'), (1, 'Chapter'), (2, 'Topic'), (3, 'Subtopic')])),
                ('toc_id', models.IntegerField()),
                ('lecture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.Lecture')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssessmentTOCMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('object_status', models.SmallIntegerField(choices=[(1, 'Deleted'), (0, 'Active')], default=0)),
                ('level', models.SmallIntegerField(choices=[(0, 'Unit'), (1, 'Chapter'), (2, 'Topic'), (3, 'Subtopic')])),
                ('toc_id', models.IntegerField()),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Assessment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssessmentSectionQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('object_status', models.SmallIntegerField(choices=[(1, 'Deleted'), (0, 'Active')], default=0)),
                ('negative_marking_per_q', models.IntegerField(default=0)),
                ('assessment_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.AssessmentSection')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.Question')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
