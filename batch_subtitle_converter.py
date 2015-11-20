# added functionality: will do batch conversion for all files in the current working directory.
import os
all_srt_files = [fl for fl in os.listdir('.') if os.path.isfile(fl) and fl[-3:] == "srt"]

def subtitle_converter(file_name):
    # file_name = "01 - Introduction.srt"
    fr = open(file_name, "r")

    # new_file_list = 

    original_file = fr.read()
    splitted_file = original_file.split("\n")

    modified_splitted_file = splitted_file[:]
    # print type(modified_splitted_file)
    # print modified_splitted_file
    c_index = 0    # in the new file
    subtitle_index = 1

    modified_splitted_file.insert(c_index,str(subtitle_index))
    # print type(modified_splitted_file)
    '''
    insertion_point_in_new_file = 0
    for i in xrange(len(splitted_file)):
        if splitted_file[i] = ""
            insertion_point_in_new_file = insertion_point_in_new_file + 1
            subtitle_index = subtitle_index + 1
            modified_splitted_file.insert(insertion_point_in_new_file,i/3)
            continue
    '''

    for line in splitted_file:
        # try: print line.replace(",", " --> ", 1).replace(".", ",", 2)
        # except: pass
        c_index = c_index + 1
        if line == "":
            subtitle_index = subtitle_index + 1
            modified_splitted_file.insert(c_index + 1,str(subtitle_index))
            c_index = c_index + 1
            continue
        # print line
        try: 
            # print line[0:3]
            if line[0:3] == ">> ": modified_splitted_file[c_index] = ""+ line[3:]
        except: pass
        if len(line) < 15 : continue
        if line.find(":") == -1 : continue
        ind = line.find(":")
        # print ind
        try:
            if line[ind] == line[ind+3] == ":":
                # print type(line)
                # print line
                # print line.replace(",", " --> ", 1).replace(".", ",", 2)
                modified_splitted_file[c_index] = line.replace(",", " --> ", 1).replace(".", ",", 2) #this line was the culprit, and I checked almost the whole code
                # print "working"
        except:
            print "'{}' line".format(line)
    modified_splitted_file.pop()
    new_file_string = "\n".join(modified_splitted_file)
    # print new_file_string

    fw = open(file_name, "w")
    fw.write(new_file_string)
    print "'{}' converted successfully".format(file_name)
    return

for srt in all_srt_files:
    subtitle_converter(srt)