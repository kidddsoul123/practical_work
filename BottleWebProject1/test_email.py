import re
import unittest
import re_email


list_correct_mail = ["john.doe@example.com",
"jane_smith123@example.com",
"david-king@example.com",
"emily+thomas@example.com",
"alexander.brown@example.com",
"lisa123@example.com",
"mike.miller@example.com",
"sarah_jones@example.com",
"peter_smith@example.com",
"anna.baker@example.com",
"robert-lee@example.com",
"jennifer+johnson@example.com"]

list_uncorrect_email = ["john.doe@example",
"jane_smith123@.com",
"david-king@examplecom",
"emily+thomas@example..com",
"alexander.brown@example_com",
"lisa123@.example.com",
"mike.miller@example..com",
"sarah_jones@example_com",
"peter_smith@example.",
"anna.baker@example_com",
"robert-lee@example..com",
"jennifer+johnson@example_.com"]

class MailTest(unittest.TestCase):
    def test_correct_mail(self):
        for mail in list_correct_mail:
            self.assertTrue(re_email.is_mail(mail))

    def test_uncorrect_mail(self):
        for mail in list_uncorrect_email:
             self.assertFalse(re_email.is_mail(mail))
            
if __name__ == '__main__':
    unittest.main()
