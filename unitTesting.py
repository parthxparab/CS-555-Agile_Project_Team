import unittest
import project04

class functionTest(unittest.TestCase):
    def test_userstory03(self):
        result03 = ['I4 : Robb /Stark/ has a ERRORNEOUS Birthdate with respect to Deathdate',
                    'I6 : Jon /Barathaon/ has a ERRORNEOUS Birthdate with respect to Deathdate',
                    'I9 : Raegar /Targarayen/ has a ERRORNEOUS Birthdate with respect to Deathdate',
                    'I12 : Margery /Tyrell/ has a ERRORNEOUS Birthdate with respect to Deathdate']
        self.assertEqual(project04.us03(),result03) 

    def test_userstory04(self):
        result04 = ['F2 : Robert /Barathaon/ and Cate /Laniaster/ have a ERRORNEOUS Marriage date with respect to Divorced date', 'F3 : Jamie /Lanaster/ and Cercie /Tyrell/ have a ERRORNEOUS Marriage date with respect to Divorced date']
        self.assertEqual(project04.us04(),result04) 

    def test_userstory01(self):
        result01 = 'Number of Entries found: 3'
        self.assertEqual(project04.US01(),result01) 

    def test_userstory02(self):
        result02 = 'Number of Entries found: 7'
        self.assertEqual(project04.US02(),result02) 


if __name__=='__main__':
    unittest.main()
