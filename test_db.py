import unittest
import functionality as f
import psycopg2


class TestDataBase(unittest.TestCase):

    # def test_values_Oberhause(self):
    #     self.assertEqual([(1, 'Lipezig', 20, 2000),(10, 'Munchen',500)],f.adding_into_db())

    def test_stock(self):
        test_var=[('Lipezig',), ('Munchen',), ('Oberhausen',), ('Munchen',), ('Oberhausen',), ('Munchen',), ('Oberhausen',), ('Munchen',), ('Oberhausen',), ('Munchen',), ('Oberhausen',), ('Munchen',), ('Oberhausen',), ('Munchen',), ('Oberhausen',)]
        self.assertEqual(test_var,f.sorting_db_greaterthan5())

if __name__=='__main__':
    unittest.main()