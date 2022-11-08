from doctors.viewsets import DoctorsViewset
from testcrud.viewsets import TestCrudViewset
from back_call.viewsets import BackCallViewset
from cabinets.viewsets import CabinetsViewset
from receptions.viewsets import ReceptionsViewset

from rest_framework import routers

router = routers.DefaultRouter()
router.register('testcrud', TestCrudViewset)
router.register('back_call', BackCallViewset)
router.register('cabinets', CabinetsViewset)
router.register('doctors', DoctorsViewset)
router.register('receptions', ReceptionsViewset)


# localhost:p/api/
#Get, post, update, delete
