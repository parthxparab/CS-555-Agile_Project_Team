import unittest
import project04


class functionTest(unittest.TestCase):
    def test_userstory03(self):
        result03 = ['ERROR: INDIVIDUAL: US03: 3:  I4: Robb /Stark/ has a future Birthdate: 1960-04-04 with respect to Deathdate: 1950-09-14', 'ERROR: INDIVIDUAL: US03: 5:  I6: Jon /Barathaon/ has a future Birthdate: 2050-07-10 with respect to Deathdate: 1950-09-14', 'ERROR: INDIVIDUAL: US03: 8:  I9: Raegar /Targarayen/ has a future Birthdate: 1940-07-08 with respect to Deathdate: 1920-09-08', 'ERROR: INDIVIDUAL: US03: 11:  I12: Margery /Tyrell/ has a future Birthdate: 1967-07-09 with respect to Deathdate: 1966-01-08']
        self.assertEqual(project04.us03(), result03)

    def test_userstory04(self):
        result04 = ['ERROR: FAMILY: US04: 1:  F2:  have a future Marriage Date : 1980-04-05 with respect to Divorced Date : 1970-12-11', 'ERROR: FAMILY: US04: 2:  F3:  have a future Marriage Date : 2090-06-20 with respect to Divorced Date : 1955-01-13']
        self.assertEqual(project04.us04(), result04)

    def test_userstory01(self):
        result01 = 'Number of Entries found: 3'
        self.assertEqual(project04.US01(), result01)

    def test_userstory02(self):
        result02 = 'Number of Entries found: 7'
        self.assertEqual(project04.US02(), result02)

    def test_userstory07(self):
        result07 = ['ERROR: INDIVIDUAL: US07: 4: I5: Robert /Barathaon/ is 154 years old which is more then 150',
                    'ERROR: INDIVIDUAL: US07: 10: I11: Olenna /Tully/ is 302 years old which is more then 150']
        self.assertEqual(project04.US07(), result07)

    def test_userstory08(self):
        result08 = ['ERROR: FAMILY: US08: 5: I6: Jon /Barathaon/ is born after 9 months from divorce of parents',
                    'ERROR: FAMILY: US08: 2: I3: Cate /Laniaster/ is born before marriage of parents',
                    'ERROR: FAMILY: US08: 11: I12: Margery /Tyrell/ is born after 9 months from divorce of parents']
        self.assertEqual(project04.US08(), result08)

    def test_userstory05(self):
        result05 = ['I1 : Arya /Stark/ has an ERRORNEOUS marriage with respect to Death',
                    'I12 : Margery /Tyrell/ has an ERRORNEOUS marriage with respect to Death',
                    'I4 : Robb /Stark/ has an ERRORNEOUS marriage with respect to Death',
                    'I5 : Robert /Barathaon/ has an ERRORNEOUS marriage with respect to Death',
                    'I6 : Jon /Barathaon/ has an ERRORNEOUS marriage with respect to Death',
                    'I7 : Jamie /Lanaster/ has an ERRORNEOUS marriage with respect to Death',
                    'I9 : Raegar /Targarayen/ has an ERRORNEOUS marriage with respect to Death']
        self.assertEqual(project04.us_05_marriage_before_death(), result05)

    def test_userstory06(self):
        result06 = ['I1 : Arya /Stark/ has an ERRORNEOUS divorce with respect to Death',
                    'I10 : Ramsay /Tyrell/ has an ERRORNEOUS divorce with respect to Death',
                    'I12 : Margery /Tyrell/ has an ERRORNEOUS divorce with respect to Death',
                    'I2 : Ned /Stark/ has an ERRORNEOUS divorce with respect to Death',
                    'I4 : Robb /Stark/ has an ERRORNEOUS divorce with respect to Death',
                    'I5 : Robert /Barathaon/ has an ERRORNEOUS divorce with respect to Death',
                    'I6 : Jon /Barathaon/ has an ERRORNEOUS divorce with respect to Death',
                    'I9 : Raegar /Targarayen/ has an ERRORNEOUS divorce with respect to Death']
        self.assertEqual(project04.us_06_divorce_before_death(), result06)


if __name__ == '__main__':
    unittest.main()
