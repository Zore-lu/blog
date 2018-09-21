from django.db import models

# Create your models here.
# https://zhangjia.tv/852.html

class User(models.Model):
    '''
    用户信息
    '''
    pass
    # 用户id

    # 用户名

    # 用户密码

    # 用户邮箱

    # 用户头像

    # 用户等级

    # 用户权限

    # 注册时间

    # 用户手机号


class Articles(models.Model):
    '''
    博客信息
    '''

    pass
    # 博客id

    # 用户id

    # 博客标题

    # 博客标签

    # 博客内容

    # 浏览量

    # 评论总数

    # 发表日期

    # 更改日期

    # 点赞数

class Comments(models.Model):
    '''
    文章评论
    '''
    pass

    # 评论id

    # 用户id

    # 评论内容

    # 点赞数

    # 评论日期



