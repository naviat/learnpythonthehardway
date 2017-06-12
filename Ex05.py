# -*- coding: utf-8 -*-

my_name = 'Đàm Văn Hải'
my_age  = 28
my_height = 65
my_weight = 60
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print("Let's talk about %s" % my_name)
print("He's %d cm tall." % my_height)
print("He's %d kg heavy." % my_weight)
print("Actually that’s not too heavy.")
print("He’s got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)
# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))