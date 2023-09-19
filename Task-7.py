#Function and FileHandling

#1.write a python program using function to which will do the following
#a.the function will create text file with current timestamp
#b.the file content should have the content of current timestamp

#solution:
import  datetime
#for get date,time we import datetime module

#create function with respective name
def timestamp(current_datetime):

    # create variable for create new text file
    new_textfile = open("current_timestamp.txt","w")

    #after creating file.txt & add content to inside  file using variablename with write()method
    new_textfile.write(f'current_date_time is: {current_datetime}')

    #close file
    new_textfile.close()

#for datetime format we create format variable and we using datetime.now() method with directive
format =datetime.datetime.now().strftime("%A_%d/%B_%m/%Y_%I:%M:%S_%p")

#calling function
timestamp(format)

#2.write another python function to read from text file.the function will take the name of text file and display the contentof the file into console
#solution
def file_read():

    #for read textfile we create variable and to opena file open()method passing textfile with 'r'
    read_file = open("current_timestamp.txt","r")

    # read() are read content inside in the text file
    print(read_file.read())

    # use close() method to close file
    read_file.close()

#calling function
file_read()

