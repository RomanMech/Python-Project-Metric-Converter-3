# Python Project 3
# Programmer:         Roman. A 
# Date Of Completion: 29th May 2024
# Description:        Asks User for their input on what their weight is, whatever number the user inputs they will be prompted with a choice of
#                     of whether the number the user meant was Kg or Lbs. If a user picks either of the metrics the response from the compiler
#                     will prompt what the weight would be in the other metric.


weight = input("Weight: ")
float(weight)

metric = input("(K)g or (L)bs: ")

if metric == "L" or "l":
    calculation = float(weight) * 0.45
    print(f"Weight in Kg: {calculation}")
elif metric == "K" or "k":
    calculation = float(weight) / 0.45
    print(f"Weight in Lbs: {calculation}")
