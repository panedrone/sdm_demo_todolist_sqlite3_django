"""
This code was generated by a tool. Don't modify it manually.
http://sqldalmaker.sourceforge.net
"""

from django.db import models


class GroupLI(models.Model):
    g_id = models.AutoField(db_column='g_id', primary_key=True, max_length=256)
    g_name = models.CharField(db_column='g_name', max_length=256)
    g_tasks_count = models.CharField(db_column='g_tasks_count', max_length=256)

    class Meta:
        managed = False

    SQL = """select g.*,  
                (select count(*) from tasks where g_id=g.g_id) as g_tasks_count 
                from groups g 
                order by g.g_id"""
