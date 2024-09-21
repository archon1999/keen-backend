from common.api.routers import OptionalSlashRouter

from apps.problems.views import ProblemViewSet

router = OptionalSlashRouter()
router.register('problems', ProblemViewSet, basename='problems')

urlpatterns = router.urls
