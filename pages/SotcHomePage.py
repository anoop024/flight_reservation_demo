class SotcHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.Login_dropdown_css_selector = "body.holidays.sotc_home_page.showCookeiPolicy:nth-child(2) div.top-header:nth-child(3) a.pull-right:nth-child(4) > span.caret.hidden-xs"
        self.driver.Login_button_css_selector = "#mainLogIn0"
        self.driver.Register_link_css_selector = "body.holidays.sotc_home_page:nth-child(2) div.top-header:nth-child(3) div.dropdown-menu.login_dropdown:nth-child(6) div.col-lg-12.col-md-12.col-sm-12.user_details.text-center:nth-child(1) div.new_user_reg:nth-child(5) p:nth-child(1) > a.show_register_form"
        self.driver.ManageBooking_link_css_selector = "body.holidays.sotc_home_page:nth-child(2) div.top-header:nth-child(3) div.dropdown-menu.login_dropdown:nth-child(6) div.col-lg-12.col-md-12.col-sm-12.user_activities:nth-child(2) ul:nth-child(1) li:nth-child(1) > a:nth-child(1)"
        self.driver.Cancellation_link_css_selector = "body.holidays.sotc_home_page:nth-child(2) div.top-header:nth-child(3) div.dropdown-menu.login_dropdown:nth-child(6) div.col-lg-12.col-md-12.col-sm-12.user_activities:nth-child(2) ul:nth-child(1) li:nth-child(2) > a:nth-child(1)"
        self.driver.Profile_link_css_selector = "body.holidays.sotc_home_page:nth-child(2) div.top-header:nth-child(3) div.dropdown-menu.login_dropdown:nth-child(6) div.col-lg-12.col-md-12.col-sm-12.user_activities:nth-child(2) ul:nth-child(1) li:nth-child(3) > a:nth-child(1)"
        self.driver.PostBookingDoc_link_css_selector = "body.holidays.sotc_home_page.showCookeiPolicy:nth-child(2) div.top-header:nth-child(3) div.dropdown-menu.login_dropdown:nth-child(6) div.col-lg-12.col-md-12.col-sm-12.user_activities:nth-child(2) ul:nth-child(1) li:nth-child(4) > a:nth-child(1)"
        self.driver.Flights_link_css_selector = "body.holidays.sotc_home_page:nth-child(2) header.navbar.navbar-static-top.bs-docs-nav.home:nth-child(6) div.container-fluid nav.navbar.navbar-default.navbar_menu_mob_on div.collapse.navbar-collapse.js-navbar-collapse ul.nav.navbar-nav.hidden-xs li.dropdown.mega-dropdown:nth-child(6) > a:nth-child(1)"

    def login_dropdown(self):
        self.driver.find_element_by_css_selector(self.driver.Login_dropdown_css_selector).click()

    def open_login_popup(self):
        self.driver.find_element_by_css_selector(self.driver.Login_button_css_selector).click()

    def open_new_registration_popup(self):
        self.driver.find_element_by_css_selector(self.driver.Register_link_css_selector).click()

    def open_manage_booking_page(self):
        self.driver.find_element_by_css_selector(self.driver.ManageBooking_link_css_selector).click()

    def open_cancellation_page(self):
        self.driver.find_element_by_css_selector(self.driver.Cancellation_link_css_selector).click()

    def open_profile(self):
        self.driver.find_element_by_css_selector(self.driver.Profile_link_css_selector).click()

    def open_flight_booking_page(self):
        self.driver.find_element_by_css_selector(self.driver.Flights_link_css_selector).click()
