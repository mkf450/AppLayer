<?php

error_reporting(~E_WARNING);

if (!($sock = socket_create(AF_INET, SOCK_DGRAM, 0))) {
    $errorcode = socket_last_error();
    $errormsg = socket_strerror($errorcode);

    die("Couldn't create socket: [$errorcode] $errormsg \n");
}

echo "Socket created \n";

if (!socket_bind($sock, "127.0.0.1", 9999)) {
    $errorcode = socket_last_error();
    $errormsg = socket_strerror($errorcode);

    die("Could not bind socket : [$errorcode] $errormsg \n");
}

echo "Socket bind OK \n";

while (1) {
    echo "Waiting for data ... \n";

    $r = socket_recvfrom($sock, $buf, 2045, 0, $remote_ip, $remote_port);
    echo "$remote_ip : $remote_port -- " . $buf;

    socket_sendto($sock, "OK " . $buf, 2045, 0, $remote_ip, $remote_port);
}

socket_close($sock);
