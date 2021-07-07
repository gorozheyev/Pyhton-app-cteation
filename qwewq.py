import requests
import json
import string
import random
import datetime
import time
from selenium import webdriver
import psycopg2
import selenium.common.exceptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-logging")
#options.add_argument("--disable-extensions")
options.page_load_strategy = 'normal'
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument("--use-fake-device-for-media-stream")
#options.add_argument("--disable-notifications")
#options.add_argument("--enable-infobars")
#options.add_argument("--allow-file-access")
#options.add_argument("--start-maximized")
#driver="/opt/auto_app_create/settings/chromedriver/chromedriver"
driver="/chromedriver/chromedriver"
url_demo='https://dinero.ua-demo.dev.f10.cloud'
url_staging='https://dinero.ua-staging.dev.f10.cloud'
upload_file='/chromedriver/temp_file.png'
#upload_file='/opt/auto_app_create/settings/temp_file.png'
sqlpad_demo='https://sqlpad.ua-demo.dev.f10.cloud'
sqlpad_staging='https://sqlpad.ua-staging.dev.f10.cloud'

def generate_letters_cyrilic(length):
    letters = ['Ж','З','з','А','а','Б','б','В','в','Г','г','Л','л','П','п','У','у','Ф','ф','Ш','ш','Ю','ю']
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def generate_letters(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def generate_numbers(length):
    letters = '123456789'
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def generate_phone():
 phone=('98 '+generate_numbers(3)+' '+generate_numbers(4))
 return phone

def generate_identificator():
 identificator=('313'+generate_numbers(7))
 return identificator

def generate_passport():
 passport=('СВ'+generate_numbers(6))
 return passport

def generate_email():
 email=generate_numbers(8)+'@funderly.finance'
 return email

def generate_name():
 name=generate_letters_cyrilic(10)
 return name

def generate_name_list():
    list = ['Марина','Єлисей','Кирило','Віталій','Тимофій','Миколай','Григорій','Макар','Мілена','Наталія','Аарон','Франц','Аркадій','Леон','Варфоломій','Златослава','Альберт','Варфоломій','Борислав','Станіслав','Ольга','Вікторія']
    result= random.choice(list)
    return result

def generate_surname():
 name=generate_letters_cyrilic(10)
 return name

def generate_surname_list():
    list = ['Москаль','Чалий','Усик','Артюх','Дутка','Килимник','Забарний','Андрощук','Дашенко','Токар','Чорновіл','Їжакевич','Артеменко','Василенко','Таран','Стельмах','Бабариченко','Абраменко','Луценко','Матвієнко','Філіпенко','Удовенко','Туркало','Ґалаґан','Рубан']
    result= random.choice(list)
    return result

def random_amount_spl():
    amount=[500,800,1000,1500,3000,5000,7000,15000,20000]
    result=random.choice(amount)
    return result

def generate_password():
    password=str(generate_letters(8)+generate_numbers(2))
    return password

def ua_www_app(url,term):
    def sql_pad(url_pad, sql):
        br.get(url_pad)
        wait = WebDriverWait(br, 20).until(EC.element_to_be_clickable((By.XPATH, "//select")))
        time.sleep(2)
        br.find_element_by_xpath("//select").click()
        br.find_element_by_xpath("//option[contains(.,'erp-db')]").click()
        br.find_element_by_xpath("//textarea").send_keys(sql)
        br.find_element_by_xpath("//button[contains(.,'Run')]").click()
        time.sleep(3)
        a = br.find_element_by_xpath(
            "/html/body/div[1]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div[3]/div/pre").text
        # br.quit()
        return a

    # web element definitions
    amount_input = "//input[@type='text']"
    term_7 = "//div[@id='app']/div/div/div[2]/div[3]/div/div[1]"
    term_14 = "//div[@id='app']/div/div/div[2]/div[3]/div/div[2]"
    term_30 = "//div[@id='app']/div/div/div[2]/div[3]/div/div[3]"
    submit_application_button = "//div[@id='app']/div/div/div[2]/div[5]/div/a"
    phone_form = "//input[@type='text' and @id='username']"
    phone_form_submit = "//button[@id='form_button']"
    surname = "//input[@type='text' and @id='surname']"
    name = "//input[@type='text' and @id='name']"
    middle_name = "//input[@type='text' and @id='middleName']"
    identificator = "//input[@type='text' and @id='person-id-number']"
    email = "//input[@type='text' and @id='email']"
    passport = "//input[@type='text' and @id='passportNumberAndSeries']"
    reg_date_day = "//div[@id='passportNumberAndSeriesContainer']/div[2]/div[3]/div/div/div/div[2]/b"
    choose_reg_date_day = "//li[contains(.,'3')]"
    reg_date_month = "//div[@id='passportNumberAndSeriesContainer']/div[2]/div[3]/div[2]/div/div/div[2]/b"
    choose_reg_date_month = "//div[2]/div/div/div[3]/div/ul/li[11]"
    reg_date_year = "//div[@id='passportNumberAndSeriesContainer']/div[2]/div[3]/div[3]/div/div/div[2]/span"
    choose_reg_date_year = "//li[contains(.,'2020')]"
    accept_check_box = "//form[@id='contact_data_doc_form']/label/span"
    submit_button = "//button[@type='submit']"
    credit_card = "//input[@id='credit_card_number']"
    expire_month = "//input[@id='expire_month']"
    expire_year = "//input[@id='expire_year']"
    cvv = "//input[@id='cvv2']"
    card_holder = "//input[@id='customer_name_utf8']"
    submit_card = "//button[@type='submit']"
    submit_emulation = "//button[@type='submit']"
    accept_popup = "//section[@class='popup']//a[@title='Ok']"
    first_selfie = "//div[@class='fileinput _inb']//input[@name='files[]'][1]"
    second_selfie = "//div[@class='cont_noimg ']//div[@class='fileinput _inb']//input[@name='files[]']"
    submit_pictures = "//button[@title='Продовжити']"
    sms_code_input = "//input[@name='activationCode' and @id='activationCode']"
    application_code_inpute = "//div[@class='cinput default invalid']/input"
    confirm_sms_code = "//button[@title='Подтвердить']"
    confirm_phone = "//button[@id='form_button']"
    go_to_sign_agreement_page = "//div[@class='_alr']/button"
    try:
        if url=='staging':
            url=url_staging
            sqlp=sqlpad_staging
        if url=='demo':
            url=url_demo
            sqlp=sqlpad_demo
        br = webdriver.Chrome(driver, options=options)
        br.set_window_size(1920, 1080)
        br.implicitly_wait(10)
        print('1.Opening url: ' + url)
        br.get(url)
        clear_amount = br.find_element_by_xpath(amount_input).clear()
        amount = random_amount_spl()
        choose_amount = br.find_element_by_xpath(amount_input).send_keys(amount)
        print('2.Choosing amount=' + str(amount))
        if term==1:
            term=term_7
        if term==2:
            term=term_14
        if term==3:
            term=term_30
        choose_term = br.find_element_by_xpath(term).click()
        continue_application = br.find_element_by_xpath(submit_application_button).click()
        time.sleep(2)
        phone = generate_phone()
        sql_phone = phone.replace(" ", "")
        print('3.Generating phone:' + sql_phone)
        br.find_element_by_xpath(phone_form).click()
        br.find_element_by_xpath(phone_form).clear()
        time.sleep(1)
        br.find_element_by_xpath(phone_form).send_keys(phone)
        time.sleep(1)
        br.find_element_by_xpath(phone_form_submit).send_keys(Keys.ENTER)
        sms_code_sql_demo = """Select ltrim(split_part(split_part(body,' ',7),'.',1)) from erp_notifications where phone='+380'||'{number}' and template_id=379 order by created_at desc limit 1;""".format(number=sql_phone)
        time.sleep(3)
        br.execute_script("window.open('');")
        br.switch_to.window(br.window_handles[1])
        sql = sms_code_sql_demo
        get_sms_code = sql_pad(sqlp, sql)
        br.switch_to.window(br.window_handles[0])
        br.find_element_by_xpath(application_code_inpute).send_keys(get_sms_code)
        br.find_element_by_tag_name('html').send_keys(Keys.END)
        time.sleep(1)
        br.find_element_by_xpath(confirm_phone).click()
        print('4.Starting client data block')
        wait = WebDriverWait(br, 20).until(EC.element_to_be_clickable((By.XPATH, surname)))
        surname_gen = generate_surname_list()
        fill_surname = br.find_element_by_xpath(surname).send_keys(surname_gen)
        name_gen = generate_name_list()
        fill_name = br.find_element_by_xpath(name).send_keys(name_gen)
        print('6.Generating client name :' + str(name_gen) + ' ' + str(surname_gen))
        fill_middle_name = br.find_element_by_xpath(middle_name).send_keys('Аутоматика') #generate_letters_cyrilic(8)
        fill_identificator = br.find_element_by_xpath(identificator).send_keys(generate_identificator())
        fill_email = br.find_element_by_xpath(email).send_keys(generate_email())
        fill_passport = br.find_element_by_xpath(passport).send_keys(generate_passport())
        select_doc_day = br.find_element_by_xpath(reg_date_day).click()
        choose_doc_day = br.find_element_by_xpath(choose_reg_date_day).click()
        select_regdate_month = br.find_element_by_xpath(reg_date_month).click()
        choose_regdate_mnth = br.find_element_by_xpath(choose_reg_date_month).click()
        select_regdate_year = br.find_element_by_xpath(reg_date_year).click()
        choose_regdate_y = br.find_element_by_xpath(choose_reg_date_year).click()
        br.find_element_by_tag_name('html').send_keys(Keys.END)
        time.sleep(0.5)
        accept_chk_bpx = br.find_element_by_xpath(accept_check_box).click()
        submit_step = br.find_element_by_xpath(submit_button).click()
        print('7.Client data block finished')
        time.sleep(2)
        print('8.Starting to add credit card')
        wait = WebDriverWait(br, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//div[@id='card_checkout']//iframe")))
        fill_credit_card = br.find_element_by_xpath(credit_card).send_keys('4444555566661111')
        time.sleep(0.3)
        fill_expire_month = br.find_element_by_xpath(expire_month).send_keys('06')
        time.sleep(0.3)
        fill_expire_year = br.find_element_by_xpath(expire_year).send_keys('22')
        time.sleep(0.3)
        fill_cvv = br.find_element_by_xpath(cvv).send_keys('123')
        time.sleep(0.3)
        fill_card_holder = br.find_element_by_xpath(card_holder).send_keys('Card Holder')
        time.sleep(1)
        finish_card = br.find_element_by_xpath(submit_card).click()
        time.sleep(2)
        br.switch_to.default_content()
        time.sleep(1)
        wait = WebDriverWait(br, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//div[@class='oplata_popup_content']//iframe")))
        finish_emulation = br.find_element_by_xpath(submit_emulation).click()
        time.sleep(3)
        popup_process = br.find_element_by_xpath(accept_popup).click()
        print('9.Credit card added')
        time.sleep(1)
        try:
            br.find_element_by_xpath(go_to_sign_agreement_page).click()
            print("Клик на кнопку Далее после добавления карты")
        except Exception:
            print("Кнопки не было")
        time.sleep(2)
        br.maximize_window()
        time.sleep(3)
        # br.get_screenshot_as_file('/opt/auto_app_create/UA/screenshots/'+generate_numbers(6)+'.png')
        br.find_element_by_xpath("(//a[contains(@href, '#')])[5]").click()
        br.find_element_by_xpath("//span[contains(.,'Зробити фотографію')]").click()
        br.find_element_by_xpath("//div[2]/a/span").click()
        print('10.First selfie uploaded')
        br.find_element_by_xpath("(//a[contains(@href, '#')])[8]").click()
        time.sleep(3)
        br.find_element_by_xpath("//span[contains(.,'Зробити фотографію')]").click()
        time.sleep(1)
        br.find_element_by_xpath("//span[contains(.,'Завантажити')]").click()
        wait = WebDriverWait(br, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Продовжити']")))
        br.find_element_by_xpath("//button[@title='Продовжити']").click()
        print('11.Second selfie uploaded')
        sms_code_sql_demo = """Select ltrim(split_part(split_part(body,' ',4),'.',1)) from erp_notifications where phone='+380'||'{number}' and template_id=205 order by created_at desc limit 1;""".format(number=sql_phone)
        time.sleep(3)
        br.execute_script("window.open('');")
        br.switch_to.window(br.window_handles[1])
        sql=sms_code_sql_demo
        get_sms_code = sql_pad(sqlp, sql)
        print('12.Sms code get using sqlpad done. Code:' + str(get_sms_code))
        br.switch_to.window(br.window_handles[0])
        br.find_element_by_xpath(sms_code_input).send_keys(get_sms_code)
        br.find_element_by_xpath(confirm_sms_code).click()
        print('13.Application processed succesfully')
        print('#####################################')
        time.sleep(5)
        br.capabilities.clear()
        br.quit()
    except Exception as e:
        print(e)
        br.get_screenshot_as_file('/opt/auto_app_create/error_screenshots/' +'ua'+ generate_numbers(6) + '.png')
        br.quit()

print('UA Dinero www application auto creator v.1.0')
print('Which environment you want to use? 1=demo,2=staging')
env=int(input())
if env==1:
    url='demo'
if env==2:
    url='staging'
print('Which term you want to use for loan? 1=7 days, 2=14 days, 3=30 days')
t=int(input())
if t not in (1,2,3):
    t=3
else:
    t=t
print('How many applications you want to create?')
c=int(input())
i=c
start = datetime.datetime.now()
while i>0:
    ua_www_app(url,t)
    i=i-1
end = datetime.datetime.now()
duration = (end - start)
final_duration = str(duration)[:-7]
print('Finished in: ' + str(final_duration))
