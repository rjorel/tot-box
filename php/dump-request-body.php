<?php

$body = file_get_contents('php://input');

// Automatically convert JSON request bodies.
if ($_SERVER['CONTENT_TYPE'] == 'application/json') {
    $body = json_decode($body);
}

var_dump($body);
