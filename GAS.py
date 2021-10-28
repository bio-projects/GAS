from Bio import Entrez
import time
import os
from Bio.Blast import NCBIWWW
from Bio import SearchIO
import urllib.request as request
from Bio.SeqIO import *
from Bio import SeqIO
from tkinter import *
import tkinter as tk
import tkinter.messagebox as tkMessageBox
from tkinter.filedialog import *
import ntpath
import math

def vp_start_gui():
    global homecwd, root, Entry1, Button1, Button2, Label3, sciname, queryfilename, Entry2, var, Radiobutton1, Radiobutton2, Button3, blastvar, Radiobutton3, Radiobutton4, listofacc, usremail, filtervar, Entry3, retri
    homecwd = os.getcwd()
    root = tk.Tk()
    root.geometry("500x600+600+50")
    root.minsize(1, 1)
    root.maxsize(1351, 738)
    root.resizable(0,  0)
    root.title("GAS")
    root.configure(background="#e0001a")
    root.protocol("WM_DELETE_WINDOW", callbackForRoot)
    
    Label1 = tk.Label(root)
    Label1.place(relx=0.0, rely=0.05, height=100, width=500)
    Label1.configure(background="#e0001a")
    Label1.configure(font="-family {Helvetica} -size 70 -weight bold")
    Label1.configure(foreground="white")
    Label1.configure(text='GAS')

    var = IntVar()
    Radiobutton1 = tk.Radiobutton(root)
    Radiobutton1.place(relx=0.2, rely=0.25, height=22, width=300)
    Radiobutton1.configure(background="#e0001a")
    Radiobutton1.configure(borderwidth="0")
    Radiobutton1.configure(font="-family {Helvetica} -size 11")
    Radiobutton1.configure(foreground="white")
    Radiobutton1.configure(text='Enter Scientific Name')
    Radiobutton1.configure(variable=var)
    Radiobutton1.configure(value=1)
    Radiobutton1.configure(highlightthickness=0)
    Radiobutton1.configure(command=Select)
    Radiobutton1.configure(selectcolor="#e0001a", activebackground="#cfcebc")
    Radiobutton1.select()

    sciname = ''
    Entry1 = tk.Entry(root)
    Entry1.place(relx=0.2, rely=0.29, height=35, width=300)
    Entry1.configure(background="white")
    Entry1.configure(borderwidth="0")
    Entry1.configure(font="-family {Helvetica} -size 11")
    Entry1.configure(relief="flat")

    Radiobutton2 = tk.Radiobutton(root)
    Radiobutton2.place(relx=0.2, rely=0.37, height=22, width=300)
    Radiobutton2.configure(background="#e0001a")
    Radiobutton2.configure(borderwidth="0")
    Radiobutton2.configure(font="-family {Helvetica} -size 11")
    Radiobutton2.configure(foreground="white")
    Radiobutton2.configure(text='Enter Assembly Accessions')
    Radiobutton2.configure(variable=var)
    Radiobutton2.configure(value=2)
    Radiobutton2.configure(highlightthickness=0)
    Radiobutton2.configure(command=Select)
    Radiobutton2.configure(selectcolor="#e0001a", activebackground="#cfcebc")

    listofacc = ''
    Button3 = tk.Button(root)
    Button3.place(relx=0.2, rely=0.41, height=35, width=300)
    Button3.configure(background="white", activebackground="#cfcebc")
    Button3.configure(borderwidth="0")
    Button3.configure(font="-family {Helvetica} -size 11")
    Button3.configure(relief="flat")
    Button3.configure(text='Browse the List of Assembly Accessions')
    Button3.configure(command=GetListAcc)
    Button3.configure(state=DISABLED)

    Label4 = tk.Label(root)
    Label4.place(relx=0.2, rely=0.49, height=20, width=300)
    Label4.configure(background="#e0001a")
    Label4.configure(borderwidth="0")
    Label4.configure(font="-family {Helvetica} -size 11")
    Label4.configure(foreground="white")
    Label4.configure(text='Enter Your Email')

    usremail = ''
    Entry2 = tk.Entry(root)
    Entry2.place(relx=0.2, rely=0.53, height=35, width=300)
    Entry2.configure(background="white")
    Entry2.configure(borderwidth="0")
    Entry2.configure(font="-family {Helvetica} -size 11")
    Entry2.configure(relief="flat")

    Label3 = tk.Label(root)
    Label3.place(relx=0.2, rely=0.61, height=20, width=250)
    Label3.configure(background="#e0001a")
    Label3.configure(borderwidth="0")
    Label3.configure(font="-family {Helvetica} -size 11")
    Label3.configure(foreground="white")
    Label3.configure(text='No. of retrieved sequences')

    retri = 0
    Entry3 = tk.Entry(root)
    Entry3.place(relx=0.7, rely=0.61, height=20, width=50)
    Entry3.configure(background="white")
    Entry3.configure(borderwidth="0")
    Entry3.configure(font="-family {Helvetica} -size 11")
    Entry3.configure(relief="flat")

    queryfilename = ''
    Button2 = tk.Button(root)
    Button2.place(relx=0.2, rely=0.65, height=35, width=300)
    Button2.configure(background="white", activebackground="#cfcebc")
    Button2.configure(borderwidth="0")
    Button2.configure(font="-family {Helvetica} -size 11")
    Button2.configure(relief="flat")
    Button2.configure(text='Browse Sequence FASTA file')
    Button2.configure(command=GetFileName)

    blastvar = StringVar()
    Radiobutton3 = tk.Radiobutton(root)
    Radiobutton3.place(relx=0.2, rely=0.80, height=22, width=150)
    Radiobutton3.configure(background="#e0001a")
    Radiobutton3.configure(borderwidth="0")
    Radiobutton3.configure(font="-family {Helvetica} -size 11")
    Radiobutton3.configure(foreground="white")
    Radiobutton3.configure(text='Megablast', justify='right')
    Radiobutton3.configure(variable=blastvar)
    Radiobutton3.configure(value='on')
    Radiobutton3.configure(highlightthickness=0)
    Radiobutton3.configure(selectcolor="#e0001a", activebackground="#cfcebc")
    Radiobutton3.select()

    Radiobutton4 = tk.Radiobutton(root)
    Radiobutton4.place(relx=0.5, rely=0.80, height=22, width=150)
    Radiobutton4.configure(background="#e0001a")
    Radiobutton4.configure(borderwidth="0")
    Radiobutton4.configure(font="-family {Helvetica} -size 11")
    Radiobutton4.configure(foreground="white")
    Radiobutton4.configure(text='Blastn', justify='left')
    Radiobutton4.configure(variable=blastvar)
    Radiobutton4.configure(value='off')
    Radiobutton4.configure(highlightthickness=0)
    Radiobutton4.configure(selectcolor="#e0001a", activebackground="#cfcebc")

    filtervar = IntVar()
    Checkbutton1 = tk.Checkbutton(root)
    Checkbutton1.place(relx=0.35, rely=0.74, height=22, width=150)
    Checkbutton1.configure(background="#e0001a")
    Checkbutton1.configure(borderwidth="0")
    Checkbutton1.configure(font="-family {Helvetica} -size 11")
    Checkbutton1.configure(foreground="white")
    Checkbutton1.configure(text="Filter without Blast")
    Checkbutton1.configure(variable=filtervar)
    Checkbutton1.configure(onvalue=1)
    Checkbutton1.configure(offvalue=0)
    Checkbutton1.configure(highlightthickness=0)
    Checkbutton1.configure(selectcolor="#e0001a", activebackground="#cfcebc")
    Checkbutton1.configure(command=FilterState)
    
    Button1 = tk.Button(root)
    Button1.place(relx=0.2, rely=0.87, height=35, width=300)
    Button1.configure(background="white", activebackground="#cfcebc")
    Button1.configure(borderwidth="0")
    Button1.configure(font="-family {Helvetica} -size 11")
    Button1.configure(relief="flat")
    Button1.configure(text='Start GAS')
    Button1.configure(command=CheckInputs)

    root.mainloop()

