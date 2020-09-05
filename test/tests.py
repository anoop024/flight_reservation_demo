from selenium import webdriver
from pages.SotcHomePage import SotcHomePage
# from pages.LoginAndRegistration import LoginAndRegistration
from pages.FlightBookingHomePage import FlightBookingHomePage

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=r"C:\Users\angupta\PycharmProjects\F2Fportal_demo\drivers\chromedriver.exe", options=chrome_options)
driver.maximize_window()
driver.get("https://www.sotc.in//")
driver.implicitly_wait(10)
# SotcHomePage(driver).login_dropdown()
# SotcHomePage(driver).open_new_registration_popup()
# LoginAndRegistration(driver).register_new_account(title="Ms", firstname="tester", lastname="test", email_id="anoopforfriends@gmail.com", password="easyjet", mobile_no="9876543210")
SotcHomePage(driver).open_flight_booking_page()
FlightBookingHomePage(driver).departing_and_arriving_airport(departing_airport="Delhi", arrival_airport="Mumbai")
FlightBookingHomePage(driver).one_way_date_selection(dep_day="10", dep_month="Oct")
FlightBookingHomePage(driver).return_date_selection(dep_day="10", dep_month="Oct", arr_day="10", arr_month="Nov")
FlightBookingHomePage(driver).passenger_selection(number_of_adult="2", number_of_child="2", number_of_infant="1")


print(driver.title)
driver.close()
driver.quit()
