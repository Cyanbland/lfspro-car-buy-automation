from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

user_email = ""
user_password = ""

car_class_input = str(input("Informe a classe de carro a ser selecionada: (A, B or C):"))
num_of_tries = 1
num_of_bought_cars = 0


class CarForSale:
    def __init__(self, name, owner, hp, condition, kilometers, price, buy_btn):
        self.name = name
        self.owner = owner
        self.hp = hp
        self.condition = condition
        self.kilometers = kilometers
        self.price = price
        self.buy_btn = buy_btn


def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://forum.lfspro.net/index.php?/mycruise-ucl/")
    car_list = []
    car_objects = []
    global num_of_tries
    print("Iniciando tentativa " + str(num_of_tries))
    print("Carros comprados: " + str(num_of_bought_cars))

    def login():
        login_btn = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/ul/li[1]/a')
        login_btn.click()
        email_input = driver.find_element(By.XPATH, '/html/body/div[5]/form/div/div/div[1]/div/ul/li[1]/input')
        email_input.send_keys(user_email)
        time.sleep(2)
        password_input = driver.find_element(By.XPATH, '/html/body/div[5]/form/div/div/div[1]/div/ul/li[2]/input')
        password_input.send_keys(user_password)
        time.sleep(2)

        #submit_btn = driver.find_element(By.XPATH, '/html/body/main/div/div/div/div[1]/ul/li/div/div[2]/div/div[2]/aside/div[2]/div/div/ul/li/form[2]/button')

        submit_btn = driver.find_element(By.XPATH, '/html/body/div[5]/form/div/div/div[1]/div/ul/li[5]/button')
        submit_btn.click()

    def get_class(class_param):
        if class_param == 'a' or class_param == 'A':
            chosen_class = driver.find_element(By.XPATH, '/html/body/main/div/div/div/div[1]/ul/li/div/div[2]/div/div[2]/aside/div[2]/div/div/ul/li/form[1]/button')
            chosen_class.click()

        elif class_param == 'b' or class_param == 'B':
            chosen_class = driver.find_element(By.XPATH, '/html/body/main/div/div/div/div[1]/ul/li/div/div[2]/div/div[2]/aside/div[2]/div/div/ul/li/form[2]/button')
            chosen_class.click()

        elif class_param == 'c' or class_param == 'C':
            chosen_class = driver.find_element(By.XPATH, '/html/body/main/div/div/div/div[1]/ul/li/div/div[2]/div/div[2]/aside/div[2]/div/div/ul/li/form[3]/button')
            chosen_class.click()
        else:
            print("Erro na classe selecionada")

    def get_car_data():
        for i in range(len(car_list)):
            try:
                car_name = driver.find_element(By.XPATH, str(car_list[i]) + '/form/div[2]/h2/b')
                car_owner = driver.find_element(By.XPATH, str(car_list[i]) + '/form/div[3]/p')
                car_hp = driver.find_element(By.XPATH, str(car_list[i]) + '/form/div[4]/p')
                car_condition = driver.find_element(By.XPATH, str(car_list[i]) + '/form/div[5]/p')
                car_kilometers = driver.find_element(By.XPATH, str(car_list[i]) + '/form/div[6]/p')
                car_price = driver.find_element(By.XPATH, str(car_list[i]) + '/form/div[7]/p')
                car_buy_btn = driver.find_element(By.XPATH, str(car_list[i]) + '/form/div[11]/center/input[1]')
                #/html/body/main/div/div/div/div[1]/ul/li/div/div[2]/div/div[1]/div[2]/div/ol/div[2]/form/div[11]/center/input[1]

                print(car_name.text, car_owner.text, car_hp.text, car_condition.text, car_kilometers.text, car_price.text)
                car_objects.append(CarForSale(car_name.text, car_owner.text, car_hp.text, car_condition.text, car_kilometers.text, car_price.text, car_buy_btn))
            except:
                print("Todos os carros já foram listados!")

    def buy_car():
        found_car = False
        global num_of_bought_cars
        for car in car_objects:
            if car.owner == "Prefeitura":
                print("Carro apreendido encontrado")
                car.buy_btn.click()
                found_car = True
                num_of_bought_cars += 1
            # elif car.price == 'Lp$1':
            #     print("Carro de 1 Lp$ encontrado")
            #     car.buy_btn.click()
        if not found_car:
            print("Nenhum carro apreendido foi encontrado, tentando novamente em breve!")


    login()
    time.sleep(8)
    get_class(car_class_input)

    index = 2
    while index < 150:
        car_list.append('/html/body/main/div/div/div/div[1]/ul/li/div/div[2]/div/div[1]/div[2]/div/ol/div[' + str(index) + ']')
        #/html/body/main/div/div/div/div[1]/ul/li/div/div[2]/div/div[1]/div[2]/div/ol/div[2]/form/div[2]/h2/b
        index += 1

    get_car_data()
    buy_car()
    time.sleep(60)
    driver.close()

    num_of_tries += 1
    main()


main()







