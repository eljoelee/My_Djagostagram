from django.db import models
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

class Photo(models.Model):
    # 이용자 모델을 Photo 모델의 user 모델 필드에 ForeignKey 관계로 연결
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    image = models.ImageField(upload_to='%Y/%m/%d/orig')
    filtered_image = models.ImageField(upload_to='%Y/%m/%d/filtered')
    content = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.image.delete()
        self.filtered_image.delete()
        super(Photo, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        url = reverse_lazy('detail', kwargs = {'pk':self.pk})
        return url