from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail
from django.utils.safestring import mark_safe


class SizeCategory(models.Model):
    title = models.CharField(
        verbose_name='Название категории',
        max_length=64,
        unique=True,
    )

    class Meta:
        verbose_name = 'категория размера'
        verbose_name_plural = 'категории размера'
    
    def __str__(self) -> str:
        return self.title


class Size(models.Model):
    size = models.CharField(
        verbose_name='Размер одежды',
        max_length=32,
        unique=True,
    )
    size_category = models.ForeignKey(
        verbose_name='Категория',
        to=SizeCategory,
        default=None,
        null=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'размер'
        verbose_name_plural = 'размеры'
    
    def __str__(self) -> str:
        return self.size


class Category(models.Model):
    title = models.CharField(
        verbose_name='Название категории',
        max_length=64,
        unique=True,
    )
    thumbnail = ImageField(
        verbose_name='Изображение категории',
        default=None,
        upload_to='uploads/',
        null=True,
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        
    def __str__(self) -> str:
        return self.title

    def get_image_500x500(self):
        return get_thumbnail(self.thumbnail, '500x500', crop='center', quality=81)

    def admin_thumbnail(self):
        return mark_safe(
            f'<img src="{get_thumbnail(self.thumbnail, "500x500", crop="center", quality=41).url}" '
            f'width=30% height=30%>'
        )

    admin_thumbnail.short_description = 'Изображение'
    admin_thumbnail.allow_tags = True


class Product(models.Model):
    title = models.CharField(
        verbose_name='Название товара',
        max_length=64,
    )
    thumbnail = ImageField(
        verbose_name='Изображение товара',
        default=None,
        upload_to='uploads/',
        null=True,
    )
    category = models.ForeignKey(
        verbose_name='Категория',
        to=Category,
        default=None,
        on_delete=models.CASCADE,
    )
    description = models.TextField(
        verbose_name='Описание товара',
        blank=True,
    )
    price = models.IntegerField(
        verbose_name='Цена товара',
    )
    sizes = models.ManyToManyField(
        verbose_name='Размеры',
        to=Size,
        default=None,
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self) -> str:
        return self.title

    def get_image_1024(self):
        return get_thumbnail(self.thumbnail, '1024', crop='center', quality=81)

    def get_image_500x500(self):
        return get_thumbnail(self.thumbnail, '500x500', crop='center', quality=81)

    def admin_thumbnail(self):
        return mark_safe(
            f'<img src="{get_thumbnail(self.thumbnail, "500x500", crop="center", quality=41).url}" '
            f'width=30% height=30%>'
        )

    admin_thumbnail.short_description = 'Изображение'
    admin_thumbnail.allow_tags = True


class Image(models.Model):
    thumbnail = ImageField(
        verbose_name='Дополнительное изображение товара',
        default=None,
        upload_to='uploads/',
        null=True,
    )
    product = models.ForeignKey(
        verbose_name='Товар',
        to=Product,
        default=None,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'

    def __str__(self) -> str:
        return f'{self.id} {self.product}'
    
    def get_image_1024(self):
        return get_thumbnail(self.thumbnail, '1024', crop='center', quality=81)

    def get_image_500(self):
        return get_thumbnail(self.thumbnail, '500', crop='center', quality=81)

    def get_image_500x500(self):
        return get_thumbnail(self.thumbnail, '500x500', crop='center', quality=81)

    def admin_thumbnail(self):
        return mark_safe(
            f'<img src="{get_thumbnail(self.thumbnail, "500x500", crop="center", quality=41).url}" '
            f'width=30% height=30%>'
        )

    admin_thumbnail.short_description = 'Изображение'
    admin_thumbnail.allow_tags = True
