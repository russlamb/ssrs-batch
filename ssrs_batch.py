from json import load
from urllib.parse import urlencode
from os import path
import requests 
from requests_ntlm import HttpNtlmAuth
from  getpass import getpass


def config_data(config_json):
    """Parses JSON from file into a dictionary object"""
    with open(config_json) as data_file:
        data = load(data_file)
    return data

def querystring_parse(parameter_data):
    """Parse dictionary to querystring"""
    data = parameter_data
    return urlencode(data).replace("%2F","/")

def data_override(parameter_data, override):
    """Override parameter values with specified values"""
    data=parameter_data
    for i in override:
        data[i]=override[i]
    return data

def download_file(url, username, password, local_filename=None):
    """Download file from a url using NTLM authorization"""
    #default name for local file
    if local_filename is None:
        local_filename = url.split('/')[-1]

    #HTTP get request using NTLM
    r = requests.get(url, auth=HttpNtlmAuth(username, password))

    #save file
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    
    return local_filename

def get_identifier(params, field_array):
    """Returns a file name based on parameters"""
    my_id = ""
    for i in field_array:
        val=params[i].replace("/","_") #replace special characters with underscores.  E.g. no slashes in file names
        my_id+=val+"_"
   
    return my_id


def report_iteration(config_json, usr, pwd):
    """Download multiple iterations of SSRS report"""
    data = config_data(config_json)
    iterations = data["iterations"]
    
    for i in iterations:
        params_new = data_override( data["parameters"], i)  #parameters for report
        qs = querystring_parse( params_new )                #querystring for URL
        url_new = data["url"]+r"&"+qs                       #combined URL
        identifier = get_identifier(params_new,
                                    data["file_identifier"])    #file suffix
        file_out = path.join(data["filepath"],
                             data["filename"]+"_"+
                             identifier+data["file_extension"])  #output file path

        #print to console for debug
        print("url {}".format(url_new))
        print("downloading file {}".format(file_out))
        
        download_file(url_new, usr,pwd, file_out)           
        
    print("Download complete")
    return len(iterations)  #return number of files downloaded

def print_usage():
    print("""
Usage:
    python ssrs_batch.py <username w/domain> <config file path> <password>""" )

if __name__=="__main__":
    import sys
	
    if len(sys.argv)<2:
        print_usage()
        sys.exit(1)

    username=sys.argv[1] #must contain domain e.g. TBG_DOMAIN\username
    config_filename=sys.argv[2] if len(sys.argv)>2 else "config.json"
    password=sys.argv[3] if len(sys.argv)>3 else getpass("Enter password for user {}".format(username))	
    report_iteration(config_filename, username, password)
        
