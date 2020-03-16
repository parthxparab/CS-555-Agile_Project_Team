import unittest
import parser


class functionTest(unittest.TestCase):
    def test_userstory03(self):
        result03 = ['ERROR: INDIVIDUAL: US03: 3:  I4: Robb /Stark/ has a future Birthdate: 1960-04-04 with respect to Deathdate: 1950-09-14', 'ERROR: INDIVIDUAL: US03: 5:  I6: Jon /Barathaon/ has a future Birthdate: 2050-07-10 with respect to Deathdate: 1950-09-14',
                    'ERROR: INDIVIDUAL: US03: 8:  I9: Raegar /Targarayen/ has a future Birthdate: 1940-07-08 with respect to Deathdate: 1920-09-08', 'ERROR: INDIVIDUAL: US03: 11:  I12: Margery /Tyrell/ has a future Birthdate: 1967-07-09 with respect to Deathdate: 1966-01-08']
        self.assertEqual(parser.us03(), result03)

    def test_userstory04(self):
        result04 = ['ERROR: FAMILY: US04: 2:  F3:  have a future Marriage Date : 1980-04-05 with respect to Divorced Date : 1970-12-11',
                    'ERROR: FAMILY: US04: 3:  F4:  have a future Marriage Date : 2090-06-20 with respect to Divorced Date : 1955-01-13']
        self.assertEqual(parser.us04(), result04)

    def test_userstory17(self):
        result17 = [
            'ERROR: FAMILY: US17: 9:  F10: Parent I17 is married to their child : I16']
        self.assertEqual(parser.us17(), result17)

    def test_userstory18(self):
        result18 = ['ERROR: FAMILY: US18: 0:  F1: Siblings I4 and I1 are married',
                    'ERROR: FAMILY: US18: 7:  F8: Siblings I15 and I16 are married']
        self.assertEqual(parser.us18(), result18)

    def test_userstory01(self):
        result01 = ['ERROR: INDIVIDUAL: US01: 5: I6: Birthday 2050-07-10 occurs in the future', 'ERROR: INDIVIDUAL: US01: 10: I11: Deathday 2222-10-28 occurs in the future',
                    'ERROR: FAMILY: US01: 3: F4: Marriage Day 2090-06-20 between I7 and I8 occurs in the future']
        self.assertEqual(parser.US01(), result01)

    def test_userstory02(self):
        result02 = [
            'ERROR: INDIVIDUAL: US02: 2: I3: Husband\'s birth date 1990-06-08 after marriage date 1950-05-10']
        self.assertEqual(parser.US02(), result02)

    def test_userstory09(self):
        result09 = ['ERROR: FAMILY: US09: 4: I9: Father\'s death date 1920-09-08 before birthdate of child 1975-11-11', 'ERROR: FAMILY: US09: 5: I10: Mother\'s death date 1947-03-25 before birthdate of child 1947-09-11']
        self.assertEqual(parser.US09(), result09)

    def test_userstory10(self):
        result10 = ['ERROR: FAMILY: US10: 0: I1: Mother\'s birth date 1980-03-03 less than 14 years of marriage date 1985-02-03', 'ERROR: FAMILY: US10: 1: I3: Father\'s birth date 1990-06-08 less than 14 years of marriage date 1950-05-10', 'ERROR: FAMILY: US10: 4: I8: Mother\'s birth date 1947-09-11 less than 14 years of marriage date 1960-10-17',
                    'ERROR: FAMILY: US10: 5: I10: Father\'s birth date 1920-08-21 less than 14 years of marriage date 1923-02-10', 'ERROR: FAMILY: US10: 6: I13: Father\'s birth date 1960-06-03 less than 14 years of marriage date 1968-05-10', 'ERROR: FAMILY: US10: 9: I17: Mother\'s birth date 1968-03-02 less than 14 years of marriage date 1975-01-02']
        self.assertEqual(parser.US10(), result10)

    def test_userstory07(self):
        result07 = ['ERROR: INDIVIDUAL: US07: 4: I5: Robert /Barathaon/ is 154 years old which is more then 150',
                    'ERROR: INDIVIDUAL: US07: 10: I11: Olenna /Tully/ is 302 years old which is more then 150']
        self.assertEqual(parser.US07(), result07)

    def test_userstory08(self):
        result08 = ['ERROR: FAMILY: US08: 5: I6: Jon /Barathaon/ is born after 9 months from divorce of parents',
                    'ERROR: FAMILY: US08: 2: I3: Cate /Laniaster/ is born before marriage of parents',
                    'ERROR: FAMILY: US08: 11: I12: Margery /Tyrell/ is born after 9 months from divorce of parents']
        self.assertEqual(parser.US08(), result08)

    def test_userstory35(self):
        result35 = [
            'ERROR: INDIVIDUAL: US35: 17: I18: Leo /Stark/ is born recently on 2020-03-14']
        self.assertEqual(parser.US35(), result35)

    def test_userstort36(self):
        result36 = ['ERROR: INDIVIDUAL: US36: 16: I17: Pady /Snow/ died recently on 2020-03-13',
                    'ERROR: INDIVIDUAL: US36: 17: I18: Leo /Stark/ died recently on 2020-03-13']
        self.assertEqual(parser.US36(), result36)

    def test_userstory05(self):
        result05 = ['ERROR: INDIVIDUAL: US05: 8:  I1: Arya /Stark/ has an erroneous Marriage Date with respect to Deathdate: 2020-03-02', 'ERROR: INDIVIDUAL: US05: 14:  I12: Margery /Tyrell/ has an erroneous Marriage Date with respect to Deathdate: 1966-01-08', 'ERROR: INDIVIDUAL: US05: 9:  I4: Robb /Stark/ has an erroneous Marriage Date with respect to Deathdate: 1950-09-14', 'ERROR: INDIVIDUAL: US05: 10:  I5: Robert /Barathaon/ has an erroneous Marriage Date with respect to Deathdate: 1950-09-14',
                    'ERROR: INDIVIDUAL: US05: 11:  I6: Jon /Barathaon/ has an erroneous Marriage Date with respect to Deathdate: 1950-09-14', 'ERROR: INDIVIDUAL: US05: 12:  I7: Jamie /Lanaster/ has an erroneous Marriage Date with respect to Deathdate: 1990-07-12', 'ERROR: INDIVIDUAL: US05: 13:  I9: Raegar /Targarayen/ has an erroneous Marriage Date with respect to Deathdate: 1920-09-08']
        self.assertEqual(parser.us_05_marriage_before_death(), result05)

    def test_userstory06(self):
        result06 = ['ERROR: INDIVIDUAL: US06: 7:  I1: Arya /Stark/ has an erroneous Divorce Date with respect to Deathdate: 2020-03-02', 'ERROR: INDIVIDUAL: US06: 13:  I10: Ramsay /Tyrell/ has an erroneous Divorce Date with respect to Deathdate: 1947-03-25', 'ERROR: INDIVIDUAL: US06: 14:  I12: Margery /Tyrell/ has an erroneous Divorce Date with respect to Deathdate: 1966-01-08', 'ERROR: INDIVIDUAL: US06: 8:  I2: Ned /Stark/ has an erroneous Divorce Date with respect to Deathdate: 2020-03-02',
                    'ERROR: INDIVIDUAL: US06: 9:  I4: Robb /Stark/ has an erroneous Divorce Date with respect to Deathdate: 1950-09-14', 'ERROR: INDIVIDUAL: US06: 10:  I5: Robert /Barathaon/ has an erroneous Divorce Date with respect to Deathdate: 1950-09-14', 'ERROR: INDIVIDUAL: US06: 11:  I6: Jon /Barathaon/ has an erroneous Divorce Date with respect to Deathdate: 1950-09-14', 'ERROR: INDIVIDUAL: US06: 12:  I9: Raegar /Targarayen/ has an erroneous Divorce Date with respect to Deathdate: 1920-09-08']
        self.assertEqual(parser.us_06_divorce_before_death(), result06)


if __name__ == '__main__':
    unittest.main()
