class LoginPageLocators:
    customer_account_icon_xpath = '//div[@class="header__account col"]'
    email_input_id = 'email'
    password_input_id = 'pass'
    login_button_xpath = '//button[@class="action login primary"]'
    logout_button_xpath = '//li[@class="nav item"][7]'
    account_data_button_xpath = '//li[@class="nav item"][3]'
    reset_password_checkbox_xpath = '//div[@class="field choice"][2]'
    current_password_id = 'current-password'
    new_password_id = 'password'
    confirm_new_password_id = 'password-confirmation'
    save_button_xpath = '//button[@type="submit" and @title="Zapisz"]'
    notification_xpath = '//div[@class="notification-message-O6n"]'

class CreateAccountPageLocators:
    create_account_button_xpath = '//a[@class="action create tetriary"]'
    name_id = 'firstname'
    lastname_id = 'lastname'
    email_id = 'email_address'
    password_input_id = 'password'
    password_conf_input_id = 'password-confirmation'
    sign_in_button_xpath = '//button[@class="action submit primary"]'
    continue_as_guest_button_xpath = '//input[@class="action continue primary"]'

class MainPageLocators:
    menu_kategorie_xpath = '//div[@class="mainNavStyles-link-2oO"]'
    kategorie_href_xpath = '//a[@class="categoryListStyles-link-1xd"]'
    podkategorie_href_xpath = '//a[@class="subCategoriesStyles-link-3VT"]'
    search_input_id = 'search'
    search_button_xpath = '//button[@class="action search"]'
    accept_cookies_xpath = '//a[@class="action primary" and @title="Zgadzam się"]'
    contact_form_button_xpath = '//div[@class="header-contact__link col-auto"]'

class ContactPageLocators:
    contact_form_name_id = 'name'
    contact_form_email_id = 'email'
    contact_form_phone_id = 'telephone'
    contact_form_comment_id = 'comment'
    send_button_xpath = '//button[@class="action submit primary"]'

class SearchPageLocators:
    product_list_xpath = '//li[@class="item product product-item"]'

class ProductPageLocators:
    add_to_cart_id = 'product-addtocart-button'
    input_xpath = '//div[@class="col-12 col-md-auto select-quantity-desktop"]//child::input'
    delete_from_cart_xpath = '//span[@class="section-text-3ch" and contains(text(), "Usuń z koszyka")]'

class ExtraoptionsPageLocators:
    go_to_cart_button_xpath = '//a[@class="action primary checkout arrowed w-100"]'

class ShoppingCartPageLocators:
    go_to_order_xpath = '//button[@class="action primary arrowed checkout"]'

class CheckoutDeliveryLocators:
    email_input_id = 'customer-email'
    phone_input_xpath = '//input[@name="telephone"]'
    firstname_input_xpath = '//input[@name="firstname"]'
    lastname_input_xpath = '//input[@name="lastname"]'
    street_input_xpath = '//input[@name="street[0]"]'
    postcode_input_xpath = '//input[@name="postcode"]'
    city_input_xpath = '//input[@name="city"]'
    proceed_to_summary_button_id = 'summary-shipping-button'

class SummaryPageLocators:
    payU_xpath = '//div[@class="tr payment-method payu-payment"][0]'
    blik_xpath = '//div[@class="tr payment-method payu-payment"][1]'
    apple_pay_xpath = '//div[@class="tr payment-method payu-payment"][2]'
    raty_payU_xpath = '//div[@class="tr payment-method payu-payment"][3]'
    raty_CA_xpath = '//div[@class="tr"][1]'
    twisto_xpath = '//div[@class="tr payment-method payu-payment"][4]'
    bank_transfer_xpath = '//div[@class="tr"][2]'
    paypal_xpath = '//div[@class="tr"][3]'
    agreement_1_id = 'agreement__3'
    agreement_2_id = 'agreement__4'
    order_and_pay_button_xpath = '//button[@class="action primary w-100"]'







