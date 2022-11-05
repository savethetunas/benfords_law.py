###
### Author: Adam Fehse
### Course: CSc 110
### Description: This program simulates Benfords Law by taking a csv file and pulling out the numbers. It then
###              creates a dictionary whose values represent the number of times the leading digit is present.
###              The program will print a command line chart or a gui version.
###

from graphics import graphics
import random


def check_mode(mode,user_file,gui,random_color):
    if mode == 'text':
        create_dictionary(user_file)
    elif mode == 'gui':
        gui_chart(gui,random_color)


def create_dictionary(user_file):
    user_list = user_file.readlines()
    number_list = []
    print('\n')
    for line in user_list:
        lines_strip_split = line.strip('\n').split(',')
        for element in lines_strip_split:
            if element[0].isnumeric() and element[0] != '0' and element[len(element)-1].isnumeric():
                number_list.append(float(element))
    count_dict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for number in number_list:
        count_dict[int(str(number)[0])] += 1

    print_charts(number_list, count_dict)


def print_charts(number_list, count_dict):
    for index in count_dict.keys():
        chart_hash_tags = (count_dict[index] / len(number_list) * 100)
        print(index,'|', '#' * int(chart_hash_tags))
    print()
    percentage = count_dict[1] / len(number_list) * 100
    if float(25) <= percentage <= float(40):
        print("Follows Benford's Law")
    else:
        print("Does not follow Benford's Law")


def gui_chart(gui, random_color):
    gui.text(40,30,"Benford's Law Analysis Results:", random_color, 30)
    gui.line(40,90,40,450,random_color,5)


def main():
    user_file = open('populations.csv', 'r')
    mode = 'gui'
    gui = graphics(500, 500, "Benford's Law")
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    random_color = gui.get_color_string(red, green, blue)
    check_mode(mode, user_file, gui, random_color)
    while True:
        gui.clear()
        gui_chart(gui,random_color)
        gui.update_frame(30)


main()
