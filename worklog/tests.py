from django.test import TestCase

from tskmngr.worklog.models import Worklog

class WorklogTest(TestCase):

    def setUp(self):
        title = "Test Worklog"
        desc = "Test Desc"
        self.worklog = Worklog.objects.create(title=title, desc=desc)

    def test_save(self):
        self.assertEqual(Worklog.objects.all().count(), 1)
