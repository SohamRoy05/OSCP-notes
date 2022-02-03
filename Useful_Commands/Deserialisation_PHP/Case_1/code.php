<?php

class ReadFile{
   public function __tostring(){
 
      return file_get_contents($this->filename);

   }
}

class User{

  public $username; 
  public $isAdmin;
   
   public function CheckAdmin(){
   if($this->isAdmin){
      echo "$this->username is an admin";
   }

   else{
   	  echo "$this->username is not an admin";
   }
}
}

//$obj=new User();
//$obj->username="Soham";
//$obj->isAdmin=True;
//$obj->CheckAdmin();
//echo serialize($obj);

//O:4:"User":2:{s:8:"username";s:5:"Soham";s:7:"isAdmin";b:1;}
$obj=unserialize($_POST['Soham']);
$obj->CheckAdmin();


?>