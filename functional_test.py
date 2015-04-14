
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # she notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # she is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # she types "Buy peacock feather" into a text bo (Edith's hobby)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feather" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        # self.assertTrue(
        #     any(row.text == '1: Buy peacock feathers' for row in rows),
        #     "New to-do item did not appear in table -- its text was: \n%s" % (
        #         table.text,
        #     )
        # )

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feather to make a fly" (Edit is very methodical)
        self.fail('Finish the test!')

        # The page updates again, and now shows both items in her list

        # Edith wonders whether the site will remember her list.  Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # she visits that URL - her to-do list is still there.

        # Staisfied, she goes back to sleep

        # self.browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
