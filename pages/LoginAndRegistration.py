from selenium.webdriver.support.ui import Select


class LoginAndRegistration:

    def __init__(self, driver):
        self.driver = driver
        # for new registration
        self.driver.RegistrationPageHeader_text_css_selector = "body.holidays.sotc_home_page.modal-open:nth-child(2) div.modal.fade.login_reg_popup.in:nth-child(4) div.modal-dialog div.modal-content div.modal-header > h4.modal-title"
        self.driver.Title_dropdown_css_selector = "#regTitle"
        self.driver.Firstname_textbox_css_selector = "#registerFName"
        self.driver.Lastname_textbox_css_selector = "#registerLName"
        self.driver.Email_textbox_css_selector = "#registerEmailId"
        self.driver.Password_textbox_css_selector = "#registerPwd"
        self.driver.ConfirmPassword_textbox_css_selector = "#registerConfirmPwd"
        self.driver.Mobile_no_textbox_css_selector = "#registerMobileNo"
        self.driver.PrivacyPolicy_checkbox_css_selector = "body.holidays.sotc_home_page.modal-open:nth-child(2) div.modal.fade.login_reg_popup.in:nth-child(4) div.modal-dialog div.modal-content div.modal-body.login_reg_body div.reg_form_holder.login_reg_div form.form-horizontal div.form_control_grp:nth-child(7) > label.login_reg_sprite.css-label"
        self.driver.LoginWithFacebook_button_css_selector = "body.holidays.sotc_home_page.modal-open:nth-child(2) div.modal.fade.login_reg_popup.in:nth-child(4) div.modal-dialog div.modal-content div.modal-body.login_reg_body div.social_login_holder.login_reg_div div.social_login_btns.soc-login > a.fb_login_btn.fbbtn_bg"
        self.driver.LoginWithGoogle_button_css_selector = "#google-login"
        self.driver.Login_link_css_selector = "body.holidays.sotc_home_page.modal-open:nth-child(2) div.modal.fade.login_reg_popup.in:nth-child(4) div.modal-dialog div.modal-content div.modal-body.login_reg_body div.reg_form_holder.login_reg_div div.form_footer > a.show_login_form:nth-child(2)"
        # for login with existing account
        self.driver.Username_textbox_css_selector = "#loginId"
        self.driver.LoginWithPassword_selector_css_selector = "body.holidays.sotc_home_page.modal-open:nth-child(2) div.modal.fade.login_reg_popup.in:nth-child(3) div.modal-dialog div.modal-content div.modal-body.login_reg_body div.login_form_holder.login_reg_div form.login_reg_form div.tc_login_otp_details.full_sotcwidth:nth-child(2) > div.tc_login_otp_three.tc_login_otp_details_pass.sotc_loginwidth:nth-child(2) input.tc_login_otp_radio"
        self.driver.LoginWithOTP_selector_css_selector = "body.holidays.sotc_home_page.modal-open:nth-child(2) div.modal.fade.login_reg_popup.in:nth-child(3) div.modal-dialog div.modal-content div.modal-body.login_reg_body div.login_form_holder.login_reg_div form.login_reg_form div.tc_login_otp_details.full_sotcwidth:nth-child(2) > div.tc_login_otp_three.tc_login_otp_details_otp.sotc_loginwidth:nth-child(3) input.tc_login_otp_radio"
        self.driver.LoginPassword_textbox_css_selector = "#existloginPass"
        self.driver.Login_button_css_selector = "#loginButton"

    def register_new_account(self, title, firstname, lastname, email_id, password, mobile_no):
        print(self.driver.find_element_by_css_selector(self.driver.RegistrationPageHeader_text_css_selector).text)
        select = Select(self.driver.find_element_by_css_selector(self.driver.Title_dropdown_css_selector))
        if title == "Mr":
            select.select_by_value("Mr")

        elif title == "Mrs":
            select.select_by_value("Mrs")

        elif title == "Ms":
            select.select_by_value("Ms")

        elif title == "Dr":
            select.select_by_value("Dr")

        elif title == "Master":
            select.select_by_value("Mast")

        elif title == "Miss":
            select.select_by_value("Miss")

        else:
            print("Invalid title")
        self.driver.find_element_by_css_selector(self.driver.Firstname_textbox_css_selector).send_keys(firstname)
        self.driver.find_element_by_css_selector(self.driver.Lastname_textbox_css_selector).send_keys(lastname)
        self.driver.find_element_by_css_selector(self.driver.Email_textbox_css_selector).send_keys(email_id)
        self.driver.find_element_by_css_selector(self.driver.Password_textbox_css_selector).send_keys(password)
        self.driver.find_element_by_css_selector(self.driver.ConfirmPassword_textbox_css_selector).send_keys(password)
        self.driver.find_element_by_css_selector(self.driver.Mobile_no_textbox_css_selector).send_keys(mobile_no)
        if self.driver.find_element_by_css_selector(self.driver.PrivacyPolicy_checkbox_css_selector).is_selected() == "false":
            self.driver.find_element_by_css_selector(self.driver.PrivacyPolicy_checkbox_css_selector).click()
        print("privacy already marked")

    def login_with_existing_account(self, username, password):
        self.driver.find_element_by_css_selector(self.driver.Username_textbox_css_selector).send_keys(username)
        self.driver.find_element_by_css_selector(self.driver.LoginWithPassword_selector_css_selector).click()
        self.driver.find_element_by_css_selector(self.driver.LoginPassword_textbox_css_selector).send_keys(password)
        self.driver.find_element_by_css_selector(self.driver.Login_button_css_selector).click()
