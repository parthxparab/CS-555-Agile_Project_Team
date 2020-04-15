import unittest
import parser


class functionTest(unittest.TestCase):
    def test_userstory03(self):
        result03 = ['ERROR: INDIVIDUAL: US03: 1:  I2: Robb /Stark/ has a future Birthdate: 1960-04-14 with respect to Deathdate: 1950-09-14',
                    'ERROR: INDIVIDUAL: US03: 5:  I6: Jon /Barathaon/ has a future Birthdate: 2050-07-10 with respect to Deathdate: 2020-04-01',
                    'ERROR: INDIVIDUAL: US03: 8:  I9: Raegar /Targarayen/ has a future Birthdate: 1940-07-08 with respect to Deathdate: 1920-09-08',
                    'ERROR: INDIVIDUAL: US03: 11:  I12: Margery /Tyrell/ has a future Birthdate: 1967-07-09 with respect to Deathdate: 1966-01-08', 'ERROR: INDIVIDUAL: US03: 17:  I18: Leo /Stark/ has a future Birthdate: 2020-04-10 with respect to Deathdate: 2020-04-01']
        self.assertEqual(parser.us03(), result03)

    def test_userstory04(self):
        result04 = ['ERROR: FAMILY: US04: 2:  F3:  have a future Marriage Date : 1980-04-05 with respect to Divorced Date : 1970-12-11',
                    'ERROR: FAMILY: US04: 3:  F4:  have a future Marriage Date : 2090-06-20 with respect to Divorced Date : 1955-01-13']
        self.assertEqual(parser.us04(), result04)

    def test_userstory17(self):
        result17 = [
            'ERROR: FAMILY: US17: 7:  F8: Parent I13 is married to their child : I17']
        self.assertEqual(parser.us17(), result17)

    def test_userstory18(self):
        result18 = ['ERROR: FAMILY: US18: 0:  F1: Siblings I2 and I1 are married',
                    'ERROR: FAMILY: US18: 9:  F10: Siblings I16 and I17 are married']
        self.assertEqual(parser.us18(), result18)

    def test_userstory34(self):
        result34 = ['ERROR FAMILY US34 : I1 :The Wife is more than double the age of I2 :The Husband ',
                    'ERROR FAMILY US34 : I4 :The Wife is more than double the age of I3 :The Husband ',
                    'ERROR FAMILY US34 : I8 :The Wife is more than double the age of I9 :The Husband ',
                    'ERROR FAMILY US34 : I11 :The Wife is more than double the age of I10 :The Husband ',
                    'ERROR FAMILY US34 : I13 :The Husband is more than double the age of I12 :The Wife ']
        self.assertEqual(parser.us34(), result34)

    def test_userstory20(self):
        result20 = ['ENTRY FOUND US20 Children :  I4 have Uncle/s and Aunt/s with ID/s I12',
                    'ENTRY FOUND US20 Children :  I14 have Uncle/s and Aunt/s with ID/s I12',
                    'ENTRY FOUND US20 Children :  I16 I17 have Uncle/s and Aunt/s with ID/s I8']
        self.assertEqual(parser.us20(), result20)

    def test_userstory01(self):
        result01 = ['ERROR: INDIVIDUAL: US01: 5: I6: Birthday 2050-07-10 occurs in the future', 'ERROR: INDIVIDUAL: US01: 10: I11: Deathday 2222-10-28 occurs in the future',
                    'ERROR: FAMILY: US01: 3: F4: Marriage Day 2090-06-20 between I7 and I8 occurs in the future']
        self.assertEqual(parser.US01(), result01)

    def test_userstory02(self):
        result02 = [
            'ERROR: INDIVIDUAL: US02: 2: I3: Husband\'s birth date 1990-06-08 after marriage date 1950-04-20']
        self.assertEqual(parser.US02(), result02)

    def test_userstory09(self):
        result09 = [
            'ERROR: FAMILY: US09: 4: I9: Father\'s death date 1920-09-08 before birthdate of child 1975-11-11']
        self.assertEqual(parser.US09(), result09)

    def test_userstory10(self):
        result10 = ['ERROR: FAMILY: US10: 0: I1: Mother\'s birth date 1980-03-03 less than 14 years of marriage date 1985-04-13', 'ERROR: FAMILY: US10: 1: I3: Father\'s birth date 1990-06-08 less than 14 years of marriage date 1950-04-20',
                    'ERROR: FAMILY: US10: 5: I10: Father\'s birth date 1920-08-21 less than 14 years of marriage date 1923-02-10', 'ERROR: FAMILY: US10: 6: I13: Father\'s birth date 1960-04-30 less than 14 years of marriage date 1968-05-10', 'ERROR: FAMILY: US10: 9: I17: Mother\'s birth date 1968-03-02 less than 14 years of marriage date 1975-01-02']
        self.assertEqual(parser.US10(), result10)

    def test_userstory07(self):
        result07 = ['ERROR: INDIVIDUAL: US07: 4: I5: Robert /Barathaon/ is 154 years old which is more then 150',
                    'ERROR: INDIVIDUAL: US07: 10: I11: Olenna /Tully/ is 302 years old which is more then 150']
        self.assertEqual(parser.US07(), result07)

    def test_userstory08(self):
        result08 = ['ERROR: FAMILY: US08: 5: I6: Jon /Barathaon/ is born after 9 months from divorce of Parent',
                    'ERROR: FAMILY: US08: 3: I4: Cate /Laniaster/ is born before marriage of Parent',
                    'ERROR: FAMILY: US08: 11: I12: Margery /Tyrell/ is born after 9 months from divorce of Parent',
                    'ERROR: FAMILY: US08: 15: I16: Podrick /Tyrell/ is born before marriage of Parent',
                    'ERROR: FAMILY: US08: 16: I17: Pady /Snow/ is born before marriage of Parent']
        self.assertEqual(parser.US08(), result08)

    def test_userstory35(self):
        result35 = [
            'ERROR: INDIVIDUAL: US35: 17: I18: Leo /Stark/ is born recently on 2020-04-10']
        self.assertEqual(parser.US35(), result35)

    def test_userstory36(self):
        result36 = [
            'ERROR: INDIVIDUAL: US36: 16: I17: Pady /Snow/ died recently on 2020-04-13']
        self.assertEqual(parser.US36(), result36)

    def test_userstory38(self):
        result38 = [
            'ERROR: INDIVIDUAL: US38: 12: I13: Pod /Snow/ has upcoming Birthday on 1960-04-30']
        self.assertEqual(parser.US38(), result38)

    def test_userstory39(self):
        result39 = ['ERROR: FAMILY: US39: 1: Ned /Stark/(I3) and Cate /Laniaster/(I4) has upcoming Anniversary on 1950-04-20',
                    'ERROR: FAMILY: US39: 7: Pod /Snow/(I13) and Pady /Snow/(I17) has upcoming Anniversary on 1989-05-10']
        self.assertEqual(parser.US39(), result39)

    def test_userstory29(self):
        result29 = ['ERROR: INDIVIDUAL: US29: 1: I2: Robb /Stark/ died on 1950-09-14',
                    'ERROR: INDIVIDUAL: US29: 6: I7: Jamie /Lanaster/ died on 1990-07-12',
                    'ERROR: INDIVIDUAL: US29: 8: I9: Raegar /Targarayen/ died on 1920-09-08',
                    'ERROR: INDIVIDUAL: US29: 9: I10: Ramsay /Tyrell/ died on 1947-03-25',
                    'ERROR: INDIVIDUAL: US29: 10: I11: Olenna /Tully/ died on 2222-10-28',
                    'ERROR: INDIVIDUAL: US29: 11: I12: Margery /Tyrell/ died on 1966-01-08',
                    'ERROR: INDIVIDUAL: US29: 13: I14: Danny /Targaryen/ died on 2010-09-17',
                    'ERROR: INDIVIDUAL: US29: 16: I17: Pady /Snow/ died on 2020-04-13']
        self.assertEqual(parser.US29(), result29)

    def test_userstory30(self):
        result30 = ['ERROR: INDIVIDUAL: US30: 0: I1: Arya /Stark/ is alive and married',
                    'ERROR: INDIVIDUAL: US30: 1: I3: Ned /Stark/ is alive and married',
                    'ERROR: INDIVIDUAL: US30: 1: I4: Cate /Laniaster/ is alive and married',
                    'ERROR: INDIVIDUAL: US30: 2: I4: Cate /Laniaster/ is alive and married',
                    'ERROR: INDIVIDUAL: US30: 2: I5: Robert /Barathaon/ is alive and married',
                    'ERROR: INDIVIDUAL: US30: 3: I8: Cercie /Tyrell/ is alive and married',
                    'ERROR: INDIVIDUAL: US30: 4: I8: Cercie /Tyrell/ is alive and married',
                    'ERROR: INDIVIDUAL: US30: 6: I13: Pod /Snow/ is alive and married',
                    'ERROR: INDIVIDUAL: US30: 7: I13: Pod /Snow/ is alive and married',
                    'ERROR: INDIVIDUAL: US30: 8: I15: Jon /Snow/ is alive and married',
                    'ERROR: INDIVIDUAL: US30: 9: I16: Podrick /Tyrell/ is alive and married']
        self.assertEqual(parser.US30(), result30)

    def test_userstory05(self):
        result05 = ['ERROR: INDIVIDUAL: US05: 19:  I12: Margery /Tyrell/ has an erroneous Marriage Date with respect to Deathdate: 1966-01-08', 'ERROR: INDIVIDUAL: US05: 20:  I18: Leo /Stark/ has an erroneous Marriage Date with respect to Deathdate: 2020-04-01', 'ERROR: INDIVIDUAL: US05: 15:  I2: Robb /Stark/ has an erroneous Marriage Date with respect to Deathdate: 1950-09-14',
                    'ERROR: INDIVIDUAL: US05: 16:  I6: Jon /Barathaon/ has an erroneous Marriage Date with respect to Deathdate: 2020-04-01', 'ERROR: INDIVIDUAL: US05: 17:  I7: Jamie /Lanaster/ has an erroneous Marriage Date with respect to Deathdate: 1990-07-12', 'ERROR: INDIVIDUAL: US05: 18:  I9: Raegar /Targarayen/ has an erroneous Marriage Date with respect to Deathdate: 1920-09-08']
        self.assertEqual(parser.us_05_marriage_before_death(), result05)

    def test_userstory06(self):
        result06 = ['ERROR: INDIVIDUAL: US06: 11:  I1: Arya /Stark/ has an erroneous Divorce Date with respect to Deathdate: 2020-04-01', 'ERROR: INDIVIDUAL: US06: 16:  I10: Ramsay /Tyrell/ has an erroneous Divorce Date with respect to Deathdate: 1947-03-25', 'ERROR: INDIVIDUAL: US06: 17:  I12: Margery /Tyrell/ has an erroneous Divorce Date with respect to Deathdate: 1966-01-08', 'ERROR: INDIVIDUAL: US06: 18:  I18: Leo /Stark/ has an erroneous Divorce Date with respect to Deathdate: 2020-04-01',
                    'ERROR: INDIVIDUAL: US06: 12:  I2: Robb /Stark/ has an erroneous Divorce Date with respect to Deathdate: 1950-09-14', 'ERROR: INDIVIDUAL: US06: 13:  I3: Ned /Stark/ has an erroneous Divorce Date with respect to Deathdate: 2020-04-01', 'ERROR: INDIVIDUAL: US06: 14:  I6: Jon /Barathaon/ has an erroneous Divorce Date with respect to Deathdate: 2020-04-01', 'ERROR: INDIVIDUAL: US06: 15:  I9: Raegar /Targarayen/ has an erroneous Divorce Date with respect to Deathdate: 1920-09-08']
        self.assertEqual(parser.us_06_divorce_before_death(), result06)

    def test_userstory21(self):
        result21 = ['ERROR: FAMILY: US21: 0: Correct gender for role is violated for wife ID: I1 and Name: Arya /Stark/',
                    'ERROR: FAMILY: US21: 4: Correct gender for role is violated for husband ID: I5 and Name: Robert /Barathaon/', 'ERROR: FAMILY: US21: 9: Correct gender for role is violated for husband ID: I10 and Name: Ramsay /Tyrell/']
        self.assertEqual(parser.US21(), result21)

    def test_userstory22(self):
        result22 = ['ERROR: INDIVIDUAL: US22: 0: Unique ID violated for : I1 and Name: Arya /Stark/', 'ERROR: INDIVIDUAL: US22: 18: Unique ID violated for : I1 and Name: Robb /Stark/',
                    'ERROR: FAMILY: US22: 0: Unique ID violated for : F1, Husband Name: Robb /Stark/ and Wife Name: Arya /Stark/', 'ERROR: FAMILY: US22: 10: Unique ID violated for : F1, Husband Name: Ned Stark and Wife Name: Cate Laniaster']
        self.assertEqual(parser.US22(), result22)

    def test_userstory23(self):
        result23 = ['ERROR: INDIVIDUAL: US23: Unique name & Unique date_of_birth violated for Name: Ned /Stark/ and Date of Birth: 1990-06-08',
                    'ERROR: INDIVIDUAL: US23: Unique name & Unique date_of_birth violated for Name: Cate /Laniaster/ and Date of Birth: 1940-04-08']
        self.assertEqual(parser.US23(), result23)

    def test_userstory24(self):
        result24 = ['ERROR: FAMILY: US24: Unique spouse names & Unique marriage_date violated for Husband Name: Raegar /Targarayen/ ,Wife Name: Cercie /Tyrell/, and Marriage Date: 1960-10-17',
                    'ERROR: FAMILY: US24: Unique spouse names & Unique marriage_date violated for Husband Name: Ramsay /Tyrell/ ,Wife Name: Olenna /Tully/, and Marriage Date: 1923-02-10']
        self.assertEqual(parser.US24(), result24)
        
    def test_userstory25(self):
        result25 = ['ERROR: INDIVIDUAL: US25: No unique first name in family for name: Robb /Stark/', 'ERROR: INDIVIDUAL: US25: No unique first name in family for name: Jon /Barathaon/',
                    'ERROR: INDIVIDUAL: US25: No unique first name in family for name: Cate /Laniaster/']
        self.assertEqual(parser.US25(), result25)

    def test_userstory11(self):
        result11 = [
            'ERROR: FAMILY: US11: 1: F2: Cate /Laniaster/ is married to Ned /Stark/and Robert /Barathaon/ at the same time']
        self.assertEqual(parser.US11(), result11)

    def test_userstory12(self):
        result12 = [
            'ERROR: FAMILY: US12: 2: I5: Mother\'s age 154 is more than 60 years older than her child -30']
        self.assertEqual(parser.US12(), result12)

    def test_userstory31(self):
        result31 = ['ERROR: INDIVIDUAL: US31: 0: I1: Arya /Stark/ is of age 40 and unmarried', 'ERROR: INDIVIDUAL: US31: 3: I4: Cate /Laniaster/ is of age 80 and unmarried', 'ERROR: INDIVIDUAL: US31: 7: I8: Cercie /Tyrell/ is of age 74 and unmarried',
                    'ERROR: INDIVIDUAL: US31: 13: I14: Danny /Targaryen/ is of age 34 and unmarried', 'ERROR: INDIVIDUAL: US31: 15: I16: Podrick /Tyrell/ is of age 60 and unmarried', 'ERROR: INDIVIDUAL: US31: 16: I17: Pady /Snow/ is of age 52 and unmarried']
        self.assertEqual(parser.US31(), result31)

    def test_userstory32(self):
        result32 = [
            'ERROR: INDIVIDUAL: US32: 6: I7: Jamie /Lanaster/ and Cercie /Tyrell/ (I8) have the same birthdate 1945-07-09']
        self.assertEqual(parser.US32(), result32)


if __name__ == '__main__':
    unittest.main()
