from django.db import models

STATUS_CHOICES = [
    ('A', 'Active'),
    ('C', 'Cancel'),
]

# Create your models here.
# class CONDPAY(models.Model):
#     LICEN_NO = models.CharField(max_length=12, primary_key=True)
#     COMP_NM = models.CharField(max_length=100)
#     COMP_ADR1 = models.CharField(max_length=100) 
#     COMP_ADR2 = models.CharField(max_length=100)
#     TELP = models.CharField(max_length=50)

#     class Meta:
#         db_table = 'CONDPAY'

#     def __str__(self):
#         return '%s' % (self.COMP_NM)

# class SETTYPE(models.Model):
#     TYPECOD = models.CharField(max_length=12, primary_key=True)
#     TYPEDES = models.CharField(max_length=60)

#     class Meta:
#         db_table = 'SETTYPE'

#     def __str__(self):
#         return '%s-%s' % (self.TYPECOD, self.TYPEDES)

class SETMODEL(models.Model):
    MODELCOD = models.CharField(max_length=20, primary_key=True)
    SUBMODEL = models.CharField(max_length=20)
    MODELDES = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'SETMODEL'

    def __str__(self):
        return '%s-%s' % (self.MODELCOD, self.MODELDES)

# class INVANLS(models.Model):
#     PARTNO = models.CharField(max_length=20, primary_key=True)
#     LOCAT = models.CharField(max_length=5)
#     YEAR1 = models.CharField(max_length=4)
#     COST_12 = models.DecimalField(max_digits=10,decimal_places=2)
#     ONHN_12 = models.DecimalField(max_digits=10,decimal_places=2)
#     PARTREAL = models.CharField(max_length=5)

#     class Meta:
#         db_table = 'INVANLS'

#     def __str__(self):
#         return '%s' % (self.PARTNO)

#     def getproduct(self):
#         return '%s' % (self.PARTNO)

class OFFICER(models.Model):
    CODE = models.CharField(max_length=8, primary_key=True)
    NAME = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'OFFICER'

    def __str__(self):
        return '%s' % (self.NAME)

class Prospect_resource(models.Model):
    CODE = models.CharField(max_length=20)
    NAME = models.CharField(max_length=100)

    class Meta:
        db_table = 'PROSPECT_RESOURCE'

    def __str__(self):
        return '%s' % (self.NAME)

class Prospect_resourcemore(models.Model):
    RESOURCE = models.ForeignKey(Prospect_resource, on_delete=models.PROTECT)
    CODE = models.CharField(max_length=20)
    NAME = models.CharField(max_length=100)

    class Meta:
        db_table = 'PROSPECT_RESOURCEMORE'

    def __str__(self):
        return '%s' % (self.NAME)

class Prospect_trace(models.Model):
    CODE = models.CharField(max_length=20)
    NAME = models.CharField(max_length=100)

    class Meta:
        db_table = 'PROSPECT_TRACE'

    def __str__(self):
        return '%s' % (self.NAME)

class Prospect_requirement(models.Model):
    CODE = models.CharField(max_length=20)
    NAME = models.CharField(max_length=100)

    class Meta:
        db_table = 'PROSPECT_REQUIREMENT'

    def __str__(self):
        return '%s' % (self.NAME)

class Prospect_media(models.Model):
    CODE = models.CharField(max_length=20)
    NAME = models.CharField(max_length=100)

    class Meta:
        db_table = 'PROSPECT_MEDIA'

    def __str__(self):
        return '%s' % (self.NAME)

class Prospect_condition(models.Model):
    CODE = models.CharField(max_length=20)
    NAME = models.CharField(max_length=100)

    class Meta:
        db_table = 'PROSPECT_CONDITION'

    def __str__(self):
        return '%s' % (self.NAME)

class CUSTMAST(models.Model):
    CUSCOD = models.CharField(max_length=13, primary_key=True)
    SNAM = models.CharField(max_length=8)
    NAME1 = models.CharField(max_length=50)
    NAME2 = models.CharField(max_length=50)

    class Meta:
       managed = False
       db_table = 'CUSTMAST'

