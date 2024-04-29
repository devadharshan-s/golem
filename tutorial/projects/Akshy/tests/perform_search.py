from selenium import webdriver
from golem.actions import navigate, send_keys, click, verify_element_text, get_data

description = 'Perform a search for an article. verity that the title is correct'


def test(data):
    navigate("https://wikipedia.org")
    send_keys(('id', 'searchlnput'), "automation")
    click(('css', 'search-form button'))
    verify_element_text(('id','firstHeading'), "Automation")
    get_data()
