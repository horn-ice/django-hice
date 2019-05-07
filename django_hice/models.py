import uuid

from django.db import models

class Task(models.Model):
    # A model to save information about an asynchronous task

    # Type of invariant inference algorithm
    NONE = 'NO'
    HOUDINI = 'HO'
    SORCAR = 'SO'
    DT = 'DT'
    INFERENCE_CHOICES = (
        (NONE, 'None'),
        (HOUDINI, 'Houdini'),
        (SORCAR, 'Sorcar'),
        (DT, 'Decision trees'),
    )

    created_on = models.DateTimeField(auto_now_add=True)
    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=10, default='waiting')
    data = models.TextField(default='')
    inference = models.CharField(max_length=2, choices=INFERENCE_CHOICES, default=NONE)
    trace = models.BooleanField(default=False)
    result = models.TextField(blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.temp_file_name = None
