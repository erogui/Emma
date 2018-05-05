from django.db import models


class Identite(models.Model):
	siren = models.CharField(max_length=140)
	date_cloture_exercice = models.DateTimeField()
	code_greffe = models.CharField(max_length=140)
	num_depot = models.CharField(max_length=140)
	num_gestion = models.CharField(max_length=140) 
	code_activite = models.CharField(max_length=140)
	date_cloture_exercice_n1 = models.DateTimeField()
	duree_exercice_n = models.CharField(max_length=140)
	duree_exercice_n1 = models.CharField(max_length=140)
	date_depot = models.DateTimeField()
	code_motif = models.CharField(max_length=140)
	code_type_bilan = models.CharField(max_length=140)
	code_devise = models.CharField(max_length=140)
	code_origine_devise = models.CharField(max_length=140)
	code_confidentialite = models.CharField(max_length=140)
	denomination = models.CharField(max_length=140)
	adresse = models.CharField(max_length=140)
	
	def __str__(self):
		return self.siren
		

		

		