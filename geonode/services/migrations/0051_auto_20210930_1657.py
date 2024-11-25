# Generated by Django 3.2.7 on 2021-09-30 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0050_delete_harvestjob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(choices=[('AUTO', 'Auto-detect'), ('OWS', 'Paired WMS/WFS/WCS'), ('WMS', 'Web Map Service'), ('CSW', 'Catalogue Service'), ('REST_MAP', 'ArcGIS REST MapServer'), ('REST_IMG', 'ArcGIS REST ImageServer'), ('REST_FEATURE', 'ArcGIS REST FeatureServer'), ('OGP', 'OpenGeoPortal'), ('HGL', 'Harvard Geospatial Library'), ('GN_WMS', 'GeoNode (Web Map Service)'), ('GN_CSW', 'GeoNode (Catalogue Service)')], max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='version',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
