<?php
include 'connection.php';
if(!empty($_POST["Category_Id"])){ 
    
    $query = "SELECT * FROM sub_categories WHERE Category_Id = ".$_POST['Category_Id'].""; 
    $result = $conn->query($query); 
     
    
    if($result->num_rows > 0){ 
        
        while($row = $result->fetch_assoc()){ 
           {
            echo '<option value="'.$row['Sub_Category_Id'].'">'.$row['Sub_Category_Name'].'</option>'; 
        }
    }else{ 
        echo '<option value="">Sub Category Not Available</option>'; 
    }}
    ?>