#NOTE: Create a folder which encapsulates all the files or folders you want to share using local network and provide the path for that folder in the prompt when the program runs.
import os, socket, shutil

folder_path_to_zip = input("Enter the folder path to share: ").strip('"')
shutil.make_archive("shared_folder","zip", root_dir = folder_path_to_zip)

def primary_ip():
    local_hostname = socket.gethostname()
    primary_ip = [ip for ip in socket.gethostbyname_ex(local_hostname)[2] if not ip.startswith("127.")][:1][0]
    return primary_ip

print("\n\nLink to download:","http://"+primary_ip()+":8000/zipped.zip\nPress 'control+C' to end the sharing.\n\n\n")
os.system("python3 -m http.server -b {}".format(primary_ip()))
os.remove("zipped.zip")