def FilterState():
    if filtervar.get() == 1:
        Radiobutton3.configure(state=DISABLED)
        Radiobutton4.configure(state=DISABLED)
    else:
        Radiobutton3.configure(state=NORMAL)
        Radiobutton4.configure(state=NORMAL)

def Select():
    global listofacc, sciname
    vari = var.get()
    if vari == 1:
        listofacc = ''
        Entry1.configure(state=NORMAL)
        Button3.configure(state=DISABLED)
        Button3.configure(text='''Browse the List of Assembly Accessions''')
    if vari == 2:
        sciname = ''
        Entry1.delete(0, END)
        Entry1.configure(state=DISABLED)
        Button3.configure(state=NORMAL)

def callbackForRoot():
	if tkMessageBox.askokcancel("Quit", "Do you want to quit GAS?"):
		root.destroy()

def GetSciName():
    global sciname
    sciname = ''
    sciname = Entry1.get()

def GetFileName():
    global queryfilename, outfilename, filenameonly
    queryfilename = ''
    queryfilename = askopenfilename()
    if queryfilename:
        filenameonly = ntpath.basename(queryfilename)
        Button2.configure(text=filenameonly)
        outfilename = '%s'%''.join(queryfilename.split('.')[:-1])
    else:
        Button2.configure(text='''Browse Sequence FASTA file''')

def GetListAcc():
    global listofacc, outfilename
    listofacc = ''
    listofacc = askopenfilename()
    if listofacc:
        listfilename = ntpath.basename(listofacc)
        Button3.configure(text=listfilename)
    else:
        Button3.configure(text='''Browse the List of Assembly Accessions''')

def GetEmail():
    global usremail
    usremail = ''
    usremail = Entry2.get()

def warning(message):
	tkMessageBox.showwarning("warning", message)

def CheckInputs():
    GetSciName()
    if sciname or listofacc:
        if queryfilename:
            GetEmail()
            if usremail:
                if filtervar.get() != 1:
                    StartGAS()
                    BlastN()
                    Filter()
                else:
                    StartGAS()
                    Filter()
            else:
                warning(message="Please, enter your email!")
        else:
            warning(message="Please, select the FASTA file!")
    else:
        warning(message="Please, enter the scientific name or list of accessions!")

