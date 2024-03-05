from page_objects.base_page import BasePage


class PrescriptiveDataPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.frame = self.page.frame_locator('[id="hs-form-iframe-0"]')
        self.firstname = self.frame.locator('[name="firstname"]')
        self.lastname = self.frame.locator('[name="lastname"]')
        self.email = self.frame.locator('[name="email"]')
        self.company = self.frame.locator('[name="company"]')
        self.jobTitle = self.frame.locator('[name="jobtitle"]')
        self.frimType = self.frame.locator("[name='company_real_estate_position__c']")

        self.home_page_text = self.page.locator("//strong[contains(text(), 'Carbon Reduction')]")
        self.schedule_demo_page_text = self.page.locator("//strong[contains(text(), 'Nantum Demo')]")
        self.schedule_demo_btn = self.page.locator("//a[contains(text(), 'Schedule Demo')]")

    def go_to_schedule_demo_page(self):
        self.page.goto('https://www.prescriptivedata.io/')
        assert self.home_page_text.is_visible()
        self.page.click("//a[contains(text(), 'Schedule Demo')]")


    def filling_schedule_demo_form(self, details):
        self.firstname.fill(details['firstname'])
        self.lastname.fill(details['lastname'])
        self.email.fill(details['email'])
        self.company.fill(details['company'])
        self.jobTitle.fill(details['jobTitle'])
        self.frimType.select_option(details['frimType'])

        # click on the submit button