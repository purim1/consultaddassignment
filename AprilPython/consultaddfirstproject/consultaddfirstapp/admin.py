from django.contrib import admin
from consultaddfirstapp.models import Candidate ,CandidateInfo, CandidateAddress, CandidateSalary
# Register your models here.


admin.site.register(Candidate)
admin.site.register(CandidateInfo)
admin.site.register(CandidateAddress)
admin.site.register(CandidateSalary)

