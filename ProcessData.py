#ProcessData.py
#Name: Brooks Conway
#Date: 4/2/25
#Assignment: Lab 8

import random

def makeID(first, last, num)
  if len(last) < 5:
    last = last + "xxxxx"
    last[0,5]
  last3 = num[-3:]
  id = first[0] + last + last3
  return id

def makeMajorYear(major, year):
  first3 = major[0:3]
  year = year.upper()
  yearAb = ""
  if year == "Freshman":
    yearAb = "FR"
  elif year == "SOPHMORE":
    yearAb = "SO"
  elif year == "JUNIOR":
    yearAb = "JR"
  elif year == "SENIOR"
    yearAb == "SR"
  else
    yearAb = "Grad"
  return majorYear

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  student = "Antwan Dougherty AntwanDougherty@yahoo.com 443-13-3556 03/28/1996 Freshman Philosophy"
  studentData = student.split()
  print(studentData)
  firstName = studentDate[0]
  lastName = studentData[1]
  studentID = studentData[3]
  year = studentData[5]
  major = studentData[6]
  userID = makeID(firstName, lastName, studentID)
  majorYear = makeMajorYear(major, year)

  studentOutput = lastName + "," + firstName + "," + userID + "," + majorYear +
  outFile.write(studentOutput)


  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
