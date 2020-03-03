import unittest
import parser


class functionTest(unittest.TestCase):
    def test_userstory03(self):
        result03 = ['ERROR: INDIVIDUAL: US03: 3:  I4: Robb /Stark/ has a future Birthdate: 1960-04-04 with respect to Deathdate: 1950-09-14', 'ERROR: INDIVIDUAL: US03: 5:  I6: Jon /Barathaon/ has a future Birthdate: 2050-07-10 with respect to Deathdate: 1950-09-14', 'ERROR: INDIVIDUAL: US03: 8:  I9: Raegar /Targarayen/ has a future Birthdate: 1940-07-08 with respect to Deathdate: 1920-09-08', 'ERROR: INDIVIDUAL: US03: 11:  I12: Margery /Tyrell/ has a future Birthdate: 1967-07-09 with respect to Deathdate: 1966-01-08']
        self.assertEqual(parser.us03(), result03)

    def test_userstory04(self):
        result04 = ['ERROR: FAMILY: US04: 2:  F3:  have a future Marriage Date : 1980-04-05 with respect to Divorced Date : 1970-12-11', 'ERROR: FAMILY: US04: 3:  F4:  have a future Marriage Date : 2090-06-20 with respect to Divorced Date : 1955-01-13']
        self.assertEqual(parser.us04(), result04)

    def test_userstory17(self):
        result17 = ['ERROR: FAMILY: US17: 9:  F10: Parent I17 is married to their child : I16']
        self.assertEqual(parser.us17(), result17)

    def test_userstory18(self):
        result18 = ['ERROR: FAMILY: US18: 0:  F1: Siblings I4 and I1 are married','ERROR: FAMILY: US18: 7:  F8: Siblings I15 and I16 are married']
        self.assertEqual(parser.us18(), result18)

    def test_userstory01(self):
        result01 = 'Number of Entries found: 3'
        self.assertEqual(parser.US01(), result01)

    def test_userstory02(self):
        result02 = 'Number of Entries found: 7'
        self.assertEqual(parser.US02(), result02)

    def test_userstory07(self):
        result07 = ['ERROR: INDIVIDUAL: US07: 4: I5: Robert /Barathaon/ is 154 years old which is more then 150',
                    'ERROR: INDIVIDUAL: US07: 10: I11: Olenna /Tully/ is 302 years old which is more then 150']
        self.assertEqual(parser.US07(), result07)

    def test_userstory08(self):
        result08 = ['ERROR: FAMILY: US08: 5: I6: Jon /Barathaon/ is born after 9 months from divorce of parents',
                    'ERROR: FAMILY: US08: 2: I3: Cate /Laniaster/ is born before marriage of parents',
                    'ERROR: FAMILY: US08: 11: I12: Margery /Tyrell/ is born after 9 months from divorce of parents']
        self.assertEqual(parser.US08(), result08)

    def test_userstory05(self):
        result05 = ['ERROR: INDIVIDUAL: US05: 8:  I1: Arya /Stark/ has an erroneous Marriage Date with respect to Deathdate: 2020-03-02', 'ERROR: INDIVIDUAL: US05: 14:  I12: Margery /Tyrell/ has an erroneous Marriage Date with respect to Deathdate: 1966-01-08', 'ERROR: INDIVIDUAL: US05: 9:  I4: Robb /Stark/ has an erroneous Marriage Date with respect to Deathdate: 1950-09-14', 'ERROR: INDIVIDUAL: US05: 10:  I5: Robert /Barathaon/ has an erroneous Marriage Date with respect to Deathdate: 1950-09-14', 'ERROR: INDIVIDUAL: US05: 11:  I6: Jon /Barathaon/ has an erroneous Marriage Date with respect to Deathdate: 1950-09-14', 'ERROR: INDIVIDUAL: US05: 12:  I7: Jamie /Lanaster/ has an erroneous Marriage Date with respect to Deathdate: 1990-07-12', 'ERROR: INDIVIDUAL: US05: 13:  I9: Raegar /Targarayen/ has an erroneous Marriage Date with respect to Deathdate: 1920-09-08']
        self.assertEqual(parser.us_05_marriage_before_death(), result05)

    def test_userstory06(self):
        result06 = ['ERROR: INDIVIDUAL: US06: 7:  I1: Arya /Stark/ has an erroneous Divorce Date with respect to Deathdate: 2020-03-02', 'ERROR: INDIVIDUAL: US06: 13:  I10: Ramsay /Tyrell/ has an erroneous Divorce Date with respect to Deathdate: 1947-03-25', 'ERROR: INDIVIDUAL: US06: 14:  I12: Margery /Tyrell/ has an erroneous Divorce Date with respect to Deathdate: 1966-01-08', 'ERROR: INDIVIDUAL: US06: 8:  I2: Ned /Stark/ has an erroneous Divorce Date with respect to Deathdate: 2020-03-02', 'ERROR: INDIVIDUAL: US06: 9:  I4: Robb /Stark/ has an erroneous Divorce Date with respect to Deathdate: 1950-09-14', 'ERROR: INDIVIDUAL: US06: 10:  I5: Robert /Barathaon/ has an erroneous Divorce Date with respect to Deathdate: 1950-09-14', 'ERROR: INDIVIDUAL: US06: 11:  I6: Jon /Barathaon/ has an erroneous Divorce Date with respect to Deathdate: 1950-09-14', 'ERROR: INDIVIDUAL: US06: 12:  I9: Raegar /Targarayen/ has an erroneous Divorce Date with respect to Deathdate: 1920-09-08']
        self.assertEqual(parser.us_06_divorce_before_death(), result06)


if __name__ == '__main__':
    unittest.main()
