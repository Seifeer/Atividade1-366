# Generated by Django 2.1.5 on 2019-01-17 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='despesa',
            old_name='quitato',
            new_name='quitado',
        ),
        migrations.AlterField(
            model_name='despesa',
            name='data_criacao',
            field=models.CharField(max_length=50, verbose_name='Data de criação'),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='descricao',
            field=models.CharField(max_length=40, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='forma_pag',
            field=models.CharField(choices=[('1', 'Dinheiro'), ('2', 'Cartão de Crédito'), ('3', 'Cartão de Debito')], max_length=30, verbose_name='Pagamento'),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='tipo_despesa',
            field=models.CharField(choices=[('1', 'Remedio'), ('2', 'Alimentação'), ('3', 'Educação'), ('4', 'Transporte')], max_length=50, verbose_name='Tipo de despesa'),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='vencimento',
            field=models.DateField(verbose_name='Vencimento'),
        ),
    ]