class SETCOLOR(models.Model):
    COLORCOD = models.CharField(max_length=20, primary_key=True)
    COLORDES = models.CharField(max_length=60)

    class Meta:
       managed = False
       db_table = 'SETCOLOR'

class Prospect_test(models.Model):
    PROSPECTDT = models.DateField(null=True, blank=True)
    RESOURCE = models.ForeignKey(Prospect_resource, null=True, blank=True, on_delete=models.PROTECT)
    RESOURCEMORE = models.ForeignKey(Prospect_resourcemore, null=True, blank=True, on_delete=models.PROTECT)
    SALES_CONSULTANT = models.ForeignKey(OFFICER,  null=True, blank=True, on_delete=models.PROTECT)
    CUST_NAME = models.CharField(max_length=100, null=True, blank=True)
    CUST_LNAME = models.CharField(max_length=100, null=True, blank=True)
    CUST_TEL1 = models.CharField(max_length=20, null=True, blank=True)
    CUST_TEL2 = models.CharField(max_length=20, null=True, blank=True)
    CUST_TEL3 = models.CharField(max_length=20, null=True, blank=True)
    CUST_NOCARD = models.CharField(max_length=20, null=True, blank=True)
    CUST_BIRTHDT = models.DateField(null=True, blank=True)
    CUST_EMAIL = models.CharField(max_length=100, null=True, blank=True)
    REQUIREMENT = models.ForeignKey(Prospect_requirement, null=True, blank=True, on_delete=models.PROTECT)
    ADVISER = models.ForeignKey(CUSTMAST, db_column='ADVISER', null=True, blank=True, on_delete=models.PROTECT)
    MODEL = models.ForeignKey(SETMODEL,  null=True, blank=True, on_delete=models.PROTECT)
    SALES_PRICE = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    STATUS_PROSPECT = models.CharField(max_length=1, default='A', choices=STATUS_CHOICES)
    TRACE = models.ForeignKey(Prospect_trace, null=True, blank=True, on_delete=models.PROTECT)
    MEDIA = models.ForeignKey(Prospect_media, null=True, blank=True, on_delete=models.PROTECT)
    COLOR = models.ForeignKey(SETCOLOR, null=True, blank=True, on_delete=models.PROTECT)
    MEMO = models.CharField(max_length=1024, null=True, blank=True)
    STATUS_CRE = models.CharField(max_length=1, default='A', choices=STATUS_CHOICES)
    TERM_CONDITION = models.ForeignKey(Prospect_condition, null=True, blank=True, on_delete=models.PROTECT)
    RECEIVEDT = models.DateField(null=True, blank=True)
    MATCHDT = models.DateField(null=True, blank=True)
    DELIVERYDT = models.DateField(null=True, blank=True)
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    UPDATED_AT = models.DateTimeField(auto_now=True)

    class Meta:        
        db_table = 'PROSPECT_TEST'

    def __str__(self):
        return '%s' % (self.CUST_NAME)

class INVTRAN(models.Model):
    RECVNO = models.CharField(max_length=12, primary_key=True)
    RECVDT = models.DateField(null=True, blank=True)
    GCODE = models.CharField(max_length=3, null=True, blank=True)
    TYPE = models.CharField(max_length=12, null=True, blank=True)
    # MODEL = models.CharField(max_length=12, null=True, blank=True)
    MODEL = models.ForeignKey(SETMODEL, db_column='MODEL', null=True, blank=True, on_delete=models.PROTECT)
    BAAB = models.CharField(max_length=20, null=True, blank=True)
    COLOR = models.ForeignKey(SETCOLOR, db_column='COLOR', null=True, blank=True, on_delete=models.PROTECT)
    # COLOR = models.CharField(max_length=12, null=True, blank=True)
    STRNO = models.CharField(max_length=20, null=True, blank=True)
    ENGNO = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
       managed = False
       db_table = 'INVTRAN'

class SECRET(models.Model):
    USERID = models.CharField(max_length=8, primary_key=True)
    ENDCODE = models.CharField(max_length=40)

    class Meta:
       managed = False
       db_table = 'SECRET'