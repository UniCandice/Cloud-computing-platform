package lly;

import javax.swing.JFileChooser; 
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.swing.filechooser.FileFilter;
import java.io.FileInputStream;  
import java.io.FileNotFoundException;  
import java.io.FileOutputStream;  
import javax.swing.*;
import java.io.File;
import java.util.HashSet;  
import javax.swing.JDialog;  
import java.io.IOException;  

public class FileLLY extends JFrame{
    /**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private FileFilter createFileFilter(String description,
            boolean showExtensionInDescription, String... extensions) {
        if (showExtensionInDescription) {
            description = createFileNameFilterDescriptionFromExtensions(
                    description, extensions);
        }
        return new FileNameExtensionFilter(description, extensions);
    }
    private String createFileNameFilterDescriptionFromExtensions(
            String description, String[] extensions) {
        String fullDescription = (description == null) ? "(" : description
                + " (";
        fullDescription += "." + extensions[0];
        for (int i = 1; i < extensions.length; i++) {
            fullDescription += ", .";
            fullDescription += extensions[i];
        }
        fullDescription += ")";
        return fullDescription;
    }
    public static void mkDir(File file){
    	  if(file.getParentFile().exists()){
    	   file.mkdir();
    	  }else{
    	   mkDir(file.getParentFile());
    	   file.mkdir();
    	  }
    }
    public String  do_it(String webpath, String uploadfilesdir, String username,String testcase, String random){
    	//upload path =   web_path/uploadfiles/$username/$testcase_$random
         String path = webpath+"/"+uploadfilesdir+"/"+username+"/"+testcase+"_"+random;
         System.out.println("path:"+path);
    	JFileChooser chooser = new JFileChooser();
    	
	//add file .grd .bc .cgns .dat
	FileFilter allFilter = createFileFilter(
                    "JPEG Compressed Image Files",
                    true, "grd","bc","cgns","dat");

	//add file .grd
	FileFilter grdFilter = createFileFilter(
                    "JPEG Compressed Image Files",
                    true, "grd");

	//add file .bc
	FileFilter bcFilter = createFileFilter(
                    "JPEG Compressed Image Files",
                    true, "bc");

	//add file .cgns
	FileFilter cgnsFilter = createFileFilter(
                    "JPEG Compressed Image Files",
                    true, "cgns");

	//add file .dat
	FileFilter datFilter = createFileFilter(
                    "JPEG Compressed Image Files",
                    true, "dat");

	chooser.setAcceptAllFileFilterUsed(false);
	//add file in recognize
        chooser.addChoosableFileFilter(allFilter);
        chooser.addChoosableFileFilter(grdFilter);
        chooser.addChoosableFileFilter(bcFilter);
        chooser.addChoosableFileFilter(cgnsFilter);
        chooser.addChoosableFileFilter(datFilter);

	chooser.setMultiSelectionEnabled(true);
	chooser.showOpenDialog(this);
	File[] files = chooser.getSelectedFiles();
	String pathmsg = "";
	String retsolver = "";
	if(files !=null && files.length >0){
		pathmsg = "";
		for(File file : files){
			pathmsg = pathmsg + "<br>" + file.getPath();
			if(file.getName().substring(0,2).equals("ch")){ //如果文件以ch开头，则认为是Solver
				retsolver = file.getName();
			}
		}
		uploadfile(files,path);
	}
	showmesg(pathmsg+"<br>to  path:"+path);
	 return retsolver;
    }
	public void uploadfile(File[] files,String path){
		FileInputStream input = null;  
            FileOutputStream out = null;  
           
            File filetest =new File(path);    
          //如果文件夹不存在则创建    
          if  (!filetest .exists()  && !filetest .isDirectory())      
          {       
              //System.out.println("//不存在");  
        	  mkDir(filetest);
          }   
            try {  
                for (File f : files) {  
                    File dir = new File(path);  
                    /** 目标文件夹 * */  
                    File[] fs = dir.listFiles();  
                    HashSet<String> set = new HashSet<String>();  
                    for (File file : fs) {  
                        set.add(file.getName());  
                    }  
                    /** 判断是否已有该文件* */  
                    if (set.contains(f.getName())) {  
                        JOptionPane.showMessageDialog(new JDialog(), "已有该文件！");  
                        return;  
                    }  
                    input = new FileInputStream(f);  
                    byte[] buffer = new byte[1024];  
                    File des = new File(path, f.getName());  
                    out = new FileOutputStream(des);  
                    int len = 0;  
                    while (-1 != (len = input.read(buffer))) {  
                        out.write(buffer, 0, len);  
                    }  
                    out.close();  
                    input.close();  
                }  
            } catch (FileNotFoundException e1) {  
                e1.printStackTrace();  
            } catch (IOException e1) {  
                e1.printStackTrace();  
            }  
           return ;
	}
	public void showmesg(String msg){//show upload result 
		JFrame frame = new JFrame("upload result");
		String m = "<html>You have uploaded:"+msg+"</html>";
		JOptionPane.showMessageDialog(frame,m);
		return ;
	}
    public static void main(String []args){
    	System.out.println("jar : main function");
    	return ;
    }
    public String showdialog(String webpath, String uploadfilesdir, String username,String testcase, String random){
    	//upload path =   web_path/uploadfiles/$username/$testcase_$random
    	FileLLY ft = new FileLLY();
    	return ft.do_it(webpath,uploadfilesdir,username,testcase,random);
    }
    
}
