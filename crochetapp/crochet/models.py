import uuid
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class StitchType(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Full name of the stitch (e.g., Single Crochet)")
    abbreviation = models.CharField(max_length=10, unique=True, help_text="Common abbreviation (e.g., SC)")

    class Meta:
        verbose_name = "Stitch Type"
        verbose_name_plural = "Stitch Types"

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"

class Material(models.Model):
    MATERIAL_TYPES = [
        ('YARN', 'Yarn'),
        ('HOOK', 'Hook'), 
        ('NOTION', 'Notion'),
        ('OTHER', 'Other')
    ]

    name = models.CharField(max_length=100, help_text="Descriptive name (e.g., Worsted Weight Yarn, 4.0mm Hook)")
    type = models.CharField(max_length=50, choices=MATERIAL_TYPES, default='YARN')
    gauge_info = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        help_text="Optional: Tension or gauge specifications for this material."
    )

    class Meta:
        verbose_name_plural = "Materials"
        unique_together = ('name', 'type') 

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"


class Pattern(models.Model):
    DIFFICULTY_CHOICES = [
        ('EASY', 'Easy'),
        ('MEDIUM', 'Medium'),
        ('HARD', 'Hard'),
        ('EXPERT', 'Expert'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patterns') 
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, help_text="Detailed summary of the pattern.")
    instructions = models.TextField(help_text="Step-by-step crochet instructions.")
    difficulty_level = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES, default='EASY')
    is_public = models.BooleanField(default=True, help_text="If checked, the pattern is visible to all users.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at'] 

    def __str__(self):
        return self.title


class PatternMaterial(models.Model):
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE, related_name='required_materials')
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.CharField(
        max_length=100, 
        help_text="Specific amount needed (e.g., '3 skeins', '1 hook')"
    )

    class Meta:
        unique_together = ('pattern', 'material')
        verbose_name = "Required Material"
        verbose_name_plural = "Required Materials"

    def __str__(self):
        return f"{self.quantity} of {self.material.name} for {self.pattern.title}"

class PatternStitch(models.Model):
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE, related_name='used_stitches')
    stitch_type = models.ForeignKey(StitchType, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('pattern', 'stitch_type')
        verbose_name = "Pattern Stitch"
        verbose_name_plural = "Pattern Stitches"

    def __str__(self):
        return f"{self.stitch_type.abbreviation} used in {self.pattern.title}"

class Comment(models.Model):
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.pattern.title}"
