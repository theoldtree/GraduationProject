<?php
function print_title(){
  if(isset($_GET['id'])){
    echo $_GET['id'];
  }else {
    echo "환영합니다";
  }
}
function print_list(){
  $list = scandir("./data");
  $cnt = count($list);
  $i = 0;
  while($i < $cnt){
    if($list[$i] != "." && $list[$i] != ".."){
      echo "<li><a href=\"index.php?id=$list[$i]\">$list[$i]</a></li>";
    }
    $i = $i + 1;
  }
}
function print_description(){
  if(isset($_GET['id'])){
    echo file_get_contents("data/".$_GET['id']);
  }else{
    echo "HELLO";
  }
}
$conn = mysqli_connect("localhost","root","tlqkf12!@");
mysqli_select_db($conn,"pig_management");
$result = mysqli_query($conn, "SELECT * FROM pig_count");
?>
<!DOCTYPE html>
<html lang="ko" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>
      <?php
      print_title();
      ?>
    </title>
  </head>
  <body>
    <h1><a href="index.php">편리한 돈사관리를 위한 어플리케이션</a></h1>
    <ol>
      <?php
      print_list();
      ?>
    </ol>
    <?php
      print_description();
    ?>
    <?php
    echo var_dump($result);
    ?>
  </body>
</html>
