#!/usr/bin/python

import rarfile, os, optparse, glob

parser = optparse.OptionParser()
parser.add_option("-R", "--recursive", dest="recursive",  action="store_true")
            
            
(options, args) = parser.parse_args()


def rar_check_dir(rdir):
    print "checking", rdir
    os.chdir(rdir)


    rfp = glob.glob("*.rar")

    if len(rfp) > 0:

        rf = rarfile.RarFile(rfp[0])
    
        allfound = True
    
        for f in rf.infolist():
    
            if not os.path.exists(f.filename):
                allfound = False
        
        
            if allfound:
                
                
                partfiles =  glob.glob("*.r[0-9][0-9]");
                partfiles.extend(glob.glob("*.rar"))
                
            
                for f in partfiles:
                    print "rm %s" % f
                    os.remove(f)

def recurse_dir(dir):
    print "recursing", dir
    files = os.listdir(dir)

    for f in files:
        subdir = "%s/%s" % (dir, f)
        if os.path.isdir(subdir):
            rar_check_dir(subdir)
            recurse_dir(subdir)

if options.recursive:
    cdir = os.path.expanduser(args[0])
    
    recurse_dir(cdir)


else:
    rar_check_dir(args[0])