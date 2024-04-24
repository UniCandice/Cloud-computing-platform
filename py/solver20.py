# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 09:10:46 2015

@author: ssheng
"""

from sts_class import Config20
import csv,os,os.path,glob,shutil,subprocess,platform,optparse,sys
import constant
import MySQLdb

randtest=''
if sys.argv:
   randtest=str(sys.argv[2])
if not randtest:
   os._exit(0)

db=MySQLdb.connect(constant.mysql['host'],constant.mysql['user'],constant.mysql['password'],constant.mysql['dbname1'])

cursor=db.cursor()

sql="select * from computing_list where Type='Upload' and Random="+randtest
try:
    cursor.execute(sql)
    results_us=cursor.fetchall()
    for row_us in results_us:
        Users=row_us[2]
        Solvers=row_us[3]
        Test_Rand=row_us[4]
except:
    print 'Error: unable to fetch data'
    os._exit(0)
db.close()

runexe=r'run_'+Users+r'.sh'
testpath=''
testpath=os.path.join(constant.path['current'],'Upload'+Users+r'_'+str(randtest))
sourcepath=os.path.join(testpath,'data')
number_path=os.path.join(testpath,r'number.txt')
state_path=os.path.join(testpath,r'state.txt')
downpath=os.path.join(testpath,'download')

testcase=os.path.join(testpath,r'testcase20.csv')
sts_path=os.path.join(testpath,r'bhcfd.sts')


def cp():
#   将ch20求解器及.cgns文件拷贝到目标区域
    global testpath
    global testcase
    
    fileou=open(testcase,'rb')
    csv_reader=csv.DictReader(fileou)

    file1=glob.glob(testpath+os.sep+r'ch*')
    file1+=glob.glob(testpath+os.sep+r'*.cgns')

    for row in csv_reader:
        if row['dotask(Yes=1)']=='1':
            repath=row['TaskName']
            outputdir=os.path.join(testpath,repath)
            sourcedir=testpath
            for files in os.listdir(sourcedir):
                sourceFile=os.path.join(sourcedir,files) 
                if os.path.isfile(sourceFile):
                    if not os.path.exists(outputdir):
                        os.makedirs(outputdir)
                    if sourceFile==file1[0] or sourceFile==file1[1]:
                        shutil.copy(sourceFile,outputdir)


def getsts():
#   根据测试表信息相应的bhcfd.sts
    global testpath
    global testcase
    global sts_path
    
    fileou=open(testcase,'rb')
    csv_reader=csv.DictReader(fileou)
    for row in csv_reader:
        repath=row['TaskName']
        sts=Config20(filename=sts_path)
        
        sts['TaskName']               = row['cases']
        sts['Nondimension_L']         = row['Nondimension_L']
        sts['GridType']               = row['GridType']
        sts['SolverType']             = row['SolverType']
        sts['Initial_way']            = row['Initial_way']       
        sts['Height']                 = row['Height']
        sts['Mach']                   = row['Mach']
        sts['Alpha']                  = row['Alpha']
        sts['Beta']                   = row['Beta'] 
        sts['Twall']                  = row['Twall']
        sts['Gamma']                  = row['Gamma']
        sts['Prandtl_Lam']            = row['Prandtl_Lam']
        sts['Prandtl_Turb']           = row['Prandtl_Turb']
        sts['ATM_Pressure']           = row['ATM_Pressure']
        sts['ATM_Density']            = row['ATM_Density']
        sts['ATM_Temperature']        = row['ATM_Temperature']    
        sts['TimeScheme']             = row['TimeScheme']
        sts['InvDiscretMethod']       = row['InvDiscretMethod']
        sts['VisDiscretMethod']       = row['VisDiscretMethod']    
        sts['FluxScheme']             = row['FluxScheme']
        sts['Limiter']                = row['Limiter']
        sts['VisDirection']           = row['VisDirection']
        sts['UnphysicsCorrect']       = row['UnphysicsCorrect']
        sts['TimeSizeMethod']         = row['TimeSizeMethod']
        sts['RelaxFactor']            = row['RelaxFactor']          
        sts['EntropyFix']             = row['EntropyFix']
        sts['EntropyFixD']            = row['EntropyFixD']
        sts['EntropyFixO']            = row['EntropyFixO']
        sts['JSTCoe2']                = row['JSTCoe2']
        sts['JSTCoe4']                = row['JSTCoe4']
        sts['FlowModel']              = row['FlowModel']   
        sts['CompressibilityCorrect'] = row['CompressibilityCorrect']
        sts['DES_Method']             = row['DES_Method']
        sts['CDES']                   = row['CDES']
        sts['CDES_SST']               = row['CDES_SST']         
        sts['IsRestart']              = row['IsRestart']
        sts['IterationNum']           = row['IterationNum']
        sts['CFL']                    = row['CFL']
        sts['IOUT']                   = row['IOUT']
        sts['ErrorTol']               = row['ErrorTol'] 
        sts['InitialStepNum']         = row['InitialStepNum']     
        sts['Ref_Area']               = row['Ref_Area'] 
        sts['Ref_Length']             = row['Ref_Length']
        sts['Ref_X']                  = row['Ref_X']
        sts['Ref_Y']                  = row['Ref_Y']
        sts['Ref_Z']                  = row['Ref_Z'] 
        sts['Unsteady']               = row['Unsteady']
        sts['TimeSize']               = row['TimeSize']
        sts['MaxTimeSteps']           = row['MaxTimeSteps']
        sts['EndTime']                = row['EndTime'] 
        sts['SubCFL']                 = row['SubCFL']
        sts['SubStepNum']             = row['SubStepNum'] 
        sts['SubErrorTOL']            = row['SubErrorTOL']
        sts['IPlot']                  = row['IPlot']
        sts['QuasiSteadySteps']       = row['QuasiSteadySteps']
        sts['QuasiRestartSteps']      = row['QuasiRestartSteps'] 
        sts['SG1']                    = row['SG1']
        sts['SG2']                    = row['SG2']
        sts['SG3']                    = row['SG3']
        sts['SG4']                    = row['SG4']
        outputdir=os.path.join(testpath,repath)
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)           
        sts.write(outputdir+os.sep+'bhcfd.sts')
    fileou.close()

def getrunsh():
    """ builds an run.sh for given number of processes """
    #生成ch20 run文件
    global Users
    global testpath
    global Solvers
    global testcase
    global runexe
    
    fileou=open(testcase,'rb')
    csv_reader=csv.DictReader(fileou)
    for row in csv_reader:
        repath=row['TaskName']
        outputdir=os.path.join(testpath,repath)
        if not os.path.exists(outputdir):
            os.makedirs(outputdir) 
            
        runpath=os.path.join(outputdir,runexe)
        f = open(runpath, 'w')
        
        processes=row['NCPUs']
        taskname=row['TaskName']
        f.write("#!/bin/bash\n")
        f.write("#PBS -N "+Users+'_'+taskname+"\n")
        f.write("#PBS -j oe "+"\n")
        f.write("#PBS -o ./ "+"\n")
        f.write("#PBS -q default "+"\n")
        f.write("#PBS -l nodes="+str(processes)+"\n")
        f.write("#PBS -l walltime=240:00:00 \n")
        f.write(r"# Special PBS control comments, need to change: -N and suround by"+"\n")
        f.write("#============================"+"\n")
        f.write("# Set up the path"+"\n")
        f.write(r"#export PATH=/usr/local/stow/openmpi-1.2.6/bin:$PATH"+"\n")
        f.write(r"#export LD_LIBRARY_PATH=/usr/local/stow/openmpi-1.2.6/lib:$LD_LIBRARY_PATH"+"\n")
        f.write(r"root_dir=`echo $PBS_O_WORKDIR|sed  's/^\/media\/node[0-9][0-9]*\//\//p'`"+"\n")
        f.write("# Set up the something \n")
        f.write("#============================ \n")
        f.write("exeName="+'"'+Solvers+'"'+"\n")
        f.write("users="+'"'+Users+'"'+"\n")
        f.write("#============================ \n")
        f.write("# prepare to run \n")
        #写运行语句
        f.write(r"cd $root_dir"+"\n")
        f.write(r"echo Running on hosts `hostname`"+"\n")
        f.write(r"echo Time is `date`"+"\n")
        f.write(r"echo Directory is $PWD"+"\n")
        f.write("echo This job runs on the following nodes:\n")
        f.write(r"cat $PBS_NODEFILE"+"\n")
        f.write(r"cat  $PBS_NODEFILE>hosts.txt"+"\n")
        f.write(r"nodes=`wc -l hosts.txt |awk '{print $1}'`"+"\n")
        f.write("#============================ \n")
        f.write(r"chmod 777 $exeName "+"\n")
        f.write(r"ulimit -s unlimited"+"\n")
        f.write(r"mpirun -n $nodes -f hosts.txt ./$exeName |tee output.txt "+"\n")
        f.write("#============================ \n")
        f.write(r"echo Finish Time is `date`"+"\n")
        f.close
    fileou.close()

def tecplot_mrc():
    global Users
    global testpath
    global testcase
    global runexe
    global downpath
    
    fileou=open(testcase,'rb')
    csv_reader=csv.DictReader(fileou)
    
    for row in csv_reader:
        repath=row['TaskName']
        outputdir=os.path.join(testpath,repath)
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)  
        fconv_mrc=os.path.join(outputdir,r'fconv.mcr')
        f=open(fconv_mrc, 'w')
        f.write(constant.tecplot['version']+"\n")
        f.write(r"$!VarSet |MFBD| = '"+outputdir+r"'"+"\n")
        f.write(r"$!READDATASET  '"+r'"|MFBD|'+os.sep+r'FCONV.dat" '+r"'"+"\n")
        f.write(r"READDATAOPTION = NEW"+"\n")
        f.write(r"RESETSTYLE = YES"+"\n")
        f.write(r"INCLUDETEXT = NO"+"\n")
        f.write(r"INCLUDEGEOM = NO"+"\n")
        f.write(r"INCLUDECUSTOMLABELS = NO"+"\n")
        f.write(r"VARLOADMODE = BYNAME"+"\n")
        f.write(r"ASSIGNSTRANDIDS = YES"+"\n")
        f.write(r"INITIALPLOTTYPE = XYLINE"+"\n")
        f.write(r"VARNAMELIST = '"+r'"ISTEP" "CX" "CY" "CZ" "MX" "MY" "MZ"'+r"'"+"\n")
        f.write(r"$!XYLINEAXIS XDETAIL 1 {TITLE{TEXTSHAPE{ISITALIC = YES}}}"+"\n")
        f.write(r"$!XYLINEAXIS XDETAIL 1 {TITLE{TEXTSHAPE{HEIGHT = 3}}}"+"\n")
        f.write(r"$!XYLINEAXIS XDETAIL 1 {TICKLABEL{TEXTSHAPE{ISBOLD = YES}}}"+"\n")
        f.write(r"$!XYLINEAXIS XDETAIL 1 {TICKLABEL{TEXTSHAPE{ISITALIC = YES}}}"+"\n")
        f.write(r"$!XYLINEAXIS YDETAIL 1 {TITLE{SHOWONAXISLINE = NO}}"+"\n")
        f.write(r"$!XYLINEAXIS YDETAIL 1 {TICKLABEL{TEXTSHAPE{ISBOLD = YES}}}"+"\n")
        f.write(r"$!XYLINEAXIS YDETAIL 1 {TICKLABEL{TEXTSHAPE{ISITALIC = YES}}}"+"\n")
        f.write(r"$!ATTACHTEXT"+"\n")
        f.write(r"ANCHORPOS"+"\n")
        f.write(r"{"+"\n")
        f.write(r"X = 49.17287014061208"+"\n")
        f.write(r"Y = 91.68734491315136"+"\n")
        f.write(r"}"+"\n")
        f.write(r"TEXTSHAPE"+"\n")
        f.write(r"{"+"\n")
        f.write(r"ISITALIC = YES"+"\n")
        f.write(r"SIZEUNITS = FRAME"+"\n")
        f.write(r"HEIGHT = 3.6"+"\n")
        f.write(r"}"+"\n")
        f.write(r"TEXT = 'CX'"+"\n")
        f.write(r"$!PICK SETMOUSEMODE"+"\n")
        f.write(r"MOUSEMODE = SELECT"+"\n")
        f.write(r"$!LINEMAP [1-6]  LINES{LINETHICKNESS = 0.59999999999999998}"+"\n")
        f.write(r"$!LINEMAP [1-6]  CURVES{CURVETYPE = PARASPLINE}"+"\n")
        f.write(r"$!VIEW FIT"+"\n")
        f.write(r"$!EXPORTSETUP EXPORTFORMAT = JPEG"+"\n")
        f.write(r"$!EXPORTSETUP IMAGEWIDTH = 900"+"\n")
        f.write(r"$!VarSet |JPGSAVE| = '"+downpath+os.sep+repath+"_map"+r"'"+"\n")
        f.write(r"$!EXPORTSETUP EXPORTFNAME = '|JPGSAVE|"+os.sep+r"cx.jpeg'"+"\n")
        f.write(r"$!EXPORT "+"\n")
        f.write(r"EXPORTREGION = CURRENTFRAME"+"\n")
        f.write(r"$!PICK ADDATPOSITION"+"\n")
        f.write(r"X = 5.64392059553"+"\n")
        f.write(r"Y = 0.835607940447"+"\n")
        f.write(r"CONSIDERSTYLE = YES"+"\n")
        f.write(r"$!PICK CLEAR"+"\n")
        f.write(r"$!ATTACHTEXT"+"\n")
        f.write(r"ANCHORPOS"+"\n")
        f.write(r"{"+"\n")
        f.write(r"X = 49.17287014061208"+"\n")
        f.write(r"Y = 91.68734491315136"+"\n")
        f.write(r"}"+"\n")
        f.write(r"TEXTSHAPE"+"\n")
        f.write(r"{"+"\n")
        f.write(r"ISITALIC = YES"+"\n")
        f.write(r"SIZEUNITS = FRAME"+"\n")
        f.write(r"HEIGHT = 3.6"+"\n")
        f.write(r"}"+"\n")
        f.write(r"TEXT = 'CY'"+"\n")
        f.write(r"$!ACTIVELINEMAPS = [2]"+"\n")
        f.write(r"$!PICK ADDATPOSITION"+"\n")
        f.write(r"X = 5.35607940447"+"\n")
        f.write(r"Y = 3.37655086849"+"\n")
        f.write(r"CONSIDERSTYLE = YES"+"\n")
        f.write(r"$!VIEW FIT"+"\n")
        f.write(r"$!EXPORTSETUP EXPORTFNAME = '|JPGSAVE|"+os.sep+r"cy.jpeg'"+"\n")
        f.write(r"$!EXPORT"+"\n")
        f.write(r"EXPORTREGION = CURRENTFRAME"+"\n")
        f.write(r"$!PICK ADDATPOSITION"+"\n")
        f.write(r"X = 5.71339950372"+"\n")
        f.write(r"Y = 0.746277915633"+"\n")
        f.write(r"CONSIDERSTYLE = YES"+"\n")
        f.write(r"$!PICK CLEAR"+"\n")
        f.write(r"$!ATTACHTEXT"+"\n")
        f.write(r"ANCHORPOS"+"\n")
        f.write(r"{"+"\n")
        f.write(r"X = 49.17287014061208"+"\n")
        f.write(r"Y = 91.68734491315136"+"\n")
        f.write(r"}"+"\n")
        f.write(r"TEXTSHAPE"+"\n")
        f.write(r"{"+"\n")
        f.write(r"ISITALIC = YES"+"\n")
        f.write(r"SIZEUNITS = FRAME"+"\n")
        f.write(r"HEIGHT = 3.6"+"\n")
        f.write(r"}"+"\n")
        f.write(r"TEXT = 'CZ'"+"\n")
        f.write(r"$!ACTIVELINEMAPS = [3]"+"\n")
        f.write(r"$!PICK ADDATPOSITION"+"\n")
        f.write(r"X = 6.99379652605"+"\n")
        f.write(r"Y = 2.64205955335"+"\n")
        f.write(r"CONSIDERSTYLE = YES"+"\n")
        f.write(r"$!VIEW FIT"+"\n")
        f.write(r"$!EXPORTSETUP EXPORTFNAME = '|JPGSAVE|"+os.sep+r"cz.jpeg'"+"\n")
        f.write(r"$!EXPORT"+"\n")
        f.write(r"EXPORTREGION = CURRENTFRAME"+"\n")
        f.write(r"$!PICK ADDATPOSITION"+"\n")
        f.write(r"X = 5.65384615385"+"\n")
        f.write(r"Y = 0.795905707196"+"\n")
        f.write(r"CONSIDERSTYLE = YES"+"\n")
        f.write(r"$!PICK CLEAR"+"\n")
        f.write(r"$!ATTACHTEXT"+"\n")
        f.write(r"ANCHORPOS"+"\n")
        f.write(r"{"+"\n")
        f.write(r"X = 49.17287014061208"+"\n")
        f.write(r"Y = 91.68734491315136"+"\n")
        f.write(r"}"+"\n")
        f.write(r"TEXTSHAPE"+"\n")
        f.write(r"{"+"\n")
        f.write(r"ISITALIC = YES"+"\n")
        f.write(r"SIZEUNITS = FRAME"+"\n")
        f.write(r"HEIGHT = 3.6"+"\n")
        f.write(r"}"+"\n")
        f.write(r"TEXT = 'MX'"+"\n")
        f.write(r"$!ACTIVELINEMAPS = [4]"+"\n")
        f.write(r"$!LINEMAP [4]  LINES{COLOR = BLACK}"+"\n")
        f.write(r"$!VIEW FIT"+"\n")
        f.write(r"$!EXPORTSETUP EXPORTFNAME = '|JPGSAVE|"+os.sep+r"mx.jpeg'"+"\n")
        f.write(r"$!EXPORT"+"\n")
        f.write(r"EXPORTREGION = CURRENTFRAME"+"\n")
        f.write(r"$!PICK ADDATPOSITION"+"\n")
        f.write(r"X = 5.6141439206"+"\n")
        f.write(r"Y = 0.795905707196"+"\n")
        f.write(r"CONSIDERSTYLE = YES"+"\n")
        f.write(r"$!PICK CLEAR"+"\n")
        f.write(r"$!ATTACHTEXT"+"\n")
        f.write(r"ANCHORPOS"+"\n")
        f.write(r"{"+"\n")
        f.write(r"X = 49.17287014061208"+"\n")
        f.write(r"Y = 91.68734491315136"+"\n")
        f.write(r"}"+"\n")
        f.write(r"TEXTSHAPE"+"\n")
        f.write(r"{"+"\n")
        f.write(r"ISITALIC = YES"+"\n")
        f.write(r"SIZEUNITS = FRAME"+"\n")
        f.write(r"HEIGHT = 3.6"+"\n")
        f.write(r"}"+"\n")
        f.write(r"TEXT = 'MY'"+"\n")
        f.write(r"$!ACTIVELINEMAPS = [5]"+"\n")
        f.write(r"$!LINEMAP [5]  LINES{COLOR = PURPLE}"+"\n")
        f.write(r"$!PICK ADDATPOSITION"+"\n")
        f.write(r"X = 5.96153846154"+"\n")
        f.write(r"Y = 3.08870967742"+"\n")
        f.write(r"CONSIDERSTYLE = YES"+"\n")
        f.write(r"$!VIEW FIT"+"\n")
        f.write(r"$!EXPORTSETUP EXPORTFNAME = '|JPGSAVE|"+os.sep+r"my.jpeg'"+"\n")
        f.write(r"$!EXPORT"+"\n")
        f.write(r"EXPORTREGION = CURRENTFRAME"+"\n")
        f.write(r"$!PICK ADDATPOSITION"+"\n")
        f.write(r"X = 5.70347394541"+"\n")
        f.write(r"Y = 0.73635235732"+"\n")
        f.write(r"CONSIDERSTYLE = YES"+"\n")
        f.write(r"$!PICK CLEAR"+"\n")
        f.write(r"$!ATTACHTEXT"+"\n")
        f.write(r"ANCHORPOS"+"\n")
        f.write(r"{"+"\n")
        f.write(r"X = 49.17287014061208"+"\n")
        f.write(r"Y = 91.68734491315136"+"\n")
        f.write(r"}"+"\n")
        f.write(r"TEXTSHAPE"+"\n")
        f.write(r"{"+"\n")
        f.write(r"ISITALIC = YES"+"\n")
        f.write(r"SIZEUNITS = FRAME"+"\n")
        f.write(r"HEIGHT = 3.6"+"\n")
        f.write(r"}"+"\n")
        f.write(r"TEXT = 'MZ'"+"\n")
        f.write(r"$!ACTIVELINEMAPS = [6]"+"\n")
        f.write(r"$!LINEMAP [6]  LINES{COLOR = CUSTOM7}"+"\n")
        f.write(r"$!PICK ADDATPOSITION"+"\n")
        f.write(r"X = 4.93920595533"+"\n")
        f.write(r"Y = 2.59243176179"+"\n")
        f.write(r"CONSIDERSTYLE = YES"+"\n")
        f.write(r"$!VIEW FIT"+"\n")
        f.write(r"$!EXPORTSETUP EXPORTFNAME = '|JPGSAVE|"+os.sep+r"mz.jpeg'"+"\n")
        f.write(r"$!EXPORT"+"\n")
        f.write(r"EXPORTREGION = CURRENTFRAME"+"\n")
        f.write(r"$!Quit"+"\n")
        f.write(r"$!RemoveVar |MFBD|"+"\n")
        f.write(r"$!RemoveVar |JPGSAVE|"+"\n")
        f.close
		
        econv_mrc=os.path.join(outputdir,r'econv.mcr')
        f1=open(econv_mrc, 'w')
        f1.write(constant.tecplot['version']+"\n")
        f1.write(r"$!VarSet |MFBD| = '"+outputdir+r"'"+"\n")
        f1.write(r"$!READDATASET  '"+r'"|MFBD|/'+repath+r'.ECONV" '+r"'"+"\n")
        f1.write(r"READDATAOPTION = NEW"+"\n")
        f1.write(r"RESETSTYLE = YES"+"\n")
        f1.write(r"VARLOADMODE = BYNAME"+"\n")
        f1.write(r"ASSIGNSTRANDIDS = YES"+"\n")
        f1.write(r"$!FRAMELAYOUT SHOWBORDER = NO"+"\n")
        f1.write(r"$!LINEMAP [1-2]  LINES{LINETHICKNESS = 0.400000000000000022}"+"\n")
        f1.write(r"$!VIEW FIT"+"\n")
        f1.write(r"$!XYLINEAXIS YDETAIL 1 {COORDSCALE = LOG}"+"\n")
        f1.write(r"$!VIEW FIT"+"\n")
        f1.write(r"$!EXPORTSETUP EXPORTFORMAT = JPEG"+"\n")
        f1.write(r"$!PRINTSETUP PALETTE = COLOR"+"\n")
        f1.write(r"$!EXPORTSETUP IMAGEWIDTH = 820"+"\n")
        f1.write(r"$!VarSet |JPGSAVE| = '"+downpath+r'/'+repath+r"'"+"\n")
        f1.write(r"$!EXPORTSETUP EXPORTFNAME = '|JPGSAVE|/error_ave.jpeg'"+"\n")
        f1.write(r"$!EXPORT "+"\n")
        f1.write(r"EXPORTREGION = CURRENTFRAME"+"\n")
        f1.write(r"$!ACTIVELINEMAPS += [2]"+"\n")
        f1.write(r"$!ACTIVELINEMAPS -= [1]"+"\n")
        f1.write(r"$!VIEW FIT"+"\n")
        f1.write(r"$!EXPORTSETUP EXPORTFNAME = '|JPGSAVE|/error_max.jpeg'"+"\n")
        f1.write(r"$!EXPORT "+"\n")
        f1.write(r"EXPORTREGION = CURRENTFRAME"+"\n")
        f1.close
    fileou.close()
	
def run_project():
#   目标区域并执行run.sh
    global runexe
    global testcase
    global testpath
    global number_path
    
    fileou=open(testcase,'rb')
    csv_reader=csv.DictReader(fileou)
    

    f=open(number_path,'w')
    for row in csv_reader:
        if row['dotask(Yes=1)']=='1':
            repath=row['TaskName']
            rundir=os.path.join(testpath,repath)
            if not os.path.exists(rundir):
                os.makedirs(rundir)
            if platform.system() =='Windows':
                cmd='cd '+rundir+' & start '+runexe
                print cmd
                os.system(cmd)
            else:
                cmd=r'cd '+rundir+r';'+constant.pbs['qsub']+r' '+runexe
                print cmd
                proc=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,)
                remainder=proc.communicate()[0]
                print remainder
                mainder=remainder.split(".")
                la=mainder.pop(0)
                f.write(row['TaskName']+'  '+str(la)+"\n")
  
    f.close
    fileou.close()
    
def rerun_project():
#   续算所有的状态
    global runexe
    global testcase
    global testpath
    global number_path
    
    fileou=open(testcase,'rb')
    csv_reader=csv.DictReader(fileou)
    
    f=open(number_path,'w')
    for row in csv_reader:
        if row['dotask(Yes=1)']=='1':
            repath=row['TaskName']
            rundir=os.path.join(testpath,repath)
            print rundir
            changests(rundir,row)
            if not os.path.exists(rundir):
                os.makedirs(rundir)
            if platform.system() =='Windows':
                cmd='cd '+rundir+' & start '+runexe
                print cmd
                os.system(cmd)
            else:
                cmd=r'cd '+rundir+r';'+constant.pbs['qsub']+r' '+runexe
                print cmd
                proc=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,)
                remainder=proc.communicate()[0]
                print remainder
                mainder=remainder.split(".")
                la=mainder.pop(0)
                f.write(row['TaskName']+'  '+str(la)+"\n")
  
    f.close
    fileou.close()
    
def changests(dirname,row):
    filests=dirname+os.sep+'bhcfd.sts'
    print filests
    sts=Config20(filename=filests)

    sts['FlowModel']=row['FlowModel']
    sts['IsRestart']="1"
    sts['IterationNum']=row['IterationNum']
    sts['CFL']=row['CFL']
    sts['Height']=row['Height']
    sts['Mach']=row['Mach']
    sts['Alpha']=row['Alpha']
    sts['Beta']=row['Beta']
    sts['Twall']=row['Twall']
    sts['Ref_Area']=row['Ref_Area']
    sts['Ref_Length']=row['Ref_Length']
    sts['Ref_X']=row['Ref_X']
    sts['Ref_Y']=row['Ref_Y']
    sts['Ref_Z']=row['Ref_Z']
    sts['ATM_Pressure']=row['ATM_Pressure']
    sts['ATM_Density']=row['ATM_Density']
    sts['ATM_Temperature']=row['ATM_Temperature']
    filestsou=dirname+os.sep+'bhcfd.sts'
    sts.write(filestsou)
    
def DeleteFile(Dir):
#   删除项目文件
    if os.path.isfile(Dir):
        try:
            os.remove(Dir)
        except:
            pass
    elif os.path.isdir(Dir):
        for item in os.listdir(Dir):
            itemdir=os.path.join(Dir,item)
            DeleteFile(itemdir)
        try:
            os.rmdir(Dir)
        except:
            pass

def removeFile(targetDir): 
    for files in os.listdir(targetDir): 
        targetFile = os.path.join(targetDir,files) 
        if os.path.isfile(targetFile): 
             os.remove(targetFile)


def eraseFile():
    global testpath

    DeleteFile(testpath)

def plot():
    global testcase
    global testpath
    global downpath
    
    fileou=open(testcase,'rb')
    csv_reader=csv.DictReader(fileou)
    
    for row in csv_reader:
        if row['dotask(Yes=1)']=='1':
            repath=row['TaskName']
            rundir=os.path.join(testpath,repath)
            outputdir=os.path.join(downpath,repath+"_map")
            if not os.path.exists(outputdir):
                os.makedirs(outputdir)
            if platform.system() =='Windows':
                cmd1='cd '+rundir+' & start '+r'fconv.mcr'
                print cmd1
                os.system(cmd1)
            else:
                cmd1=constant.tecplot['path']+r' -b '+rundir+r'/'+r'fconv.mcr'
                print cmd1
                os.system(cmd1)
    fileou.close()

def download_list():
    global testcase
    global testpath
    global downpath
    
    fileou=open(testcase,'rb')
    csv_reader=csv.DictReader(fileou)
    
    for row in csv_reader:
        if row['dotask(Yes=1)']=='1':
            repath=row['TaskName']
            rundir=os.path.join(testpath,repath)
            field_path=os.path.join(rundir,"field_file")
            outputdir=os.path.join(downpath,repath)
            outfield_path=os.path.join(outputdir,"field_file")
            
            if not os.path.exists(outputdir):
                os.makedirs(outputdir)
            if not os.path.exists(outfield_path):
                os.makedirs(outfield_path)
            
            for files in os.listdir(field_path):
                sourceFile=os.path.join(field_path,files) 
                if os.path.isfile(sourceFile):
                    shutil.copy(sourceFile,outfield_path)

            file1=glob.glob(rundir+os.sep+r'field_file.mcr')
            file1+=glob.glob(rundir+os.sep+r'FCONV.dat')
            file1+=glob.glob(rundir+os.sep+r'FDATA.csv')
            for files in os.listdir(rundir):
                sourceFile=os.path.join(rundir,files) 
                if os.path.isfile(sourceFile):
                    if sourceFile==file1[0] or sourceFile==file1[1] or sourceFile==file1[2]:
                        shutil.copy(sourceFile,outputdir)
            tarname=repath+'.tar.gz'
            cmd1=r'cd '+downpath+r';'+r'tar czvf '+tarname+' '+repath
            os.system(cmd1)
            cmd2=r'cd '+downpath+r';'+r'rm -fr '+repath
            os.system(cmd2)
    fileou.close()
	 
def checkjob(state):
    global number_path
    global state_path
    
    cmd=constant.pbs['qstat']
    proc=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,)
    ream=proc.communicate()[0]
    fstate=open(state_path,'w')
    if not ream :
       fstate.write('Maybe The program has been completed!'+"\n")
       fstate.close
       return
    re=ream.split("\n")
    re.pop()
    re.pop(0)
    re.pop(0)
    
    s={}
    for line in re:
        a=line.split()
        c=a[0].split('.')
        s[c[0]]=a[4]
    
    f=open(number_path,'rb')
    num_reader=f.read().split("\n")
    num_reader.pop()
    num={}
    f.close()

    for line in num_reader:
        i=line.split()
        print i
        num[i[0]]=i[1]
        
    status={}
    for i in s.keys():
        for j in num.keys():
            if str(i)==num[j]:
                status[j]=s[i]
                break
                
    
    if state!='k':
        for i in num.keys():
            strue=False
            for j in status.keys():
                if i==j:
                    if (status[i]=='R'):
                        fstate.write(i+' in '+num[i]+' status is '+' R: '+'The program is running! You can kill it!'+"\n")
                    elif (status[i]=='E'):
                        fstate.write(i+' in '+num[i]+' status is '+' E: '+'The program has exited! Perhaps there are errors!'+"\n")
                    elif (status[i]=='Q'):
                        fstate.write(i+' in '+num[i]+' status is '+' Q: '+'The program is suspended state to wait for the compute nodes!'+"\n")
                    elif (status[i]=='C'):
                        fstate.write(i+' in '+num[i]+' status is '+' C: '+'The program has been completed!'+"\n")
                    strue=True
                    break
            if not strue:
                fstate.write(i+' in '+num[i]+', Maybe the program has been completed or there are errors!'+"\n")
                
    
    if state=='k':
        fstate.write('Kill all nodes!'+"\n")
        for i in num.keys():
            strue=False
            for j in status.keys():
                if i==j:
                    if (status[i]=='R'):
                        cmd1=constant.pbs['qdel']+r' '++num[i]
                        os.system(cmd1)
                        fstate.write(i+' in '+num[i]+' status is running'+' And has killed!'+"\n")
                    elif (status[i]=='Q'):
                        cmd1=constant.pbs['qdel']+r' '++num[i]
                        os.system(cmd1)
                        fstate.write(i+' in '+num[i]+' status is suspended'+' And has killed!'+"\n")
                    strue=True
                    break
            if not strue:
                fstate.write(i+' in '+num[i]+', Maybe the program has been completed or there are errors!'+"\n")
    fstate.close
   

def main(args):
    global testpath
    
    parser=optparse.OptionParser()
    parser.add_option('-r','--run',dest="rflag",default=False,action="store_true")
    parser.add_option('-g','--gen',dest="gflag",default=False,action="store_true")
    parser.add_option('-k','--kill',dest="kflag",default=False,action="store_true")
    parser.add_option('-x','--rerun',dest="reflag",default=False,action="store_true")
    parser.add_option('-s','--erase',dest="sflag",default=False,action="store_true")
    parser.add_option('-c','--check',dest="cflag",default=False,action="store_true")
    parser.add_option('-p','--plot',dest="pflag",default=False,action="store_true")
    parser.add_option('-d','--download',dest="dflag",default=False,action="store_true")
    parser.add_option('-u','--upload',dest="uflag",default=False,action="store_true")
    parser.add_option('--cprun',dest="cprunflag",default=False,action="store_true")
    parser.add_option('--list=',dest="lists",action="store",type=str)
    option,args=parser.parse_args()
    runflag=False

    if option.gflag:
        getrunsh()
        getsts()
        tecplot_mrc()
        cp()
        runflag=True
    if option.rflag:
        getrunsh()
        getsts()
        tecplot_mrc()
        cp()
        run_project()
        runflag=True
    if option.reflag:
        rerun_project()
        runflag=True
    if option.cflag:
        checkjob('c')
        runflag=True
    if option.kflag:
        checkjob('k')
        runflag=True
    if option.sflag:
        eraseFile()
        runflag=True
    if option.pflag:
        plot()
        runflag=True
    if option.dflag:
        download_list()
        runflag=True
#    if option.uflag:
#        get_csv_config()
#        if option.lists:
#            par_upload_list(option.lists)
#        runflag=True
#    if option.sflag:
#        get_csv_config()
#        if option.lists:
#            eraseFile(option.lists)
#        runflag=True
#    if option.cprunflag:
#        get_csv_config()
#        cp()
#        run_project()
#        runflag=True     
    if not runflag:
        print unicode("""Created on Fri Jun 12 17:03:58 2015
    .. help::
    配置文件bhcfd20.sts.template
    python solver20.py  -r(或者：--run，第一次提状态使用,相应的生成run.sh/bhcfd.sts,然后cp,run_project)
    python solver20.py  -g(任何时候可单独使用，相应的生成run.sh/bhcfd.sts)
    python solver20.py  -x(或者：--rerun，sts更改istart,cfl,nstep,并提交)
    python solver20.py  -s --list=*(--san，删除计算文件，list指定后缀，*全删除)
    python solver20.py  -k(或者：--kill，停状态)
    python solver20.py  -c(或者：--check)
    python solver20.py  -u --list=bhcfd.sts(--upload,将filetocopy中list指定名字上传)
                    多个文件：    --list=bhcfd.sts,bhcfd.grd,bhcfd.bc
    python solver20.py  -d --list=FCONV,ECONV  (--download,list指定后缀下载文件)
    python solver20.py  -p (生成力曲线图、残差收敛图)

    @author:ssheng
   ""","utf-8")
     
if __name__=="__main__":
    main(sys.argv)
    
