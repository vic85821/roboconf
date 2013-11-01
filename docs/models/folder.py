from django.db import models
from django.utils.timezone import now

class Folder(models.Model):
	name = models.CharField(max_length=256)
	parent = models.ForeignKey('self', null=True, related_name='folders')
	last_modified = models.DateTimeField(editable=False, default=now)
	permissions = models.ManyToManyField('Permission', related_name='perm+')
	
	# == Version control ==
	is_archived = models.BooleanField(default=False)
	starring = models.ManyToManyField(User, related_name='starred_files')

	# == Linkbacks from other models ==
	# folders (OneToManyField to self)
	# files (OneToManyField to File)

	def __unicode__(self):
		return self.name
