 

def jacardindex(a,b):
    # Find the union of the two sets
    union = a.union(b)
    #reuslt intercection
    intersection=a.intersection(b)

    if len(union)==0:
        return 0
    if len(intersection)!=0:
        print("")

    return len(intersection)/len(union)


#Tropos A kai B
#RETURN: set with doc id that has this category
# Extracts all the documents id that has this category and inializes a set
def get_doc_id_from_category_file(category,categoryFile):
    docId = set() 

    # thiscategoryFile="Term.txt"
    # termFile1="lyrl2004_vectors_test_pt0.dat.txt"

# Open the text file for reading
    with open(categoryFile, 'r') as file:
        # Loop through each line in the file
        for line in file:
            # Split the line by space
            parts = line.split()
            # Check if there are at least two parts (a key and a value)
            if len(parts) >= 2:
                # Extract the key and value
                if(parts[0]==category):
                    key = parts[0]
                    docId.add( (parts[1]))

    return docId
                
#Tropos A
#reads and searches in the file for term intializing the set of  document id
# RETURN: set with document_id 
def get_doc_id_from_term_file(term,file):
        
        #the result set where the doct ids that contains the term will be stored
        Doct_id=set()
        ## reads the text line by line assiging each line to ln
        for ln in file:
            line=ln.split()
            #traverses the array that holds the line ,looking for the terms ,starts from 1 because 0 is the doct id
            for words in line[1:]:
                #separate the term form the weight
                trm=words.split(':')
                if trm[0]==term:
                    Doct_id.add(line[0])
                    break
       
        return Doct_id

#Tropos B
#readTermAndinitStructureWithALLTerms(termFile1) 
def get_doc_id_from_term_file_B_Tropos(fileName):
    
    word_data = {}

    with open(fileName, 'r') as file: 
         for ln in file:
             
             line=ln.split()

             #traverse the array of words
             for words in line[1:]:
                 trm=words.split(':')
                 if trm[0] not in word_data:
                     word_data[trm[0]]=set()
                     word_data[trm[0]].add(line[0])
                 else:
                    word_data[trm[0]].add(line[0])
    return word_data


def get_term_id_from_stem_file(fileName):
    stem_term_Id={}
    with open (fileName, "r",encoding="latin-1") as file:
        lines = file.readlines()
        for line in lines[2:]:
            # Split the line by space
            parts = line.split()
            if len(parts)>=2:
                stem_term_Id[parts[0]]=parts[1]
            
    return stem_term_Id
             

def search_in_files_doc_id_term_id(files,term):
    doct_id={}


 

 

def _1_A_tropos(category,k):
     categoryFile="rcv1-v2.topics.qrels.txt"
     termFile1="lyrl2004_vectors_test_pt0.dat.txt"

     DidCategory=get_doc_id_from_category_file('E11',categoryFile)


     ##call function that retuens all the tems id in a set

     #the doct id variew form 2 to a big number
     #calling the readTerm for some terms

     #test to open the file here

     file = open(termFile1, "r")

     J_I_rslts=set()
     doclen=set()
     for i in range(1,47232):
        # print("i is: ",i)
        doctSet=get_doc_id_from_term_file(str(i),file)
        doclen.add(len(doclen))
        rsl=jacardindex(doctSet,DidCategory)
        J_I_rslts.add(rsl)
    

     print("comlete")
     orted_list = sorted(J_I_rslts)
     
     file.close()
         
   
 

def _1_B_tropos(category,k):
    categoryFile="rcv1-v2.topics.qrels.txt"
    termFile1="lyrl2004_vectors_test_pt0.dat.txt"
    Terms=get_doc_id_from_term_file_B_Tropos(termFile1)
    
    DidCategory=get_doc_id_from_category_file('E11',categoryFile)
    TersmId={}
    
    for key, value in Terms.items():
        rslt=jacardindex(DidCategory,value)
        TersmId[key]=rslt
    
    sorted_dict = dict(sorted(TersmId.items(), key=lambda item: item[1], reverse=True))
    
    print("end")

 


#RETURN: set with files inside this folder
def read_files_names(folder_path ):
    file_names_set = set()

    # Iterate through files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):  # Check if the file has a .txt extension
            file_names_set.add(folder_path+"/"+file_name)

    return file_names_set

 #-----------------------------------------------------------------------------------------------------------------------------------------------------       
 


def top_k_stems_of_category(k,category):
    #------------------------------files declerations--------------------------------------------------
    #Category_File                                                                                    
    Category_File="doc_id-category_id/rcv1-v2.topics.qrels.txt"                                       
                                                                                                        
    #stem-term_id file                                                                                
    stem_term_id_file="stem-term_id/stem.termid.idf.map.txt"                                          
                                                                                                      
    #FOLDER_Name_of_doc_id-term_id, inside the folder multiple files are containing                   
    doc_id_term_id_folder_name="doc_id_-_Term_id"                                                     
    doc_id_term_id_files=read_files_names(doc_id_term_id_folder_name) #set with names of the file     
    #--------------------------------End files declarations--------------------------------------------
    
    #dictionary with key=terms_id and data=stems
    terms_ids=get_term_id_from_stem_file(stem_term_id_file)

    all_categories_with_all_doc_ids=scan_category_file()

    for key in all_categories_with_all_doc_ids:

        #get set with doct_id from category file
        doct_ids_category=get_doc_id_from_category_file(key,Category_File)

        #dictionary with key=term_id data jacard_index result
        jcrd_index={}
        #calculate jacard of all term intialize jcr_index
        jcrd_index=calculate_jcr_index_all_terms(doc_id_term_id_files,doct_ids_category,terms_ids)
    
        #sort dictionary
        sorted_dict = dict(sorted(jcrd_index.items(), key=lambda item: item[1], reverse=True))
   
    #print("")
    DidCategory=search_in_files_doc_id_term_id( category,Category_File)

def calculate_jcr_index_all_terms(files,doc_ids_form_category,term_ids):
    
    file1 = open(files.pop(), "r")
    file2 = open(files.pop(), "r")
    file3 = open(files.pop(), "r")
    file4 = open(files.pop(), "r")
    file5 = open(files.pop(), "r")
    filespointer=[file1,file2,file3,file4]
    
    filesPointers={}
    var=0
    jcrd_results={}
    #traverse all the files
    for key, value in term_ids.items():
        doct_id_from_term=set()
        var+=1
        if var==50:
            print()

        for file_name in filespointer:
             
            doc_id=get_doc_id_from_term_file(value,file_name)
            if len(doc_id)!=0:
                print("d")
            doct_id_from_term=doct_id_from_term.union(doc_id)
            
        rsl=jacardindex(doct_id_from_term,doc_ids_form_category)
        if rsl!=0:
            print("the rsl",rsl)
        jcrd_results[key]=rsl  
    #print("end")
    return jcrd_results
             

import os



 
def scan_category_file():
    categoryFile="rcv1-v2.topics.qrels.txt"

    categor_doc_id={}

    with open(categoryFile,"r") as file:
        for ln in file:
            parts = ln.split()
            categor_doc_id[parts[0]]=parts[1]
    
    return categor_doc_id


 

top_k_stems_of_category(10,"ECAT")
 



