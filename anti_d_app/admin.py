from django.contrib import admin
from anti_d_app.models import DisasterName, Report, LocalGovernment, OrganizationType, RelatedOrganization

# Register your models here.
admin.site.register(LocalGovernment)
admin.site.register(OrganizationType)
admin.site.register(RelatedOrganization)
admin.site.register(DisasterName)
admin.site.register(Report)
