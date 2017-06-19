from urllib import request      #import request module

ibm_csv_url = "https://www.ibm.com/support/knowledgecenter/en/SVU13_7.2.1/com.ibm.ismsaas.doc/reference/AssetsImportExtendedSample.csv?view=kc"

def download_web_file(webURL):
    response = request.urlopen(webURL)      #connect to the web and url
    csv = response.read()                   #read the content of the URL
    csv_str = str(csv)                      #convert the received content to string
    
    lines = csv_str.split("\\n")            #tokenize the string based on new characters and new lines

    dest_url = r'ibmAssetInport.csv'        #specify destination URL

    fw = open(dest_url, 'w')                #open new file for write operation
    for line in lines:                      #write the file content using write operation
        fw.write(line + '\n')
    fw.close() 



download_web_file(ibm_csv_url)              #call the function