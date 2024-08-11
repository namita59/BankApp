import pytest
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    if browser  == "chrome":
        print("Test run - Browser Chrome")
        driver = webdriver.Chrome()

    elif browser == "firefox":
        print("Test run -  Browser Firefox")
        driver = webdriver.Firefox()

    elif browser =="edge":
        print("Test run - Browser Edge")
        driver = webdriver.Edge()

    else:
        print("Test run - Headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://bankapp.credence.in/")
    yield driver
    driver.quit()

@pytest.fixture(params=[
    ("mragrendrata","Mragren@123","Login_pass"),
    ("Mragrendrat","Mragren@123","Login_fail"),
    ("Mragrendrata","ragren@123","Login_fail"),
    ("Mragrendrat","ragren@123","Login_fail")
])
def getDataForLoginValidation(request):
    return request.param

@pytest.fixture(params=[("kishore","Singh","07022005","shiv puram 23","Agra","Uttra Pradesh","282001")])
def getDataForCustomerCreate(request):
    return request.param

@pytest.fixture(params=[("56",'Current Account','115000')])
def getDataForAccountCreate(request):
    return  request.param
@pytest.fixture(params=[("143","21","1000","bill")])
def getDataForFundTransferCreate(request):
    return request.param

@pytest.fixture(params=[("143","Deepak","5000","Food")])
def getDataForBillPayment(request):
    return request.param