from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Oficinas(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    Nombre_oficina = models.CharField(max_length=100)

    def __str__(self):
        return self.Nombre_oficina


class Trabajador(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    PrimerApellido = models.CharField(max_length=35)
    SegundoApellido = models.CharField(max_length=35)
    Nombre = models.CharField(max_length=35)
    Genero = [
            ('F', 'Femenino'),
            ('M', 'Masculino')
    ]
    Genero = models.CharField(max_length=1, choices=Genero, default='F')

    Oficinas = models.ForeignKey(Oficinas, null=False, blank=False, on_delete=models.CASCADE)
    Vigencia = models.BooleanField(default=True)
    def __str__(self):
        return self.Nombre


class Diagnosticos (models.Model):
    
    motivo_diagnostico = (
    ('Asignacion', 'Asignacion'),
    ('Diagnostico de compra', 'Diagnostico de compra'),
    ('Baja', 'baja'),
    ('Diagnostico', 'Diagnostico') , 
    ('Prestamos', 'Prestamos'),
    )

    equipo_a_reparar = (
    ('CPU', 'CPU'),
    ('MONITOR', 'MONITOR'),
    ('TECLADO', 'TECLADO'),
    ('MOUSE', 'MOUSE'),
    ('UPS', 'UPS'),
    ('IMPRESORA', 'IMPRESORA'),
    ('ESCANER', 'ESCANER'),
    ('ESTABILIZADOR', 'ESTABILIZADOR'),
    ('DISCO DURO', 'DISCO DURO'),
    ('SWITCH', 'SWITCH'),
    ('ROUTER', 'ROUTER'),
    ('LAPTOP', 'LAPTOP'),
    ('ACOMULADORES', 'ACOMULADORES'),
    ('ART.VARIOS', 'ART.VARIOS'),
    ('SERVIDOR', 'SERVIDOR'),
    ('DATASHOW', 'DATASHOW'),
    ('TONER', 'TONER'),
    ('FOTOCOPIADORA', 'FOTOCOPIADORA'),
    ('INFORMACION', 'INFORMACION'),
    ('PARLANTES', 'PARLANTES'),
    ('TELEFONO_IP', 'TELEFONO_IP'),
    )

    lugar_del_equipo = (
    ('Asociaciones Sindicales 27', 'Asociaciones Sindicales 27'),
    ('Asuntos Internacionales 9', 'Asuntos Internacionales 9'),
    ('Auditoria Interna 7', 'Auditoria Interna 7'),
    ('Auditorio Jose Benito E. 46', 'Auditorio Jose Benito E. 46'),
    ('Auditorio Luisa Amanda Aguilar 43', 'Auditorio Luisa Amanda Aguilar 43'),
    ('Biblioteca 44', 'Biblioteca 44'),
    ('Boaco 107', 'Boaco 107'),
    ('Call Center 22', 'Call Center 22'),
    ('Carazo 109', 'Carazo 109'),
    ('Chichigalpa 118', 'Chichigalpa 118'),
    ('Chinandega 117', 'Chinandega 117'),
    ('Chontales 108', 'Chontales 108'),
    ('CLS 121', 'CLS 121'),
    ('Conciliacion Individual 21', 'Conciliacion Individual 21'),
    ('Contabilidad 40','Contabilidad 40'),
    ('Contraloria (Bodega_Despacho) 11', 'Contraloria (Bodega_Despacho) 11'),
    ('DAF 122', 'DAF 122'),
    ('Defensoria Laboral 23', 'Defensoria Laboral 23'),
    ('Depto. Observatorio Mercado Laboral 14', 'Depto. Observatorio Mercado Laboral 14'),
    ('Despacho Ministra 12', 'Despacho Ministra 12'),
    ('Despacho Vice-Ministro 10', 'Despacho Vice-Ministro 10'),
    ('DGAF 34', 'DGAF 34'),
    ('DGDCAL 20', 'DGDCAL 20'),
    ('DGHyST 8', 'DGHyST 8'),
    ('DGPES 16', 'DGPES 16'),
    ('Direccion De Analisis e Intermediacion Laboral 13', 'Direccion De Analisis e Intermediacion Laboral 13'),
    ('Direccion Juridica 24', 'Direccion Juridica 24'),
    ('DPYP 17', 'DPYP 17'),
    ('Esteli 114', 'Esteli 114'),
    ('Granada 103', 'Granada 103'),
    ('Informatica 3', 'Informatica 3'),
    ('Inspect. Trabajo Infantil 36', 'Inspect. Trabajo Infantil 36'),
    ('Inspectoria General De Trabajo 31', 'Inspectoria General De Trabajo 31'),
    ('Jalapa 119', 'Jalapa 119'),
    ('Jinotega 112', 'Jinotega 112'),
    ('Leon 102', 'Leon 102'),
    ('Local I (Construccion) 28', 'Local I (Construccion) 28'),
    ('Local II (Servicio) 30', 'Local II (Servicio) 30'),
    ('Local III (Agro_Industria) 29', 'Local III (Agro_Industria) 29'),
    ('Madriz 115', 'Madriz 115'),
    ('Masaya 110', 'Masaya 110'),
    ('Matagalpa 113', 'Matagalpa 113'),
    ('Migracion Laboral 18', 'Migracion Laboral 18'),
    ('Negociacion Colectiva 26', 'Negociacion Colectiva 26'),
    ('Nueva Segovia 116', 'Nueva Segovia 116'),
    ('OAIP 41', 'OAIP 41'),
    ('Observatorio Laboral 25', 'Observatorio Laboral 25'),
    ('Oficina de Genero 32', 'Oficina de Genero 32'),
    ('Oficina de presupuesto 37', 'Oficina de presupuesto 37'),
    ('Oficina de presupuesto 5', 'Oficina de presupuesto 5'),
    ('PALO 35', 'PALO 35'),
    ('Planificacion 4', 'Planificacion 4'),
    ('Planta Telefonica 6', 'Planta Telefonica 6'),
    ('Productividad y Salario 19', 'Productividad y Salario 19'),
    ('RAAN 111', 'RAAN 111'),
    ('RAAS 106', 'RAAS 106'),
    ('Rivas 104', 'Rivas 104'),
    ('RRHH 15', 'RRHH 15'),
    ('Sala de Capacitacion 33', 'Sala de Capacitacion 33'),
    ('San Carlos 105', 'San Carlos 105'),
    ('San Juan de Rio Coco 120', 'San Juan de Rio Coco 120'),
    ('Secretaria Laboral 2', 'Secretaria Laboral 2'),
    ('SEPEM 1', 'SEPEM 1'),
    ('Servicios Generales 38', 'Servicios Generales 38'),
    ('SITMIT 47', 'SITMIT 47'),
    ('Suministro 42', 'Suministro 42'),
    ('Tesoreria 45', 'Tesoreria 45'),
    ('Transporte 48', 'Transporte 48'),
    ('Unidad de Adquisicion 39', 'Unidad de Adquisicion 39'),
    ('Unidad de Control de Bienes 49', 'Unidad de Control de Bienes 49'),
    )





    ID = models.AutoField(primary_key=True)
    FechaSalida = models.DateTimeField(auto_now_add=True)
    Para = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    De = models.ForeignKey(User, on_delete=models.CASCADE)
    FechaIngreso = models.DateField(null=True)
    Asunto = models.CharField(max_length=100)
    PorEsteMedioEmito = models.CharField(max_length=100, choices=motivo_diagnostico,)
    de = models.CharField(max_length=100, choices=equipo_a_reparar)
    DeLaOficina_Delegacion = models.CharField(max_length=100, choices=lugar_del_equipo)
    Nota = models.TextField()

    
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    S_N = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    INV = models.CharField(max_length=100)
    situacion = models.TextField()
    conclusión = models.TextField()
    identificador = models.CharField(max_length=20, unique=True, blank=True, null=True)

    
    def save(self, *args, **kwargs):
        if not self.identificador:
            tipo_abreviado = self.de[:3].upper()
            secuencia = Diagnosticos.objects.filter(de=self.de).count() + 1
            self.identificador = f"{tipo_abreviado}-{secuencia}"
        super().save(*args, **kwargs)
 
    def __str__(self):
        return self.identificador