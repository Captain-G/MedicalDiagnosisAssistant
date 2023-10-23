from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import mysql.connector
from prettytable import PrettyTable

mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="password1",
    database="MedicalDiagnosisAssistant"
)
my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE IF NOT EXISTS MedicalDiagnosisAssistant")
my_cursor.execute(
    "CREATE TABLE IF NOT EXISTS Diseases (disease_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, disease_name VARCHAR(255), link VARCHAR(255))")
options = Options()
options.add_experimental_option("detach", True)


def scrapeNHS():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.nhsinform.scot/illnesses-and-conditions/a-to-z/")
    driver.maximize_window()

    diseases_nhs = []
    links_nhs = []
    diseases_a = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual a_detail']//ul/li/a")
    diseases_b = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual b_detail']//ul/li/a")
    diseases_c = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual c_detail']//ul/li/a")
    diseases_d = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual d_detail']//ul/li/a")
    diseases_e = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual e_detail']//ul/li/a")
    diseases_f = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual f_detail']//ul/li/a")
    diseases_g = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual g_detail']//ul/li/a")
    diseases_h = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual h_detail']//ul/li/a")
    diseases_i = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual i_detail']//ul/li/a")
    diseases_k = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual k_detail']//ul/li/a")
    diseases_l = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual l_detail']//ul/li/a")
    diseases_m = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual m_detail']//ul/li/a")
    diseases_n = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual n_detail']//ul/li/a")
    diseases_o = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual o_detail']//ul/li/a")
    diseases_p = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual p_detail']//ul/li/a")
    diseases_r = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual r_detail']//ul/li/a")
    diseases_s = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual s_detail']//ul/li/a")
    diseases_t = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual t_detail']//ul/li/a")
    diseases_u = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual u_detail']//ul/li/a")
    diseases_v = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual v_detail']//ul/li/a")
    diseases_w = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual w_detail']//ul/li/a")
    diseases_y = driver.find_elements(by=By.XPATH, value="//div[@class='az_list_indivisual y_detail']//ul/li/a")

    for i in range(len(diseases_a)):
        # diseases_nhs.append(diseases_a[i].get_attribute("innerText"))
        # links_nhs.append(diseases_a[i].get_attribute("href"))
        dis = [diseases_a[i].get_attribute("innerText"), diseases_a[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)
    for i in range(len(diseases_b)):
        # diseases_nhs.append(diseases_b[i].get_attribute("innerText"))
        # links_nhs.append(diseases_b[i].get_attribute("href"))
        dis = [diseases_b[i].get_attribute("innerText"), diseases_b[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)
    for i in range(len(diseases_c)):
        # diseases_nhs.append(diseases_c[i].get_attribute("innerText"))
        # links_nhs.append(diseases_c[i].get_attribute("href"))
        dis = [diseases_c[i].get_attribute("innerText"), diseases_c[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)
    for i in range(len(diseases_d)):
        # diseases_nhs.append(diseases_d[i].get_attribute("innerText"))
        # links_nhs.append(diseases_d[i].get_attribute("href"))
        dis = [diseases_d[i].get_attribute("innerText"), diseases_d[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)
    for i in range(len(diseases_e)):
        # diseases_nhs.append(diseases_e[i].get_attribute("innerText"))
        # links_nhs.append(diseases_e[i].get_attribute("href"))
        dis = [diseases_e[i].get_attribute("innerText"), diseases_e[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)
    for i in range(len(diseases_f)):
        # diseases_nhs.append(diseases_f[i].get_attribute("innerText"))
        # links_nhs.append(diseases_f[i].get_attribute("href"))
        dis = [diseases_f[i].get_attribute("innerText"), diseases_f[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)
    for i in range(len(diseases_g)):
        # diseases_nhs.append(diseases_g[i].get_attribute("innerText"))
        # links_nhs.append(diseases_g[i].get_attribute("href"))
        dis = [diseases_g[i].get_attribute("innerText"), diseases_g[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)
    for i in range(len(diseases_h)):
        # diseases_nhs.append(diseases_h[i].get_attribute("innerText"))
        # links_nhs.append(diseases_h[i].get_attribute("href"))
        dis = [diseases_h[i].get_attribute("innerText"), diseases_h[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)
    for i in range(len(diseases_i)):
        # diseases_nhs.append(diseases_i[i].get_attribute("innerText"))
        # links_nhs.append(diseases_i[i].get_attribute("href"))
        dis = [diseases_i[i].get_attribute("innerText"), diseases_i[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)
    for i in range(len(diseases_k)):
        # diseases_nhs.append(diseases_k[i].get_attribute("innerText"))
        # links_nhs.append(diseases_k[i].get_attribute("href"))
        dis = [diseases_k[i].get_attribute("innerText"), diseases_k[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)
    for i in range(len(diseases_l)):
        # diseases_nhs.append(diseases_l[i].get_attribute("innerText"))
        # links_nhs.append(diseases_l[i].get_attribute("href"))
        dis = [diseases_l[i].get_attribute("innerText"), diseases_l[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)
    for i in range(len(diseases_m)):
        # diseases_nhs.append(diseases_m[i].get_attribute("innerText"))
        # links_nhs.append(diseases_m[i].get_attribute("href"))
        dis = [diseases_m[i].get_attribute("innerText"), diseases_m[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)
    for i in range(len(diseases_n)):
        # diseases_nhs.append(diseases_n[i].get_attribute("innerText"))
        # links_nhs.append(diseases_n[i].get_attribute("href"))
        dis = [diseases_n[i].get_attribute("innerText"), diseases_n[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)
    for i in range(len(diseases_o)):
        # diseases_nhs.append(diseases_o[i].get_attribute("innerText"))
        # links_nhs.append(diseases_o[i].get_attribute("href"))
        dis = [diseases_o[i].get_attribute("innerText"), diseases_o[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)
    for i in range(len(diseases_p)):
        # diseases_nhs.append(diseases_p[i].get_attribute("innerText"))
        # links_nhs.append(diseases_p[i].get_attribute("href"))
        dis = [diseases_p[i].get_attribute("innerText"), diseases_p[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)
    for i in range(len(diseases_r)):
        # diseases_nhs.append(diseases_r[i].get_attribute("innerText"))
        # links_nhs.append(diseases_r[i].get_attribute("href"))
        dis = [diseases_r[i].get_attribute("innerText"), diseases_r[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)
    for i in range(len(diseases_s)):
        # diseases_nhs.append(diseases_s[i].get_attribute("innerText"))
        # links_nhs.append(diseases_s[i].get_attribute("href"))
        dis = [diseases_s[i].get_attribute("innerText"), diseases_s[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)
    for i in range(len(diseases_t)):
        # diseases_nhs.append(diseases_t[i].get_attribute("innerText"))
        # links_nhs.append(diseases_t[i].get_attribute("href"))
        dis = [diseases_t[i].get_attribute("innerText"), diseases_t[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)
    for i in range(len(diseases_u)):
        # diseases_nhs.append(diseases_u[i].get_attribute("innerText"))
        # links_nhs.append(diseases_u[i].get_attribute("href"))
        dis = [diseases_u[i].get_attribute("innerText"), diseases_u[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)
    for i in range(len(diseases_v)):
        # diseases_nhs.append(diseases_v[i].get_attribute("innerText"))
        # links_nhs.append(diseases_v[i].get_attribute("href"))
        dis = [diseases_v[i].get_attribute("innerText"), diseases_v[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)
    for i in range(len(diseases_w)):
        # diseases_nhs.append(diseases_w[i].get_attribute("innerText"))
        # links_nhs.append(diseases_w[i].get_attribute("href"))
        dis = [diseases_w[i].get_attribute("innerText"), diseases_w[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)
    for i in range(len(diseases_y)):
        # diseases_nhs.append(diseases_y[i].get_attribute("innerText"))
        # links_nhs.append(diseases_y[i].get_attribute("href"))
        dis = [diseases_y[i].get_attribute("innerText"), diseases_y[i].get_attribute("href")]
        sqlFormula = "INSERT INTO Diseases (disease_name, link) VALUES (%s, %s)"
        my_cursor.execute(sqlFormula, dis)

    # print("***** DISEASES SOURCED FROM https://www.nhsinform.scot/illnesses-and-conditions/a-to-z/ *****")
    # print(f"Diseases : {diseases_nhs}")
    # print(f"Length of diseases list : {len(diseases_nhs)}")
    # print(f"Links : {links_nhs}")
    # print(f"Length of links : {len(links_nhs)}")
    # print("***** END *****")

    # for i in range(10):
    #     link = links_nhs[i]
    #     driver.get(link)
    #     headings = driver.find_elements(by=By.XPATH,
    #                                     value="//div[@class='active js-plethoraplugins-tab-panel']//h2[@class='wp-block-heading']")
    #     # text = driver.find_elements(by=By.XPATH, value="")
    #     for j in range(len(headings)):
    #         print(headings[j].get_attribute("innerText"))
    #     print("------------------")
    mydb.commit()


def showDiseases():
    my_cursor.execute("SELECT * FROM Diseases")
    view_results = my_cursor.fetchall()
    table = PrettyTable()
    table.field_names = ['disease_id', 'disease_name', 'link']
    for row in view_results:
        table.add_row(row)
    print(table)


def scrapeECDC():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.ecdc.europa.eu/en/all-topics")
    driver.maximize_window()

    new_diseases_ecdc = []
    diseases_ecdc = driver.find_elements(by=By.XPATH, value="//ul[@class='disease-overview']//ul//li//a")
    for i in range(len(diseases_ecdc)):
        new_diseases_ecdc.append(diseases_ecdc[i].get_attribute("innerText"))
    print(f"Diseases : {new_diseases_ecdc}")
    print(f"Length : {len(new_diseases_ecdc)}")


def scrapeNIAMS():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.niams.nih.gov/health-topics/all-diseases")
    driver.maximize_window()

    new_diseases_niams = []
    diseases_niams = driver.find_elements(by=By.XPATH, value="//h3[@class='icon-card-title']//a")

    for i in range(len(diseases_niams)):
        new_diseases_niams.append(diseases_niams[i].get_attribute("innerText"))
    print(f"Diseases : {new_diseases_niams}")
    print(f"Length : {len(new_diseases_niams)}")


def test():
    counter = 0
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(
        "https://www.nhsinform.scot/illnesses-and-conditions/heart-and-blood-vessels/conditions/abdominal-aortic-aneurysm/")
    driver.maximize_window()
    headings = driver.find_elements(by=By.XPATH,
                                    value="//div[@class='active js-plethoraplugins-tab-panel']//h2[@class='wp-block-heading']")
    all_paragraphs = driver.find_elements(by=By.XPATH,
                                          value=f"//div[@class='active js-plethoraplugins-tab-panel']//h2[@class='wp-block-heading']//following-sibling::p")
    print(len(all_paragraphs))
    for i in range(len(headings)):
        paragraphs = driver.find_elements(by=By.XPATH,
                                          value=f"//div[@class='active js-plethoraplugins-tab-panel']//h2[@class='wp-block-heading'][{len(headings) - i}]//following-sibling::p")
        print(headings[len(headings) - i - 1].get_attribute("innerText"))
        for j in range(len(paragraphs) - counter):
            print(paragraphs[j].get_attribute("innerText"))
        counter += len(paragraphs)
        print("-----------------------------------------------------------------")


# scrapeNHS()
# scrapeECDC()
# scrapeNIAMS()
# showDiseases()
test()
