import os
import random
import time
import shutil
import schedule
def cotd():


    cotdDir = '/var/www/html/cotd/'
    cotd_file_path = '/var/www/html/cotd/cat.jpg'

    #cotd_file_path = '/home/heavenborn/test/cats/cotd/cat.jpg'
    #old_file_path = '/home/heavenborn/test/cats/old/' + 'cat_' + str(time.time()) + '.jpg'
    old_file_path = '/var/www/html/cats/old/' + 'cat_' + str(time.time()) + '.jpg'


    if os.listdir(cotdDir) == []:
        print("theres nothing here")
    else:
        cotdOld = os.listdir('cotd/')
        os.rename(cotd_file_path, old_file_path)


    catNames = ['MrFoof', 'MrKitty', 'Isabella']
    cotd = random.choice(catNames)

    chosen_dir = os.listdir(cotd + '/')

    

    cotd_pic = random.choice(chosen_dir)
    picPath = cotd + '/' + cotd_pic
    os.rename(picPath, cotd_file_path)


    print(cotd, cotd_pic, picPath)
    print(old_file_path)

schedule.every().day.at('21:45').do(cotd)
while True:
    schedule.run_pending()
    time.sleep(30)