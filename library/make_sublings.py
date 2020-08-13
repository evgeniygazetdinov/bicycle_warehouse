from main_action import Views_Main_Window
import os


action =  Views_Main_Window()

categories = action.get_category_values()
childs = action.find_child_category(categories)
f1=open('{}/sublings.py'.format(os.getcwd()), 'a')
f1.write('\n')
f1.write('category_ids ={')
for category in categories:
    f1.write('"{}":{},'.format(category['name_category'],category['id']))
f1.write('}')
f1.write('\n')
f1.write('childs = {}'.format(childs))
f1.close()



