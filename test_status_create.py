from pages.pages import DashboardPage


def test_create_status(app, driver, logged_user):
    input_text = 'Welcome!'
    dashboard_page = DashboardPage(driver)
    # Locate existed text statuses
    old_status_list = dashboard_page.status_elements
    # Create new status
    assert dashboard_page.status_input_field.placeholder == "What’s happening?"
    dashboard_page.create_new_text_status(input_text)
    dashboard_page.wait_new_status_appear(old_status_list)
    # Verification
    new_status_element = dashboard_page.status_elements[0]
    assert new_status_element.text == input_text
    assert new_status_element.user == logged_user
    # user_link = dashboard_page.user_status_elements[0].get_attribute("href")
    # assert user_link.split("/")[-1] == logged_user.username
