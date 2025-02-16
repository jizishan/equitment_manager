from django.views.generic import ListView
from .models import Equipment

class EquipmentListView(ListView):
    model = Equipment
    template_name = 'equipment/list.html'
    context_object_name = 'equipments'
    paginate_by = 10