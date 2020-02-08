# -*- coding: utf
# משימה שלישית- מציאת המטריצה המקסימלית 
import numpy as np

def find_the_max,_2d_arry():
    a1 = np.arange(8).reshape(2,4) #הגדרת מערך ראשון
    a2 = np.arange(15).reshape(5,3) #הגדרת מערך שני
    shape_ofa1 = a1.shape #ייצוג גודל המערך הראשון
    shape_ofa2 = a2.shape #ייצוג גודל המערך השני   
    size = lambda x1, x2 : x1 if (x1 > x2) else x2  הגדרת משתנה "גודל" המייצג את הגודל המקסימלי של חיבור המטריצות   
    biggest_x = size(shape_ofa1[0], shape_ofa2[0]) #גודל השורה
    biggest_y = size(shape_ofa1[1], shape_ofa2[1])  #גודל הטור  
    maxarry = np.zeros((biggest_x, biggest_y), dtype=int) # הגדרת מערך בגודל מקסימלי המורכב מ2 המערכים שהוגדרו  
    for row in range(shape_ofa1[0]): 
        for tor in range(shape_ofa1[1]):
            maxarry[row][tor] += a1[row][tor] #מכניס את ערכי המערך הראשון למערך המקסימלי
    for row in range(shape_ofa2[0]):
        for tor in range(shape_ofa2[1]):
            maxarry[row][tor] += a2[row][tor] # מכניס את ערכי המערך השני למערך המקסימלי ומבצע חיבור בין הערכים שהוכנסו מהמערך הראשון
    print(maxarry) # הדפסת המערך המקסימלי

if __name__ == "__main__":

 