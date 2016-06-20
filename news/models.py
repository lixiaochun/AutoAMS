# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse

@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField('栏目名称',max_length=256)
    slug = models.CharField('栏目网址',max_length=256,db_index=True)
    intro = models.TextField('栏目简介',default='')

    nav_display = models.BooleanField('导航显示', default=False)
    home_display = models.BooleanField('首页显示', default=False)

    def get_absolute_url(self):
        return reverse('column', args=(self.slug,))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = '文章分类'
        ordering = ['name'] # 按照哪个栏目排序

@python_2_unicode_compatible
class Article(models.Model):

    title = models.CharField('标题',max_length=256)
    slug = models.CharField('网址',max_length=256,db_index=True)
    #column = models.ManyToManyField(Column,verbose_name='归属栏目') # 多对多，一篇文章多个分类
    column = models.ForeignKey(Column,verbose_name='分类')
    author = models.CharField('作者',max_length=256)
    content = models.TextField('内容',default='',blank=True)
    count = models.IntegerField('统计',default=0)
    pub_date = models.DateTimeField('发布时间',auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间',auto_now=True,null=True)
    published = models.BooleanField('正式发布',default=True)

    def get_absolute_url(self):
        return reverse('article', args=(self.pk,))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章列表'
        verbose_name_plural = '文章列表'