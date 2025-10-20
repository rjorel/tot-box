<?php

spl_autoload_register(function (string $class) {
    echo "You requested: $class\n";
});

spl_autoload_register(function (string $class) {
    echo "Now registering: $class\n";
    require $class . '.php';
});

spl_autoload_call('Foo'); // Call registered autoload functions for specified class.

$obj1 = new Foo(); // Do not call autoload functions, because `Foo` is known.
$obj2 = new Foo();

var_dump($obj1);
var_dump($obj2);

// Unregister autoload functions just for using maximum of spl_* functions.
foreach (spl_autoload_functions() as $fn) {
    echo "Unregistering: ";
    var_dump($fn);

    spl_autoload_unregister($fn);
}