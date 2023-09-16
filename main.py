import time
from selenium import webdriver
import csv
import re

driver = webdriver.Chrome()
pid_list = []

with open('mobiles.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            product_title = row[2]
            if product_title != '' and 'flipkart' in product_title:
                pid_list.append(product_title)

all_colors = {}

for pid in range(106,len(pid_list)):
    print(len(pid_list))
    driver.get(pid_list[pid])
    try:
        JAVASCRIPT = """
            let property_name = document.getElementsByClassName("_1hKmbr")
            let property_val = document.getElementsByClassName("_21lJbe")
            let array_of_colors = [];
            let color = "";
            let elements = document.getElementsByClassName("_3V2wfe");
            if(elements.length > 0){
                for(let k of elements){
                    if(k.id.includes("color")){
                        let color_inner_div_tag = k.getElementsByClassName("_3Oikkn");
                        for(j of color_inner_div_tag){
                            array_of_colors.push((j.innerHTML).toLowerCase());
                        }
                    }
                }
            }
            else{
                for (let i = 0; i < property_name.length; i++) {
                    if (property_name[i].innerText == "Color") {
                        array_of_colors.push((property_val[i].innerText).toLowerCase());
                    }
                }
            }
            return array_of_colors;
        """
        colors = driver.execute_script(JAVASCRIPT)
        all_colors[pid] = colors
        print(all_colors)
    except Exception as e:
        color = 'error_code'
        print(e)

print("All Colors:", all_colors)

driver.quit()