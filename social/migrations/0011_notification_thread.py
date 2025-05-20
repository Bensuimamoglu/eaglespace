from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0010_messagemodel_threadmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='social.threadmodel'),
        ),
    ]
