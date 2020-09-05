from selenium.common.exceptions import NoSuchElementException
import keyboard
import time


class FlightBookingHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.NewRulesPopupClose_button_xpath = "//div[@class='modal fade in']//button[@class='close'][contains(text(),'×')]"
        self.driver.OneWay_radiobutton_css_selector = "#oneWay"
        self.driver.Return_radiobutton_css_selector = "#round"
        self.driver.DepartingAirport_textbox_css_selector = "#input-search-from"
        self.driver.ArrivalAirport_textbox_css_selector = "#input-search-to"
        self.driver.DepartingDateForOneWay_datepicker_xpath = "//div[@class='form-group has-feedback-left pull-left posrel col-lg-2 col-md-2 col-sm-2 col-xs-6']//input[@placeholder='Depart On']"
        self.driver.ArrivalDate_datepicker_xpath = "//input[@placeholder='Return on']"
        self.driver.PassengerSelection_dropdown_css_selector = "#travellerDetail"
        self.driver.SearchForFlight_button_css_selector = "#search-button"

        self.driver.DepartingDateMonth_text_xpath = "div.ui-datepicker div.ui-corner-left div.ui-datepicker-title span.ui-datepicker-month"
        self.driver.DepartingDateYear_text_css_selector = "body.flights:nth-child(2) div.ui-datepicker.ui-widget.ui-widget-content.ui-helper-clearfix.ui-corner-all.ui-datepicker-multi.ui-datepicker-multi-2:nth-child(18) div.ui-datepicker-group.ui-datepicker-group-first:nth-child(1) div.ui-datepicker-header.ui-widget-header.ui-helper-clearfix.ui-corner-left div.ui-datepicker-title > span.ui-datepicker-year"
        self.driver.DepartingDateDay_text_css_selector = "body.flights:nth-child(2) div.ui-datepicker.ui-widget.ui-widget-content.ui-helper-clearfix.ui-corner-all.ui-datepicker-multi.ui-datepicker-multi-2:nth-child(18) div.ui-datepicker-group.ui-datepicker-group-first:nth-child(1) table.ui-datepicker-calendar tbody:nth-child(2) tr:nth-child(1) td:nth-child(5) > a.ui-state-default"
        self.driver.DatepickerNextMonth_button_css_selector = "div.ui-datepicker-group-last a.ui-datepicker-next"
        self.driver.AddAdultPax_button_xpath = "body.flights div.rposition div.flight-search div.form-group div.dropdown div.travellerDetails div.adultscol:nth-child(1) div.form-group button.btn.btn-default.btn-number.plus"
        self.driver.AddChildPax_button_xpath = "body.flights div.rposition div.flight-search div.form-group div.dropdown div.travellerDetails div.adultscol:nth-child(2) div.form-group button.btn.btn-default.btn-number.plus"
        self.driver.AddInfantPax_button_xpath = "body.flights div.rposition div.flight-search div.form-group div.dropdown div.travellerDetails div.adultscol:nth-child(3) div.form-group button.btn.btn-default.btn-number.plus"

    def departing_and_arriving_airport(self, departing_airport, arrival_airport):
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_class_name("cookies_cross").click()
        self.driver.find_element_by_xpath(self.driver.NewRulesPopupClose_button_xpath).click()
        self.driver.find_element_by_css_selector(self.driver.DepartingAirport_textbox_css_selector).send_keys(departing_airport)
        time.sleep(0.5)
        keyboard.press('Tab')
        self.driver.find_element_by_css_selector(self.driver.ArrivalAirport_textbox_css_selector).send_keys(arrival_airport)
        keyboard.press('Tab')

    def one_way_date_selection(self, dep_day, dep_month):
        self.driver.find_element_by_xpath(self.driver.DepartingDateForOneWay_datepicker_xpath).click()
        for all_month in range(1, 13):
            if dep_month == self.driver.find_element_by_css_selector(self.driver.DepartingDateMonth_text_xpath).text:
                for date_row in range(1, 7):
                    for date_column in range(1, 8):
                        date = "div.ui-datepicker div.ui-datepicker-group-first table.ui-datepicker-calendar tbody tr:nth-child(" + str(date_row) + ") td:nth-child(" + str(date_column) + ") a"
                        try:
                            self.driver.implicitly_wait(1 / 100)
                            if dep_day == self.driver.find_element_by_css_selector(date).text:
                                self.driver.find_element_by_css_selector(date).click()
                                break
                        except NoSuchElementException:
                            continue
                break
            else:
                self.driver.find_element_by_css_selector(self.driver.DatepickerNextMonth_button_css_selector).click()

    def return_date_selection(self, dep_day, dep_month, arr_day, arr_month):
        self.driver.find_element_by_css_selector(self.driver.Return_radiobutton_css_selector).click()
        self.driver.find_element_by_xpath(self.driver.DepartingDateForOneWay_datepicker_xpath).click()
        for all_month in range(1, 13):
            if dep_month == self.driver.find_element_by_css_selector(self.driver.DepartingDateMonth_text_xpath).text:
                for date_row in range(1, 7):
                    for date_column in range(1, 8):
                        date = "div.ui-datepicker div.ui-datepicker-group-first table.ui-datepicker-calendar tbody tr:nth-child(" + str(date_row) + ") td:nth-child(" + str(date_column) + ") a"
                        try:
                            self.driver.implicitly_wait(1 / 100)
                            if dep_day == self.driver.find_element_by_css_selector(date).text:
                                self.driver.find_element_by_css_selector(date).click()
                                break
                        except NoSuchElementException:
                            continue
                break
            else:
                self.driver.find_element_by_css_selector(self.driver.DatepickerNextMonth_button_css_selector).click()
        self.driver.find_element_by_xpath(self.driver.ArrivalDate_datepicker_xpath).click()
        for all_month in range(1, 13):
            if arr_month == self.driver.find_element_by_css_selector(self.driver.DepartingDateMonth_text_xpath).text:
                for date_row in range(1, 7):
                    for date_column in range(1, 8):
                        date = "div.ui-datepicker div.ui-datepicker-group-first table.ui-datepicker-calendar tbody tr:nth-child(" + str(date_row) + ") td:nth-child(" + str(date_column) + ") a"
                        try:
                            self.driver.implicitly_wait(1 / 100)
                            if arr_day == self.driver.find_element_by_css_selector(date).text:
                                self.driver.find_element_by_css_selector(date).click()
                                break
                        except NoSuchElementException:
                            continue
                break
            else:
                self.driver.find_element_by_css_selector(self.driver.DatepickerNextMonth_button_css_selector).click()

    def passenger_selection(self, number_of_adult, number_of_child, number_of_infant):
        self.driver.find_element_by_css_selector(self.driver.PassengerSelection_dropdown_css_selector).click()
        for adult_pax in range(int(number_of_adult) - 1):
            self.driver.find_element_by_css_selector(self.driver.AddAdultPax_button_xpath).click()
        for child_pax in range(int(number_of_child)):
            self.driver.find_element_by_css_selector(self.driver.AddChildPax_button_xpath).click()
        for infant_pax in range(int(number_of_infant)):
            self.driver.find_element_by_css_selector(self.driver.AddInfantPax_button_xpath).click()
        self.driver.find_element_by_css_selector(self.driver.SearchForFlight_button_css_selector).click()
