__author__ = 'ryanj'


import os, sys, shutil, logging
import httplib, urllib


conn = httplib.HTTPSConnection("api.pushover.net:443")

#send string to pushover
def send_push (push_message):
   conn.request("POST", "/1/messages.json",
     urllib.urlencode({
       "token": "token",
       "user": "user",
       "message": push_message,
      }), { "Content-type": "application/x-www-form-urlencoded" })
   conn.getresponse()
   return





#Logger Setup
logger = logging.getLogger('Sync Season')
hdlr = logging.FileHandler('c:/Sync Test/sync_season.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

# Settings
#dl_path = "c:/Stern Test/"
sync_root = "c:/Sync Test/"
show_name = "Neon Gen"
sync_path = sync_root + show_name + "/"
arch_root = "c:/Users/ryanj/Dropbox/Sync/Sync to Nexus/"
arch_path = arch_root + show_name + "/"
sync_dirs = os.listdir( sync_path ) #not used atm
max_shows = 5

#Number of files currently in sync folder
num_in_sync = len([name for name in os.listdir(sync_path)])
#print num_in_sync
#create list of files in Sync Path and Archive
files_sync = sorted( os.listdir(sync_path))
files_arch = sorted( os.listdir(arch_path))
#print files_sync
#get file name for last episode found in sync
last_eps = files_sync[len(files_sync) - 1]
#print last_eps

#number of files that need to be added to sync
eps_needed = max_shows - num_in_sync
if last_eps in files_sync:
    loc_last_ep = files_arch.index(last_eps)
print loc_last_ep

new_files = files_arch[loc_last_ep + 1:loc_last_ep + 1 + eps_needed]
print new_files
for epi in new_files:
    shutil.copy(arch_path+epi, sync_path+epi)
    print ("Moving "+epi+" to Sync")



