from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_create_a_course_or_see_courses(self):
        # Balaji(The geeky) heard about a new cool elearning website
        self.browser.get('http://localhost:8000')


        # He notices the page title and the header mention vle
        self.assertIn('vle', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('vle', header_text)
        
        
        # He sees that there are no courses
        table = self.browser.find_element_by_id('id_course_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            all(row.text == '' for row in rows), 
            "Table already has some course"
        )

        # but there is a button to create a new course
        button = self.browser.find_element_by_id('id_new_course')
        self.assertEqual(
                button.text,
                'Create course'
         )
        

        self.fail('Finish the test!')
        # So he wants to create his new awesome coding course
        # Button redirect him to new page with three boxes
        # He saw course title box and enters the course title
            
            

        # Now his new coding course is also available in the courses list
        # He fill the course title, course id and course description

        # All the fans of Balaji can see his course in list

        # He is invited to see the already available courses
        # click on the available courses and see the course title, course id and course description
        



if __name__ == '__main__':
    unittest.main()
