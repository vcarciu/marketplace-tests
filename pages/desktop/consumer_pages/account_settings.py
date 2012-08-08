#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.desktop.consumer_pages.base import Base
from selenium.webdriver.support.ui import WebDriverWait


class AccountSettings(Base):
    """
    Account settings base page
    Contains the common objects in the account setting area
    """
    _payment_locator = (By.CSS_SELECTOR, '.sub-nav > li:nth-child(2) > a')
    _header_title_locator = (By.CSS_SELECTOR, 'header.c > h1')
    _payment_page_locator = (By.ID, 'purchases')

    def click_payment_menu(self):
        self.selenium.find_element(*self._payment_locator).click()
        self.wait_for_page_loaded()
        return Payments(self.testsetup)

    @property
    def header_title(self):
        return self.selenium.find_element(*self._header_title_locator).text

    def wait_for_page_loaded(self):
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.is_element_present(*self._payment_page_locator))

class BasicInfo(AccountSettings):
    """
    User Account Settings page
    https://marketplace-dev.allizom.org/en-US/settings/
    """

    _page_title = "Account Settings | Mozilla Marketplace"
    _avatar_photo_locator = (By.CSS_SELECTOR, ".avatar.photo")
    _upload_photo_locator = (By.ID, "id_photo")
    _browser_id_email_input_locator = (By.ID, "email")
    _manage_account_link_locator = (By.CSS_SELECTOR, "#email+a")
    _browser_id_password_input_locator = (By.ID, "fake-password")
    _change_password_link_locator = (By.CSS_SELECTOR, "#fake-password+a")
    _display_name_input_locator = (By.ID, "id_display_name")
    _display_name_hint_locator = (By.CSS_SELECTOR, "#id_display_name+span.hint")
    _username_input_locator = (By.ID, "id_username")
    _location_input_locator = (By.ID, "id_location")
    _occupation_input_locator = (By.ID, "id_occupation")
    _homepage_input_locator = (By.ID, "id_homepage")
    _bio_input_locator = (By.ID, "id_bio_0")
    _bio_tooltip_locator = (By.CSS_SELECTOR, ".html-support .tooltip")
    _email_me_checkbox_locator = (By.ID, "id_notifications_3")
    _email_me_text_locator = (By.CSS_SELECTOR, ".check")
    _email_me_note_locator = (By.CSS_SELECTOR, ".note")
    _save_button_locator = (By.CSS_SELECTOR, ".form-footer > button")
    _delete_account_link_locator = (By.CSS_SELECTOR, ".form-footer .delete")
    _notification_box_locator = (By.CSS_SELECTOR,".notification-box.full")

    @property
    def browser_id_email(self):
        return self.selenium.find_element(*self._browser_id_email_input_locator).get_attribute('value')

    @property
    def is_browser_id_email_enabled(self):
        return self.selenium.find_element(*self._browser_id_email_input_locator).is_enabled()

    def click_manage_account_link(self):
        self.selenium.find_element(*self._manage_account_link_locator).click()

    @property
    def browser_id_password(self):
        return self.selenium.find_element(*self._browser_id_password_input_locator).get_attribute('value')

    @property
    def is_browser_id_password_enabled(self):
        return self.selenium.find_element(*self._browser_id_password_input_locator).is_enabled()

    def click_change_password_link(self):
        self.selenium.find_element(*self._change_password_link_locator).click()

    @property
    def display_name(self):
        return self.selenium.find_element(*self._display_name_input_locator).get_attribute('value')

    @property
    def display_name_hint_text(self):
        return self.selenium.find_element(*self._display_name_hint_locator.text)

    @property
    def username(self):
        return self.selenium.find_element(*self._username_input_locator).get_attribute('value')

    @property
    def location(self):
        return self.selenium.find_element(*self._location_input_locator).get_attribute('value')

    @property
    def occupation(self):
        return self.selenium.find_element(*self._occupation_input_locator).get_attribute('value')

    @property
    def homepage(self):
        return self.selenium.find_element(*self._homepage_input_locator).get_attribute('value')

    @property
    def bio(self):
        return self.selenium.find_element(*self._bio_input_locator).get_attribute('value')

    @property
    def bio_tooltip_text(self):
        return self.selenium.find_element(*self._bio_tooltip_locator).get_attribute('title')

    @property
    def is_email_me_checked(self):
        return self.selenium.find_element(*self._email_me_checkbox_locator).is_selected()

    @property
    def email_me_text(self):
        return self.selenium.find_element(*self._email_me_text_locator).text

    @property
    def email_me_note_text(self):
        return self.selenium.find_element(*self._email_me_note_locator).text

    def save_changes(self):
        self.selenium.find_element(*self._save_button_locator).click()

    def click_delete_account_link(self):
        self.selenium.find_element(*self._delete_account_link_locator).click()

    @property
    def notification_text(self):
        return self.selenium.find_element(*self._notification_box_locator).text

    def edit_display_name(self, text):
        self.type_in_element(self._display_name_input_locator, text)

    def edit_username(self,text):
        self.type_in_element(self._username_input_locator, text)

    def edit_location(self, text):
        self.type_in_element(self._location_input_locator, text)

    def edit_occupation(self, text):
        self.type_in_element(self._occupation_input_locator, text)

    def edit_homepage(self, text):
        self.type_in_element(self._homepage_input_locator, text)

    def edit_bio(self, text):
        self.type_in_element(self._bio_input_locator, text)

    def check_email_me_checkbox(self):
        self.selenium.find_element(*self._email_me_checkbox_locator).click()

class Payments(AccountSettings):
    """
    Payment Settings page
    https://marketplace-dev.allizom.org/en-US/settings/payment
    """

    _page_title = "Payment Settings | Mozilla Marketplace"

    _set_up_pre_approval_locator = (By.CSS_SELECTOR, '#preapproval > footer > button')
    _pre_approval_enabled_locator = (By.CSS_SELECTOR, '#preapproval .enabled')
    _remove_pre_approval_locator = (By.CSS_SELECTOR, '#preapproval > footer > button.delete')
    _preapproval_success_message_locator = (By.CSS_SELECTOR, 'section.notification-box.full > div.success')

    def go_to_payment(self):
        self.selenium.get('%s/settings/payment/' % self.base_url)

    @property
    def is_success_message_visible(self):
        return self.is_element_visible(*self._preapproval_success_message_locator)

    def click_set_up_pre_approval(self):
        self.selenium.find_element(*self._set_up_pre_approval_locator).click()
        from pages.desktop.paypal.paypal_sandbox import PayPalSandbox
        return PayPalSandbox(self.testsetup)

    @property
    def is_pre_approval_enabled(self):
        return self.is_element_visible(*self._pre_approval_enabled_locator)

    @property
    def pre_approval_enabled(self):
        return self.selenium.find_element(*self._pre_approval_enabled_locator).text

    def click_remove_pre_approval(self):
        self.selenium.find_element(*self._remove_pre_approval_locator).click()

    @property
    def is_remove_pre_approval_button_visible(self):
        return self.is_element_visible(*self._remove_pre_approval_locator)
