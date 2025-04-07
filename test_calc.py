import unittest
import calc

class TestCalc(unittest.TestCase):
    
    # def add_test(self): --> Penamaan salah! pastikan diawali kata test, karena pasti unit test tdk akan menjalankan ini
    def test_add(self):    
        # result = calc.add(10,5)
        # self.assertEqual(result,15)
        self.assertEqual(calc.add(10,5), 15)
        # self.assertEqual(calc.add(10,5), 14) muncul error karena unit test tidak sesuai
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-1,-1), -2)

    def test_substract(self):      
        self.assertEqual(calc.substract(10,5), 5)
        self.assertEqual(calc.substract(-1,1), -2)
        self.assertEqual(calc.substract(-1,-1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5), 50)
        self.assertEqual(calc.multiply(-1,1), -1)
        self.assertEqual(calc.multiply(-1,-1), 1)

    def test_divide(self):      
        self.assertEqual(calc.divide(10,5), 2)
        self.assertEqual(calc.divide(-1,1), -1)
        self.assertEqual(calc.divide(-1,-1), 1)
        # self.assertEqual(calc.divide(5,2), 2) # jika menggunakan for division (//) success
        self.assertEqual(calc.divide(5,2), 2.5) # jika menggunakan regular division (/) success

        self.assertRaises(ValueError, calc.divide, 10, 0)

if __name__ == '__main__':
    unittest.main()