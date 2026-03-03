from django.db import models


class Employee(models.Model):
    """An employee who can be marked absent."""

    name = models.CharField(max_length=200)
    # Optional: later you can add role, phone, etc.

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class Absence(models.Model):
    """A record of an employee being absent on a given date."""

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='absences')
    date = models.DateField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-date']
        unique_together = ('employee', 'date')

    def __str__(self) -> str:
        return f"{self.employee.name} absent on {self.date}"

