from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

class BlogModel(models.Model):
    title = models.CharField(max_length=150, verbose_name="Başlık")
    description = models.CharField(max_length=500, verbose_name="Açıklama")
    content = RichTextUploadingField()
    img = models.ImageField(verbose_name="Resim")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated = models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Yazar")
    likes = models.ManyToManyField(User, blank=True, related_name="likes", verbose_name="Beğeniler")
    slug = models.SlugField(editable=False)
    status = models.BooleanField(verbose_name="Aktif / Pasif", default=0)

    def __str__(self):
        return self.title

    def get_like_count(self):
        return self.likes.count

    def get_absolute_url(self):
        return reverse("", kwargs={'slug' : self.slug})
        
    def get_unique_slug(self):
        slug = slugify(self.title.replace("ı", "i"))
        unique_slug = slug
        counter = 1
        while BlogModel.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug,counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        super(BlogModel, self).save(*args, **kwargs)