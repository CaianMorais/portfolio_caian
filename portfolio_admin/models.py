from django.db import models

def upload_projeto(instance, filename):
    return f'midia/projeto-{instance.titulo}/{filename}'

def upload_sobre(instance, filename):
    return f'midia/sobre-{instance.nome}/{filename}'

def upload_tecnologia(instance, filename):
    return f'midia/tecnologia-{instance.nome}/{filename}'

def upload_contato(instance, filename):
    return f'midia/contato-{instance.id}/{filename}'

# Create your models here.
class Projetos(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200, null=False, blank=False)
    subtitulo = models.CharField(max_length=300, null=False, blank=False)
    descricao = models.TextField(max_length=10000, null=False, blank=False)
    midia = models.ImageField(upload_to=upload_projeto, null=True, blank=True)
    publico = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
    
class Sobre(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    profissao = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(max_length=5000, null=False, blank=False, )
    foto = models.ImageField(upload_to=upload_sobre, null=True, blank=True)
    publico = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    
class Tecnologias(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(max_length=2000, null=True, blank=False)
    icone = models.ImageField(upload_to=upload_tecnologia, null=True, blank=True)
    publico = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    
class Curriculo(models.Model):
    id = models.AutoField(primary_key=True)
    arquivo = models.FileField(upload_to=f'midia/curriculos/', null=False, blank=False)
    publico = models.BooleanField(default=True)

    def __str__(self):
        return f'Curriculo {self.id}'
    
    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old = Curriculo.objects.get(pk=self.pk)
            except Curriculo.DoesNotExist:
                old = None

            if old and old.arquivo != self.arquivo:
                old.arquivo.delete(save=False)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.arquivo:
            self.arquivo.delete(save=False)
        super().delete(*args, **kwargs)