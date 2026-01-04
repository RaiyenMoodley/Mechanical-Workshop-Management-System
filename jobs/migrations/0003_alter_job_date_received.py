# Generated manually

from django.db import migrations, models
from datetime import date


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_date_completed_job_invoice_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='date_received',
            field=models.DateField(default=date.today),
        ),
    ]

