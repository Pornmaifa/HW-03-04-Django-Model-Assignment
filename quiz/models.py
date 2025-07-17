from django.db import models

class Question(models.Model):
    text = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return f"คำถาม:\n{self.text}\nวันที่เผยแพร่: {self.published_date}"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    def __str__(self):
        status = '✓ ถูกต้อง' if self.correct else '✗ ผิด'
        return f"ตัวเลือก:\n{self.text}\nสถานะ: {status}"
