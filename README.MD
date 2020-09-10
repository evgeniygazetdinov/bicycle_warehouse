
### WAREHOUSE on qt5


*from designer to py with runner*
>pyuic5 -x template.ui -o template.py

*compile project*
>pyinstaller -D -F -n main -c "main.py"

*for run*

>python3 -m venv env 

>source env/bin/activate

>pip install -r requirements.txt

>python3 main.py

###########################################

# release notes:

## release 0.2:

categories 

get values from sqlite file


## release 0.3:
'''
search 

change resolution elements

new good window
'''
## release 0.4:
'''
>fix word case for search good same window for add/edit category change height beetween line 
>edits in cart enlarge height cart make tab widget responsible(tabwidget and tree widget in process)

add status bar for cart table for any column fix price column in good table(add formula)

add basic behavior for add good to card add displaying total cost and total profit
'''
## release 0.5:
'''
add queries for add/edit/delete 

fix displaying redisplaying table

from add/edit/delete for category/good window

add window for delete good/category

sub category are same now

fix close good window
'''

## release 0.6

>add basic sorting for columns in main table widget

>fix floating number for int strings

>fix basic sorting number by click

>fix blank cells

>add cant delete good  with == qty 0 add warning window

>add buttons for custom price

>add basic logic for custom price buttons

>add sorting by numbers

>add clean logic for clean button

###release 0.7|

>speed up search(change approach)

>change field for search

>remove filter and category labels

>resize search lineEdit move x button

###release 0.8|

>fix search by category add by word in substring

>add column in cart

>add exceptions for add 0 product and limit for add products in cart

>add window for handle qty product in cart

>fix counter products in cart

>add logic for add/remove item from cart

