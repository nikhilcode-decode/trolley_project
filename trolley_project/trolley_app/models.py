from django.contrib.auth.models import User
from django.db import models

class TrolleyChecklist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    trolley_no = models.CharField(max_length=200)
    inspector_name = models.CharField(max_length=100)
    trolley_no_availability = models.CharField(max_length=100)
    trolley_rust_condition = models.CharField(max_length=100)
    trolley_handle_condition = models.CharField(max_length=100)
    part_resting_support_conditions = models.CharField(max_length=100)
    joint_welding_conditions = models.CharField(max_length=100)
    tow_hook_condition = models.CharField(max_length=100)
    wheel_moments = models.CharField(max_length=100)
    Wheel_lock_and_balancing = models.CharField(max_length=100)
    wheel_plate_conditions = models.CharField(max_length=100)
    Trolley_cushioning_material_conditions = models.CharField(max_length=100)
    Sharp_edge_check = models.CharField(max_length=100)
    flap_trolley_cover_conditions = models.CharField(max_length=100)
    trolley_plate_availability = models.CharField(max_length=100)
    trolley_door_hinge_condition = models.CharField(max_length=100)
    trolley_holding_position_greencolor = models.CharField(max_length=100)
    trolley_pinch_hazard_orangecolour = models.CharField(max_length=100)

    status = models.CharField(max_length=100)  # OK or NG
    date_checked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.trolley_no} - {self.inspector_name}"
