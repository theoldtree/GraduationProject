<?php
function print_title(){
  if(isset($_GET['id'])){
    echo $_GET['id'];
  }else {
    echo "환영합니다";
  }
}

function print_href_list(){
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

function print_arr($arr){
  foreach($arr as $value){
    echo "<td>$value</td>";
  }
}

function print_query_data($result, $arr){
  while($row = $result -> fetch_assoc()){
    echo "<tr>";
    foreach ($arr as $value) {
      echo "<td>$row[$value]</td>";
    }
    echo "</tr>";
  }
}

function get_query_table($title,$name){
  $conn = mysqli_connect("localhost","root","tlqkf12!@");
  mysqli_select_db($conn,"pig_management");
  $result = mysqli_query($conn, "SELECT * FROM ".$name);
  $field_list = [];
  while($field = mysqli_fetch_field($result)){
    $field_name = $field->name;
    array_push($field_list,$field_name);
  }
  $array_length = count($field_list);
  echo "<h3>$title</h3>";
  echo "<p>";
  echo "<table>";
  echo "<tr>";
  echo print_arr($field_list);
  echo "</tr>";
  echo print_query_data($result,$field_list);
  echo "</table>";
  echo "<p>";
}
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
      print_href_list();
      ?>
    </ol>
    <br>
    <p>
      <?php
        get_query_table('재고관리','pig_count');
      ?>
    </p>
      <?php
        get_query_table('돈방이동관리','pig_movement');
      ?>
      <?php
        get_query_table('출하관리','sold_pig');
      ?>
      <?php
        get_query_table('이상행동관리','strange_action_info');
      ?>
      <?php
        get_query_table('영상관리','video_info');
      ?>
  </body>
</html>
