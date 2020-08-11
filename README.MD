*WAREHOUSE on qt5*

*from designer to py with runner*

 pyuic5 -x template.ui -o template.py

*compile project*

pyinstaller -D -F -n main -c "main.py"

*for run*

python3 -m venv env 

source env/bin/activate

pip install -r requirements.txt

python3 main.py

###########################################

release notes:

release 0.2:

categories 

get values from sqlite file


release 0.3:

search 

change resolution elements

new good window

|release 0.4|:

fix word case for search good same window for add/edit category change height beetween line 
edits in cart enlarge height cart make tab widget responsible(tabwidget and tree widget in process)

add status bar for cart table for any column fix price column in good table(add formula)

add basic behavior for add good to card add displaying total cost and total profit

|release 0.5|:

add queries for add/edit/delete -good/category

fix displaying redisplaying table

from add/edit/delete for category/good window

add window for delete good/category

sub category are same now

fix close good window