def StartGAS():
    global databasename, databases, ftpfile, nofiles
    print('Start',time.strftime(("%H:%M:%S")))
    if sciname:
        taxid = []
        Entrez.email = usremail
        info = Entrez.read(Entrez.esearch(db='taxonomy', term=sciname))
        for sciids in info['IdList']:
            taxid.append(sciids)

    if listofacc:
        taxid = []
        with open(listofacc, 'r+') as accses:
            readaccs = accses.read()
            splitlistofacc = readaccs.split('\n')
            for spli in filter(None, splitlistofacc):
                splitspli = spli.split('\t')
                if len(splitspli) > 1:
                    taxid.append(splitspli[0])
                else:
                    taxid.append(spli)

    taxid = set(taxid)
    databases = []
    for tax in taxid:
        Entrez.email = usremail
        if sciname:
            searchterm = 'txid%s[Organism:exp]'%tax
        elif listofacc:
            searchterm = '%s[Assembly Accession]'%tax
        sea = Entrez.read(Entrez.esearch(db='assembly', term=searchterm, idtype='acc', retmax=200000000))
        acclist = sea['IdList']
        
        for acid, ac in enumerate(acclist):
            Entrez.email = usremail
            summ = Entrez.read(Entrez.esummary(db='assembly', id=ac), validate=False)
            for su in summ['DocumentSummarySet']['DocumentSummary']:
                if su['WGS'] != '':
                    databases.append('genomic/%s/%s'%(su['Taxid'], su['AssemblyAccession']))

    print(' '.join(databases))
    for fi in os.listdir():
        if '.dtd' in fi:
            os.remove(os.path.basename(fi))

    databasename = ' '.join(databases)
    print('The number of assemblies is', str(len(databases)))

    nofiles = 0
    for fe in SeqIO.parse(queryfilename, format="fasta"):
        nofiles += 1
    print('The number of query sequences is %i'%nofiles)

def BlastN():
    print('The number of blastn searches is %i'%(len(databases)*nofiles))
    print('The blastn starts at: %s'%str(time.strftime(("%H:%M:%S"))))
    if Entry3.get():
        retri = Entry3.get()
    else:
        retri = math.ceil(len(databases)*1.5)
    for ifasfile, fasfil in enumerate(SeqIO.parse(queryfilename, 'fasta')):
        Entrez.email = usremail
        print('(blastn search) query %s'%(str(ifasfile+1)),time.strftime(("%H:%M:%S")))
        result_handle = NCBIWWW.qblast("blastn", database=databasename, sequence=fasfil.format('fasta'), megablast=str(blastvar.get()), hitlist_size=retri)
        with open("%s_%s.xml"%(outfilename,str(ifasfile+1)), "w") as save_to:
            save_to.write(result_handle.read())
            result_handle.close()
        print('Wait 300 seconds')
        time.sleep(300)
        print('Thanks for understanding')
    print('The blastn ends at:',time.strftime(("%H:%M:%S")))

def Filter():
    collectoutputnames = []
    os.chdir(queryfilename.replace(filenameonly, ''))
    for file in os.listdir():
        namepattern = ntpath.basename(queryfilename)        
        splitnamepattern = namepattern.split('.')
        if splitnamepattern[0] in file and 'xml' in file:
            collectoutputnames.append(file)
        if '.dtd' in file:
            os.remove(file)

    print('The conversion starts at:',time.strftime(("%H:%M:%S")))
    out_kwarg = {'comments': True}
    for files in collectoutputnames:
        SearchIO.convert(files, 'blast-xml', '%s.tab'%''.join(files.split('.')[:-1]), 'blast-tab', out_kwargs=out_kwarg)

    print('The conversion ends at:%s'%str(time.strftime(("%H:%M:%S"))))
    print('The filtration starts at:%s'%str(time.strftime(("%H:%M:%S"))))
    os.chdir(queryfilename.replace(filenameonly, ''))
    collectfetchinfo = []
    ftpcheck = []
    for outputfile in collectoutputnames:
        for blastrecord in SearchIO.parse(outputfile, "blast-xml"):
            for ibr in blastrecord:
                if '%s %s' %(ibr.query_id, ibr.accession) not in ftpcheck:
                    for jind, jbr in enumerate(ibr):
                        if jind == 0:
                            jbr.hit.id = jbr.hit.id + str(jind) + '|' + ibr.query_id
                            collectfetchinfo.append(jbr.hit.format('fasta'))
                            ftpcheck.append('%s %s' %(ibr.query_id, ibr.accession))

    print('The filtration ends at:',time.strftime(("%H:%M:%S")))
    with open('%s.assemblies.fasta'%outfilename, 'w+') as w:
        w.write(''.join(collectfetchinfo))

    os.chdir(homecwd)
    print('Finish',time.strftime(("%H:%M:%S")))

if __name__ == '__main__':
    vp_start_gui()