<?php
$conn = mysqli_connect("localhost","root","tlqkf12!@");
mysqli_select_db($conn,"pig_management");
$result = mysqli_query($conn, "SELECT * FROM pig_movement");
?>
<!DOCTYPE html>
<html lang="ko" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>돈방이동관리</title>
  </head>
  <body>
    <h2>돈방이관리</h2>
    <?php
    echo var_dump($result);
    ?>
  </body>
</html>
