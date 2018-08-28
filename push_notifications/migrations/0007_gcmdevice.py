from django.db import migrations, models


class Migration(migrations.Migration):

	dependencies = [
		('push_notifications', '0006_webpushdevice'),
	]

	operations = [
		migrations.AlterField(
			model_name='gcmdevice',
			name='registration_id',
			field=models.CharField(db_index=True, max_length=255, verbose_name='Registration ID'),
		),
	]
