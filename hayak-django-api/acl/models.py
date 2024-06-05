from django.db import models

class Role(models.Model):
  name = models.CharField(max_length=50, unique=True)
  
  class Meta:
    db_table = "roles"

  def __str__(self):
    return self.name

class Permission(models.Model):
  name = models.CharField(max_length=50, unique=True)
  
  class Meta:
    db_table = "permissions"

  def __str__(self):
    return self.name
  
class RolePermission(models.Model):
  role = models.ForeignKey(Role, on_delete=models.CASCADE)
  permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

  class Meta:
    db_table = "role_permissions"

  def __str__(self):
    return f"{self.role.name} - {self.permission.name}"