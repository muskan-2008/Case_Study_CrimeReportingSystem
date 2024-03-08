import unittest
from dao.incidentsdao import IncidentsDao

class MyTestCase(unittest.TestCase):
    def test_incident_creation_table(self):
        isCreated= IncidentsDao.create_incidents_table(self)
        self.assertTrue(isCreated)
        self.assertEqual(True, False)  # add assertion here



if __name__ == '__main__':
    unittest.main()
