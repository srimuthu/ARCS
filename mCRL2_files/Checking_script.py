#-------------------------------------------------------------------------------
# Name:        Checking_script.py
# Purpose:      Convert mcrl2 to lps ad verify with the .mcf files
#               present in the cwd
#
# Author:      SriMuthuNarayanan
#
# Created:     03-10-2015
# Copyright:   (c) SriMuthuNarayanan 2015
#-------------------------------------------------------------------------------


import os,time
pbesTag=''
lpsFile=''
for file in os.listdir(os.getcwd()):
    if file.endswith(".mcrl2"):
        mcrlFile = str(file)
        os.system('mcrl22lps'+' '+mcrlFile+' '+mcrlFile.replace('.mcrl2','.lps'))
        os.system('lps2lts'+' '+mcrlFile.replace('.mcrl2','.lps')+' '+mcrlFile.replace('.mcrl2','.lts'))
#        os.system('ltsgraph'+' '+mcrlFile.replace('.mcrl2','.lts'))
        lpsFile=mcrlFile.replace('.mcrl2','.lps')
        pbesTag=mcrlFile.replace('.mcrl2','.pbes')

for file in os.listdir(os.getcwd()):
    if file.endswith(".mcf"):
        verFile = str(file)
        pbesFile = verFile.replace('.mcf',str(pbesTag))
        os.system('lps2pbes -v -f '+ verFile+ ' '+ lpsFile + ' '+pbesFile)
        os.system('pbes2bool -v '+pbesFile)
        print('Requirement : '+str(verFile))
        time.sleep(2)

print("Verification of "+pbesTag.replace('.pbes','.mcrl2')+' Complete!')
time.sleep(2)